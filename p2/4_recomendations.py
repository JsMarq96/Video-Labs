#!/usr/bin/env python3

from analizer_ex1 import fetch_data_of_video

# Knoleadge base of the suppoerted codecs of each broadcasting protocol
broadcasting_data = {'ATSC': {'video': ['mpeg2', 'h264'],
                              'audio': ['ac3']},
                     'DTMB': {'video': ['mpeg2', 'h264', 'avs', 'avs+'],
                              'audio': ['ac3', 'aac', 'dra', 'mp3', 'mp2']}
                     }


def check_codec_compatiblity(video_dir):
    video_data = fetch_data_of_video(video_dir)

    usable_broadcasting = []

    for standart in broadcasting_data:
        compatible_codecs = broadcasting_data[standart]

        # Check if audio and video's codecs are present on the supported list
        # of the protocol
        if video_data['video_codec'] in compatible_codecs['video']:
            if video_data['audio_codec'] in compatible_codecs['audio']:
                usable_broadcasting.append(standart)

    return usable_broadcasting


if __name__ == '__main__':
    print('Recomended: ', check_codec_compatiblity('BBB.mp4'))
