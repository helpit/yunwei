#views.py文件
from django.http import HttpResponse
 
def my_image(request):
    image_data = open("picture.png","rb").read()
    return HttpResponse(image_data,mimetype="image/png")
 
#urls.py文件
from django.conf.urls import patterns, include, url
from mysite.views import my_image
 
urlpatterns = patterns('',
    (r'^image/$',my_image),
    )
