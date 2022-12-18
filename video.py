import cv2
import glob


convert_image_path = '/Users/douzi/Desktop/S9/master project/Shot-Transition-Detection/data/video_photo6'


#Frame rate (fps), size (size), the fps set here is 24, size is the size of the picture, the size of the picture converted in this article is 400×1080,
#That is, the width is 400 and the height is 1080. You need to modify the picture size according to your own situation.
fps = 10
size = (640,360)

videoWriter = cv2.VideoWriter('Video_6.mp4',cv2.VideoWriter_fourcc('m','p','4','v'),
                              fps,size)

for img in glob.glob(convert_image_path + "/*.jpg") :
    read_img = cv2.imread(img)
    videoWriter.write(read_img)
videoWriter.release()