#!/usr/bin/env python3

import ffmpeg


def resize_video(video_input, video_output, width, height, codec):
    '''
    Scale the input video witht he specified aspect ratio
    video_input: (string)
    video_output: (string)
    width: (int)
    height: (int)
    '''
    input_vid = ffmpeg.input(video_input)
    input_vid.filter('scale', width, height) \
        .output(video_output, vcodec=codec) \
        .overwrite_output() \
        .run()


if __name__ == '__main__':
    '''
    Convert the crop.mp4 video to the selected resolutions
    '''
    '''
    Convert the crop.mp4 video to the selected resolutions
    '''
    formats = [(1280, 720),
               (640, 480),
               (360, 240),
               (160, 120)]

    codecs = [('libvpx', '.webm'),
              ('libvpx-vp9', '.webm'),
              ('libx265', '.mp4'),
              ('libaom-av1', '.webm')]

    for codec, ext in codecs:
        print('Processing codec ', codec)
        for res in formats:
            file_name = codec + '_' + str(res[0]) + 'x' + str(res[1])
            resize_video('BBB.mp4', file_name + ext, res[0], res[1], codec)
