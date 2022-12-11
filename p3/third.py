#!/usr/bin/env python3

import ffmpeg

SERVER_URL = 'http://127.0.0.1:8080'

# Stream a video using Flash video
def livestream_video(video):
    vid = video.output(SERVER_URL,
                       codec='copy',
                       listen=1,
                       f='flv')
    vid = vid.global_args("-re")
    return vid


if __name__ == '__main__':
    video = ffmpeg.input('video_example.mp4')

    stream = livestream_video(video)

    stream.run()

    # In order to open the stream, you can use the command
    #       ffplay -f flv http://192.168.1.40:8080
    # With that the being the local IP of the machine running
    # the stream
