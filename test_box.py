import unittest
from box import Box

class BoxTestCase(unittest.TestCase):
    def test_box_init(self):
        self.assertRaises(ValueError, Box,2.0,4.0,1.0,5.0)

    def test_overlap(self):
        box1=Box(2.0,1.0,5.0,5.0)
        box2=Box(3.0,2.0,5.0,7.0)
        self.assertEqual(box1.overlap(box2), True)

    def test_non_overlap(self):
        box1=Box(1.0,1.0,3.0,3.0)
        box2=Box(10.0,10.0,30.0,30.0)
        self.assertEqual(box1.overlap(box2), False)

    def test_contains(self):
        box1=Box(0.0,0.0,10.0,10.0)
        box2=Box(1.0,1.0,2.0,2.0)
        self.assertEqual(box1.contains(box2), True)

    def test_contains_false(self):
        box1=Box(0.0,0.0,10.0,10.0)
        box2=Box(1.0,1.0,2.0,2.0)
        self.assertEqual(box2.contains(box1), False)


if __name__ == '__main__':
    unittest.main()
