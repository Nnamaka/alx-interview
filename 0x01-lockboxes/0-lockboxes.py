#!/usr/bin/python3
"""0x01. Lockboxes"""


def canUnlockAll(boxes):
    keyz = set(boxes[0])

    # check if boxes can be opened
    for i in range(len(boxes)):

        if i in keyz or i == 0:
            keyz.update(set(boxes[i]))
        else:
            found = False

            for j in keyz:
                if j >= len(boxes):
                    continue

                if i in boxes[j]:
                    keyz.update(set(boxes[j]))
                    found = True
                    break
            if not found:
                return False

    return True

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))