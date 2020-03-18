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

    def get_context_data(self, **kwargs):
        IntroductionsCategories = IntroductionCategory.objects.all()
        IntroductionCategoryById = {}

        for Category in IntroductionsCategories:
            IntroductionCategoryById[str(Category.id)] = Category.category_name

        tags = TagCategory.objects.all()
        tagById = {}
        for tag in tags:
            tagById[str(tag.id)] = tag.category


        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context ["IntroductionCategoryById"] = IntroductionCategoryById
        context ["tagById"] = tagById
        return context



def form_upload(request):
    form = UploadForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('webapp:index')
    else:
        form = UploadForm()
        return render(request,'webapp/add_employee.html', {'form': form})


'''
def form_upload(request):
    form = UploadForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('webapp:index')
    else:
        form = UploadForm()
        return render(request,'webapp/add_employee.html', {'form': form})
'''
