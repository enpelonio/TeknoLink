from django.db import models
from django.utils.timezone import now as date_now

class User(models.Model):
    user_id=models.CharField(max_length=50,primary_key=True,default=date_now)
    password=models.CharField(max_length=25)
    user_type=models.CharField(max_length=25,default='Student')
    class Meta:
        db_table='User'

class Community(User):
    date_created=models.DateField(default=date_now)
    name=models.CharField(max_length=50,primary_key=True)
    create_admin_id=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name='create_admin_id_set')
    isAdmin=models.BooleanField()
    isOffice=models.BooleanField()
    description=models.TextField(null=True,blank=True)
    location=models.CharField(max_length=200,null=True,blank=True)
    video_cover=models.FileField(null=True,blank=True)
    image_cover=models.ImageField(null=True,blank=True)
    isDeleted=models.BooleanField(default=False)
    delete_admin_id=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name='delete_admin_id_set')
    class Meta:
        db_table='Community'

class College(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)

    class Meta:
        db_table='College'

class Department(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    college_id=models.ForeignKey(College,null=False,blank=False,on_delete=models.CASCADE)

    class Meta:
        db_table='Department'

class Student(User):
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    street_address=models.CharField(max_length=100, null=True, blank=True)
    brgy_address=models.CharField(max_length=100, null=True,blank=True)
    city_address=models.CharField(max_length=100,null=True,blank=True)
    province_address=models.CharField(max_length=100,null=True,blank=True)
    zip_address=models.CharField(max_length=20)
    country_address=models.CharField(max_length=100,null=True,blank=True)
    department_id=models.ForeignKey(Department,null=False,blank=False,on_delete=models.CASCADE)
    class Meta:
        db_table='Student'

class User_Contact_Number(models.Model):
    user_id=models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE,to_field='user_id')
    contact_number=models.CharField(max_length=11)

    class Meta:
        db_table='User_Contact_Number'

class Chat_Room(models.Model):
    room_id=models.AutoField(primary_key=True)

    class Meta:
        db_table='Chat_Room'

class Chat_Room_Participants(models.Model):
    user_id=models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE,to_field='user_id')
    room_id=models.ForeignKey(Chat_Room,null=False,blank=False,on_delete=models.CASCADE)

    class Meta:
        db_table='Chat_Room_Participants'

class Message(models.Model):
    room_owner_id=models.ForeignKey(Chat_Room,null=False,blank=False,on_delete=models.CASCADE)
    sender_user_id=models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE)
    content=models.TextField(null=False,blank=False)
    send_datetime=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Message'

class Message_File(models.Model):
    message_id=models.ForeignKey(Message,null=False,blank=False,on_delete=models.CASCADE)
    message_file=models.FileField(null=False,blank=False)

    class Meta:
        db_table='Message_File'

class Notification_Type(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    description=models.TextField(null=True,blank=True)
    
    class Meta:
        db_table='Notification_Type'

class Notification(models.Model):
    sender_user_id=models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE,related_name='sender_user_id')
    receiver_user_id=models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE,related_name='receiver_user_id')
    type_id=models.ForeignKey(Notification_Type,null=False,blank=False,on_delete=models.CASCADE)
    send_datetime=models.DateTimeField(auto_now_add=True)
    isRead=models.BooleanField(default=False)
    text=models.CharField(max_length=50)
    direct_link=models.TextField(null=True,blank=True)

    class Meta:
        db_table='Notification'

class Student_Community_Subscription(models.Model):
    community_id=models.ForeignKey(Community,null=False,blank=False,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE)
    subscribe_datetime=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Student_Community_Subscription'

class Community_Member(models.Model):
    community_id=models.ForeignKey(Community,null=False,blank=False,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE)
    join_datetime=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Community_Member'

class Activity_Status(models.Model):
    name=models.CharField(max_length=20,primary_key=True)

    class Meta:
        db_table="Activity_Status"

