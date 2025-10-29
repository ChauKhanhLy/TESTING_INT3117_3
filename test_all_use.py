import unittest
from tinh_tien import tinh_tien

class TestAllUses(unittest.TestCase):
  
    def test_soVeThuong_0_1(self):
        self.assertEqual(tinh_tien(-1, 10, 30), "Invalid")  

    def test_soVeThuong_0_7(self):
        self.assertEqual(tinh_tien(10, 10, 30), 1900000)     

    def test_soVe3D_0_3(self):
        self.assertEqual(tinh_tien(10, 51, 30), "Invalid")   

    def test_soVe3D_0_7(self):
        self.assertEqual(tinh_tien(10, 10, 30), 1900000)     

    def test_tuoi_0_5(self):
        self.assertEqual(tinh_tien(10, 10, -5), "Invalid")  

    def test_tuoi_0_8(self):
        self.assertEqual(tinh_tien(10, 10, 20), 1615000)     
    def test_base_7_9(self):
        self.assertEqual(tinh_tien(10, 10, 20), 1615000)    

    def test_base_7_10(self):
        self.assertEqual(tinh_tien(10, 10, 30), 1900000)     

    def test_base_9_10(self):
        self.assertEqual(tinh_tien(10, 10, 65), 1615000)     


if __name__ == '__main__':
    unittest.main()
