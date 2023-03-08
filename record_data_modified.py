from __future__ import print_function
import cv2
from datetime import datetime

from robolab_turtlebot import Turtlebot, sleep

from scipy.io import savemat

# initialize turlebot
turtle = Turtlebot(rgb=True, depth=True, pc=True)

# sleep 2 set to receive images
sleep(2)

# get K, images, and point cloud
data = dict()
data['K_rgb'] = turtle.get_rgb_K()
data['K_depth'] = turtle.get_depth_K()
data['image_rgb'] = cv2.cvtColor(turtle.get_rgb_image(),cv2.COLOR_BGR2RGB)
data['image_depth'] = turtle.get_depth_image()
data['point_cloud'] = turtle.get_point_cloud()

# save data to .mat file
filename = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
savemat(filename+"_rgb.mat", data)

#save hsv:
data['image_rgb'] = cv2.cvtColor(data['image_rgb'],cv2.COLOR_BGR2HSV)
savemat(filename+"_hsv.mat", data)

print('Data saved in {}'.format(filename))
