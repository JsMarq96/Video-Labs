#!/usr/bin/env python3

import ffmpeg


def export_as_HLS(video_source, output_name, time):
    result = video_source.output(output_name,
                                 format='hls',
                                 hls_time=time,
                                 hls_playlist_type='event')
    return result


if __name__ == '__main__':
    video = ffmpeg.input('video_example.mp4')

    video = export_as_HLS(video, 'result.mp4', 8)

    video.run()
