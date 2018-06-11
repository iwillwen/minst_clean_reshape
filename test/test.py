import os
import importlib.util
import imageio

spec = importlib.util.spec_from_file_location("cleanAndReshape", os.path.join(os.path.dirname(os.path.realpath(__file__)), "../clean_reshape.py"))
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)

def test(number):
  print('Number: {0}'.format(number))
  imgPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./images/{0}.png".format(number))
  img = imageio.imread(imgPath)
  processedImg = cr.cleanAndReshapeImage(img)
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