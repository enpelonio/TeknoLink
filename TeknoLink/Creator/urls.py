#from django.contrib import admin
from django.urls import path
from . import views

app_name='Creator'
urlpatterns = [
     path('communities',views.CommunitiesView.as_view(),name="communities_view"),
     path('departments-colleges',views.DeptAndCollegesView.as_view(),name="departments_colleges_view"),
     path('students',views.StudentsView.as_view(), name="students_view"),
     path('skill-skill-category',views.SkillAndCategoryView.as_view(),name="skill_skill_category_view"),
     path('student-posts',views.StudentPostView.as_view(),name='student_posts_view'),
     path('get-departments-belonging-to-college/', views.getDepartmentsBelongingToCollege, name='get-departments-belonging-to-college'),
     path('validate-community-name/',views.validateCommunityName, name='validate-community-name'),
     #path('students-view',views.StudentDetailView.as_view(),name="student_detail_view"),
     path('get-skills-of-a-category/',views.getSkillsOfACategory,name="get-skills-of-a-category"),
     path('validate-student-id/',views.validateStudentId,name="validate-user-id")
]  