import cv2 

def frameCapture(path):
    vidObj = cv2.VideoCapture(path)
    count = 0 
    success = 1
    while success :
        success, image = vidObj.read()
        cv2.imwrite("frame%d.jpg" % count, image)
        
        count += 1
