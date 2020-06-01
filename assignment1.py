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

import sys
np.set_printoptions(threshold=sys.maxsize)

class Assignment1():
    
    @staticmethod
    def showSlice(self,brain,slice, view):
        if view == 'axial': 
            plt.title("raw")
            plt.imshow(self.anti_reverse(brain[:, :, slice])) #to do, modify the antireverse function
            matplotlib.image.imsave('axial.png', self.anti_reverse(brain[:, :, slice]))
        elif view == 'sagittal':
            plt.title("raw")
            plt.imshow(self.anti_reverse(brain[:, slice, :])) 
            matplotlib.image.imsave('sagittal.png', self.anti_reverse(brain[:, slice, :]))
        elif view == 'coronal':
            plt.title("raw")
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
    def GaussianFilterForSmoothing (img):   
        sz_x = img.shape[0]
        sz_y = img.shape[1]
        [X, Y] = np.mgrid[0:sz_x, 0:sz_y]
        xpr = X - int(sz_x) // 2
        ypr = Y - int(sz_y) // 2
        sigma = 21
        gaussfilt = np.exp(-((xpr**2+ypr**2)/(2*sigma**2)))/(2*np.pi*sigma**2)
        orignalData = fftshift(fft2(img)) #Fourier transform of raw
        plt.imshow(np.abs(ifft2(gaussfilt* orignalData)));
        
    @staticmethod
    def highPassFilterForEdgeDetection (img):   
        rows, cols = img.shape
        crow, ccol = int(rows / 2), int(cols / 2)  # center

        # Circular HPF mask, center circle is 0, remaining all ones
        mask = np.ones((rows, cols))
        r = 17
        center = [crow, ccol]
        x, y = np.ogrid[:rows, :cols]
        print((x - center[0]) ** 2 + (y - center[1]) ** 2)
        mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
        mask[mask_area] = 0
        
        orignalData = fftshift(fft2(img)) #Fourier transform of raw
         
        plt.imshow(np.abs(ifft2(orignalData*mask)));
        
     








            
    @staticmethod 
    def getSourceImage (imageDirectoryNfilename):
        directory = os.path.join(os.path.dirname(__file__))
        dataDirectory = os.path.join(directory, imageDirectoryNfilename)
        img = nib.load(dataDirectory)
        imgData = img.get_fdata()
        return imgData
    
    
  
    '''
    nib.showSlices.OrthoSlicer3D(imgData, affine=None, axes=None, title=None)
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
a1 = Assignment1()
plt.subplot(3,3,2)
res = a1.showSlice(a1,imgData,slice=250,view="axial")
plt.subplot(3,3,7)
a1.FFt2dWithLog(a1.anti_reverse(imgData[:,:,250]))
'''

#result for q1a
a1 = Assignment1()

#result for q1a
q1AimgData = a1.getSourceImage("images/t1.nii")
#a1.showSlice(a1,q1AimgData,slice=250,view="axial")

def outPutSliceImage(direction, sliceValue):
    return a1.showSlice(a1,q1AimgData,slice=sliceValue,view=direction)


#result for q2a
q2AimgData = a1.getSourceImage("images/t2.nii")
#sliceQ2a = a1.FFt2dWithLog (q2AimgData[:,:,250])

#result for q2b

q2BimgData = a1.getSourceImage("images/swi.nii")
#sliceQ2b = a1.FFt2dWithLog (q2BimgData[:,:,250])
#a1.frequencyDomainGaussianFilterForQ2b (sliceQ2b, q2BimgData[:,:,250])


#result for q2c
q1AimgData = a1.getSourceImage("images/tof.nii")
#a1.GaussianFilterForSmoothing(q1AimgData[:,:,250])

a1.highPassFilterForEdgeDetection(q1AimgData[:,:,120])

def outPutForFFt2dWithLog():
    a1.FFt2dWithLog (q2AimgData[:,:,250])
    matplotlib.image.imsave('outPutForFFt2dWithLog.png', a1.anti_reverse(a1.FFt2dWithLog (q2AimgData[:,:,250])))
   