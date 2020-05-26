#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:04:00 2020

@author: ernie
"""
import os
current_directory = os.path.join(os.path.dirname(__file__))
data_directory = os.path.join(current_directory, "images/t1.nii")
import numpy as np
from nibabel.testing import data_path
import nibabel as nib
import matplotlib.pyplot as plt
import matplotlib 
img = nib.load(data_directory)
imgData = img.get_fdata()
from numpy.fft import fft, fft2, ifft, ifft2, fftfreq, fftshift

class ErnieImageViewer():

    
     #shape (274, 384, 384)
    @staticmethod
    def viewer(self,brain,slice, view):
        if view == 'axial': 
            plt.imshow(self.anti_reverse(brain[:, :, slice])) #to do, modify the antireverse function
            matplotlib.image.imsave('axial.png', self.anti_reverse(brain[:, :, slice]))
        elif view == 'sagittal':
            plt.imshow(self.anti_reverse(brain[:, slice, :])) 
            matplotlib.image.imsave('sagittal.png', self.anti_reverse(brain[:, slice, :]))
        elif view == 'coronal':
            plt.imshow(self.anti_reverse(brain[190, :, :]))
            matplotlib.image.imsave('coronal.png', self.anti_reverse(brain[190, :, :]))
        
         
    
    @staticmethod
    def FFt2dWithLog (imageSlice):
        Ahat = fft2(imageSlice)
        F = np.log(np.abs(fftshift(Ahat)))
        plt.imshow(F)
    
    
    
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
    
    
    
    
    
    
    
    

            
     
    
    
    '''
    nib.viewers.OrthoSlicer3D(imgData, affine=None, axes=None, title=None)
    nib.viewers.OrthoSlicer3D(imgData).show()
    '''
    '''
    def show_slices(slices):
       """ Function to display row of image slices """
       fig, axes = plt.subplots(1, len(slices))
       for i, slice in enumerate(slices):
           axes[i].imshow(slice.T, origin="lower")
           
    slice_0 = imgData[137, :, :]
    slice_1 = imgData[:, 192, :]
    slice_2 = imgData[:, :, 250]
    '''
    #show_slices([slice_0, slice_1, slice_2])
    
    #plt.suptitle("Center slices for EPI image")
    '''
    from skimage.io import imread
    import matplotlib.image as mpimg
    img=imread('lecture 1.png')
    result = FFt2dWithLog(img)

'''    '''
a1 = ErnieImageViewer()
plt.subplot(3,3,2)
res = a1.viewer(a1,imgData,slice=250,view="axial")
plt.subplot(3,3,7)
a1.FFt2dWithLog(a1.anti_reverse(imgData[:,:,250]))
'''

def outPutImage(direction, sliceValue):
    a1 = ErnieImageViewer()
    return a1.viewer(a1,imgData,slice=sliceValue,view=direction)

outPutImage("axial", 250)