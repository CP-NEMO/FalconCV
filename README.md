
 ## FalconCV

FalconCV is an open-source python library that offers developers an interface to interact with some of the most popular computer vision frameworks, such as Tensorflow Object detection API and Detectron. The main objective behind it is to unify the set of tools available and simplify the use of them. This library is focused mainly on Computer Vision practitioners but also is flexible enough to allow researchers to configure the models at a low-level. Additionally, taking advantage of the fantastic features that OpenVINO offers, a custom model can be trained and optimized to run efficiently in the target hardware with just a few lines of code. It is important to say that FalconCV does not attempt to replace any of the tools mentioned previously; instead, it takes the best of them and offers a solution to improve accessibility to new users. 

<img src="data:image/png;base64,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" width="300px"/>

## Supported frameworks

- Tensorflow object detection API

## Roadmap

**Frameworks Support**

- Detectron2
- GluonCV

## Using Docker
Coming soon

## How to contribute
Send a pull request

## License

Free software: MIT license
Citation: haruiz. FalconCV. Git code (2020).https://github.com/haruiz/FhalconCV
