Since the goal is to reduce the quality, I took lenna.png, converted it to lenna_out.jpeg, and downscalled it; while also setting the quantization to the max, resulting in a loose of quality, perceptually and data wise.

I used the command:


ffmpeg -i lenna.png -vf scale=iw/2:ih/2 -q:v 30 lenna_out.jpeg
