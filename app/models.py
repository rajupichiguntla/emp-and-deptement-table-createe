from django.db import models



# Create your models here.
class Dept(models.Model):
    dept_no=models.IntegerField()
    dept_name=models.CharField(max_length=100,primary_key=True)
    location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.dept_name





class Emp(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.CharField(max_length=100)
    dept_name=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.ename