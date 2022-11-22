#!/usr/bin/env python3

import ffmpeg
import os


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


def resize_bitrate(video_input, video_output, width, height, codec, bitrate):
    '''
    Scale the input video witht he specified aspect ratio
    video_input: (string)
    video_output: (string)
    width: (int)
    height: (int)
    '''
    input_vid = ffmpeg.input(video_input)
    input_vid.filter('scale', width, height) \
        .output(video_output, vcodec=codec, **{'b:v': bitrate}) \
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

    bitrates = ['400k',
                '200k',
                '100k',
                '50k']

    codecs = [('libvpx', '.webm'),
              ('libvpx-vp9', '.webm'),
              ('libx265', '.mp4'),
              ('libaom-av1', '.webm')]

    # Part 1, export at diferent res
    for codec, ext in codecs:
        print('Processing codec ', codec)
        for res in formats:
            file_name = codec + '_' + str(res[0]) + 'x' + str(res[1])
            resize_video('BBB.mp4', file_name + ext, res[0], res[1], codec)
    
    # Export each codec at 4 different bitrates
    for codec, ext in codecs:
        print('Processing codec ', codec)
        res = formats[0]
        for bits in bitrates:
            file_name = codec + '_' + bits
            resize_bitrate('BBB.mp4',
                           file_name + ext,
                           res[0],
                           res[1],
                           codec,
                           bits)

    # Merge the videos of the same codec, and different bitrates
    for codec, ext in codecs:
        commands = 'ffmpeg'
        print('Processing codec ', codec)
        res = formats[0]
        for bits in bitrates:
            file_name = codec + '_' + bits
            commands = commands + ' -i ' + file_name + ext

        res_name = 'res_' + codec + '.webm'
        commands = commands + ' -filter_complex hstack=inputs=4 ' + res_name
        print(commands)
        os.system(commands)
