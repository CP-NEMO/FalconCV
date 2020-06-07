# Home 

<div style="text-align:center">
    <img src="images/full_logo.png" width="400">
</div>

FalconCV is an open-source Python library that offers developers an interface to interact with some of the most popular computer vision frameworks, such as TensorFlow Object detection API and Detectron.

The main objective behind it is to unify the set of tools available and simplify the use of them. This library is focused mainly on Computer Vision practitioners but also is flexible enough to allow researchers to configure the models at a low-level.

Additionally, taking advantage of the fantastic features that OpenVINO offers, a custom model can be trained and optimized to run efficiently in the target hardware with just a few lines of code. It is important to say that FalconCV does not attempt to replace any of the tools mentioned previously; instead, it takes the best of them and offers a solution to improve accessibility to new users.

!!! warning
    This is a pre-release version of the FalconCV, which is still undergoing final testing before its official release. The website, its software and all content found on it are provided on an "as is" and "as available" basis. We hope to release an stable version soon. Another consideration is that FalconCV is compatible only with TensorFlow 1.x for now.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Q_l7RsAFiITJVj8yOMLR0yVNf97T7r43)

## Install FalconCV from GitHub source

### Create environment

1. Download and install Anaconda (Python 3+).
2. Open the anaconda terminal and execute:

```console
 conda create --name falconcv python=3.6
```

### Install dependencies

```console
pip install matplotlib
pip install numpy==1.17
pip install opencv-contrib-python
pip install pillow
pip install cython
pip install tqdm
pip install scipy
pip install requests
pip install clint
pip install validators
pip install more-itertools
pip install pandas
pip install imutils
pip install boto3
pip install "dask[complete]"
pip install lxml
pip install Mako
pip install colorlog
pip install colorama
pip install bs4
pip install pick
pip install -U scikit-learn
pip install gitpython
```

***Linux***

```console
conda install -c anaconda wxpython
sudo apt install protobuf-compiler
pip install pycocotools
```

***Windows***

```console
pip install wmi
pip install windows-curses
pip install pycocotools-win
```

### Install backends

***TensorFlow:***

```console
conda install tensorflow-gpu==1.15.0
```

## Install FalconCV from Github

```console
pip uninstall falconcv -y && pip install git+https://github.com/haruiz/FalconCV.git
```
