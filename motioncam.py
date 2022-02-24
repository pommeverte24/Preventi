import cv2
from colorama import Fore, Back, Style
cap=cv2.VideoCapture(0) # prise de caméra


frame_count = 1
previous_gray = None    # image précédente

while(True):            # si la caméra est branché
    count = 0
    ret2,frame2=cap.read()
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (29, 29), 0)
    if previous_gray is not None:
        deltaframe=cv2.absdiff(previous_gray,gray2)
        threshold = cv2.threshold(deltaframe, 25, 255, cv2.THRESH_BINARY)[1]
        threshold = cv2.dilate(threshold,None)
        cv2.imshow('mouvement',threshold)   # affichage de la fenetre "mouvement"
        count = cv2.countNonZero(threshold)
    if frame_count == 10:       # moyenne des dix dernières image
        count = count / 10
        print(count)
        previous_gray = gray2
        frame_count = 0
    else:
        frame_count +=1
    
    if count > 60000:           # condition si nombre de pixels blanc trop grand
        print(Fore.RED + "MOUVEMENT")
        print(Style.RESET_ALL)
    
    if cv2.waitKey(20) == ord('q'):
      break
    
cap.release()
cv2.destroyAllWindows()