class Activity(models.Model):
    title=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField(null=True,blank=True)
    status_id=models.ForeignKey(Activity_Status,null=False,blank=False,on_delete=models.CASCADE)
    valid_until_date=models.DateField(null=True)
    parent_activity_id=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
    status_admin_id=models.ForeignKey(Community,null=True,blank=True,on_delete=models.CASCADE,related_name='activity_status_admin')
    creator_community_id=models.ForeignKey(Community,null=False,blank=False,on_delete=models.CASCADE,related_name='activity_creator_id')
    chat_room_id=models.ForeignKey(Chat_Room,null=False,blank=False,on_delete=models.CASCADE)
    activity_type=models.CharField(default='Announcement', max_length=50)

    class Meta:
        db_table='Activity'

class Schedule_Type(models.Model):
    schedule_type=models.CharField(max_length=50,primary_key=True)

    class Meta:
        db_table='Schedule_Type'

class Event(Activity):
    start_date=models.DateField(default=date_now)
    end_date=models.DateField(null=True,blank=True)
    start_time=models.TimeField()
    end_time=models.TimeField(null=True,blank=True)
    is_recurring=models.BooleanField(default=False)

    class Meta:
        db_table='Event'

class Event_Schedule_Pattern(models.Model):
    event_id=models.ForeignKey(Event, on_delete=models.CASCADE)
    schedule_type_id=models.ForeignKey(Schedule_Type, on_delete=models.CASCADE)
    onMonday=models.BooleanField()
    onTuesday=models.BooleanField()
    onWednesDay=models.BooleanField()
    onThursday=models.BooleanField()
    onFriday=models.BooleanField()
    onSaturday=models.BooleanField()
    onSunday=models.BooleanField()

    class Meta:
       db_table='Event_Schedule_Pattern'


class Activity_Student_Participation(models.Model):
    activity_id=models.ForeignKey(Activity,null=False,blank=False,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE)
    participate_datetime=models.DateTimeField(auto_now_add=True)
    isConfirmed=models.BooleanField(default=False)
    confirm_datetime=models.DateTimeField(null=True)

    class Meta:
        db_table="Activity_Student_Participation"

class Activity_Student_Review(models.Model):
    activity_id=models.ForeignKey(Activity,null=False,blank=False,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE)
    rate=models.IntegerField()
    content=models.TextField(null=True,blank=True)
    review_datetime=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="Activity_Student_Review"

class Review_File(models.Model):
    review_id=models.ForeignKey(Activity_Student_Review,null=False,blank=False,on_delete=models.CASCADE)
    review_file=models.FileField(null=False)

    class Meta:
        db_table="Review_File"

class Activity_Student_Target(models.Model):
    activity_id=models.ForeignKey(Activity,null=False,blank=False,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE)
    priority=models.IntegerField()

    class Meta:
        db_table="Activity_Student_Target"

class Student_Post(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    creator_student_id=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE)
    room_id=models.ForeignKey(Chat_Room,null=False,blank=False,on_delete=models.CASCADE)
    
    class Meta:
        db_table='Student_Post'

class Student_Post_File(models.Model):
    post_id=models.ForeignKey(Student_Post,null=False,blank=False,on_delete=models.CASCADE)
    post_file=models.FileField(null=False,blank=False)

    class Meta:
        db_table='Student_Post_File'

class Student_Post_Target(models.Model):
    post_id=models.ForeignKey(Student_Post,null=False,blank=False,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE)
    priority=models.IntegerField()

    class Meta:
         db_table='Student_Post_Target'

class Report_Type(models.Model):
    name=models.CharField(max_length=50,primary_key=True)

    class Meta:
        db_table='Report_Type'

class Post_Report(models.Model):
    post_id=models.ForeignKey(Student_Post,null=False,blank=False,on_delete=models.CASCADE,related_name='post_id')
    reporter_student_id=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE, related_name='reporter_student_id')
    report_type_id=models.ForeignKey(Report_Type,null=False,blank=False,on_delete=models.CASCADE)
    description=models.TextField(null=True,blank=True)

    class Meta:
        db_table='Post_Report'

class Report_File(models.Model):
    report_id=models.ForeignKey(Post_Report,null=False,blank=False,on_delete=models.CASCADE)
    report_file=models.FileField(null=False,blank=False)

    class Meta:
        db_table='Report_File'

