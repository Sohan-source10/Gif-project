import imageio.v3 as iio

frames = ['Frames/Pixel art hero 1.png', 'Frames/Pixel art hero 2.png']
images = []

for frame in frames:
    images.append(iio.imread(frame))

iio.imwrite("Pixel_Hero.gif", images, duration=500, loop=0)