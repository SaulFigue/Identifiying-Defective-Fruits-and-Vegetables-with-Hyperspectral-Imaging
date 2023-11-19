# NAME: Saul Figueroa


"""
import cv2
import matplotlib.pyplot as plt
from numpy import median

def save_imgs_MF(img_bands,Path_fruit):
    for i in range(5):
        cv2.imwrite(Path_fruit+'MF_'+str(i)+'.png',img_bands[i])

def Median_Filter(Absolute_Path):
    img1 = cv2.imread(Absolute_Path)
    final_img = img1.copy()
    # -------------------------- Zero pading ---------------------------
    img = cv2.copyMakeBorder(img1, 1, 1, 1, 1, cv2.BORDER_CONSTANT)
    rows = img.shape[0]
    cols = img.shape[1]

    # saving the kernel 3x3 in a temp_array to apply a median filter-----

    for r in range (0,rows-2):
        for c in range (0,cols-2):
            temp_array = []
            for x in range(r-1,r+2):               # Domain of Sxy------
                for y in range(c-1,c+2):
                    for z in img[x][y]:
                        temp_array.append(z)
            temp_array.sort()                      # Applying the median filter-----
            final_img[r][c] = median(temp_array)

    return final_img

# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------- MEDIAN FILTER ----------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
PathA = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Apple/3-IB/"
PathO = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Onion/3-IB/"

Path_apple = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Apple/4-MF/"
Path_onion = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Onion/4-MF/"

fruit = 'onion' 
if fruit == 'apple':
    Path  = PathA                                    # Choosing the fruit to work
    Path2 = Path_apple                               # Choosing the fruit to save
elif fruit == 'onion':
    Path  = PathO                                    # Choosing the fruit to work
    Path2 = Path_onion                               # Choosing the fruit to save

img_bands = []
IB_num = 'IB_'
for i in range(5):
    Absolute_Path = Path + IB_num + str(i) + '.png'
    final_img = Median_Filter(Absolute_Path)
    img_bands.append(final_img)

save_imgs_MF(img_bands,Path2)
"""