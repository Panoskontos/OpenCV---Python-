import cv2 
import time
# covert text to speech
import pyttsx3

# initialize Text-to-speech engine
engine = pyttsx3.init()

cap = cv2.VideoCapture(0)



while True:    
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)

    # pick pixel value
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    # color classifier-------------------------------
    color = 'undefined'
    if hue_value < 5:
        color = "red"
    elif hue_value < 22:
        color = "orange"
    elif hue_value < 33:
        color = "yellow"
    elif hue_value < 78:
        color = "green"
    elif hue_value < 131:
        color = "blue"
    elif hue_value < 170:
        color = "violet"
    else:
        color = "red"
# -------------------------------------------------------
    engine.say(color)
    # play the speech
    engine.runAndWait()
    time.sleep(3)
# -------------------------------------------------------
    print(pixel_center)
    cv2.putText(frame, color, (10,50), 0, 1, (255,0,0), 2)

    cv2.circle(frame, (cx,cy), 5, (255,0,0), 3)


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(2)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()