import cv2

# for face detection (https://stackoverflow.com/questions/30508922/error-215-empty-in-function-detectmultiscale)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# resolution of the webcam
screen_width = 1280 # try 640 if code fails
screen_height = 720

# default webcam,
stream = cv2.VideoCapture(0)

while(True):
    # capture frame-by-frame
    (grabbed, frame) = stream.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # try to detect faces in the webcam
    faces = face_cascade.detectMultiScale(rgb, scaleFactor=1.3, minNeighbors=5)

    # for each faces found
    for (x, y, w, h) in faces:
        # draw a rectrangle around face
        color = (0, 255, 255) # in BGR
        stroke = 5
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, stroke)

    # show the frame
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1) & 0xFF

    # Press q to break out of the loop
    if key == ord("q"):
        break

# cleanup
stream.release()
cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)