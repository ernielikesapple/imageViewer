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
        plt.imshow(F)
        return F
        
    @staticmethod        
    def frequencyDomainGaussianFilter (img, orignalImage):   
        sz_x = img.shape[0]
        sz_y = img.shape[1]
        [X, Y] = np.mgrid[0:sz_x, 0:sz_y]
        xpr = X - int(sz_x) // 2
        ypr = Y - int(sz_y) // 2
        count=1
        
        
        for sigma in range(1,25,5):
            gaussfilt = np.exp(-((xpr**2+ypr**2)/(2*sigma**2)))/(2*np.pi*sigma**2)
            plt.subplot(1,5,count);
            
            
            orignalData = fftshift(fft2(orignalImage))
            
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

#result for q1a
a1 = ErnieImageViewer()

def outPutImage(direction, sliceValue):
    
    return a1.viewer(a1,imgData,slice=sliceValue,view=direction)

outPutImage("axial", 250)

#result for q2a
q2AimgData = a1.getSourceImage("images/t2.nii")

sliceQ2a = a1.FFt2dWithLog (q2AimgData[:,:,250])

#result for q2b

q2BimgData = a1.getSourceImage("images/swi.nii")
sliceQ2b = a1.FFt2dWithLog (q2BimgData[:,:,250])
a1.frequencyDomainGaussianFilter (sliceQ2b, q2BimgData[:,:,250])



