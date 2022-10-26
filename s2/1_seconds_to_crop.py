#!/usr/bin/env python3

import sys
import ffmpeg


def crop_video(source, output_name, secs):
    # get the fps, via a ffmpeg probe
    probe_stream = ffmpeg.probe(source)['streams']
    video_info = next(s for s in probe_stream if s['codec_type'] == 'video')
    fps = float(video_info['r_frame_rate'].split('/')[0])

    # edit the video
    stream = ffmpeg.input(source)
    stream = stream.trim(start_frame=0, end_frame=int(secs * fps))
    stream = stream.output(output_name)
    stream.run()


if __name__ == '__main__':
    stream = ffmpeg.input('big_buck_bunny_1080p_stereo.ogg')

    crop_video('big_buck_bunny_1080p_stereo.ogg', 'crop.mp4', int(sys.argv[1]))
