import re
from django.shortcuts import render
from django.contrib import messages

from .models import Complaint

def report(request):
    return render(request,'report.html')

def post(request):
    if request.method=='POST':

        complaint_name= request.POST.get('complaint_name')
        about_complaint=request.POST.get('about_complaint')
        location = request.POST.get('location')
        dateandtime = request.POST.get('dateandtime')
        exact_location = request.POST.get('exact_location')
        action_taken = request.POST.get('action_taken')
        reported_by = request.POST.get('reported_by')

        report = Complaint(
            reported_by=reported_by,
            complaint_name=complaint_name,
            about_complaint = about_complaint,
            location = location,
            dateandtime = dateandtime,
            exact_location = exact_location,
            action_taken = action_taken,
            status = ''
            )

        report.save()

        messages.info(request,'successfully submitted')
    return  render(request,'index.html')


def submitted_complaints(request):
    complaints = Complaint.objects.filter(reported_by = request.user)
    return render(request, 'submitted_complaints.html',{'complaints':complaints})







