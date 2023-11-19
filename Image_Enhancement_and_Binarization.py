# NAME: Saul Figueroa

"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

PathA = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Apple/1-BP/"
PathO = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Onion/1-BP/"

Path_apple = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Apple/2-IE/"
Path_onion = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Onion/2-IE/"


def save_imgs_IE(img_bands,Path_fruit):
    for i in range(5):
        cv2.imwrite(Path_fruit+'IE_'+str(i)+'.png',img_bands[i])

def Image_Enhancement(Absolute_Path):
    img2 = cv2.imread(Absolute_Path, 0)
    rgb_planes = cv2.split(img2)
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))        # IMAGE DILATION
        bg_img = cv2.medianBlur(dilated_img, 21)                         # MEDIAN BLUR k=21
        diff_img = 255 - cv2.absdiff(plane, bg_img)                      # IMAGE DIFERENCE
        norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1) # IMAGE NORMALIZATION
        result_norm_planes.append(norm_img)
    result_norm = cv2.merge(result_norm_planes)
    return result_norm

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------- IMAGE ENHANCEMENT ----------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
fruit = 'onion' 
if fruit == 'apple':
    Path  = PathA                                    # Choosing the fruit to work
    Path2 = Path_apple                               # Choosing the fruit to save
elif fruit == 'onion':
    Path  = PathO                                    # Choosing the fruit to work
    Path2 = Path_onion                               # Choosing the fruit to save

img_bands = []
BP_num = 'BP_'
for i in range(5):
    Absolute_Path = Path + BP_num + str(i) + '.png'
    result_norm = Image_Enhancement(Absolute_Path)
    img_bands.append(result_norm)

save_imgs_IE(img_bands,Path2)

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------- IMAGE BINARIZATION ---------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
PathA = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Apple/2-IE/"
PathO = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Onion/2-IE/"

Path_apple = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Apple/3-IB/"
Path_onion = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Onion/3-IB/"

def save_imgs_IB(img_bands2,Path_fruit):
    for i in range(5):
        cv2.imwrite(Path_fruit+'IB_'+str(i)+'.png',img_bands2[i])

def Image_Binarization(Absolute_Path,treshold):
    img2 = cv2.imread(Absolute_Path, 0)
    ret, tresh1 = cv2.threshold(img2,treshold,255,cv2.THRESH_BINARY_INV)
    return tresh1

if fruit == 'apple':
    Path  = PathA                                    # Choosing the fruit to work
    Path2 = Path_apple                               # Choosing the fruit to save
    tresholds = [175,175,227,223,185]
elif fruit == 'onion':
    Path  = PathO                                    # Choosing the fruit to work
    Path2 = Path_onion                               # Choosing the fruit to save
    tresholds = [175,200,190,185,140]

img_bands2 = []
IE_num = 'IE_'
for i in range(5):
    Absolute_Path = Path + IE_num + str(i) + '.png'
    result = Image_Binarization(Absolute_Path,tresholds[i])
    img_bands2.append(result)
    
save_imgs_IB(img_bands2,Path2)

"""