import cv2

face_cascade = cv2.CascadeClassifier('C:/Python39/Lib/site-packages/cv2/haar-cascade-files-master/haar-cascade-files-master/haarcascade_frontalface_default.xml')

dog = cv2.imread('dogr.png')
#cv2.imshow("Filter",dog)
#cv2.waitKey(0)

org_dog_h, org_dog_w, dog_channels = dog.shape

dog_gray = cv2.cvtColor(dog, cv2.COLOR_BGR2GRAY)
#cv2.imshow("GRay filter",dog_gray)
#cv2.waitKey(0)

_, original_mask = cv2.threshold(dog_gray, 10, 255, cv2.THRESH_BINARY_INV)
original_mask_inv = cv2.bitwise_not(original_mask)
#cv2.imshow("Mask",original_mask)
#cv2.waitKey(0)
#cv2.imshow("MAsk in",original_mask_inv)
#cv2.waitKey(0)

cap = cv2.VideoCapture(0)
_,img = cap.read()
img_h, img_w = img.shape[:2]

while(True):
    _,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:

        #Location of the face
        face_x1 = x
        face_y1 = y
        face_w = w
        face_h = h
        face_x2 = face_x1 + face_w 
        face_y2 = face_y1 + face_h

        #Rescale filter to match face dimensions
        width_scale = 1.85
        filter_width = int(width_scale*face_w)
        filter_height = int(filter_width*org_dog_h/org_dog_w)

        #Positioning the filter 
        position_scale = 0.22
        filter_x1 = face_x1 + int(face_w/2)- int(filter_width/2)
        filter_y1 = face_y1 - int(filter_height*position_scale)
        filter_x2 = filter_x1 + filter_width
        filter_y2 = filter_y1 + filter_height

        #Check for filter being in frame
        if filter_x1<0:
            filter_x1 = 0      
        if filter_y1<0:
            filter_y1 = 0
        if filter_x2>img_w:
            filter_x2 = img_w
        if filter_y2>img_h:
            filter_y2 = img_h

        filter_width = filter_x2- filter_x1
        filter_height = filter_y2 - filter_y1  

        #Resize the filter according to the suitable dimensions
        dog = cv2.resize(dog, (filter_width, filter_height), interpolation = cv2.INTER_AREA)
        mask = cv2.resize(original_mask, (filter_width, filter_height), interpolation = cv2.INTER_AREA)
        mask_inv = cv2.resize(original_mask_inv, (filter_width, filter_height), interpolation = cv2.INTER_AREA)
        
        roi = img[filter_y1:filter_y2, filter_x1:filter_x2]

        #Placing the filter on the face
        bg = cv2.bitwise_and(roi,roi,mask = mask)
        fg = cv2.bitwise_and(dog,dog, mask = mask_inv)
        complete = cv2.add(bg,fg)
        img[filter_y1:filter_y2, filter_x1:filter_x2] = complete
    
    cv2.imshow("Filtered feed",img)

    if(cv2.waitKey(1)==13):
        break
    
    

cap.release()
cv2.destroyAllWindows()




    
