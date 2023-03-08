import cv2
from __future__ import print_function

from datetime import datetime

from robolab_turtlebot import Turtlebot, sleep

from scipy.io import savemat

#initialize the robot
turtle = Turtlebot(rgb=True, depth=True, pc=True)

sleep(2)

# get K, images, and point cloud
data = dict()
data['K_rgb'] = turtle.get_rgb_K()
data['K_depth'] = turtle.get_depth_K()
data['image_rgb'] = turtle.get_rgb_image()
data['image_depth'] = turtle.get_depth_image()
data['point_cloud'] = turtle.get_point_cloud()



base_filename = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")

base_rgb_filename = base_filename+"_rgb"
base_hsv_filename = base_filename+"_hsv"


mat_rgb_filename = base_rgb_filename+".mat"
jpg_rgb_filename = base_rgb_filename+".jpg"
png_rgb_filename = base_rgb_filename+".png"

mat_hsv_filename = base_hsv_filename+".mat"
jpg_hsv_filename = base_hsv_filename+".jpg"
png_hsv_filename = base_hsv_filename+".png"

# Convert the image to the HSV colorspace
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Save the HSV image in JPG, PNG, and MAT formats
cv2.imwrite(jpg_hsv_filename + '.jpg', hsv_img)
cv2.imwrite(png_hsv_filename + '.png', hsv_img)
cv2.imwrite(mat_hsv_filename + '.mat', hsv_img)

# Convert the image back to the RGB colorspace
rgb_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

cv2.imwrite(rgb_filename + '.jpg', rgb_img)
cv2.imwrite(rgb_filename + '.png', rgb_img)
cv2.imwrite(rgb_filename + '.mat', rgb_img)

# Print a success message with the filenames
print("HSV and RGB images saved as {}, {}, {}, {}, {}, and {} respectively.".format(hsv_filename+'.jpg', hsv_filename+'.png', hsv_filename+'.mat', rgb_filename+'.jpg', rgb_filename+'.png', rgb_filename+'.mat'))
