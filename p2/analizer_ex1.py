#!/usr/bin/env python3

import subprocess


def fetch_data_of_video(video_dir):
    query = 'ffmpeg -i ' + video_dir + '; exit 0'

    raw_data = str(subprocess.check_output(query,
                                           stderr=subprocess.STDOUT,
                                           shell=True))
    raw_data = raw_data.split('\\n')

    # To fill
    video_codec = ''
    video_resolution = ''
    audio_codec = ''

    for line in raw_data:
        if 'Video: ' in line:
            # Fetch video codec
            start = line.find('Video: ') + len('Video: ')
            video_codec = line[start:].split(' ')[0]

            # Fetch resolution
            video_resolution = line[start:].split(', ')[2]
        elif 'Audio: ' in line:
            start = line.find('Audio: ') + len('Audio: ')
            audio_codec = line[start:].split(' ')[0]

    return {'video_codec': video_codec,
            'video_res': video_resolution,
            'audio_codec': audio_codec}


if __name__ == '__main__':
    print(fetch_data_of_video('BBB.mp4'))
