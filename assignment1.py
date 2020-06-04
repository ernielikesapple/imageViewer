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


class Assignment1():
    
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
        return F
        
    @staticmethod
    def frequencyDomainGaussianFilterForQ2b (resultFromQ2a, orignalImageData):   
        sz_x = resultFromQ2a.shape[0]
        sz_y = resultFromQ2a.shape[1]
        [X, Y] = np.mgrid[0:sz_x, 0:sz_y]
        xpr = X - int(sz_x) // 2
        ypr = Y - int(sz_y) // 2
        count=1
        plt.figure(figsize=(5*5, 4.8*5))
        for sigma in range(1,25,5):
            gaussfilt = np.exp(-((xpr**2+ypr**2)/(2*sigma**2)))/(2*np.pi*sigma**2)
            plt.subplot(1,5,count);

            orignalData = fftshift(fft2(orignalImageData)) #Fourier transform of raw
            plt.imshow(np.abs(ifft2(gaussfilt* orignalData)));
            
            plt.title('sigma='+str(sigma)) 
            count =count + 1
             

    @staticmethod 
    def getSourceImage (imageDirectoryNfilename):
        directory = os.path.join(os.path.dirname(__file__))
        dataDirectory = os.path.join(directory, imageDirectoryNfilename)
        img = nib.load(dataDirectory)
        imgData = img.get_fdata()
        return imgData

#display reuslt
a1 = Assignment1()

#result for q1a
    
def outPutFor1A(imgName, SliceValue, direction):
    q1AimgData = a1.getSourceImage(imgName)
    
    plt.title(imgName)
    a1.showSlice(a1, q1AimgData, SliceValue, direction)    
    

    
outPutFor1A("images/t1.nii", 250, 'axial')


#result for q2a
def outPutForQuestion2a():
    q2AimgData = a1.getSourceImage("images/t2.nii")
    a1.FFt2dWithLog (q2AimgData[:,:,250])

#outPutForQuestion2a()


#result for q2b
def outPutForQuestion2b():
    q2BimgData = a1.getSourceImage("images/swi.nii")
    sliceQ2b = a1.FFt2dWithLog (q2BimgData[:,:,250])
    a1.frequencyDomainGaussianFilterForQ2b (sliceQ2b, q2BimgData[:,:,250])

#outPutForQuestion2b()



