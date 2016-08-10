from django.conf.urls import url

from  article import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^detail/(?P<id>\d+)/$',views.detail,name='detail'),
    url(r'^test/$',views.test),
    url(r'^home/$',views.home),
    url(r'^add/$',views.add,name='add')
]