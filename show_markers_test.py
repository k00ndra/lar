#!/usr/bin/env python

import cv2
from robolab_turtlebot import Turtlebot, detector
import numpy as np

WINDOW = 'markers'


def main():

    turtle = Turtlebot(rgb=True)
    turtle.play_sound(sound_id = 0)
    cv2.namedWindow(WINDOW)

    while not turtle.is_shutting_down():
        # get point cloud
        image = turtle.get_rgb_image()
        #point_cloud=turtle.get_point_cloud()
        
        # wait for image to be ready
        if image is None:
            continue
        
        lower_yellow = np.array([255,255,0])
        upper_yellow = np.array([255,255,10])

        yellow_mask = cv2.inRange(image,lower_yellow,upper_yellow)
        #image = cv2.bitwise_and(image,image,yellow_mask)
        # show image
        img = np.zeros([480,640,3])
        cv2.imshow(WINDOW, img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()
