import unittest
from land_sea import check_land, check_overlap, create_boxes_from_list
class LandSeaTestCase(unittest.TestCase):

    def test_check_overlap(self):
        boxes = ((1.0, 1.0, 10.0, 10.0),
                     (2.0, 2.0, 11.0, 11.0))
        boxObjs = create_boxes_from_list(boxes)
        self.assertRaises(ValueError, check_overlap, boxObjs)

    def test_land(self):
        boxes = ((1.0, 1.0, 10.0, 6.0),
                 (1.5, 1.5, 6.0, 5.0),
                 (2.0, 2.0, 3.0, 3.0),
                 (2.0, 3.5, 3.0, 4.5),
                 (3.5, 2.0, 5.5, 4.5),
                 (4.0, 3.5, 5.0, 4.0),
                 (4.0, 2.5, 5.0, 3.0),
                 (7.0, 3.0, 9.5, 5.5),
                 (7.5, 4.0, 8.0, 5.0),
                 (8.5, 3.5, 9.0, 4.5),
                 (3.0, 7.0, 8.0, 10.0),
                 (5.0, 7.5, 7.5, 9.5),
                 (5.5, 8.0, 6.0, 9.0),
                 (6.5, 8.0, 7.0, 9.0))
        boxObjs = create_boxes_from_list(boxes)
        result = check_land(boxObjs)
        self.assertEqual(9, result)





if __name__ == '__main__':
    unittest.main()
