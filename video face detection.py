import cv2

face_cascade= cv2.CascadeClassifier('C:\\Users\\hp\\PycharmProjects\\untitled3\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
vid = cv2.VideoCapture(0)
while True:
    frame1 , frame2 = vid.read()
    faces = face_cascade.detectMultiScale(frame2, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        frame2 = cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow('video',frame2)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

vid.release
cv2.destroyAllWindows()
