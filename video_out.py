import cv2
import os

image_folder = 'frameout'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 5, (width,height))

#video = cv2.VideoWriter(video_name, -1, 1, (width,height))

for i in range (len(images)):
    #video.write(cv2.imread(os.path.join(image_folder, image)))
    img=cv2.imread(os.path.join(image_folder, 'f'+str(i)+'.jpg'))
    #cv2.imshow('showimage',img)
    #cv2.waitKey(0)
    out.write(img)
cv2.destroyAllWindows()
out.release()
#video.release()