from django.conf.urls import url
from .import views
app_name='loginandregapp'
urlpatterns=[
    url(r'^$',views.reg,name='reg'),
    url(r'^login$',views.login,name='login'),
]