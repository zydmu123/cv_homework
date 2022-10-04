from faceDetector import *
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", default=r'data/haarcascades_cuda/haarcascade_frontalface_default.xml', help = "Path to where the face cascade resides")
ap.add_argument("-i", "--image", default='Lena.png', help = "Path to where the image file resides")
ap.add_argument("-r", "--result", default = "detectResult.jpg", help = "Path to save the results")

args = vars(ap.parse_args())
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 加载Haar级联分类器
fd = FaceDetector(args["face"])
faceRects = fd.detect(gray, scaleFactor = 1.1, minNeighbors = 8, minSize = (30, 30))

# 打印结果
for x, y, w, h in faceRects:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


# 添加文本
font=cv2.FONT_HERSHEY_PLAIN
cv2.putText(image,'Lena',(90,55),font, 2,(255,0,0),2)

cv2.imshow("Faces", image)
cv2.imwrite(args["result"], image)
cv2.waitKey(0)


