import re
import io
from .dataformat import SEQ_DATA, RAW_DATA, DTYPE_SEQ_DATA, DTYPE_RAW_DATA, HEADERKEYS, DTYPE_HEADERKEYS,MULTILINECOMPONENTS

def read_case_raw(filename):
    """Lee un archivo raw

    Args:
        filename (str): ruta del archivo

    Returns:
        dict: Mapeo de los componentes del RAW
    """
    case34 = {key: [] for key in RAW_DATA.keys()}
    key = None

    with io.open(filename, encoding="latin-1") as f:
        for line in f:

            # Get type of data
            type_data = get_type_of_data(line)
            if type_data == "END":
                break # End of file

            if type_data == "COMMENT":
                continue # Skip comment

            if type_data == "HEADER":
                parts = get_parts(line.split("/")[0], HEADERKEYS, DTYPE_HEADERKEYS)
                case34["HEADER"] = parts
                continue

            if type_data == "SKIP":
                continue

            if type_data: # Header of block data
                key = type_data
                continue

            # Populate dict if is in data block
            if key:
                if key not in MULTILINECOMPONENTS:
                    # Get parts and pad with None missing info
                    parts = get_parts(line, RAW_DATA[key], DTYPE_RAW_DATA[key])

                    # Add to the case
                    case34[key].append(parts)

                elif key == "TRANSFORMER":
                    components = []
                    for j, sublist in enumerate(RAW_DATA[key]):
                        if not line:
                            continue
                        parts = get_parts(line, sublist, DTYPE_RAW_DATA[key][j])
                        components.append(parts)
                        if j < 3:
                            line = next(f)
                        elif j == 3:
                            line = next(f) if components[0]["K"] != 0 else ""
                    # Append to case
                    case34[key].append(components)
                else:
                    components = []
                    for j, sublist in enumerate(RAW_DATA[key]):
                        parts = get_parts(line, sublist, DTYPE_RAW_DATA[key][j])
                        components.append(parts)
                        if j < len(RAW_DATA[key]) - 1:
                            line = next(f)
                    # Append to case
                    case34[key].append(components)
    return case34

def get_type_of_data(line):
    match_end = re.search(r"^Q", line)
    if match_end:
        return "END"

    match_comment = re.search(r"^@!", line)
    if match_comment:
        return "COMMENT"
    
    match_header = re.search(r"^0([^,]*,)([^,]*,)\s*34", line)
    if match_header:
        return "HEADER"

    match_data_type = re.search(r"(?<=BEGIN\s).*(?=\sDATA)", line)
    if match_data_type:
        return match_data_type.group()
    
    # esto es para el ultimo conjunto de elementos
    # para evitar leer el final del campo
    if "0" in line[0]: 
        return "SKIP"

    return None


def get_parts(line, data, dtype):
    """Genera la estructura de datos para una linea en el RAW o SEQ

    Args:
        line (str): linea 
        data (list): lista de campos del elemento que se lee
        dtype (dict): tipo de datos del campo del elemento

    Returns:
        dict: mapeo de campos -> valor en su correspondiente formato
    """
    parts = [part.strip() for part in line.split(",")]
    parts.extend([None] * (len(data) - len(parts)))
    component = {key: try_parse(dtype[key], part) for key, part in zip(data, parts)}
    return component


def try_parse(dtype, data):
    """Intenta convertir un dato a su correspondiente tipo de dato

    Args:
        dtype (fun): funcion de conversion
        data (str): texto con el valor a convertir

    Returns:
        any: dato convertido
    """
    try:
        if data and dtype == str:
            return dtype(data.replace("'", ""))
        return dtype(data)
    
    except TypeError:
        return None


def read_case_seq(filename):
    """Lee un archivo SEQ

    Args:
        filename (str): ruta del archivo SEQ

    Returns:
        dict: mapeo de componentes de los datos del SEQ
    """
    case34 = {key: [] for key in SEQ_DATA.keys()}
    key = None

    with io.open(filename, encoding="latin-1") as f:

        for line in f:
                        # Get type of data
            type_data = get_type_of_data(line)
            if type_data == "END":
                break # End of file

            if type_data == "COMMENT":
                
                continue # Skip comment

            if type_data == "HEADER":
                #parts = get_parts(line.split("/")[0], HEADERKEYS, DTYPE_HEADERKEYS)
                #case34["HEADER"] = parts
                continue

            if type_data == "SKIP":
                continue

            if type_data: # Header of block data
                key = type_data
                continue

            if key:
                if key == "ZERO SEQ. TRANSFORMER":
                    is_three_winding = line.split(",")[2].strip() != "0"
                    if is_three_winding:
                        parts = get_parts(line, SEQ_DATA[key][1], DTYPE_SEQ_DATA[key][1])
                    else:
                        parts = get_parts(line, SEQ_DATA[key][0], DTYPE_SEQ_DATA[key][0])
                else:
                    parts = get_parts(line, SEQ_DATA[key], DTYPE_SEQ_DATA[key])

                case34[key].append(parts)

    return case34
