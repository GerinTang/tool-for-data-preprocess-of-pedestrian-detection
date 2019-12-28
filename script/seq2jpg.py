import os
import glob
import cv2 as cv


# 保存图片以指定名字到指定位置
def save_img(dname, fn, i, frame):
    if(i%skip == 0):

        cv.imwrite('{}/{}_{}_I{:0>5}.jpg'.format(out_dir, os.path.basename(dname),

        os.path.basename(fn).split('.')[0], i-1), frame)



# 输出图片位置
skip = 3
out_dir = 'D:/datasets/Caltech/training_fcos'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
# seq文件位置
for dname in sorted(glob.glob('D:/datasets/Caltech/original_data/set05*')):
    for fn in sorted(glob.glob('{}/*.seq'.format(dname))):
        cap = cv.VideoCapture(fn)
        i = 1
        while True:
            # ret为标志位，bool型，是否读到数据，frame为视频帧图像数据
            ret, frame = cap.read()
            if not ret:
                break
            save_img(dname, fn, i, frame)
            i += 1
        print(fn)