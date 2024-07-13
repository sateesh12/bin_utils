#!/usr/bin/python3
# Copyright  2024  Cyient
# Sateesh.Kalidas@cyient.com
# Development set-up
# 1. Setup an RTSP server which keeps streaming video, maybe a interesting  movie
# 2. Connect to the RTSP server from feature and view the video

import cv2
# Get an RTMP stream into the open-cv world
# RTMP address
my_rtmp_address = "rtmp://localhost/live/sateesh"
read_video = cv2.VideoCapture(my_rtmp_address)
out_video = cv2.VideoWriter('output.mp4', -1, 20.0, (640,800))

while(read_video.isOpened()):
    ret, i_frame = read_video.read()
    if ret == True:
        i_frame == cv2.flip(i_frame,0)
        # Here the algorithm from development team can be invoked
        # The code from the development team must show bounding boxes or detections in an understandable way for validation team.
        out_video.write(i_frame)
        cv2.imshow('RTMP Video stream shown in an OpenCV window',i_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

read_video.release()
out_video.release()
cv2.destroyAllWindows()


