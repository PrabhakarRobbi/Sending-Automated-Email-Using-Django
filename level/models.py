from django.db import models


# course_choice=(
#     ('Python Full Stack','FSD'),
#     ('DEVOPS','DEV'),
# )
class FormData(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    # course=models.CharField(choices=course_choice,max_length=50)

    def __str__(self):
        return self.username
    
# class FormData(models.Model):
#     username=models.CharField(max_length=70)
#     email=models.EmailField(max_length=100)
#     Phone=models.CharField(max_length=20)

#     def __str__(self):
#         return self.username