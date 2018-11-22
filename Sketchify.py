import imageio
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
from PIL import Image

sigma_value = 200 #TWEAK THIS FOR QUALITY OF SKETCH

def dodge(front,back):
    result=front*256.0/(256.0-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

img1 = "https://www.catster.com/wp-content/uploads/2017/08/Pixiebob-cat.jpg" #INSERT IMAGE FILE OR URL HERE
img2 = "man.jpg"
img3 = "cat.jpg"
img4 = "dog.jpg"
img5 = "baby.jpg"

start_img = imageio.imread(img3)
gray_img = grayscale(start_img)
inverted_img = 255-gray_img
blur_img = scipy.ndimage.filters.gaussian_filter(inverted_img,sigma=sigma_value)
final_img= dodge(blur_img,gray_img)

plt.imsave('img.png', final_img, cmap='gray', vmin=0, vmax=255)

final = Image.open('img.png')

final.show()








