# import the opencv library
import cv2

# Define a video capture object
vid = cv2.VideoCapture("walking.avi")
face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')


while(True):
   
    # Capture the video frame by frame
    ret, img = vid.read()
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray,1.1,5)
    print(faces)

    for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    # Display the resulting frame
    cv2.imshow("Web cam", img)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()