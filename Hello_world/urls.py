
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.helloWorld),
    path('biker/', views.bikeFun),
    path('form/', views.formShow),
    path('model/', views.modelShow),
    path('model-form/', views.modelFormShow),

]
