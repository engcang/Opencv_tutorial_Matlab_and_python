# HSV convert and masking and then Line Detect in Python using OpenCV
+ What's [HSV](https://en.wikipedia.org/wiki/HSL_and_HSV)
+ ROS version and OpenCV version codes are available to get image in different ways
</br></br><br>

## Code explanation 
***
### ● HSV convert and Mask cropped image
  ~~~python
  hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
  LSD = cv2.createLineSegmentDetector(0)
  crop_L=hsv[350:410,40:220]
  crop_R=hsv[350:410,402:582]
  L_mask = cv2.inRange(crop_L,(36,0,165),(255,255,255))
  R_mask = cv2.inRange(crop_R,(21,50,100),(36,255,255))
  ~~~
  <br>
  
  1.For my case, used ROS or OpenCV to get image and setting the [row,col] range can easily crop the image<br><br>
    + cropped image to see right in front of forward path
  2.**cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)** transforms RGB **cropped** image into HSV image <br><br>
  3.Using **cv2.inRange**, Mask image in HSV color range (approximately white and yellow line) <br>
  
<p align="center">
<img src="https://github.com/engcang/image-files/blob/master/opencv/py_raw.JPG" width="480" hspace="30"/>
</p>

+ Showing Raw image and masked image for White and masked image for Yellow <br>
<br>

<p align="left">
<img src="https://github.com/engcang/image-files/blob/master/opencv/py_white_mask.JPG" width="360" hspace="30"/>  
<img src="https://github.com/engcang/image-files/blob/master/opencv/py_mask2.JPG" width="360" hspace="30"/>  
</p>

<br><br>
### ● Line Detect and draw
  ~~~python
  yello_line = LSD.detect(L_mask)
  white_line = LSD.detect(R_mask)
  LSD.drawSegments(img[350:410,40:220],yello_line[0])
  LSD.drawSegments(img[350:410,402:582],white_line[0])
  cv2.imshow('Lines',img[350:410,:])
  cv2.waitKey()
  ~~~
 
  4.**LSD.detect** returns lines (if exist) for the given image, in this case **mask** was given<br><br>
  5.**LSD.drawSegments** draw lines on image <br><br>
<p align="center">
<img src="https://github.com/engcang/image-files/blob/master/opencv/py_cropped_lines.JPG" width="480" hspace="0"/>
</p>

<br>

## ● Applying this code, Real Robot(Turtlebot3) can drive with Lane Keeping : [here]()

<br>
