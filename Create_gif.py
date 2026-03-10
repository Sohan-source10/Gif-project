import imageio.v3 as iio

frames = ['Frames/dino1.png', 'Frames/dino2.png', 'Frames/dino3.png', 'Frames/dino4.png']
images = []

for frame in frames:
    images.append(iio.imread(frame))

iio.imwrite("dino.gif", images, duration=2.0, loop=0)