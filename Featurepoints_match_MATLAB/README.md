# Feature points detect and match in MATLAB (SURF)
+ Speeded-Up Robust Features detect [MATLAB html in Computer Vision System Toolbox](https://kr.mathworks.com/help/vision/ref/detectsurffeatures.html)
+ RANSAC algorithm to get inliers [MATLAB html in Computer Vision System Toolbox](https://kr.mathworks.com/help/vision/ref/estimategeometrictransform.html)
</br></br>

## Code explanation 
***
### ● Get feature points from Reference image
  ~~~MATLAB
  % feature extraction of reference
  ref_img = imread('reference.jpg'); % load reference image
  ref_img_gray = rgb2gray(ref_img); % rgb2gray
  ref_pts = detectSURFFeatures(ref_img_gray); % finds SURF features structure variable (Location)
  [ref_features,  ref_validPts] = extractFeatures(ref_img_gray,  ref_pts);  % (ref_features will be used to compare)
  ~~~
  1.Get reference image to be compared and converted to gray scale <br>
  2.**detectSURFFeatures()** finds SURF features structure variable <br>
  3.**extractFeatures()** function extract _features value_ to be compared and _validPts_ which are location of feature points <br>

<br><br>
### ● Get feature points from Target image and match them
  ~~~MATLAB
  % feature extraction of defect
    def_img_gray = rgb2gray(def_img); % rgb2gray
    def_pts = detectSURFFeatures(def_img_gray); % finds SURF features
    [def_features, def_validPts] = extractFeatures(def_img_gray, def_pts);
                                                                                %same with above
    
    % Compare defect and refence
    index_pairs = matchFeatures(ref_features, def_features);        % Compare and save matched pairs
    ref_matched_pts = ref_validPts(index_pairs(:,1)).Location;      % Location
    def_matched_pts = def_validPts(index_pairs(:,2)).Location;
    figure(3);
    showMatchedFeatures(def_img, ref_img, def_matched_pts, ref_matched_pts, 'montage'); % showing matched features
  ~~~
  3.Using **cv.inRange**, Mask image in HSV color range from [14,0,120] to [255,200,220] (approximately white and yellow line) <br>
  4.**LSD=cv.LineSegmentDetector** makes handler for line detector <br>
  5.**LSD.detect** returns lines (if exist) for the given image, in this case **mask** was given after .* 255 cause it is Logical type value(Only 0 or 1)<br>
  6.**LSD.drawSegments** draw lines on image 

<br><br>
### ● Get feature points from Target image and match them
  ~~~MATLAB
  % Define Geometric Transformation Objects
    try
    [tform,inlierpoints1,inlierpoints2] = estimateGeometricTransform(def_matched_pts, ref_matched_pts,'affine'); %RANSAC to save only inlier, 'similarity','projective' https://kr.mathworks.com/help/vision/ref/estimategeometrictransform.html
    figure(4); % Draw the lines to matched points
    showMatchedFeatures(def_img, ref_img, inlierpoints1, inlierpoints2, 'montage');    %showing matched features (only inliers)
    catch
        disp('not enough feature points pairs')
    end
  ~~~

<p align="center">
<img src="https://github.com/engcang/image-files/blob/master/opencv/SURF.gif" width="1021" hspace="0"/>
</p>
<br>
