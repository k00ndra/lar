import scipy.io
import cv2

WINDOW = 'markers'
mat = scipy.io.loadmat('/home/koondra/workspaces/lar_workspaces/test01/lar/2023-03-01-14-22-47.mat')
cv2.imshow(WINDOW,mat["image_rgb"])
cv2.waitKey()
