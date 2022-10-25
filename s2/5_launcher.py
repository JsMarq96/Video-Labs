#!/usr/bin/env python3

import os
import sys


if __name__ == '__main__':
    exercise_num = int(sys.argv[1])

    if exercise_num == 1:
        os.system('python3 1_seconds_to_crop.py 11')
    elif exercise_num == 2:
        os.system('python3 2_YUV.py')
    elif exercise_num == 3:
        os.system('python3 3_resizer.py')
    elif exercise_num == 4:
        print('Not implemented...')
