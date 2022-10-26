#!/usr/bin/env python3

import ffmpeg


def crop_video(source, output_name, secs):
    # edit the video
    stream = ffmpeg.input(source)
    video = stream.video.trim(start=0, end=int(secs))
    audio = stream.audio.filter_('atrim', start=0, end=int(secs))
    ffmpeg.output(audio, video, output_name).run()


def export_audio(input_video, output_sound):
    video = ffmpeg.input(input_video)
    video.output(output_sound).run()


def export_audio_lower_bitrate(input_video, output_sound):
    probe_stream = ffmpeg.probe(input_video)['streams']
    audio_info = next(s for s in probe_stream if s['codec_type'] == 'audio')
    bit_rate = float(audio_info['bit_rate'])

    video = ffmpeg.input(input_video)
    video.output(output_sound, audio_bitrate=bit_rate / 10).run()


def package_video(input_video, new_audio, output_name):
    stream = ffmpeg.input(input_video)
    audio = ffmpeg.input(new_audio).audio
    ffmpeg.output(audio, stream.video, output_name).run()


if __name__ == '__main__':

    crop_video('BBB.mp4', 'crop.mp4', 60)
    export_audio('crop.mp4', 'audio.mp3')
    export_audio_lower_bitrate('crop.mp4', 'audio.aac')
    package_video('crop.mp4', 'audio.aac', 'result_aac.mp4')
    package_video('crop.mp4', 'audio.mp3', 'result_mmp3.mp4')