class Milestone_Type(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    description=models.TextField(null=True,blank=True)

    class Meta:
        db_table='Miletone_Type'

class Milestone(models.Model):
    owner_student_id=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE)
    milestone_type_id=models.ForeignKey(Milestone_Type,null=False,blank=False,on_delete=models.CASCADE)
    text=models.TextField()
    milestone_datetime=models.DateField(auto_now_add=True)
    directlink=models.TextField()
    milestone_photo=models.ImageField(null=True, blank=True)

    class Meta:
        db_table='Milestone'

class Job(models.Model):
    name=models.CharField(max_length=50,blank=True,default='')
    description=models.TextField()

    class Meta:
        db_table='Job'

class Job_File(models.Model):
    job_id=models.ForeignKey(Job,null=False,blank=False,on_delete=models.CASCADE)
    job_file=models.FileField()

    class Meta:
        db_table='Job_File'

class Job_Person(models.Model):
    name=models.CharField(max_length=100,default='',blank=True)
    description=models.TextField()
    picture=models.ImageField()
    job_id=models.ForeignKey(Job,null=False,blank=False,on_delete=models.CASCADE)

    class Meta:
        db_table='Job_Person'

class Company(models.Model):
    name=models.CharField(max_length=100,default='',blank=True)
    description=models.TextField()

    class Meta:
        db_table='Company'

class Company_File(models.Model):
    company_id=models.ForeignKey(Company,null=False,blank=False,on_delete=models.CASCADE)
    company_file=models.FileField()

    class Meta:
        db_table='Company_File'

class Company_Demand_Job(models.Model):
    company_id=models.ForeignKey(Company,null=False,blank=False,on_delete=models.CASCADE)
    job_id=models.ForeignKey(Job,null=False,blank=False,on_delete=models.CASCADE)
    demand_level=models.CharField(max_length=20)

    class Meta:
        db_table='Company_Demand_Job'

class Student_Aim_Job(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    job_id=models.ForeignKey(Job,on_delete=models.CASCADE)

    class Meta:
        db_table='Student_Aim_Job'

class Skill_Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()

    class Meta:
        db_table='Skill_Category'

class Skill(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    category=models.ForeignKey(Skill_Category, on_delete=models.CASCADE)

    class Meta:
        db_table='Skill'

class Job_Require_Skill(models.Model):
    job_id=models.ForeignKey(Job,on_delete=models.CASCADE)
    skill_id=models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        db_table='Job_require_Skill'

class Student_Possess_Skill(models.Model):
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    skill_id=models.ForeignKey(Skill, on_delete=models.CASCADE)
    level=models.IntegerField()
    points_in_level=models.IntegerField()
    points_to_next_level=models.IntegerField()

    class Meta:
        db_table='Student_Possess_Skill'

class Company_Want_Skill(models.Model):
    company_id=models.ForeignKey(Company, on_delete=models.CASCADE)
    skill_id=models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        db_table='Company_Want_Skill'

class Student_Watch_Skill(models.Model):
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    skill_id=models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        db_table='Student_Watch_Skill'

class Community_Improve_Skill(models.Model):
    community_id=models.ForeignKey(Community, on_delete=models.CASCADE)
    skill_id=models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_percentage_boost=models.DecimalField(max_digits=5, decimal_places=2,default=.05)

    class Meta:
        db_table='Community_Improve_Skill'

class Skill_Training_Intensity(models.Model):
    intensity=models.CharField(max_length=50,primary_key=True)

    class Meta:
        db_table='Skill_Training_Intensity'

class Event_Train_Skill(models.Model):
   event_id=models.ForeignKey(Event, on_delete=models.CASCADE)
   skill_id=models.ForeignKey(Skill, on_delete=models.CASCADE)
   training_intensity=models.ForeignKey(Skill_Training_Intensity, on_delete=models.CASCADE)
   skill_points=models.IntegerField()

   class Meta:
       db_table='Event_Train_Skill'

class Student_Schedule(models.Model):
   event_schedule_id=models.ForeignKey(Event, on_delete=models.CASCADE)
   student_id=models.ForeignKey(Student, on_delete=models.CASCADE)

   class Meta:
       db_table='Student_Schedule'


