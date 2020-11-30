from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.shortcuts import redirect
from django.core.files import File
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
from django.utils import timezone,dateformat
#functions
@csrf_exempt
def getDepartmentsBelongingToCollege(request):
    college_name=request.GET.get('college_name',None)
    departmentNames={}
    if(college_name is not None and college_name!=''):
        collegeId=College.objects.get(name=college_name).id
        for dept in Department.objects.filter(college_id=collegeId):
            departmentNames[dept.id]=dept.name
    else:
        for dept in Department.objects.all():
            departmentNames[dept.id]=dept.name
    data={
        'departments': departmentNames
    }
    return JsonResponse(data)
def getSkillsOfACategory(request):
    category_id=request.GET.get('category_id',None)
    category=Skill_Category.objects.get(id=category_id)
    skillsInCategory=Skill.objects.filter(category=category)
    skills={}
    for skill in skillsInCategory:
        skills[skill.id]=skill.name
    data={
        'skills': skills
    }
    return JsonResponse(data)

def validateCommunityName(request):
    com_name=request.GET.get('community_name',None)
    com_initial_name=request.GET.get('com_initial_name',None)
    data={
        'exists': Community.objects.filter(name=com_name).exclude(name=com_initial_name).exists()
    }
    return JsonResponse(data)

def validateStudentId(request):
    student_id=request.GET.get('student_id',None)
    student_initial_id=request.GET.get('student_initial_id',None)
    data={
        'exists':Student.objects.filter(student_id_editable=student_id).exclude(student_id_editable=student_initial_id).exists()
    }
    return JsonResponse(data)

#Classes
class CommunitiesView(View):
    def get(self,request):
        qsCommunities=Community.objects.all()
        context={
            'communities': qsCommunities
        }
        return render(request,'Communities.html',context)
    def post(self,request):
        if request.method=='POST':
            if 'btnUpdate' in request.POST:
                idCom=request.POST.get('community_id')
                name=request.POST.get('community_name')
                description=request.POST.get('community_description')
                isOffice=request.POST.get('community_type')=='Office'
                isAdmin=request.POST.get('community_isAdmin') == 'on'
                location=request.POST.get('community_location')
                contactNumbers=request.POST.getlist('community_contact_number')
                changeFlag=request.POST.get('changeFlag')
                image_cover=request.FILES.get('fileInput',None)
                updatedCommunity=Community.objects.filter(user_id=idCom).update(
                    name=name,description=description,isOffice=isOffice,isAdmin=isAdmin,location=location
                )
                if changeFlag=='T':
                    community=Community.objects.get(user_id=idCom)
                    if community.image_cover:
                        community.image_cover.delete()
                    if image_cover is not None and image_cover != '':
                        community.image_cover.save(image_cover.name+idCom, File(image_cover),save=True)
                User_Contact_Number.objects.filter(user=idCom).delete()
                user=User.objects.get(user_id=idCom)
                for i in range(len(contactNumbers)):
                    newNumber=User_Contact_Number(contact_number=contactNumbers[i],user=user)
                    newNumber.save()
            elif 'btnDelete' in request.POST:
                idCom=request.POST.get('community_id')
                community=Community.objects.get(user_id=idCom)
                if community.image_cover:
                    community.image_cover.delete()
                community.delete()
            elif 'btnCreate' in request.POST:
                name=request.POST.get('community_name')
                trimmedname=name.strip()
                idCom=str(trimmedname[:100])+str(random.randint(-100000,100000))
                description=request.POST.get('community_description')
                isOffice=request.POST.get('community_type')=='Office'
                isAdmin=request.POST.get('community_isAdmin') == 'on'
                location=request.POST.get('community_location')
                contactNumbers=request.POST.getlist('community_contact_number')
                changeFlag=request.POST.get('changeFlag')
                image_cover=request.FILES.get('fileInput',None)
                community=Community(user_id=idCom, name=name, description=description,isOffice=isOffice,isAdmin=isAdmin,location=location)
                community.save()
                if image_cover is not None and image_cover != '':
                    community.image_cover.save(image_cover.name+str(community.user_id), File(image_cover),save=True)
                for i in range(len(contactNumbers)):
                    newNumber=User_Contact_Number(contact_number=contactNumbers[i],user=community)
                    newNumber.save()
            return redirect ('Creator:communities_view')

