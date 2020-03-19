from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('adminTop/add/',views.form_upload, name='add'),
    path('adminTop/',views.IndexAdminView.as_view(), name='admin'),
    path('adminTop/update/<int:pk>',views.UpdateView.as_view(), name='update'),
    path('adminTop/delete/<int:pk>/',views.DeleteView.as_view(), name='delete'),
]
