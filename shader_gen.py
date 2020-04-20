import skimage
import io
import imageio
import numpy

img = imageio.imread('image.png')

print("#version 450")
print("layout(location = 0) out vec4 c;void main(){uint a[" + str(img.shape[0]) + "][" + str(img.shape[1]) + "] = {", end = '')
for row in img:
    print("{", end = '')
    for val in row:
        packed = val[0].astype(numpy.uint32) | (val[1].astype(numpy.uint32) << 8) | (val[2].astype(numpy.uint32) << 16) | (val[3].astype(numpy.uint32) << 24)
        print(str(packed) + ",", end = '')
    print("},", end = '')
print("};", end = '')
print("c = unpackUnorm4x8(a[int(floor(gl_FragCoord.y*" + str(img.shape[1]) + "/512))][int(floor(gl_FragCoord.x*" + str(img.shape[0]) + "/512))]);", end = '')
print("}", end = '')