class DeptAndCollegesView(View):
    def get(self,request):
        qsDept=Department.objects.all()
        qsCollege=College.objects.all()
        context={
            'departments':qsDept,
            'colleges':qsCollege
        }
        return render(request,'departments-colleges.html',context)
    def post(self,request):
        if request.method=='POST':
            if 'btnUpdateCollege' in request.POST:
                college_id=request.POST.get('college_id')
                name=request.POST.get('college_name')
                description=request.POST.get('college_description')
                location=request.POST.get('college_location')
                College.objects.filter(id=college_id).update(
                    name=name,description=description,location=location
                )
            elif 'btnCreateCollege' in request.POST:
                name=request.POST.get('college_name')
                description=request.POST.get('college_description')
                location=request.POST.get('college_location')
                college=College(
                    name=name,description=description,location=location
                )
                college.save()
            elif 'btnUpdateDepartment' in request.POST:
                department_id=request.POST.get('department_id')
                name=request.POST.get('department_name')
                college=request.POST.get('college_id')
                description=request.POST.get('department_description')
                col=College.objects.get(id=college)
                Department.objects.filter(id=department_id).update(
                    name=name, description=description, college_id=col
                )
            elif 'btnCreateDepartment' in request.POST:
                name=request.POST.get('department_name')
                description=request.POST.get('department_description')
                college=request.POST.get('college_id')
                col=College.objects.get(id=college)
                dept=Department(
                    name=name, description=description, college_id=col
                )
                dept.save()
        return redirect ('Creator:departments_colleges_view')
        


class SkillAndCategoryView(View):
    def get(self,request):
        qsSkill=Skill.objects.all()
        qsCategory=Skill_Category.objects.all()
        context={
            'skills':qsSkill,
            'categories': qsCategory
        }
        return render(request,'skill-skill_category.html',context)
    def post(self,request):
        if request.method=='POST':
            if 'btnUpdateCategory' in request.POST:
                category_id=request.POST.get('category_id')
                name=request.POST.get('category_name')
                description=request.POST.get('category_description')
                Skill_Category.objects.filter(id=category_id).update(
                    name=name,description=description
                )
            elif 'btnCreateCategory' in request.POST:
                name=request.POST.get('category_name')
                description=request.POST.get('category_description')
                Skill_Category(
                    name=name,description=description
                ).save()
            elif 'btnUpdateSkill' in request.POST:
                skill_id=request.POST.get('skill_id')
                name=request.POST.get('skill_name')
                description=request.POST.get('skill_description')
                category_id=request.POST.get('category_id')
                category=Skill_Category.objects.get(id=category_id)
                Skill.objects.filter(id=skill_id).update(
                    name=name,description=description,category=category
                )
            elif 'btnCreateSkill' in request.POST:
                name=request.POST.get('skill_name')
                description=request.POST.get('skill_description')
                category_id=request.POST.get('category_id')
                category=Skill_Category.objects.get(id=category_id)
                Skill(
                    name=name,description=description,category=category
                ).save()
        return redirect ('Creator:skill_skill_category_view')

