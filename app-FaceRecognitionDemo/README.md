# faceRecognitionDemo

### 说明
基于[face_recognition库](https://github.com/ageitgey/face_recognition)的一个使用django实现的人脸识别后台程序demo, 接收图片后分析图片中的人脸并取出特征值存入数据库供以后识别使用. 用于博客文章[初识Django](https://blog.safeandsound.cn/post/初识Django.html).

### Dockerfile
此处的Dockerfile可以用于构建该应用的镜像, 构建完成后请使用`docker run -d --name faceRecognitionDemo -p 8000:8000 构建镜像名 bash autostart`运行容器, 访问主机ip的绑定端口即可发现`this is just a test, and it works`字样, 说明运行成功.

### Centos上安装face_recognition
在运行`pip3 install face_recognition`之前请先运行`yun install python34-devel boost-devel`

### frontend目录
存放了本项目的前端项目, 基于vue编写.
