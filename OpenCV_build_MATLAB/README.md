# Opencv Build for MATLAB
+ Using [mexopencv](https://kyamagu.github.io/mexopencv/)
+ Original Build source for Windows [here](https://github.com/kyamagu/mexopencv/wiki/Installation-%28Windows%2C-MATLAB%2C-OpenCV-3%29)
+ Original Build source for Linux [here](https://github.com/kyamagu/mexopencv/wiki/Installation-(Linux,-MATLAB,-OpenCV-3))
+ MEX files are Matlab EXcutable files
+ Of course MATLAB is necessary
</br></br>

## [OpenCV](https://opencv.org/)
+ Open Source Library for Computer Vision, developed for Real-time Operation<br>
+ [Windows version build](#-windows-version) below
+ [Linux version build](https://github.com/kyamagu/mexopencv/wiki/Installation-(Linux,-MATLAB,-OpenCV-3))
<br><br>
## ● Linux version
+ Follow the instructions above link
+ Or simply use [opencv_matlab_linux.sh](https://github.com/engcang/Opencv_tutorial_Matlab_and_python/blob/master/OpenCV_build_MATLAB/opencv_matlab_linux.sh), before use, **MUST EDIT 'MATLABDIR' at last line**
~~~shell
$ cd
$ git clone https://github.com/engcang/Opencv_tutorial_Matlab_and_python && cd ~/Opencv_tutorial_Matlab_and_python/OpenCV_build_MATLAB/
$ chmod +x opencv_matlab_linux.sh
$ ./opencv_matlab_linux.sh
~~~
+ Then Execute MATLAB and
~~~MATLAB
>> cd('~/cv/mexopencv')
>> addpath('~/cv/mexopencv')
>> addpath('~/cv/mexopencv/opencv_contrib')
>> savepath()
>> cv.getBuildInformation()
~~~
You can see build information if built successfully
<br><br>
## ● Windows version
+ **Windows SDK** or **Microsoft Visual C++ 201X** is necessary _mex -setup c++_ below
+ [Download Mexopencv here](https://github.com/kyamagu/mexopencv/zipball/master), from original [mexopencv](https://kyamagu.github.io/mexopencv/)
+ Extract downloaded .zip file and then read **README.md** inside using MATLAB to know which version of OpenCV is needed
  <p align="left">
  <img src="https://github.com/engcang/image-files/blob/master/opencv/cvversion.JPG" width="450" hspace="120"/>
  </p>
+ [Download OpenCV here](https://opencv.org/releases.html) for the version checked above for **"Win pack"** <br>
+ Extract downloaded **OpenCV Win pack** file
+ Execute MATLAB and
~~~MATLAB
>> mex –setup c++
>> addpath('C:\path\to\mexopencv')
>> mexopencv.make('opencv_path', 'C:\OpenCV\build')
>> addpath('C:\path\to\mexopencv\opencv_contrib')
>> mexopencv.make('opencv_path','C:\OpenCV\build', 'opencv_contrib',true)
>> savepath()
~~~
+ Then simply type
~~~MATLAB
>> cv
~~~
to check if built well
