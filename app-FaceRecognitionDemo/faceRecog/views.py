from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from faceRecog.models import FaceChattr
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import face_recognition as fr
import os
import json
import logging

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("<h1>this is just a test, and it works</h1>")


def storeImg(request):
    image = request.FILES.get('faceImg')
    if 1024 < image.size < 20480000:
        path = default_storage.save('static/faceImg/' + image.name, ContentFile(image.read()))
        os.path.join(settings.MEDIA_ROOT, path)
        logger.info("接收图片: " + image.name + " 成功")
        return path
    else:
        return None


def getFaceEncoding(imgPath):
    img = fr.load_image_file(imgPath)
    faceEncoding = fr.face_encodings(img)
    return faceEncoding


def recogFace(unknownFaceEncoding):
    try:
        knownFaces = FaceChattr.objects.all()
        faces = []
        for face in knownFaces:
            face.charaValue = json.loads(face.charaValue)
            faces.append(face.charaValue)
        results = fr.compare_faces(faces, unknownFaceEncoding)
        if True in results:
            result = True
        else:
            result = False
        return result
    except Exception as e:
        print(e)


# 新用户脸部信息添加模块
@csrf_exempt
def addFace(request):
    try:
        path = storeImg(request)
        unknownFaceEncoding = getFaceEncoding(path)
        if not len(unknownFaceEncoding):
            return HttpResponse("<script>alert('未检测到人脸');"
                                "window.location.href='http://localhost:8080/#/AddNewFace';</script>")
        unknownFaceEncoding = unknownFaceEncoding[0]  # 取出list中的第一个数组元素
        if not recogFace(unknownFaceEncoding):
            unknownFaceEncoding = unknownFaceEncoding.tolist()  # numpy.ndarray转list类型
            unknownFaceEncoding = json.dumps(unknownFaceEncoding)  # list转json
            new = FaceChattr(charaValue=unknownFaceEncoding)  # 赋值持久化
            new.save()
            return HttpResponse('saved, charaValue is: ' + unknownFaceEncoding)
        else:
            return HttpResponse("<script>alert('已添加过');"
                                "window.location.href='http://localhost:8080/#/AddNewFace';</script>")
    except Exception as e:
        print(e)
        return HttpResponse("some error happened")


# 老用户脸部识别模块
# 接收图片并进行识别,对数据库中已有信息进行比对
@csrf_exempt
def whetherOldFriend(request):
    try:
        path = storeImg(request)
        unknownFaceEncoding = getFaceEncoding(path)
        if not len(unknownFaceEncoding):
            return HttpResponse("<script>alert('未检测到人脸');"
                                "window.location.href='http://localhost:8080/#/whetherOldFriend';</script>")
        unknownFaceEncoding = unknownFaceEncoding[0]  # 取出list中的第一个数组元素
        result = recogFace(unknownFaceEncoding)
        if result:
            return HttpResponse("welcome, old friend")
        else:
            return HttpResponse("sorry, I don't know you")
    except Exception as e:
        print(e)
        return HttpResponse("some error happened")
