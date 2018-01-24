
# coding: utf-8

# In[7]:


# loading settup
caffe_root = "/home/nvidia/caffe/"
model_weights = caffe_root + "examples/mnist/lenet_iter_10000.caffemodel"
model_def = caffe_root + "examples/mnist/lenet.prototxt"
# set up Python environment: numpy for numerical routines, and matplotlib for plotting
import numpy as np
import scipy
import os.path
import time
# import matplotlib.pyplot as plt
from PIL import Image
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe
# caffe.set_mode_cpu()
caffe.set_device(0)
caffe.set_mode_gpu()#coding=utf-8



# In[8]:


os.chdir(caffe_root)
net_file=caffe_root + 'models/bvlc_googlenet/deploy.prototxt'
caffe_model=caffe_root + 'models/bvlc_googlenet/bvlc_googlenet.caffemodel'
mean_file=caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy'



# In[10]:


net = caffe.Net(net_file,caffe_model,caffe.TEST)
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))
transformer.set_raw_scale('data', 255) 
transformer.set_channel_swap('data', (2,1,0))

im=caffe.io.load_image(caffe_root+'examples/images/cat1.jpg')
net.blobs['data'].data[...] = transformer.preprocess('data',im)
out = net.forward()


imagenet_labels_filename = caffe_root + 'data/ilsvrc12/synset_words.txt'
labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')




# In[11]:


top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]


# In[12]:


print top_k
for i in np.arange(top_k.size):
     print top_k[i], labels[top_k[i]]
    

