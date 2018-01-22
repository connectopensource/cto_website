from django.conf.urls import url
from . import views

# urlpatterns = [
#     url(r'^$', views.post_list, name='blog_post'),
# ]
urlpatterns = [
    url(r'^about/$', views.about_us, name='about'),
    url(r'^$', views.home_view, name='home'),
    url(r'^home/$', views.home_view, name='home'),

]