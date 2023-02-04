from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.PositiveIntegerField()
    category = models.CharField(max_length=50)

    class Meta:
        db_table = 'Books'
    
    def __str__(self):
        return str(self.name) + " ["+str(self.isbn)+']'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=50)
    id_no = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    photo = models.ImageField(upload_to='', blank=True)

    class Meta:
        db_table = 'Student'

    def __str__(self):
        return str(self.user) + "["+str(self.college)+']' + "["+str(self.id_no)+']'
    
    def expiry():
        return datetime.today() + timedelta(days=14)
class IssuedBook(models.Model):
    student_id = models.CharField(max_length=10, blank=True)
    book_name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(max_length=50)

    
