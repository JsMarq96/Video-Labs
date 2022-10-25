#!/usr/bin/env python3

import os


def video_audio_convertion(video, result):
    os.system('ffmpeg -i '+video+' -ac 1 '+result)
