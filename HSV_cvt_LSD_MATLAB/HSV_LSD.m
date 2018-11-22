%rosinit('192.168.2.8')
%sub_image = rossubscriber('/raspicam_node/image/compressed')

LSD=cv.LineSegmentDetector
%while 1
%color_image_temp = receive(sub_image);
%color_image_temp.Format = 'bgr8; jpeg compressed bgr8' ;
%color_image = readImage(color_image_temp);
HSV_image = cv.cvtColor(color_image,'BGR2HSV');
figure(1); imshow(color_image);
figure(2); imshow(HSV_image);
mask=cv.inRange(HSV_image(240:480,:,:),[14,0,120],[255,200,220]);
figure(3);imshow(mask);
lines=LSD.detect(mask.*255);
if size(lines,2)>0
  drew_img=LSD.drawSegments(color_image(240:480,:,:),lines);
  figure(4);imshow(drew_img);
end
%end
