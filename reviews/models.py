from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    level = models.CharField(max_length = 10)
    lecturer_name = models.CharField(max_length = 30)
    course_code = models.CharField(max_length = 10, default='default_value', null=False)
    review_or_complaint = models.TextField(max_length = 500)

    # def __str__(self):
    #     return f'{self.user.username}: {self.message}'

# class User(models.Model):
#     username = models.CharField(max_length = 30)
#     matric_number = models.IntegerField(max_length = 30)
#     email = models.EmailField(max_length = 50)

        