
# NAME: Saul Figueroa
 
# Trying to read an HS Image on format .mat

"""
import cv2
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

Path_apple = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Apple/1-BP/"
Path_onion = "C:/Users/TheKaos16/Desktop/YACHAY SAUL/8vo Semestre Carrera/2 Image Processing/Porject/PROTOTYPE II/prototype/Results/Onion/1-BP/"

# -------------------------------------------------------------------------------------------------------------
# --------------------------------- FUNCTIONS TO BANDS PREPROCESSING ------------------------------------------
# -------------------------------------------------------------------------------------------------------------

def plot_imgs(images):
    for i in range(1,5):
        plt.subplot(1, 4, i)
        plt.imshow(images[i], cmap='gray')
        plt.xticks([])
        plt.yticks([])
        plt.title(i)
        plt.savefig('BP_onion_plt.png') # Aqui se guarda la imagen sin titulo ni ejes , mejorar para q se guarden todas 1,2,3...
        
    plt.show()

def save_imgs_cv2(img_bands,Path_fruit):
    for i in range(5):
        cv2.imwrite(Path_fruit +'BP_'+str(i)+'.png',img_bands[i])

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------- IMAGE ACQUISITION ----------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
fruit = 'onion'                                       # Choose the fruit to work with
if fruit == 'apple':
    Path = Path_apple              # For BP_apple
    fruit_test = sio.loadmat('apple_dataset.mat')        # Reading the MATLAB-file for the fruit to work
elif fruit == 'onion':
    Path = Path_onion              # For BP_onion
    fruit_test = sio.loadmat('onion_dataset.mat')

fruit_test_key=list(fruit_test.keys())                # Getting the keys of the dictionary fruit_test
fruit_test_bands = (fruit_test[fruit_test_key[3]])    # Taking the elements/bands from cspaces key 

# -----------------------------------------------------------------------------------------------------------
# ----------------------------------------- BANDS -----------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

first_band = fruit_test_bands[0][0][7]
img_band1 = first_band[:,:,1]

# ------------------------------------- FOUR BANDS SELECTED -------------------------------------------------
second_band = fruit_test_bands[0][0][6]
img_band2 = second_band[:,:,0]

third_band = fruit_test_bands[0][0][0]
img_band3 = third_band[:,:,2]

fourth_band = fruit_test_bands[0][0][2]
img_band4 = fourth_band[:,:,0]

fifth_band = fruit_test_bands[0][0][5]
img_band5 = fifth_band[:,:,2]

img_bands = [img_band1,img_band2,img_band3,img_band4,img_band5]

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------- BAND PREPROCESSING ---------------------------------------------------
# ------------------------------------------------------------------------------------------------------------

save_imgs_cv2(img_bands,Path)  
#plot_imgs(img_bands)                        # Unlock to see Figure 7 of the report

"""