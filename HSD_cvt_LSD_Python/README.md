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
  1.For my case, used ROS or OpenCV to get image and setting the [row,col] range can easily crop the image<br>
  2.**cv.cvtColor(color_image, cv2.COLOR_BGR2HSV)** transforms RGB **cropped** image into HSV image <br><br>
<p align="center">
<img src="https://github.com/engcang/image-files/blob/master/opencv/py_raw.JPG" width="480" hspace="30"/>
</p>
<br>
Showing Raw image
<p align="left">
<img src="https://github.com/engcang/image-files/blob/master/opencv/py_white_mask.JPG" width="360" hspace="30"/>  
<img src="https://github.com/engcang/image-files/blob/master/opencv/py_mask2.JPG" width="360" hspace="30"/>  
</p>

<br><br>
### ● Line Detect and draw
  ~~~python
  index_L_mask = L_mask>0
  index_R_mask = R_mask>0

  yello=np.zeros_like(crop_L,np.uint8)
  white=np.zeros_like(crop_R,np.uint8)
  yello[index_L_mask]= crop_L[index_L_mask]
  white[index_R_mask]=crop_R[index_R_mask]
  cv2.imshow('masked1',yello)
  cv2.waitKey()
  cv2.imshow('masked2',white)
  cv2.waitKey()
  yello_line = LSD.detect(L_mask)
  white_line = LSD.detect(R_mask)
  LSD.drawSegments(img[350:410,40:220],yello_line[0])
  LSD.drawSegments(img[350:410,402:582],white_line[0])
  cv2.imshow('Lines',img[350:410,:])
  cv2.waitKey()
  ~~~
  3.Using **cv.inRange**, Mask image in HSV color range from [14,0,120] to [255,200,220] (approximately white and yellow line) <br>
  4.**LSD=cv.LineSegmentDetector** makes handler for line detector <br>
  5.**LSD.detect** returns lines (if exist) for the given image, in this case **mask** was given after .*255 cause it is Logical type value(Only 0 or 1)<br>
  6.**LSD.drawSegments** draw lines on image <br><br>
<p align="center">
<img src="https://github.com/engcang/image-files/blob/master/opencv/cropped_Lines.jpg" width="480" hspace="0"/>
</p>

<br>

## ● Applying this code, Real Robot(Turtlebot3) can drive with Lane Keeping : [here]()

<br>
