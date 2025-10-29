import unittest
import HtmlTestRunner
from tinh_tien import tinh_tien

class TestTinhTien(unittest.TestCase):

    def test_invalid_ve_thuong(self):
        # TC1: soVeThuong < 0
        self.assertEqual(tinh_tien(-1, 10, 25), "Invalid")

    def test_invalid_ve_3d(self):
        # TC2: soVe3D > 50
        self.assertEqual(tinh_tien(10, 60, 25), "Invalid")

    def test_invalid_tuoi(self):
        # TC3: tuoi <= 0
        self.assertEqual(tinh_tien(10, 10, 0), "Invalid")

    def test_giam_gia(self):
        # TC4: tuoi <= 22 → giảm 15%
        result = tinh_tien(10, 5, 20)
        expected = int(round((10*70000 + 5*120000) * 0.85))
        self.assertEqual(result, expected)

    def test_khong_giam_gia(self):
        # TC5: tuoi = 30 → không giảm
        result = tinh_tien(5, 5, 30)
        expected = int(round(5*70000 + 5*120000))
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='reports',       
            report_name='TinhTienReport.html',  
            combine_reports=True,
            add_timestamp=False
        )
    )
