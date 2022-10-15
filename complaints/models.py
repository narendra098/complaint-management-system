from django.db import models
from numpy import true_divide

# Create your models here.

class Complaint(models.Model):
    
    reported_by =  models.CharField(max_length=20, default='username')
    complaint_name = models.CharField(max_length=100, null=True)
    about_complaint = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=100, null= True)
    dateandtime = models.DateTimeField(blank=True, default='')
    exact_location = models.TextField(max_length=500, null= True)
    action_taken = models.TextField(max_length=500, null=True)
    status = models.CharField(max_length=100, null= True)

    def __str__(self):
        return self.reported_by