import pytest

from src.crypto.keyless import B64


@pytest.mark.parametrize('got,expected',
                         [('Hello, Crypto!', 'SGVsbG8sIENyeXB0byE='),
                          ('Привет, крипто!', '0J/RgNC40LLQtdGCLCDQutGA0LjQv9GC0L4h'),
                          ('😀', '8J+YgA=='),
                          ('137000', 'MTM3MDAw'),
                          ('ワン', '44Ov44Oz'),
                          ('', ''),
                          (' ', 'IA==')])
def test_encode(got, expected):
    assert B64.encode64(got) == expected


@pytest.mark.parametrize('got,expected',
                         [('SGVsbG8sIENyeXB0byE=', 'Hello, Crypto!'),
                          ('0J/RgNC40LLQtdGCLCDQutGA0LjQv9GC0L4h', 'Привет, крипто!'),
                          ('8J+YkQ==', '😑'),
                          ('MzIx', '321'),
                          ('44Gm', 'て'),
                          ('', ''),
                          ('IA==', ' ')])
def test_decode(got, expected):
    assert B64.decode64(got) == expected


def test_attribute_error():
    with pytest.raises(AttributeError):
        B64.encode64(123)
