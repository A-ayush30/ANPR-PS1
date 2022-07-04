#https://www.youtube.com/watch?v=IhRfqiC29Ds

import cv2
import os

cam = cv2.VideoCapture(0)
cv2.namedWindow("Video")

car_cntr = 0                           #number of cars detected

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Video", frame)

### Car detection code ###

    k = cv2.waitKey(1)
    if k%256 == 27:                     # ESC pressed
        print("Escape hit, closing...") #output statement
        break

    elif k%256 == 32:                   # SPACE pressed
    #if car_det == True                 #car detected
        car_cntr += 1                                        #increment counter
        img_name = "car_{}.png".format(car_cntr)             #unique image name
        path = r"C:\\Users\\DELL\\Desktop\\trial\\Images"    #folder to save car images
        cv2.imwrite(os.path.join(path, img_name), frame)     #save image
        print("{} written!".format(img_name))                #output statement
                                           

cam.release()

cv2.destroyAllWindows()