#!/usr/bin/env python3
import sys

# Source:  https://en.wikipedia.org/wiki/YUV


def rgb_2_yuv(value):
    result = [0.0, 0.0, 0.0]

    result[0] = 0.299 * value[0] + 0.587 * value[1] + 0.114 * value[2]
    result[1] = -0.168736 * value[0] - 0.331264 * value[1] + 0.5 * value[2]
    result[1] += 128.0
    result[2] = 0.5 * value[0] - 0.41868 * value[1] - 0.08131 * value[2]
    result[2] += 128.0

    return result


def yuv_2_rgb(value):
    result = [0.0, 0.0, 0.0]

    U = value[1] - 128.0
    V = value[2] - 128.0

    result[0] = value[0] + 1.4075 * V
    result[1] = value[0] - 0.3455 * U - 0.7169 * V
    result[2] = value[0] + 1.779 * U

    return result


if __name__ == '__main__':
    # Read the commandline and fetch the pixel values,
    # into a float array
    input_color = [float(x) for x in sys.argv[2:5]]

    if sys.argv[1] == '--RGB2YUV':
        print(rgb_2_yuv(input_color))
    elif sys.argv[1] == '--YUV2RGB':
        print(yuv_2_rgb(input_color))
    elif sys.argv[1] == '--RGB2YUV2RGB':
        print(yuv_2_rgb(rgb_2_yuv(input_color)))
