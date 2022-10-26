#!/usr/bin/env python3

import ffmpeg
import sys


def resize_video(video_input, video_output, width, height):
    '''
    Scale the input video witht he specified aspect ratio
    video_input: (string)
    video_output: (string)
    width: (int)
    height: (int)
    '''
    input_vid = ffmpeg.input(video_input)
    input_vid.filter('scale', width, height) \
        .output(video_output) \
        .overwrite_output() \
        .run()


if __name__ == '__main__':
    '''
    Convert the crop.mp4 video to the selected resolutions
    '''

    resize_video('BBB.mp4', 'adjusted.mp4', int(sys.argv[1]), int(sys.argv[2]))
