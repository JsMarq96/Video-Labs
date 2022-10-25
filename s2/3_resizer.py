#!/usr/bin/env python3

import ffmpeg


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
    formats = [(1280, 720),
               (640, 480),
               (360, 240),
               (160, 120)]

    i = 0
    for w, h in formats:
        resize_video('crop.mp4', 'res_' + str(i) + '.mp4', w, h)
        i = i + 1
