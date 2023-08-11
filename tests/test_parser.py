import psse34parser
import pytest
import os

def test_read():
    filename = "tests/data/minimal.raw"
    data = psse34parser.read_case(filename)

    assert len(data["BUS"]) == 2
    assert isinstance(data["LOAD"][0]["I"], int)
