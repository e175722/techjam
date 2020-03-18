from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import Employee, Admin, TagCategory, IntroductionCategory

# Create your views here.
class IndexView(generic.ListView):
    model = Employee
    paginate_by = 9
