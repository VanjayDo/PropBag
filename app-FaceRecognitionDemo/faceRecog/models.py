from django.db import models
from jsonfield import JSONField


# Create your models here.


class FaceChattr(models.Model):
    id = models.IntegerField(primary_key=True)
    charaValue = JSONField()  # 脸部特征值

    def __str__(self):
        return self.charaValue
