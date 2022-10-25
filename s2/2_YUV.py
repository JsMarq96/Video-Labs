#!/usr/bin/env python3

import os


def compose_histogram(s, result):
    '''
    Uses ffmpeg terminal utility
    s: string, the source file
    result: string, the resulting size
    '''
    os.system('ffmpeg -y -i ' + s + ' -filter_complex "[0:v]split=2[v0][v1]; \
    [v0]histogram=display_mode=stack,scale=1280:720,setsar=1,format=yuv420p[v2];\
    [v1]scale=1280/6:720/6,setsar=1[v3]; \
    [v2][v3]overlay=x=W-w-50:y=50[v]" -map \'[v]\' -an "' + result + '"')


if __name__ == '__main__':
    compose_histogram('crop.mp4', 'result.mp4')
