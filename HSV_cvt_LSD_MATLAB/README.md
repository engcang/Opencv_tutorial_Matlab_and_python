# HSV convert and LineSegmentDetection using OpenCV in MATLAB
+ Build OpenCV in MATLAB : [here](https://github.com/engcang/Opencv_tutorial_Matlab_and_python/tree/master/OpenCV_build_MATLAB)
+ What's [HSV](https://en.wikipedia.org/wiki/HSL_and_HSV)
</br></br>

## Code explanation 
***
### ● HSV convert
  ~~~MATLAB
  %color_image_temp = receive(sub_image);
  %color_image_temp.Format = 'bgr8; jpeg compressed bgr8' ;
  %color_image = readImage(color_image_temp);
  HSV_image = cv.cvtColor(color_image,'BGR2HSV');
  figure(1); imshow(color_image);
  figure(2); imshow(HSV_image);
  ~~~
  <br>
  1.For my case, used ROS to get image <br>
  2.**cv.cvtColor(color_image,'BGR2HSV');** transforms RGB image into HSV image <br>
<p align="left">
<img src="https://github.com/engcang/image-files/blob/master/opencv/raw.JPG" width="360" hspace="30"/>
<img src="https://github.com/engcang/image-files/blob/master/opencv/hsv.JPG" width="360" hspace="30"/>  
</p>

<br><br>
### ● LineSegmentDetection
  ~~~MATLAB
  mask=cv.inRange(HSV_image(240:480,:,:),[14,0,120],[255,200,220]);
  figure(3);imshow(mask);
  LSD=cv.LineSegmentDetector
  lines=LSD.detect(mask.*255);
  if size(lines,2)>0
    drew_img=LSD.drawSegments(color_image(240:480,:,:),lines);
    figure(4);imshow(drew_img);
  end
  ~~~
  <br>
  3.Using **cv.inRange**, Mask image in HSV color range from [14,0,120] to [255,200,220] (approximately white and yellow line)
  4.**LSD=cv.LineSegmentDetector** makes handler for line detector
  5.**LSD.detect** returns lines (if exist)
  6.**LSD.drawSegments** draw lines on image
<br><br>
### ● Line Detection for raw image
  ~~~MATLAB
  lines2=LSD.detect(rgb2gray(color_image));
  drew_img2=LSD.drawSegments(color_image,lines2);
  figure(5);imshow(drew_img2);
  ~~~
  <p align="center">
  <img src="https://github.com/engcang/image-files/blob/master/opencv/raw_LineSeg.JPG" width="480" hspace="0"/>
  </p>
