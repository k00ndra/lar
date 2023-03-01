#!/usr/bin/env python

import cv2
from robolab_turtlebot import Turtlebot, detector
import numpy as np

WINDOW = 'markers'


def main():

    turtle = Turtlebot(rgb=True,pc = True)
    turtle.play_sound(sound_id = 0)
    cv2.namedWindow(WINDOW)

    while not turtle.is_shutting_down():
        # get point cloud
        image = turtle.get_rgb_image()
        #point_cloud=turtle.get_point_cloud()
        
        # wait for image to be ready
        if image is None:
            continue
        
        lower_yellow = np.array([100,100,0])
        upper_yellow = np.array([255,255,50])

        yellow_mask = cv2.inRange(image,lower_yellow,upper_yellow)
        highlighted_markers = cv2.bitwise_and(image,image,yellow_mask)
        # show image

        result_img = image-highlighted_markers

        cv2.imshow(WINDOW, result_img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()
