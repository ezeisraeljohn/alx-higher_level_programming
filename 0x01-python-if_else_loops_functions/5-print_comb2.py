#!/usr/bin/python3
for i in range(0, 100):
    if i != 99:
        cus_string = "{}, ".format(i) if i > 9 else "{}, ".format("0" + str(i))
        print(cus_string, end = "")
    if i == 99:
        print(i)
