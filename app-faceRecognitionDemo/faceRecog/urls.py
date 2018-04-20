from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('whetherOldFriend', views.whetherOldFriend, name='whetherOldFriend'),
    url('addFace', views.addFace, name='addFace'),

]
