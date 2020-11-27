from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.shortcuts import redirect
from django.core.files import File

class CommunitiesView(View):
    def get(self,request):
        qsCommunities=Community.objects.all()
        context={
            'communities': qsCommunities
        }
        return render(request,'Communities.html',context)

class DeptAndCollegesView(View):
    def get(self,request):
        return render(request,'departments-colleges.html')

class SkillAndCategoryView(View):
    def get(self,request):
        return render(request,'skill-skill_category.html')

class StudentsView(View):
    def get(self, request):
        return render(request,'Students.html')
