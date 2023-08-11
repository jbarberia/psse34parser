import pandas as pd

def convert_to_dataframe(data: list) -> pd.DataFrame:

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

def generate_dataframe_model(data: dict) -> dict:
    df_model = {}
    for key, values in data.items():
        df_model[key] = convert_to_dataframe(values)
