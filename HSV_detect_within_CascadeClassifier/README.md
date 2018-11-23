# Detect object using _**CascadeClassifier**_ AND **Color detection** in OpenCV, Python
+ Using trained result _**.xml**_ file from [_here_](https://github.com/engcang/CascadeObjectDetector_MATLAB_Python/tree/master/Train_Detector_MATLAB) via MATLAB
+ Detecting code is using from [_here_](https://github.com/engcang/CascadeObjectDetector_MATLAB_Python/tree/master/Detect_Python)
</br></br>

## Detector code running
+ Python<br><br>
  ~~~python
  #!/usr/bin/env python
  """
  Created on Tue Nov  6 17:36:50 2018
  @author: mason
  """

  import numpy as np
  import cv2
  import time

  cap = cv2.VideoCapture(1)
  detector_start = cv2.CascadeClassifier('name.xml')
  time.sleep(1) #wait 1 second till camera data comes in

  def detecting(image):
      scale=1.2 # resize .*100%, smaller detect more but take longer
      minNeighbors=6 # when higher, higher quality, less detection
      detected_img = detector_start.detectMultiScale(image,scale,minNeighbors)
      for (x,y,w,h) in detected_img:
          cv2.rectangle(image, (x,y), (x+w,y+h),(100,255,0), 2)
          cv2.putText(image,'Detected',(x-5,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.3,(100,255,0), 2)

  while 1:
      a=time.time()
      ret, image = cap.read()
      #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      detecting(image)
      print(time.time()-a)    
      cv2.imshow('detected_image',image)
      if cv2.waitKey(1)>0 : break
  ~~~
<br>

1.For me, used OpenCV to get and consequtive images <br><br>

2.make detector handler using _**'cv2.CascadeClassifier('name.xml')'**_ <br><br>

3.and detect image using _**'detector_start.detectMultiScale(image,scale,minNeighbors)'**_ it yields _**'detected_img'**_ which is in rectangle form (x_start_point,y_start_point,width,height) <br><br>

4.using _**cv2.rectangle**_ and _**cv2.putText**_, showing detected part of image <br><br><br>

  <p align="center">
  <img src="" width="600" hspace="0"/>
  </p></br>


