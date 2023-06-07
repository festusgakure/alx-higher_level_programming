#!/usr/bin/python3
for numb in range(97, 123):
    if chr(numb) not in ['e', 'q']:
        print("{}".format(chr(numb)), end="")
