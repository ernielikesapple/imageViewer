#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:27:58 2020

@author: ernie
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:04:00 2020

@author: ernie
"""
import os
import numpy as np
from nibabel.testing import data_path
import nibabel as nib
import matplotlib.pyplot as plt
import matplotlib 
from numpy.fft import fft, fft2, ifft, ifft2, fftfreq, fftshift, fftn, ifftn


class part2C():
    
    @staticmethod
    def showSlice(self,brain,slice, view):
        if view == 'axial': 
            plt.title("raw axial")
            plt.imshow(self.anti_reverse(brain[:, :, slice])) #to do, modify the antireverse function
            matplotlib.image.imsave('axial.png', self.anti_reverse(brain[:, :, slice]))
        elif view == 'sagittal':
            plt.title("raw sagittal")
            plt.imshow(self.anti_reverse(brain[:, slice, :])) 
            matplotlib.image.imsave('sagittal.png', self.anti_reverse(brain[:, slice, :]))
        elif view == 'coronal':
            plt.title("raw coronal")
            plt.imshow(self.anti_reverse(brain[slice, :, :]))
            matplotlib.image.imsave('coronal.png', self.anti_reverse(brain[slice, :, :]))
    
    @staticmethod   
    def anti_reverse(array):
        (rows,cols) = array.shape
        store_all_list = []
        
        for i in range(rows):
            take_raws = array[i,:].tolist()
            reverse_rows = take_raws[::-1]
            store_all_list.append(reverse_rows)
            matrix = np.mat(store_all_list)
            new_matrix = matrix.T       
        return new_matrix
    
    @staticmethod 
    def FFt2dWithLog (imageSlice):  
        Ahat = fft2(imageSlice)
        F = np.log(np.abs(fftshift(Ahat)))
        plt.title("frequency domain of raw")
        plt.imshow(F)
        matplotlib.image.imsave('fftRawImage.png', F)
        return F
    @staticmethod
    def highPassFilterForEdgeDetection (img):   
        rows, cols = img.shape
        crow, ccol = int(rows / 2), int(cols / 2)  # center

        # Circular HPF mask, center circle is 0, remaining all ones
        mask = np.ones((rows, cols))
        r = 17
        center = [crow, ccol]
        x, y = np.ogrid[:rows, :cols]

        mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
        mask[mask_area] = 0
        
        orignalData = fftshift(fft2(img)) #Fourier transform of raw
        result = np.abs(ifft2(orignalData*mask))
        plt.title("After Edge Enhancement")
        plt.imshow(result);
        matplotlib.image.imsave('rawImageAfterEdgeEnhancement.png', result)        
  
    @staticmethod
    def GaussianFilterForSmoothing (img):   
        sz_x = img.shape[0]
        sz_y = img.shape[1]
        [X, Y] = np.mgrid[0:sz_x, 0:sz_y]
        xpr = X - int(sz_x) // 2
        ypr = Y - int(sz_y) // 2
        sigma = 21
        gaussfilt = np.exp(-((xpr**2+ypr**2)/(2*sigma**2)))/(2*np.pi*sigma**2)
        orignalData = fftshift(fft2(img)) #Fourier transform of raw
        result = np.abs(ifft2(gaussfilt* orignalData))
        plt.title("After Smoothing")        
        plt.imshow(result);
        matplotlib.image.imsave('rawImageAfterSmoothing.png', result)
        
    @staticmethod 
    def getSourceImage (imageDirectoryNfilename):
        directory = os.path.join(os.path.dirname(__file__))
        dataDirectory = os.path.join(directory, imageDirectoryNfilename)
        img = nib.load(dataDirectory)
        imgData = img.get_fdata()
        return imgData
    

#display reuslt
#result for q2c

def outPutFor2C(imgName, SliceValue, direction):
    a1 = part2C()
    q2CimgData = a1.getSourceImage(imgName)
    sliceData  = []
    if direction == 'axial': 
        sliceData = q2CimgData[:, :, SliceValue]
    elif direction == 'sagittal':
        sliceData = q2CimgData[:, SliceValue, :]
    elif direction == 'coronal':
        sliceData = q2CimgData[SliceValue, :, :]
       
    plt.title(imgName)
                      
    plt.subplot(241)
    a1.showSlice(a1, q2CimgData, SliceValue, direction)    
    
    plt.subplot(243)
    a1.FFt2dWithLog(sliceData)
    
    plt.subplot(245)    
    a1.highPassFilterForEdgeDetection(sliceData)    
    
    plt.subplot(247)    
    a1.GaussianFilterForSmoothing(sliceData)
    

#Example :    
outPutFor2C("images/swi.nii", 150, "coronal")

