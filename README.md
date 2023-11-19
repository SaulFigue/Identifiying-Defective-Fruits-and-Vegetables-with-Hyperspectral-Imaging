# Identifying Defective Fruits by Using Image Processing Techniques

This is a GUIDE for running in the right way each script of python. If you follow the below steps, the results will be exactly as the presented in the 2022 Third International Conference on Information Systems and Software Technologies (ICI2ST) from the paper [Identifying Defective Fruits and Vegetables with Hyper-spectral Images: A Brief Tutorial](https://scholar.google.com.ec/scholar?oi=bibs&cluster=7353641407101134420&btnI=1&hl=es&authuser=1)

## Abstract

Horticulture is the branch of agriculture that addresses the crop of fruits and vegetables. This art of cultivating natural products has been a critical research area that helped to satisfy human's food consumption. The enhancement of quality control has improved the cost-effectiveness and increased the financial profit of the production. This study presents a processing pipeline architecture that assesses the quality of fruits and vegetables through image processing. The solution involves hyper-spectral imaging, image enhancement, image binarization, and median filtering. Our experiments demonstrate that our image processing pipeline proposal successfully identifies the defective regions in a publicly available dataset that contains images of apples and onions.

## Instructions

Step 1: Create two different folders where you want to save all the images.

Step 2: Open the frist Script [Final_prototype.py](Final_prototype.py)

Step 3: Change the Paths according to your folders created, and choose the dataset you want to work (type apple or onion in the fruit variable) e.g fruit = 'apple'

Step 4: Excecute the .py file and move to the next Script [Image_Enhancement_and_Binarization.py](Image_Enhancement_and_Binarization.py)

Step 5: Repeat Step 1 and Step 3. and run the .py file.

Step 6: Move to the last Script [Median_filter.py](Median_filter.py)

Step 7: Repeat Step 5.

## Note: 

For obtaining the Figure 7 presented in the paper, uncomment the ```plot_imgs``` function in the first Script. Change the variable fruit between apple and onion to get both BP
