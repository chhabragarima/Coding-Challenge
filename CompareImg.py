#	REQUIRED TASK 3 AND BONUS TASK 2

from skimage.measure import compare_ssim as ss #to calculate structural similarity measure
import numpy as np
import cv2 #image reading, transformation and grayscale conversion

def main():
	test_image1=cv2.imread("test_data/diff_test/test_image_1.png")
	test_image2=cv2.imread("test_data/diff_test/test_image_2.png")
	#print(len(image1[0]))
	image1=cv2.imread("test_data/2D/w1.png")
	image2=cv2.imread("test_data/2D/w0.png")


	#converting into grayscale using cv2
	
	#Required Task 3
	image_comparision(test_image1,test_image2)
	image_comparision(image1,image2)
	
	#Bonus Task 2
	transformation(image1, image2)

#comparing images by two methods: 1) Mean Squared Error 2) Structural Similarity
def image_comparision(image1,image2):
	image1=cv2.cvtColor(image1,cv2.COLOR_RGB2GRAY)
	image2=cv2.cvtColor(image2,cv2.COLOR_RGB2GRAY)


	mean_sq_error=mean_square_error(image1,image2)
	stuct_similarity=ss(image1,image2)

	print("Mean Squared Error:",mean_sq_error)
	print("Structural Similarity:",stuct_similarity)

def mean_square_error(image1,image2):
    np_array1=image1.astype("float")
    np_array2=image2.astype("float")
    error=np.sum((np_array1-np_array2)**2)
    error=error/(image1.shape[0]*image1.shape[1])

    return error


def transformation(image1, image2):
	
	rows=image1.shape
	cols=len(image1[0])

	#first roatating to the image w1 to improve the angle
	M = cv2.getRotationMatrix2D((cols/2,rows[0]/2),-4,1)
	dst=cv2.warpAffine(image1,M,(cols,rows[0]))

	#translating the image w1 to get the image present on image1 out of the site so as to avoid the part of image that is common to the 2 images
	M1=np.float32([[1,0,-150],[0,1,5]])
	dst1=cv2.warpAffine(dst,M1,(cols,rows[0]))

	#translating the image w0 so that it is in-line with the other image and to eliminate the part that is covered in the other image
	M2=np.float32([[1,0,100],[0,1,5]])
	dst2=cv2.warpAffine(image2,M2,(cols,rows[0]))
	
	#combining both the images
	combine=np.concatenate((dst2,dst1),axis=1)

	#image distplay
	cv2.imshow('Combined Image',combine)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__=='__main__':
	main()