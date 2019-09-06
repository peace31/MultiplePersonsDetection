import numpy as np
from moviepy.editor import *
from moviepy.Clip import *
from moviepy.video.VideoClip import *
from moviepy.editor import *
import cv2
import os
from natsort import natsorted
import glob
# image_folder = 'frameout'
# images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
# frame = cv2.imread(os.path.join(image_folder, images[0])).tolist()
# #height, width, layers = frame.shape
# Max_frames=100
# # clip  = VideoFileClip("TownCentreXVID.avi")
# # new_clip = clip.subclip( 0 / clip.fps, Max_frames / clip.fps)
# #
# # new_frames = [ frame for frame in new_clip.iter_frames()]
# #
# # nframe=new_frames[0:Max_frames]
# clips=[]
# for i in range (Max_frames):
#     #video.write(cv2.imread(os.path.join(image_folder, image)))
#     img=cv2.imread(os.path.join(image_folder, 'f'+str(i)+'.jpg'))
#     #img1=cv2.resize(img,(640,480))
#     clips.append(ImageClip(os.path.join(image_folder, 'f'+str(i)+'.jpg')))
#     #nframe[i]=img
#     # cv2.imshow("frame",img)
#     # cv2.waitKey(0)
base_dir = os.path.realpath("./frameout")
print(base_dir)

gif_name = 'pic'

fps = 24

file_list = glob.glob('*.jpg')  # Get all the pngs in the current directory
file_list_sorted = natsorted(file_list,reverse=False)  # Sort the images

clips = [ImageClip(m).set_duration(2)
         for m in file_list_sorted]

concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile("test.mp4", fps=fps)
#clip  = VideoFileClip("cirque1.mp4")
#new_frames = [ frame for frame in clip.iter_frames()]
# video = ImageSequenceClip(nframe, fps=clip.fps)
# # video.write_videofile('test.mp4', fps=clip.fps)
# video = concatenate_videoclips(clips, method='compose')
# video.write_videofile('test.mp4',fps=24)
# cv2.destroyAllWindows()
print ("done")