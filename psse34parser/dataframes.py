import pandas as pd
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
