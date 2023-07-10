#!/usr/bin/python3
"""0x01. Lockboxes"""

def canUnlockAll(boxes):
    keyz = set(boxes[0])

    # check if boxes can be opened
    for i in range( len(boxes)):

        if i in keyz or i == 0:
            # print("inside loop {}".format(i))
            keyz.update(set(boxes[i]))
        else :
            # print("Breaking here")
            # print(i)
            # print(keyz)
            return False
        
    return True


# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes))

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes))

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes))

# save all the keys as you collect them in a non-duplicating datastructure eg set
# iterete over the box list and compare the box index with the saved keys to see /
# if the key exist for that index in the cummulated keys, save the keys in that box index
# no_dup.update(set(dd))