class StudentsView(View):
    def get(self, request):
        qsStudent=Student.objects.all()
        qsDept=Department.objects.all()
        qsCollege=College.objects.all()
        context={
            'students':qsStudent,
            'departments':qsDept,
            'colleges':qsCollege
        }
        return render(request,'Students.html',context)
    def post(self,request):
        if request.method=='POST':
            if 'btnDelete' in request.POST:
                idStud=request.POST.get('idStud')
                student=Student.objects.get(user_id=idStud)
                # Student_Community_Subscription.objects.filter(student_id=student).delete()
                # Community_Member.objects.filter(student_id=student).delete()
                # Activity_Student_Participation.objects.filter(student_id=student).delete()
                # studentReviews=Activity_Student_Review.objects.filter(student_id=student)
                # for review in studentReviews:
                #     Review_File.objects.filter(review_id=review).delete()
                # studentReviews.delete()
                # Activity_Student_Target.objects.filter(student_id=student).delete()
                # studentPosts=Student_Post.objects.filter(creator_student_id=student)
                # for post in studentPosts:
                #     Student_Post_File.objects.filter(post_id=post).delete()
                #     Student_Post_Target.objects.filter(post_id=post).delete()
                #     post_reports=Post_Report.objects.filter(post_id=post)
                #     for report in post_reports:
                #         report.deleteFiles()
                #     post_reports.delete()
                # studentPosts.delete()
                # Student_Post_Target.objects.filter(student_id=student).delete()
                # studentReports=Post_Report.objects.filter(reporter_student_id=student)
                # for report in studentReports:
                #     report.deleteFiles()
                # studentReports.delete()
                # Milestone.objects.filter(owner_student_id=student).delete()
                # Student_Aim_Job.objects.filter(student_id=student).delete()
                # Student_Possess_Skill.objects.filter(student_id=student).delete()
                # Student_Watch_Skill.objects.filter(student_id=student).delete()
                # Student_Schedule.objects.filter(student_id=student).delete()
                student.delete()
                return redirect('Creator:students_view')
            elif 'btnViewStudent' in request.POST:
                idStud=request.POST.get('idStud')
                student=Student.objects.get(user_id=idStud)
                qsSkills=Student_Possess_Skill.objects.filter(student_id=student)
                qsMilestones=Milestone.objects.filter(owner_student_id=student)
                qsColleges=College.objects.all()
                qsDepartments=Department.objects.filter(college_id=student.department_id.college_id)
                qsSkillCategory=Skill_Category.objects.all()
                category_id=qsSkillCategory[0].id if qsSkillCategory else 0
                qsDefaultSkillSet=Skill.objects.filter(category_id=category_id)
                qsMilestoneTypes=Milestone_Type.objects.all()
                context={
                    'student':student,
                    'skills':qsSkills,
                    'milestones':qsMilestones,
                    'colleges':qsColleges,
                    'departments':qsDepartments,
                    'skill_categories':qsSkillCategory,
                    'default_skill_set': qsDefaultSkillSet,
                    'milestone_types':qsMilestoneTypes
                }
                return render(request,'viewStudent.html',context)
            elif 'btnUpdateStudent' in request.POST:
                idStud=request.POST.get('student_id')
                idStudOrig=request.POST.get('student_id_orig')
                fName=request.POST.get('first_name')
                mName=request.POST.get('middle_name')
                lName=request.POST.get('last_name')
                streetAd=request.POST.get('street_address')
                brgyAd=request.POST.get('brgy_address')
                cityAd=request.POST.get('city_address')
                provinceAd=request.POST.get('province_address')
                zipAd=request.POST.get('zip_address')
                countryAd=request.POST.get('country_address')
                contactNumbers=request.POST.getlist('contact_number')
                department=Department.objects.get(id=request.POST.get('department_belong'))
                Student.objects.filter(user_id=idStudOrig).update(
                    student_id_editable=idStud, first_name=fName,middle_name=mName,last_name=lName, street_address=streetAd,brgy_address=brgyAd,city_address=cityAd,
                    province_address=provinceAd,zip_address=zipAd,country_address=countryAd,department_id=department
                )
                User_Contact_Number.objects.filter(user=idStudOrig).delete()
                user=User.objects.get(user_id=idStudOrig)
                for i in range(len(contactNumbers)):
                    newNumber=User_Contact_Number(contact_number=contactNumbers[i],user=user)
                    newNumber.save()
                changeFlag=request.POST.get('changeFlag')
                profile_picture=request.FILES.get('fileInput',None)
                if changeFlag=='T':
                    student=Student.objects.get(user_id=idStudOrig)
                    if student.profile_picture:
                        student.profile_picture.delete()
                    if profile_picture is not None and profile_picture != '':
                        student.profile_picture.save(profile_picture.name+idStud, File(profile_picture),save=True)
                return redirect('Creator:students_view')
            elif 'btnUpdateSkill' in request.POST:
                idStud=request.POST.get('student_id')
                idSkill=request.POST.get('skill_id')
                level=request.POST.get('skill_level')
                current_points=request.POST.get('skill_current_points')
                Student_Possess_Skill.objects.filter(student_id=idStud,skill_id=idSkill).update(
                    level=level,points_in_level=current_points
                )
                return redirect('Creator:students_view')
            elif 'btnDeleteSkill' in request.POST:
                idStud=request.POST.get('student_id')
                idSkill=request.POST.get('skill_id')
                Student_Possess_Skill.objects.filter(student_id=idStud,skill_id=idSkill).delete()
                return redirect('Creator:students_view')
            elif 'btnGrantSkill' in request.POST:
                idStud=request.POST.get('student_id')
                idSkill=request.POST.get('skill_id')
                student=Student.objects.get(user_id=idStud)
                skill=Skill.objects.get(id=idSkill)
                level=request.POST.get('skill_level')
                currentPoints=request.POST.get('skill_current_points')
                Student_Possess_Skill(student_id=student,skill_id=skill,level=level,points_in_level=currentPoints,points_to_next_level=level*100).save()
                return redirect('Creator:students_view')
            elif 'btnUpdateMilestone' in request.POST:
                print(request.FILES)
                idMilestone=request.POST.get('milestone_id')
                name=request.POST.get('milestone_name')
                milestone_type=request.POST.get('milestone_type')
                text=request.POST.get('milestone_text')
                link=request.POST.get('milestone_link')
                changeFlag=request.POST.get('changeFlag')
                picture=request.FILES.get('fileInput',None)
                Milestone.objects.filter(id=idMilestone).update(
                    milestone_type_id=milestone_type,text=text,directlink=link,name=name
                )
                print(picture)
                if changeFlag=='T':
                    milestone=Milestone.objects.get(id=idMilestone)
                    if milestone.milestone_photo:
                        milestone.milestone_photo.delete()
                    if picture is not None and picture != '':
                        milestone.milestone_photo.save(picture.name+idMilestone, File(picture),save=True)
                return redirect('Creator:students_view')
            elif 'btnDeleteMilestone' in request.POST:
                idMilestone=request.POST.get('milestone_id')
                Milestone.objects.get(id=idMilestone).delete()
                return redirect('Creator:students_view')
            elif 'btnGrantMilestone' in request.POST:
                name=request.POST.get('milestone_name')
                idStud=request.POST.get('student_id')
                milestone_type=request.POST.get('milestone_type')
                text=request.POST.get('milestone_description')
                link=request.POST.get('milestone_link')
                changeFlag=request.POST.get('changeFlag')
                picture=request.FILES.get('fileInput',None)
                milestoneType=Milestone_Type.objects.get(name=milestone_type)
                student=Student.objects.get(user_id=idStud)
                milestone=Milestone(name=name,milestone_type_id=milestoneType,text=text,directlink=link,owner_student_id=student)
                milestone.save()
                if picture is not None and picture != '':
                    milestone.milestone_photo.save(picture.name+str(milestone.id), File(picture),save=True)
                return redirect('Creator:students_view')
            elif 'btnCreateStudent' in request.POST:
                idStud=request.POST.get('student_id')
                fName=request.POST.get('first_name')
                mName=request.POST.get('middle_name')
                lName=request.POST.get('last_name')
                streetAd=request.POST.get('street_address')
                brgyAd=request.POST.get('brgy_address')
                cityAd=request.POST.get('city_address')
                provinceAd=request.POST.get('province_address')
                zipAd=request.POST.get('zip_address')
                countryAd=request.POST.get('country_address')
                contactNumbers=request.POST.getlist('contact_number')
                department=Department.objects.get(id=request.POST.get('department_belong'))
                user_id=dateformat.format(timezone.now(), 'Y-m-d-H-i-s')
                student=Student(
                    user_id=user_id,student_id_editable=idStud,first_name=fName,middle_name=mName,last_name=lName, street_address=streetAd,brgy_address=brgyAd,city_address=cityAd,
                    province_address=provinceAd,zip_address=zipAd,country_address=countryAd,department_id=department
                )
                student.save()
                for i in range(len(contactNumbers)):
                    newNumber=User_Contact_Number(contact_number=contactNumbers[i],user=student)
                    newNumber.save()
                profile_picture=request.FILES.get('fileInput',None)

                if profile_picture is not None and profile_picture != '':
                    student.profile_picture.save(profile_picture.name+idStud, File(profile_picture),save=True)

                return redirect('Creator:students_view')
class StudentPostView(View):
    def get(self,request):
        qsPostType=Student_Post_Type.objects.all()
        qsPost=Student_Post.objects.all()
        context={
            'post_types':qsPostType,
            'posts':qsPost
        }
        return render(request,'student_posts.html',context)
    def post(self,request):
        if request.method=='POST':
            if 'btnDelete' in request.POST:
                post_id=request.POST.get('post_id')
                Student_Post.objects.get(id=post_id).delete()
        return redirect('Creator:student_posts_view')


            

                
