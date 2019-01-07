import cv2
import numpy as np
import time

bondaries = [
    ([120, 82, 10], [160, 122, 50]),
    ([98, 162, 162], [118, 182, 182]),
    ([53, 43, 43], [67, 57, 57]),
    ([81, 114, 163], [101, 134, 183])
]

fingers = ['Index', 'Middle', 'Ring', 'Pinky']

cap = cv2.VideoCapture(1)

while True:
    i = 0
    ret, image = cap.read()
    for (lower, upper) in bondaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)

        notNull = np.where(output != 0)
        try:
            notNull = (np.average(notNull[1], weights=notNull[2]), np.average(notNull[0], weights=notNull[2]))
        except:
            notNull = (np.mean(notNull[1]), np.mean(notNull[0]))
        print fingers[i], notNull
        i = i+1
        #if i==2:
        cv2.imshow('Colors', np.hstack([image, output]))
        
    i = 0
    print "========="
    #time.sleep(2)

    k = cv2.waitKey(30)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
