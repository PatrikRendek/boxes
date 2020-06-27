from box import Box

def create_boxes_from_list(coordinates: list):
    """Create Box objects and add their in a list.

        Parameters:
        coordinates (list) -- list of coordinates

        Returns:
        list: list of Box objects
    """
    boxesObjs = list()
    for box in coordinates:
        box = Box(box[0], box[1], box[2], box[3])
        boxesObjs.append(box)
    return boxesObjs

def check_overlap(boxes: list):
    """Check for overlap in boxes and Raise ValueError if there is a overlap.

        Parameters:
        boxes (list) -- list of Box objects
    """
    for box1 in boxes:
        for box2 in boxes:
            if box1 is not box2:
                if box1.overlap(box2) and not box1.contains(box2) and not box2.contains(box1):
                    raise ValueError('Boxes overlap')


def check_land(boxes: list):
    """Check for land boxes.

        Parameters:
        boxes (list) -- list of Box objects

        Returns:
        int: Number of Box objects with land  == True
    """
    result = 0
    for box1 in boxes:
        for box2 in boxes:
            if box1 is not box2:
                if box1.contains(box2):
                    box2.nested += 1
    for box in boxes:
        if (box.nested % 2) == 0:
            result += 1
    return result


if __name__ == '__main__':
    """Get number of boxes and their coordinates from input."""

    boxCount = input("Number of boxes:")
    counter = 1
    boxes = []
    while counter != int(boxCount)+1:
        coordinates = input("Box {} coordinates:".format(counter))
        coordinates = coordinates.split(" ",)[:4]
        counter += 1
        boxes.append(coordinates)
    box_objs = create_boxes_from_list(boxes)
    check_overlap(box_objs)
    print("Land boxes: {}".format(check_land(box_objs)))
