# Detect object using _**CascadeClassifier**_ AND **Color detection** in OpenCV, Python
+ Using trained result _**.xml**_ file from [_here_](https://github.com/engcang/CascadeObjectDetector_MATLAB_Python/tree/master/Train_Detector_MATLAB) via MATLAB
+ Detecting code is using from [_here_](https://github.com/engcang/CascadeObjectDetector_MATLAB_Python/tree/master/Detect_Python)
</br></br><br>

## Detector code running
+ Detect via classifier and count the pixel numbers <br>
  ~~~python
  def detector(self,img,hsv):
    global detector_start
    scale=1.2 # resize .*100%, smaller detect more but take longer
    minNeighbors=6 # higer, higer quality, less detection
    bbox_start = detector_start.detectMultiScale(img,scale,minNeighbors)
    if np.shape(bbox_start)[0]!=0:
        if color_pixel_number(hsv,[(170,150,80),(180,255,130)],bbox_start)>300: #pixel number condition should be tuned
            print('start_sign detected')
  ~~~
<br>

1.For me, used ROS to get and consequtive images <br>

2.make detector handler using _**'cv2.CascadeClassifier('name.xml')'**_ <br><br>

3.and detect image using _**'detector_start.detectMultiScale(image,scale,minNeighbors)'**_ it yields _**'detected_img'**_ which is in rectangle form (x_start_point,y_start_point,width,height) <br><br>

4.using _**detected_img**_ from above, count pixel numbers inside rectangle(_**detected_img**_) which is in range of HSV values of wanted object <br><br>

5.If Detected, print('sign detected') and show image by **cv2.imshow()** <br><br>

+ Pixel number counting function
  ~~~python
  def color_pixel_number(hsv,color,bbox):
    if np.shape(bbox)[0]>1:
        area=np.zeros(np.shape(bbox)[0])
        for i in range(np.shape(bbox)[0]):
            area[i]=bbox[i][2]*bbox[i][3]
        I=list(area).index(max(area))
        mask = cv2.inRange(hsv[bbox[I][1]:bbox[I][1]+bbox[I][3],bbox[I][0]:bbox[I][0]+bbox[I][2]],color[0],color[1])
        index_mask=mask>0
    else:
        mask = cv2.inRange(hsv[bbox[0][1]:bbox[0][1]+bbox[0][3],bbox[0][0]:bbox[0][0]+bbox[0][2]],color[0],color[1])
        index_mask=mask>0
    print (np.sum(index_mask))
    return np.sum(index_mask)
  ~~~
<br>

6.when rectangle bbox is plural, the biggest bbox will be considered <br>
7.Using _**numpy.sum()**_ function, count pixel numbers of masked image <br><br>


  <p align="center">
  <img src="" width="600" hspace="0"/>
  </p></br>


