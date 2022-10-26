#!/usr/bin/env python3

import subprocess
import ffmpeg
import sys


class cVideoUtils:

    def __init__(self, video):
        self.video_dir = video

    '''
    First exercise ================
    '''
    def fetch_data_of_video(self):
        query = 'ffmpeg -i ' + self.video_dir + '; exit 0'

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
                'audio_coded': audio_codec}

    '''
    Second exercise ================
    '''
    def crop_video(self, output_name, secs):
        # edit the video
        stream = ffmpeg.input(self.video_dir)
        video = stream.video.trim(start=0, end=int(secs))
        audio = stream.audio.filter_('atrim', start=0, end=int(secs))
        ffmpeg.output(audio, video, output_name).run()

    def export_audio(self, output_sound):
        video = ffmpeg.input(self.video_dir)
        video.output(output_sound).run()

    def export_audio_lower_bitrate(self, output_sound):
        # Get the current bitrate, so it server as a reference
        probe_stream = ffmpeg.probe(self.video_dir)['streams']
        audio_inf = next(s for s in probe_stream if s['codec_type'] == 'audio')
        bit_rate = float(audio_inf['bit_rate'])

        video = ffmpeg.input(self.video_dir)
        video.output(output_sound, audio_bitrate=bit_rate / 10).run()

    def package_video(self, new_audio, output_name):
        stream = ffmpeg.input(self.video_dir)
        audio = ffmpeg.input(new_audio).audio
        ffmpeg.output(audio, stream.video, output_name).run()

    '''
    Third exercise ====================
    '''
    def resize_video(self, video_output, width, height):
        '''
        Scale the input video witht he specified aspect ratio
        video_input: (string)
        video_output: (string)
        width: (int)
        height: (int)
        '''
        input_vid = ffmpeg.input(self.video_dir)
        input_vid.filter('scale', width, height) \
                 .output(video_output) \
                 .overwrite_output() \
                 .run()


if __name__ == '__main__':
    # First exercise
    video_utility = cVideoUtils('BBB.mp4')
    print(video_utility.fetch_data_of_video())

    # Second exercise
    video_utility.crop_video('crop.mp4', 60)

    cropped_video = cVideoUtils('crop.mp4')
    cropped_video.export_audio('audio.mp3')
    cropped_video.export_audio_lower_bitrate('audio.aac')
    cropped_video.package_video('audio.aac', 'result_aac.mp4')
    cropped_video.package_video('audio.mp3', 'result_mp3.mp4')

    # Third exercise
    cropped_video.resize_video('adjusted.mp4', 100, 200)
