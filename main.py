import cv2

cap=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('C:/Users/gawal/PycharmProjects/FaceDetection/venv/FaceDetect/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/gawal/PycharmProjects/FaceDetection/venv/FaceDetect/haarcascades/haarcascade_eye.xml')
hand_cascade = cv2.CascadeClassifier('C:/Users/gawal/PycharmProjects/FaceDetection/venv/FaceDetect/haarcascades/palm.xml')



while (True):
    ret, frame=cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        hand = hand_cascade.detectMultiScale(gray, 1.1, 5)
        for (hx, hy, hw, hh) in hand:
            cv2.rectangle(frame, (hx, hy), (hx + hw, hy + hh), (0, 0, 255), 2)


    cv2.imshow('Frame', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()