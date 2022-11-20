The repo is at: https://github.com/JsMarq96/Video-Labs/tree/main/s3 


About the video analisis:
The order of each video's bitrate:
1) 400k
2) 200k
3) 100k
4) 50k

I will focus on the first frames, with the fade in and the sky, wich seemed more telling.

- AV1 codec:
It manages to have a very nitid image, without an apparent lose in clarity on subject like the trees, even with a 50k bitrate;
but with details with a more "high frequency" like the noise-like clouds, the blocking is apparent at the lower bitrate,
but its performance and clarity is astounding, specially compared to the other codecs.

- VP9 codec:
The blocking is very apparent up to 400k bitrate in the high frequency clouds, and on 50k 100k its still a loss of detail
on the trees, specially on teh borders of the frame, where we dont have a lot cof continuity data.

- VP8 codec:
The performance is really bad all over the table, specially when comparing tot he previus two, with blocking clearly visible,
and problems maintainign the color palet on the 50 and 100k bitrates. Out of these for, I would only consider whatchable 
400k version.

- h256 codec:
I found the performance very similar to the VP9, but with worse blocking ocurring all across the board on the clouds; but had 
no trouble maintaining the less challenging detail of the trees, even at lower bitrates