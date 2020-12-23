import face_recognition
import cv2
import numpy as np
from datetime import datetime

cap=cv2.VideoCapture(0)
known_face_encodings=[]
known_face_names=[]


mark=face_recognition.load_image_file('/Users/shashwat/master training openpycv/images/mark.jpg')
immarkencode=face_recognition.face_encodings(mark)[0]



known_face_encodings=[immarkencode]
known_face_names=['mark']

face_locations=[]
face_encodings=[]
face_names=[]
process_this_frame=True

i=0
got_name=[]
while True:
    ret,frame=cap.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    rgb_small_frame=small_frame[:,:,::-1]
    if process_this_frame:
        face_locations=face_recognition.face_locations(rgb_small_frame)
        face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
        name_list=[]
        face_names=[]
        for face_encoding in face_encodings:
            matches=face_recognition.compare_faces(known_face_encodings,face_encoding,tolerance=0.5)
            face_distances=face_recognition.face_distance(known_face_encodings,face_encoding)
            best_match_index=np.argmin(face_distances)
            if matches[best_match_index]:
                name=known_face_names[best_match_index]
                face_names.append(name)
    i=i+1
    if i==5:
        curr_name=name
        print(curr_name)
        got_name.append(curr_name)
    if len(face_names)==0:
        i=0
    process_this_frames=not process_this_frame
    for(top,right,bottom,left), name in zip(face_locations,face_names):
        top*=2
        right*=2
        bottom*=2
        left*=2
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        cv2.rectangle(frame,(left,bottom-35),(right,bottom),(0,255,255),cv2.FILLED)
        cv2.putText(frame,name,(left+6,bottom-6),cv2.FONT_HERSHEY_COMPLEX,1.0,(255,255,0),1)
    cv2.imshow('got you',frame)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()
print(got_name)    
