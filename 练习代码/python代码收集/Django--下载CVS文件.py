#views.py文件
from django.http import HttpResponse
import csv
 
UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273,281,304,203]
 
def unruly_passengers_csv(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment;filename=unruly.csv'
 
    writer = csv.writer(response)
    writer.writerow(['Year','Unruly Airline Passengers'])
    for (year,num) in zip(range(1995,2006),UNRULY_PASSENGERS):
        writer.writerow([year,num])
 
    return response
 
#urls.py文件
from django.conf.urls import patterns, include, url
from mysite.views import unruly_passengers_csv
 
urlpatterns = patterns('',
    (r'^unruly/$',unruly_passengers_csv),
    )
