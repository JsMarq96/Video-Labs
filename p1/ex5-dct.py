#!/usr/bin/env python3
import sys
from scipy.fftpack import dct, idct

if __name__ == '__main__':
    input_list = [float(x) for x in sys.argv[2:]]

    if sys.argv[1] == '--DCT':
        print(dct(input_list, 1, norm='ortho'))
    elif sys.argv[1] == '--iDCT':
        print(idct(input_list, 1, norm='ortho'))
    elif sys.argv[1] == '--DCT+IDCT':
        print(idct(dct(input_list, 1,  norm='ortho'), 1, norm='ortho'))
