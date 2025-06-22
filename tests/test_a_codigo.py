import psse34parser

def test_codigo():
    raw_file = "tests/data/sample.raw"
    seq_file = "tests/data/sample.seq"
    raw = psse34parser.read_case_raw(raw_file)
    seq = psse34parser.read_case_seq(seq_file)
    codigo = psse34parser.crea_codigo(raw, seq)

    assert isinstance(codigo, str)
