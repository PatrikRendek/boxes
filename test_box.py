import unittest
from boxes.box import Box


class BoxTestCase(unittest.TestCase):
    def test_box_init(self):
        self.assertRaises(ValueError, Box,2.0,4.0,1.0,5.0)
    def test_overlap(self):
        box1=Box(2.0,1.0,5.0,5.0)
        box2=Box(3.0,2.0,5.0,7.0)
        self.assertEqual(box1.check_overlap(box2), True)


if __name__ == '__main__':
    unittest.main()
