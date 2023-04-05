from triangle import triangle

def test_invalid():
    assert triangle(-1,0,1) == -1

def test_equilateral():
    assert triangle(3,3,3) == 1