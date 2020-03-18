from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import UploadForm
from django.http import HttpResponse, HttpResponseRedirect

from .models import Employee, Admin, TagCategory, IntroductionCategory

import sys
# Create your views here.
class IndexView(generic.ListView):
    model = Employee
    paginate_by = 6


class DetailView(generic.DetailView):
    model = Employee


def form_upload(request):
    form = UploadForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('webapp:index')
    else:
        form = UploadForm()
        return render(request,'webapp/add_employee.html', {'form': form})
