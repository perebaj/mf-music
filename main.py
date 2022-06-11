import cv2
import os

image_folder = './images'
video_name = 'video.avi'
each_image_duration = 5 # in secs
fourcc = cv2.VideoWriter_fourcc(*'XVID') # define the video codec

images = [img for img in os.listdir(image_folder) if img.endswith(".jpeg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
print(frame.shape)

video = cv2.VideoWriter(video_name, fourcc, 1.0, (width, height))

for image in images:
    for _ in range(each_image_duration):
        video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()