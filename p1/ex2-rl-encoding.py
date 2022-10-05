#!/usr/bin/env python3
import sys


def run_lenght_encode(byte_sequence):
    result = []
    curr_element = byte_sequence[0]
    curr_count = 1

    for byte in byte_sequence[1:]:
        if byte == curr_element:
            curr_count += 1
        else:
            result.append((curr_element, curr_count))
            curr_element = byte
            curr_count = 1

    result.append((curr_element, curr_count))
    return result


if __name__ == '__main__':
    # Get the bytes of all the input commands, contenated
    byte_list = bytes([int(x) for x in sys.argv[1:]])

    print(run_lenght_encode(byte_list))
