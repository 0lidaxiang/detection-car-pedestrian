# detection-car-pedestrian

## Detectect the cat kinds and others
识别猫的代码使用了自带的model去识别,效果还不错.

The result show:
![Detectect the cat kinds](./images/detectect-the-cat.png)

## Detectect the MNIST handwritten digit database
手写数字的图片识别.

[This database link](http://yann.lecun.com/exdb/mnist/)

The result show:
![Detectect the MNIST handwritten digit](./images/detect-handwritten-digit.png)

## Socket
python-socket 部分是为了传输 tx2 里面的预测结果到另外一台电脑上所做的工作.  
基本是为了给下面一项 python-camera 所做的辅助工作.

## python-camera
使用 Python 调用已有模型去分类和识别.  
[bvlc_googlenet.caffemodel 下载地址](http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel)

#### tegra-cam.py
这里只是用Python调用打开 tx2 的板载摄像头或者外接的 USB 摄像头.  
外接USB摄像头明显反应速度和识别像素高太多.

1. dump帮助信息：
```
python3 tegra-cam-caffe.py --help
```
2. 使用默认的bvlc_reference_caffenetmodel使用Jetson机载相机(python程序的默认行为)来进行Caffe图像分类。
python3 tegra-cam-caffe.py

3. 使用USB网络摄像头 /dev/video1 ，同时分辨率设置为 1280x720.
python3 tegra-cam-caffe.py --usb --vid 1 --width 1280 --height 720

4. 或者使用IP摄像头.(未测试)
```
python3 tegra-cam-caffe.py --rtsp --uri rtsp://admin:XXXXXX@192.168.1.64:554
```

原文和使用链接如下:
[在Jetson TX2上用Python捕获摄像头影像](http://www.jetsoner.com/thread-147-1-1.html)

#### tegra-cam-caffe.py
用板载摄像机对不同的Caffe模型进行图像分类:
```
python tegra-cam-caffe.py --prototxt $HOME/caffe/models/bvlc_googlenet/deploy.prototxt \
                             --model  $HOME/caffe/models/bvlc_googlenet/deploy.prototxt \
                             --labels $HOME/caffe/data/ilsvrc12/synset_words.txt \
                             --mean $HOME/caffe/data/ilsvrc12/imagenet_mean.binaryproto
```

[在Jetson TX2上用Python捕获摄像头影像，并用Caffe进行推理 ](http://www.jetsoner.com/thread-149-1-1.html)


