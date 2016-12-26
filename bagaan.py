# USAGE
# python recognize.py --training images/training --testing images/testing

from featuredetectors.local_binary_pattern import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from imutils import paths
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--training", required=True,
                help="path to the training set")
ap.add_argument("-e", "--testing", required=True,
                help="path to the test images")
args = vars(ap.parse_args())
desc = LocalBinaryPatterns(24, 8)
data = []
labels = []

def shrink_image(image):
    r = 480.0 / image.shape[1]
    dim = (480, int(image.shape[0] * r))
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return image


for imagePath in paths.list_images(args["training"]):
    image = cv2.imread(imagePath)
    image = shrink_image(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    labels.append(imagePath.split("/")[-2])
    data.append(hist)

model = LinearSVC(C=100.0, random_state=42)
model.fit(data, labels)

for imagePath in paths.list_images(args["testing"]):
    image = cv2.imread(imagePath)
    image = shrink_image(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist)[0]
    
    cv2.putText(image, prediction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 0, 255), 3)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
