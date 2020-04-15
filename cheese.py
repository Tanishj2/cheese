import cv2

cap = cv2.VideoCapture(0)

ret,photo = cap.read()

print(ret)		#it return photo is save or not

cv2.imwrite("/root/Desktop/riya.png",photo) 	#save photo with given name and location 

cap.release()


