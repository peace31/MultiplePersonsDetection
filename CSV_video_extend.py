

import csv
import urllib
import cv2
import numpy as np
# getting bounding box coordinate with width and height
def coordinate_get(annotation):
    X=[];Y=[];W=[];H=[]
    Fstr=annotation.split('}')
    num=0
    for annotation in Fstr:
        if(annotation==']'  or annotation==''):
            continue
        vstr = annotation.split(':')
        if(num==0):
            for k in range(2,6):
                vv=vstr[k].split(',')
                if(k==2):
                    x=int(vv[0])
                elif(k==3):
                    y=int(vv[0])
                elif(k==5):
                    width=int(vv[0])
                else:
                    height=int(vv[0])
            num+=1
        else:
            for k in range(1,5):
                vv=vstr[k].split(',')
                if(k==1):
                    x=int(vv[0])
                elif(k==2):
                    y=int(vv[0])
                elif(k==4):
                    width=int(vv[0])
                else:
                    height=int(vv[0])
        X.append(x)
        Y.append(y)
        W.append(width)
        H.append(height)
    return X,Y,W,H
img_lab=[]# image label array
img_bounding=[]# image  coordinate array
img_url=[]# image url array
# loading data from csv fille
with open('f1209310_full cirque formatted.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    series=[]
    for row in reader:
        img_lab.append(row['_city'])
        img_bounding.append(row['annotation'])
        img_url.append(row['image_url'])
# read image from url by opencv
img_path=img_url[0]# the first image url
resp = urllib.urlopen(img_path)# sending request to get image data with url
image = np.asarray(bytearray(resp.read()), dtype="uint8")# getting image data
image = cv2.imdecode(image, cv2.IMREAD_COLOR)# converting url image into cv image
height, width, layers = image.shape# get the width, height of image
# define videowriter by opencv
out = cv2.VideoWriter('outvideo.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (width,height))

# writing video from each url image
for i in range (len(img_url)):

    resp = urllib.urlopen(img_url[i])
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    print(img_url[i])
    # if annotation is not null, we add bound box with box label
    if ('noShapesFound'in img_bounding[i]):
        out.write(image)
    else:
        X, Y, W, H = coordinate_get(img_bounding[i])# getting coordinate and widh, height
        for index in range(len(W)):
            cv2.rectangle(image, (X[index], Y[index]), (X[index]+W[index], Y[index]+H[index]), (0, 255, 0), 2)
            if(img_lab[i]!=''):
                font = cv2.FONT_HERSHEY_SIMPLEX# fonr type
                cv2.putText(image, img_lab[i], (X[index], Y[index]), font, 1, (255, 0, 255), 2, cv2.LINE_AA)
        out.write(image)
cv2.destroyAllWindows()
out.release()
out.release()