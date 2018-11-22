# HSV convert and LineSegmentDetection using OpenCV in MATLAB
+ Build OpenCV in MATLAB : [here](https://github.com/engcang/Opencv_tutorial_Matlab_and_python/tree/master/OpenCV_build_MATLAB)
+ [HSV](https://en.wikipedia.org/wiki/HSL_and_HSV)
</br></br>

## Code explanation 
***
### ● HSV convert
  ~~~MATLAB
  LSD=cv.LineSegmentDetector
  %color_image_temp = receive(sub_image);
  %color_image_temp.Format = 'bgr8; jpeg compressed bgr8' ;
  %color_image = readImage(color_image_temp);
  HSV_image = cv.cvtColor(color_image,'BGR2HSV');
  figure(1); imshow(color_image);
  figure(2); imshow(HSV_image);
  ~~~
<br><br>
### ● LineSegmentDetection
  ~~~MATLAB
  mask=cv.inRange(HSV_image(240:480,:,:),[14,0,120],[255,200,220]);
  figure(3);imshow(mask);
  lines=LSD.detect(mask.*255);
  if size(lines,2)>0
    drew_img=LSD.drawSegments(color_image(240:480,:,:),lines);
    figure(4);imshow(drew_img);
  end
  ~~~
<br><br>
### ● Line Detection for raw image
  ~~~MATLAB
  lines2=LSD.detect(rgb2gray(color_image));
  drew_img2=LSD.drawSegments(color_image,lines2);
  figure(5);imshow(drew_img2);
  ~~~
  <p align="center">
  <img src="https://github.com/engcang/image-files/tree/master/opencv/raw_LineSeg.JPG" width="480" hspace="0"/>
  </p>
