#from django.contrib import admin
from django.urls import path
from . import views

app_name='Creator'
urlpatterns = [
     path('communities',views.CommunitiesView.as_view(),name="communities_view"),
     path('departments-colleges',views.DeptAndCollegesView.as_view(),name="departments_colleges_view"),
     path('students',views.StudentsView.as_view(),name="students_view"),
     path('skill-skill-category',views.SkillAndCategoryView.as_view(),name="skil_skill_category_view"),
]  