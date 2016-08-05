from django.conf.urls import url

from  article import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^detail/(?P<my_args>\d+)/$',views.detail),
    url(r'^test/$',views.test),
    url(r'^home/$',views.home)
]