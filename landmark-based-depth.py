#!/usr/bin/python3
#Author : Sateesh Kalidas
#Date   : 13/July/2024
#Reference: https://medium.com/artificialis/swift-and-simple-calculate-object-distance-with-ease-in-just-few-lines-of-code-38889575bb12
#Purpose : Landmark based depth estimation
import mediapipe as mp
import cv2
import numpy as np

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode = False)


#Not sure
alpha = 0.6
previous_depth = 0.0


#Filter the depth
def apply_ema_filter(current_depth):
    global previous_depth
    filtered_depth = alpha * current_depth + (1 - alpha) * previous_depth
    previous_depth = filtered_depth
    return filtered_depth


# Relative depth into m, this is like black magic
def depth_to_distance(depth_value, depth_scale):
    return -1.0 / (depth_value * depth_scale)


# Input camera feed
cap = cv2.VideoCapture('distance.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(img)
    if results.pose_landmarks is not None:
        landmarks = [ ]

        for landmark in results.pose_landmarks.landmark:
            landmarks.append((landmark.x, landmark.y, landmark.z))

        nose_landmark = landmarks[mp_pose.PoseLandmark.NOSE.value]
        _,_,nose_z = nose_landmark

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        filter = apply_ema_filter(nose_z)
        distance = depth_to_distance(filter,1)
        
        cv2.putText(img, 'Depth units:' + str(np.format_float_positional(distance, precision=1)),(20,50),cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255),3)
        cv2.imshow('ImgWindow',img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
        
