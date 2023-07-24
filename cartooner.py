import cv2
import numpy as np

def color_quantization(img, k):
# Transform the image
  data = np.float32(img).reshape((-1, 3))

# Determine criteria
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

# Implementing K-Means
  ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result


def edge_mask(img, line_size, blur_value):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_blur = cv2.medianBlur(gray, blur_value)
  edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
  return edges


print("количество цветов на видео (рекомендуется 10-100)")
total_color = int(input())
line_size = 7
blur_value = 7
print("создание изображений...")
count = 1

vidcap = cv2.VideoCapture('vid.mp4')
success, image = vidcap.read()


while success:
  success, image = vidcap.read()

  edges = edge_mask(image, line_size, blur_value)
##  cv2.imshow('what',edges)

  image = color_quantization(image, total_color)
  ##cv2.imshow('what',img)

  blurred = cv2.bilateralFilter(image, d=7, sigmaColor=200,sigmaSpace=200)
  ##cv2.imshow('what',blurred)

  cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
  ##cv2.imshow('what',cartoon)

  cv2.imwrite(str(count) + '.jpg', cartoon)
  print("корректно сохранена " + str(count) + "-ая картинка")
  count += 1
