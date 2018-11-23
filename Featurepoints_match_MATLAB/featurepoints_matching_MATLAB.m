% Simple demo to visualize SURF features

% close all; 
% clc;
% rosshutdown
% rosinit('192.168.2.15')

% feature extraction of reference
ref_img = imread('reference.jpg'); % load reference image
ref_img_gray = rgb2gray(ref_img); % rgb2gray
ref_pts = detectSURFFeatures(ref_img_gray); % finds SURF features structure variable (Location)
[ref_features,  ref_validPts] = extractFeatures(ref_img_gray,  ref_pts);  % (ref_features will be used to compare)

% sub_image = rossubscriber('/zed/rgb/image_rect_color/compressed');
while 1
    color_image_temp = receive(sub_image);
    def_img = readImage(color_image_temp);
    
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
    
    % Define Geometric Transformation Objects
    try
    [tform,inlierpoints1,inlierpoints2] = estimateGeometricTransform(def_matched_pts, ref_matched_pts,'affine'); %RANSAC to save only inlier, 'similarity','projective' https://kr.mathworks.com/help/vision/ref/estimategeometrictransform.html
    figure(4); % Draw the lines to matched points
    showMatchedFeatures(def_img, ref_img, inlierpoints1, inlierpoints2, 'montage');    %showing matched features (only inliers)
    catch
        disp('not enough feature points pairs')
    end
end
