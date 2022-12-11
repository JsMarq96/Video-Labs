#!/usr/bin/env python3

import os

def to_MPD(video_file, result, frag_duration, key):
    # First, fragment the video
    fragment_video = 'frag_' + video_file
    command_frag = 'mp4fragment ' + video_file
    command_frag = command_frag + ' --fragment-duration '
    command_frag = command_frag + str(frag_duration)
    command_frag = command_frag + ' ' + fragment_video

    print(command_frag)
    os.system(command_frag)

    # then, package it, using the marlin DRM,
    # since according to bento4's docs, is the simplest way
    # to DRM a DASH stream

    DRM_command_frag = 'mp4dash --marlin --encryption-key='
    DRM_command_frag = DRM_command_frag + key
    DRM_command_frag = DRM_command_frag + ' '
    DRM_command_frag = DRM_command_frag + fragment_video

    print(DRM_command_frag)
    os.system(DRM_command_frag)

if __name__ == '__main__':
    key = '121a0fca0f1b475b8910297fa8e0a07e:a0a1a2a3a4a5a6a7a8a9aaabacadaeaf'

    to_MPD('video_example.mp4', 'mpd_video', 4000, key)


    '''
        How to play
        If the data is un-DRMed, you can open the stream using ffmplay, like:
            ffplay stream.mpd
        being the .mpd file on the root of the output folder generated from
        bento4.
        But if its DRMed, the result will be a corrupted stream (but with the
        correct aspect ratio).
        For a correct viewing, it will need to be decripted first.
    '''
