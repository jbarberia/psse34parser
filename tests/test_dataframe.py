import psse34parser
import pytest
import os

minimal_data = psse34parser.read_case("tests/data/minimal.raw")
transformer_data = psse34parser.read_case("tests/data/transformer.raw")

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

def test_full_case():
    df = psse34parser.generate_dataframe_model(minimal_data)
