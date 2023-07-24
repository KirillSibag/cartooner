import cv2
import moviepy.editor as moviepy
from time import sleep
import os

print("фотографий:")
count = int(input())
print("кадров в секунду:")
fps = int(input())

counter = 1
img_array = []
for i in range(count):
    img = cv2.imread(str(counter) + ".jpg")
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    if os.path.isfile(str(counter) + ".jpg"):
        os.remove(str(counter) + ".jpg")
    
    counter += 1

    if counter - 1 % 10 == 0:
      print("успешно превращены в видео " + str(counter) + " из " + str(count) + " фотографий")


out = cv2.VideoWriter('cartoon.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()


print("готово видео в формате .avi, но вы его нигде не воспроизведёте,")
print("сейчас произойдёт конвертация в .mp4")
print("конвертация...")
print()
clip = moviepy.VideoFileClip("cartoon.avi")
clip.write_videofile("result.mp4")
print()

print("программа завершена! спасибо, что воспользовались cartooner 1.2!")
print("терминал автоматически закроется через 60 секунд")
sleep(60)
