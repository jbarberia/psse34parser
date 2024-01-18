import pandas as pd
import openpyxl
from .parser import read_case_raw, read_case_seq

def convert_to_dataframe(data):
    """Genera una tabla para cada entrada de los elementos. Las columnas son los campos

    Args:
        data (list): componentes del RAW o SEQ

    Returns:
        pd.DataFrame: tabla resumida
    """
    
    # Empty dict for no data
    # TODO sumar columnas
    if not data: 
        return pd.DataFrame()
    
    # Headers
    if isinstance(data, dict):
        return pd.Series(data)

    # Flatten multiline data
    if isinstance(data[0], list):
        flatten_data = []
        for element in data:
            flatten_dict = {k: v for d in element for k, v in d.items()}
            flatten_data.append(flatten_dict)
        data = flatten_data
        
    # Convert to dataframe
    df = pd.DataFrame(data)
    return df


def generate_dataframe_model(data):
    """Genera un diccionario con cada tabla de componente en su interior

    Args:
        data (dict): modelo de datos de diccionario proveniente del RAW o SEQ

    Returns:
        dict: diccionario con tablas de datos en su interior
    """
    df_model = {}
    for key, values in data.items():
        if isinstance(values, dict):
            df_model[key] = values
            continue
        
        if len(values) == 0:
            continue

        df_model[key] = convert_to_dataframe(values)
    return df_model


def export_raw_to_excel(raw, ofile):
    """Genera un excel con los datos de un archivo RAW

    Args:
        raw (str): ruta del archivo RAW
        ofile (str): ruta del excel de salida
    """
    wb = openpyxl.Workbook()
    wb.save(filename=ofile)

    raw = read_case_raw(raw)
    raw_df = generate_dataframe_model(raw)
    for key in raw_df:
        if isinstance(raw_df[key], pd.DataFrame):
            with pd.ExcelWriter(ofile, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
                raw_df[key].to_excel(writer, sheet_name=key, float_format="%.6f", index=False)

def export_seq_to_excel(seq, ofile):
    """Genera un excel con los datos de un archivo SEQ
    
    Args:
        seq (str): ruta del archivo SEQ
        ofile (str): ruta del excel de salida
    """
    wb = openpyxl.Workbook()
    wb.save(filename=ofile)

    seq = read_case_seq(seq)
    seq_df = generate_dataframe_model(seq)
    for key in seq_df:
        if isinstance(seq_df[key], pd.DataFrame):
            with pd.ExcelWriter(ofile, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
                seq_df[key].to_excel(writer, sheet_name=key, float_format="%.6f", index=False)

