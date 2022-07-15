# Face and Hand Detection Project

We have used Harr CascadeClassifier method to detect Face and palm detection.

First we will capture the video through webcam  
cap = cv2.VideoCapture(0)

Next we have used and created 3 objects of cascase classifier i.e. 
1. haarcascade_frontalface_default.xml
2.  haarcascade_eye.xml
3. palm.xml

You can use different cascade classifier file to detect different objects.

Later, by using "detectMultiScale" function it will detect and locate the object.
