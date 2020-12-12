#from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name='Creator'
urlpatterns = [
     path('communities',login_required(views.CommunitiesView.as_view(),login_url='/Creator/login'),name="communities_view"),
     path('departments-colleges',login_required(views.DeptAndCollegesView.as_view(),login_url='/Creator/login'),name="departments_colleges_view"),
     path('students',login_required(views.StudentsView.as_view(),login_url='/Creator/login'), name="students_view"),
     path('skill-skill-category',login_required(views.SkillAndCategoryView.as_view(),login_url='/Creator/login'),name="skill_skill_category_view"),
     path('student-posts',login_required(views.StudentPostView.as_view(),login_url='/Creator/login'),name='student_posts_view'),
     path('jobs-companies',login_required(views.JobCompanyView.as_view(),login_url='/Creator/login'),name='jobs_companies_view'),
     path('activities',login_required(views.ActivitiesView.as_view(),login_url='/Creator/login'),name='activities_view'),
     path('get-departments-belonging-to-college/', views.getDepartmentsBelongingToCollege, name='get-departments-belonging-to-college'),
     path('validate-community-name/',views.validateCommunityName, name='validate-community-name'),
     path('validate-college-name/',views.validateCollegeName, name='validate-college-name'),
     path('validate-department-name/',views.validateDepartmentName, name='validate-department-name'),
     path('students-view/<str:id>/',login_required(views.viewStudentDetails,login_url='/Creator/login'),name="student_detail_view"),
     path('view-activity/<int:id>/',login_required(views.viewActivityDetails,login_url='/Creator/login'),name="activity_detail_view"),
     path('get-skills-of-a-category/',views.getSkillsOfACategory,name="get-skills-of-a-category"),
     path('validate-student-id/',views.validateStudentId,name="validate-user-id"),
     path('get-all-skills/',views.getAllSkills,name="get-all-skills"),
     path('get-all-jobs/',views.getAllJobs,name="get-all-jobs"),
     path('login',views.loginUser,name="login_view"),
     path('logout',views.logoutUser,name="logout"),
     path('unauthorized',views.unauthorizedView,name='unauthorized_view')
]  