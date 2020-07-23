
# coding: utf-8
#旋轉後 圖片會有空白
import math
import cv2
import numpy as np
import os

#亮度 function
def contrast_img(img1,c,b):
    rows,cols,channels=img1.shape
    
    #新建全零圖片陣列src2,將height和width，型別設定為原圖片的通道型別(色素全為零，輸出為全黑圖片)
    blank=np.zeros([rows,cols,channels],img1.dtype)
    dst=cv2.addWeighted(img1,c,blank,1-c,b)#合成圖片
    return dst


if __name__ == "__main__":
    pic_path="E:\\chung\\ppcb\\slide_code\\pic\\test\\" #picture path
    save_path="E:\\chung\\ppcb\\slide_code\\pic\\rotate\\"
    choice=1  # 1:旋轉 2:亮度 3:大小 4:平移 5:鏡射
    
    file=os.listdir(pic_path)
    print(len(file))
    for i in file:
        image = cv2.imread(pic_path+i)
        image_height, image_width = image.shape[0:2]
        if choice==1:
            #旋轉
            angle=30  #rotate angle
            center = (image_width/2,image_height/2)
            M = cv2.getRotationMatrix2D(center,angle,1)#旋转缩放矩阵：(旋转中心，旋转角度，缩放因子)
            rotated = cv2.warpAffine(image,M,(image_width,image_height), borderValue=(255,255,255))
            cv2.imwrite(save_path+i[:-4]+"_angle"+str(angle)+".jpg",rotated)
            
        elif choice==2:
            #亮度
            bright=100 #亮度值
            contrast=contrast_img(image,1.2,bright)#(原始像素,對比度,亮度值)
            cv2.imwrite(save_path+i[:-4]+"_"+str(bright)+".jpg",contrast)
            
        elif choice==3:
            #大小
            #缩放成widthxheight的图像
            imagescale = cv2.resize(image, (200, 50)) #(宽度,高度)
            cv2.imwrite(save_path+i[:-4]+"_"+str('scale')+".jpg",imagescale)
            
        elif choice==4:
            #平移
            shift_right=100
            shift_down=50
            M = np.float32([[1,0,shift_right], [0,1,shift_down]])#矩陣 
            dst = cv2.warpAffine(image, M, (image_width, image_height), borderValue=(255,255,255))
            cv2.imwrite(save_path+i[:-4]+"_"+str('shift')+".jpg",dst)
            
        elif choice==5:
            #鏡射
            flip=1 #1水平鏡射 0垂直鏡射 -1：水平、垂直同時
            xImg = cv2.flip(image,flip,dst=None)
            cv2.imwrite(save_path+i[:-4]+"_"+str('flip')+".jpg",xImg)