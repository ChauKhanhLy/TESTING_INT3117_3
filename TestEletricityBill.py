import unittest
from electricity_bill import calculate_bill

class TestElectricityBill(unittest.TestCase):
    def test_boundary_values(self):
        self.assertEqual(calculate_bill(0, "residential", 30), 0.00)
        self.assertEqual(calculate_bill(50, "residential", 30), 30.00)
        self.assertEqual(calculate_bill(51, "residential", 30), 30.80)
        self.assertEqual(calculate_bill(100, "residential", 30), 70.00)
        self.assertEqual(calculate_bill(101, "residential", 30), 71.00)
        self.assertEqual(calculate_bill(200, "residential", 30), 170.00)
        self.assertEqual(calculate_bill(201, "residential", 30), 171.20)

    def test_business_and_discount(self):
        # Business surcharge
        self.assertEqual(calculate_bill(120, "business", 40), 99.00)
        # Elderly discount
        self.assertEqual(calculate_bill(50, "residential", 70), 27.00)
        # Business + elderly discount
        self.assertEqual(calculate_bill(120, "business", 70), 89.10)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate_bill(-1, "residential", 30)
        with self.assertRaises(ValueError):
            calculate_bill(1_000_001, "residential", 30)


if __name__ == "__main__":
    unittest.main()