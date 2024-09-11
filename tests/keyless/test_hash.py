import pytest
from crypto.keyless import LetsHash

def test_md5():
    assert LetsHash('md5').hash('Hello, Crypto!') == 'b46433b9878f2bcdc06ad1eeb350b0be'

def test_sha1():
    assert LetsHash('sha1').hash('Hello, Crypto!') == 'cd111cb699aafff690458e5da87ebc1db6029a37'

def test_sha256():
    assert LetsHash('sha256').hash('Hello, Crypto!') == 'de0640f1dc17ca1b01fb9eba3019ed07c12e2af4ae990ecb36aa669898a9fd40'

def test_sha512():
    assert LetsHash('sha512').hash('Hello, Crypto!') == '7ae95e085f4040c9a2edad76a59c57330203bf837f1c2dd11910659ab325bdaa39ac774d68f253a41330eaad83ff091249865cea10a1b2978343954563cec8ac'

def test_blake2b():
    assert LetsHash('blake2b').hash('Hello, Crypto!') == '90ca3388d50ac6b7c359d1bd47fa7af2a6b9794d68304ca1c777b281a53bac9c577caca8e873d0eea3df382c1cb943522849169a7325eefcee47b31723ac86e2'

def test_blake2s():
    assert LetsHash('blake2s').hash('Hello, Crypto!') == '4f5be857360a27cfa1a2285bed46caa5436d5efe2f8e97934661097dfe963cc5'