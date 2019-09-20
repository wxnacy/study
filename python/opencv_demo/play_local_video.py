#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 播放本地视频

import cv2

cap = cv2.VideoCapture('/Users/wxnacy/Downloads/xiaobai.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

#  while(cap.isOpened()):
    #  ret, frame = cap.read()
    #  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #  cv2.imshow('frame',gray)
    #  if cv2.waitKey(1) & 0xFF == ord('q'):
        #  break

cap.release()
cv2.destroyAllWindows()
