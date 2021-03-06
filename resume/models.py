from django.db        import models
from users.models     import Users


class SavingTypes(models.Model) :
    saving_type = models.CharField(max_length=15)

    class Meta :
        db_table = 'savingtypes'
    
class Resume(models.Model) :
    user         = models.ForeignKey(Users, on_delete=models.CASCADE) 
    saving_type  = models.ForeignKey(SavingTypes, on_delete=models.CASCADE)
    title        = models.CharField(max_length=100) 
    phone        = models.CharField(max_length=15)
    email        = models.CharField(max_length=40)
    blog         = models.URLField(max_length=3000)
    about_me     = models.TextField()	
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'resume'

class Projects(models.Model) : #리스트 요소(한 resume 안에 여러개의 프로 젝트)
    resume        = models.ForeignKey(Resume, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=100)
    github        = models.URLField(max_length=3000)
    description   = models.TextField()
    what_did_i_do = models.TextField()
    tech_stack    = models.TextField()

    class Meta :
        db_table = 'projects'
