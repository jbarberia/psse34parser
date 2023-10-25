import psse34parser
import pytest
import os

def test_read_raw():
    filename = "tests/data/minimal.raw"
    data = psse34parser.read_case_raw(filename)

    assert len(data["BUS"]) == 2
    assert isinstance(data["LOAD"][0]["I"], int)


def test_read_seq():
    filename = "tests/data/example.seq"
    data = psse34parser.read_case_seq(filename)

    assert isinstance(data, dict)
    assert len(data["GENERATOR"]) == 6
    assert data["GENERATOR"][0]["I"] == 101

    