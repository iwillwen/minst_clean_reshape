import os
import imageio
from clean_reshape import cleanAndReshapeImage

def test(number):
  print('Number: {0}'.format(number))
  imgPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./test_images/{0}.png".format(number))
  img = imageio.imread(imgPath)
  processedImg = cleanAndReshapeImage(img)
  print(processedImg)
  print('')

if __name__ == '__main__':
  test(0)
  test(1)
  test(2)
  test(3)
  test(4)
  test(5)
  test(6)
  test(7)
  test(8)
  test(9)