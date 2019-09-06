

import numpy as np
import os.path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
#from skimage import io
import time
import argparse
import cv2
import random
from sort import Sort
from detector import GroundTruthDetections
# random color generation function and return label string
def random_color(seed_index,labelstring):
    # generate one random number
    random.seed(seed_index)
    r=random.random()
    # decide color and label string according to probability
    if(r<0.7):
        val=(255,0,0)
        return val, labelstring[0]
    elif(r>=0.7 and r<0.85):
        val=(0,255,0)
        return val, labelstring[1]
    else:
        val=(0,0,255)
        return val, labelstring[2]

def main():
    # Max frame number to detect and track
    Max_frames=800
    # video file name
    video_path='TownCentreXVID.avi'
    # label string list given by users.
    labelstring=['good person', 'bad person','Good person']
    # video capture
    vidcap = cv2.VideoCapture(video_path)
    #args = parse_args()
    display = True
    #use_dlibTracker  = args.use_dlibTracker
    saver = False

    total_time = 0.0
    total_frames = 0

    # for disp
    if display:
        colours = np.random.rand(32, 3)  # used only for display
        # plt.ion()
        # fig = plt.figure(figsize=(10,5))


    #init detector
    detector = GroundTruthDetections()

    #init tracker
    tracker =  Sort(use_dlib= False) #create instance of the kalman tracker

    frames = detector.get_total_frames()
    for frame in range(0, frames):  # frame numbers begin at 0!
        # get detections
        detections = detector.get_detected_items(frame)
        # get the total frames
        total_frames += 1
        if (total_frames > Max_frames):
            break
        # get one fram from video
        success, img = vidcap.read()
        # fn = 'test/frame%d.jpg' % (frame)  # video frames are extracted to 'test/Pictures%d.jpg' with ffmpeg
        # img = io.imread(fn)
        # if (display):
        #     ax1 = fig.add_subplot(111, aspect='equal')
        #     ax1.imshow(img)

        start_time = time.time()
        # update tracker
        trackers = tracker.update(detections, img)
        # time tracking
        cycle_time = time.time() - start_time
        total_time += cycle_time

        print('frame: %d...took: %3fs' % (frame, cycle_time))
        # object tracking
        for d in trackers:
            #f_out.write('%d,%d,%d,%d,x,x,x,x,%.3f,%.3f,%.3f,%.3f\n' % (d[4], frame, 1, 1, d[0], d[1], d[2], d[3]))
            if (display):
                d = d.astype(np.int32)
                color, label_string = random_color(d[4], labelstring)
                # add rectangle of object
                cv2.rectangle(img, (d[0], d[1]), (d[2], d[3]), color, 3)
                # ax1.add_patch(patches.Rectangle((d[0], d[1]), d[2] - d[0], d[3] - d[1], fill=False, lw=3,
                #                                 ec=color))
                # ax1.set_adjustable('box-forced')
                # add label string
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, label_string, (d[0], d[1]), font, 1, color, 2, cv2.LINE_4)
                # ax1.annotate(label_string, xy=(d[0], d[1]), xytext=(d[0], d[1]))
                # if detections != []:  # detector is active in this frame
                #     ax1.annotate(" DETECTOR", xy=(5, 45), xytext=(5, 45))
        if (display):
            # plt.axis('off')
            # #fig.canvas.flush_events()
            # plt.draw()
            # fig.tight_layout()
            cv2.imshow("frame",img)
            cv2.waitKey(0)
            # save the frame with tracking boxes
            if (saver):
                cv2.imwrite("frameout/f"+str(frame)+".jpg",img)
            #     fig.set_size_inches(18.5, 10.5)
            #     fig.savefig("frameout/f%d.jpg" % frame, dpi=200)
            # ax1.cla()




    print("Total Tracking took: %.3f for %d frames or %.1f FPS"%(total_time,total_frames,total_frames/total_time))
"""""
def parse_args():
    #Parse input arguments.
    parser = argparse.ArgumentParser(description='Experimenting Trackers with SORT')
    parser.add_argument('--NoDisplay', dest='display', help='Disables online display of tracker output (slow)',action='store_false')
    parser.add_argument('--dlib', dest='use_dlibTracker', help='Use dlib correlation tracker instead of kalman tracker',action='store_true')
    parser.add_argument('--save', dest='saver', help='Saves frames with tracking output, not used if --NoDisplay',action='store_true')

    args = parser.parse_args()
    return args
"""
if __name__ == '__main__':
    main()