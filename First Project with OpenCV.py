import cv2
import time
import datetime

#Acessing and using webcam
cap = cv2.VideoCapture(0)

#Detecting faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#Detecting Body
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

#Frame size of webcam
frame_size = (int(cap.get(3)), int(cap.get(4)))
#Video Format
fourcc = cv2.VideoWriter_fourcc(*"mp4v")


#Main programme
while True:
    _, frame = cap.read()
    
    #Converting the frame to a grey scale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Determines accuracy, speed of algorithm and number of faces and body
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    body = body_cascade.detectMultiScale(gray, 1.2, 5)
    
    #Creates a rectangle on a face and body
    for (x, y, width, height) in faces:
        #Location, thickness and color of frame
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255,0,0), 3)

    for (x, y, width, height) in body:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255,0,0), 3)
        
    #Recording
    if len(faces) + len(body) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            
            #Name of video file
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            
            #An output stream
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 30, frame_size)

            print("Started Recording!")
    
    #Start timer to end recording        
    elif detection:
        if timer_started:

            #Check if timer past the number of seconds it should stop after not detecting a face and a body
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print("Stopped Recording!")
        else:
            timer_started = True
            detection_stopped_time = time.time()
    
    #Writing to ouput stream only when recording
    if detection:
        out.write(frame)
    
    #Name of the window 
    cv2.imshow("CV Camera", frame)
    
    #Allowing user to quit the programme
    if cv2.waitKey(1) == ord('q'):
        break


#Releasing resources
out.release()
cap.release()

#Quits the Camera window
cv2.destroyAllWindows()

