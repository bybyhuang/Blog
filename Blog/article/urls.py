from django.conf.urls import url

from  article import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view()),
    url(r'^detail/(?P<id>\d+)/$',views.ArticleDetailView.as_view(),name='detail'),
    url(r'^test/$',views.test),
    url(r'^home/$',views.home),
    url(r'^add/$',views.add,name='add'),
    url(r'^categoryList/(?P<category_id>\d+)/$',views.CategotyListView.as_view(),name='categoryList')
]