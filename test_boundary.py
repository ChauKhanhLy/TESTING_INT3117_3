import pytest
from tinh_tien import tinh_tien

@pytest.mark.parametrize("soVeThuong, soVe3D, tuoi, expected", [
    (25, 25, 0, "Invalid"),           
    (25, 25, 1, 4037500),              
    (25, 25, 30, 4750000),            
    (25, 25, 2**31-2, 4037500),    
    (25, 25, 2**31-1, 4037500),  
    (25, 0, 30, 1750000),      
    (25, 1, 30, 1870000),        
    (25, 49, 30, 7630000),       
    (25, 50, 30, 7750000),     
    (0, 25, 30, 3000000),          
    (1, 25, 30, 3070000),            
    (49, 25, 30, 6430000),           
    (50, 25, 30, 6500000),         
])
def test_boundary_values(soVeThuong, soVe3D, tuoi, expected):
    assert tinh_tien(soVeThuong, soVe3D, tuoi) == expected
