import pytest
from tinh_tien import tinh_tien

@pytest.mark.parametrize("soVeThuong, soVe3D, tuoi, expected", [
    (25, 25, 2, 4037500),       
    (25, 25, 30, 4750000),      
    (25, 25, 0, "Invalid"),  
    (25, 25, 2*31-1, 4037500), 

    (25, -1, 0, "Invalid"),      
    (25, -1, 14, "Invalid"),
    (25, -1, 30, "Invalid"),
    (25, -1, 60, "Invalid"),

    (-1, 25, 0, "Invalid"),      
    (-1, 25, 21, "Invalid"),
    (-1, 25, 30, "Invalid"),
    (-1, 25, 60, "Invalid"),

    (-1, -1, 0, "Invalid"),      
    (-1, -1, 22, "Invalid"),
    (-1, -1, 30, "Invalid"),
    (-1, -1, 67, "Invalid"),
])
def test_decision_table(soVeThuong, soVe3D, tuoi, expected):
    assert tinh_tien(soVeThuong, soVe3D, tuoi) == expected
