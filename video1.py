from PIL import Image
import os
import numpy as np
import re
import cv2
import shutil


def endPhoto():
    photos='/Users/douzi/Desktop/S9/master project/Shot-Transition-Detection/videos/frames_BAR_RMA_GOAL1'
    photos_list = os.listdir(photos)
    photos_list.sort(key=lambda x: int(x.replace("frame","").split('.')[0]))  
    
    save_out='/Users/douzi/Desktop/S9/master project/Shot-Transition-Detection/data/video_photo6'
    #new_paths='/Users/douzi/Desktop/S9/master project/Shot-Transition-Detection/data/video_photo'
    
    start_photo='/Users/douzi/Desktop/S9/master project/Shot-Transition-Detection/data/start'
    start_list = os.listdir(start_photo)
    #print(len(start_list))
    start_list.sort(key=lambda x: int(x.replace("frame","").split('.')[0]))   

    end_photo='/Users/douzi/Desktop/S9/master project/Shot-Transition-Detection/data/end'
    end_list = os.listdir(end_photo)
    end_list.sort(key=lambda x: int(x.replace("frame","").split('.')[0]))
    #print(end_list)

    list=start_list+end_list
    list.sort(key=lambda x: int(x.replace("frame","").split('.')[0]))
    a=list[12]
    b=list[13]
  
    a_index=photos_list.index(a)
    b_index=photos_list.index(b)


    photos_list_iterator=iter(photos_list)

    while a in photos_list:
        img_path=r"/Users/douzi/Desktop/S9/master project/Shot-Transition-Detection/data/photos/{}".format(a)
        print(img_path)
        shutil.copy(img_path,save_out)

        img_index=photos_list.index(a)

        if a_index != b_index:
          a_index = a_index+1
          a=photos_list[a_index]
        else: break     

if __name__ == '__main__':
     endPhoto()

