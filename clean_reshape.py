import sys
import pandas as pd
import numpy as np
import imageio as imageio
from sklearn import svm
from skimage import transform
from skimage import color
  
def cleanAndReshapeImage(imageArray):
  # Resize the image into 28x28
  img = transform.resize(imageArray, (28, 28))

  # Convert the image's RGB to grayscale array
  grays = color.rgb2gray(img).flatten()

  # Training the SVM model
  clf = svm.SVC()
  clf.fit([
    [ np.min(grays), np.min(grays) ],
    [ np.max(grays), np.max(grays) ]
  ], [ 1, 0 ])

  # Converting the grayscale array to a 2d ndarray
  grays_2d = np.zeros((len(grays), 2))
  for i in range(len(grays)):
    grays_2d[i][0] = grays[i]
    grays_2d[i][1] = grays[i]

  # Execute the SVM model
  prediction = clf.predict(grays_2d)
  predDF = pd.DataFrame({ 'pred': prediction })
  writeprintIndexes = predDF[predDF['pred'] == 1].index

  processedImg = np.zeros(len(grays), dtype=int)

  for i in range(len(writeprintIndexes)):
    processedImg[writeprintIndexes[i]] = 1

  # Reshape the image
  processedImg = np.reshape(processedImg, (-1, np.sqrt(len(grays)).astype(int)))

  rowsSum = np.sum(processedImg, axis=1)
  cropedImg = np.array([], dtype=int)

  for i, sum in np.ndenumerate(rowsSum):
    if sum > 0:
      cropedImg = np.append(cropedImg, processedImg[i])

  cropedImg = np.reshape(cropedImg, (-1, 28))
  nrow = len(cropedImg)

  processedImgCols = np.rot90(cropedImg)
  colsSum = np.sum(processedImgCols, axis=1)
  cropedImg = np.array([], dtype=int)

  for i, sum in np.ndenumerate(colsSum):
    if sum > 0:
      cropedImg = np.append(cropedImg, processedImgCols[i])

  cropedImg = np.reshape(cropedImg, (-1, nrow))
  cropedImg = np.rot90(cropedImg, k=3)

  cropedImg = transform.resize(color.gray2rgb(cropedImg), (28, 28))
  grays = color.rgb2gray(cropedImg) * 1e19
  resizedImg = np.zeros(grays.shape, int)

  for index, g in np.ndenumerate(grays):
    if g > 1:
      resizedImg[index] = 1

  return resizedImg

if __name__ == '__main__':
  print(sys.argv)
  if len(sys.argv) > 1:
    imagePath = sys.argv[1]
    img = imageio.imread(imagePath)

    processedImg = cleanAndReshapeImage(img)
    print(processedImg)