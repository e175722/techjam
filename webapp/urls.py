from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('add/',views.form_upload, name='add'),
    #path('success/url/',views.success),
]
