#!/bin/bash
sudo apt-get autoremove libopencv-dev
sudo apt-get -y install build-essential cmake pkg-config git
sudo apt-get -y install zlib1g-dev libjpeg-dev libpng12-dev libpng16-dev libtiff5-dev libjasper-dev libopenexr-dev
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get -y install libv4l-dev libdc1394-22-dev libxine2-dev libgphoto2-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev 
sudo apt-get -y install libgtk2.0-dev libtbb-dev libeigen3-dev libblas-dev liblapacke-dev libatlas-base-dev
# library installation done!
mkdir ~/cv && cd ~/cv
wget -O opencv-3.4.1.zip https://github.com/opencv/opencv/archive/3.4.1.zip
wget -O opencv_contrib-3.4.1.zip https://github.com/opencv/opencv_contrib/archive/3.4.1.zip
unzip opencv-3.4.1.zip
unzip opencv_contrib-3.4.1.zip

mkdir ~/cv/build && cd ~/cv/build
cmake -G "Unix Makefiles" \
    -DBUILD_DOCS=OFF \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_PERF_TESTS=OFF \
    -DBUILD_TESTS=OFF \
    -DBUILD_JAVA=OFF \
    -DWITH_CUDA=OFF \
    -DWITH_CUBLAS=OFF \
    -DWITH_CUFFT=OFF \
    -DWITH_NVCUVID=OFF \
    -DWITH_MATLAB=OFF \
    -DBUILD_opencv_cudaarithm=OFF \
    -DBUILD_opencv_cudabgsegm=OFF \
    -DBUILD_opencv_cudacodec=OFF \
    -DBUILD_opencv_cudafeatures2d=OFF \
    -DBUILD_opencv_cudafilters=OFF \
    -DBUILD_opencv_cudaimgproc=OFF \
    -DBUILD_opencv_cudalegacy=OFF \
    -DBUILD_opencv_cudaobjdetect=OFF \
    -DBUILD_opencv_cudaoptflow=OFF \
    -DBUILD_opencv_cudastereo=OFF \
    -DBUILD_opencv_cudawarping=OFF \
    -DBUILD_opencv_cudev=OFF \
    -DBUILD_opencv_java=OFF \
    -DBUILD_opencv_java_bindings_generator=OFF \
    -DBUILD_opencv_js=OFF \
    -DBUILD_opencv_python2=OFF \
    -DBUILD_opencv_python3=OFF \
    -DBUILD_opencv_python_bindings_generator=OFF \
    -DBUILD_opencv_ts=OFF \
    -DBUILD_opencv_world=OFF \
    -DBUILD_opencv_matlab=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr/local \
    -DOPENCV_ENABLE_NONFREE=ON \
    -DOPENCV_EXTRA_MODULES_PATH=~/cv/opencv_contrib-3.4.1/modules ~/cv/opencv-3.4.1
make
sudo make install

#add cmake prefix lib-dir to locations searched for shared libraries
sudo sh -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv3.conf'
sudo ldconfig

export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH
pkg-config --modversion opencv
pkg-config --cflags --libs opencv

#mexopencv
cd ~/cv
wget -O mexopencv-master.zip https://github.com/kyamagu/mexopencv/archive/master.zip
unzip mexopencv-master.zip && mv mexopencv-master mexopencv

#matlab directory should be edited 
cd ~/cv/mexopencv
make MATLABDIR=~/Document/Matlab2018 WITH_CONTRIB=true all contrib
