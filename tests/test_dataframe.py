import psse34parser
import pytest
import os

minimal_data = psse34parser.read_case_raw("tests/data/minimal.raw")
transformer_data = psse34parser.read_case_raw("tests/data/transformer.raw")
seq_data = psse34parser.read_case_seq("tests/data/example.seq")

def test_convert_to_dataframe_bus():
    df = psse34parser.convert_to_dataframe(minimal_data["BUS"])
    assert df["I"].to_list() == [1, 2]

    df.set_index("I", inplace=True)
    assert df.loc[1]["VM"] == 1.05
    assert df.loc[2]["VM"] == 1.00

def test_convert_to_dataframe_multi_components():
    df = psse34parser.convert_to_dataframe(transformer_data["TRANSFORMER"])
    assert len(df.columns) == 114
    assert len(df) == 2

def test_convert_to_dataframe_seq_data():
    df = psse34parser.convert_to_dataframe(seq_data["GENERATOR"])
    assert len(df.columns) == 14
    assert len(df) == 6
    
def test_generate_data_model():
    data_model = psse34parser.generate_dataframe_model(transformer_data)
    assert isinstance(data_model, dict)

# def test_to_excel():
    # transformer_data = psse34parser.export_raw_to_excel("tests/data/sample.raw", "sample.xlsx")