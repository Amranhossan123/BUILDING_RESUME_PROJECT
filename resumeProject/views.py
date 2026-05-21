from django.shortcuts import render,redirect
from resumeApp.models import *

def resume(request):
    resumeData=resumeModel.objects.all()

    resumeDic={
        'data':resumeData
    }

    return render(request,'resume.html',resumeDic)

def addresume(request):
    if request.method=='POST':
        profilepicture=request.FILES.get('profilepicture')
        fullname=request.POST.get('fullname')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        careeerobjective=request.POST.get('careerobjective')
        skills=request.POST.get('skills')
        certification=request.POST.get('certification')
        projects=request.POST.get('projects')
        references=request.POST.get('references')

        degree=request.POST.get('degree')
        institution=request.POST.get('institution')
        graduationyear=request.POST.get('graduationyear')

        company=request.POST.get('company')
        position=request.POST.get('position')
        startdate=request.POST.get('startdate')
        enddate=request.POST.get('enddate')

        resumeData=resumeModel(
            ProfilePicture=profilepicture,
            FullName=fullname,
            Address=address,
            Phone=phone,
            Email=email,
            CareerObjective=careeerobjective,
            Skills=skills,
            Certification=certification,
            Projects=projects,
            References=references
        )

        educationData=educationModel(
            Degree=degree,
            Institution=institution,
            GraduationYear=graduationyear
        )

        workData=workModel(
            Company=company,
            Position=position,
            StartDate=startdate,
            EndDate=enddate
        )

        resumeData.save()
        educationData.save()
        workData.save()
        return redirect('resume')
    return render(request,'addResume.html')


def editresume(request,myid):
    resumeData=resumeModel.objects.get(id=myid)
    educationData=educationModel.objects.get(id=myid)
    workData=workModel.objects.get(id=myid)

    allDic={
        'resumedata':resumeData,
        'educationdata':educationData,
        'workdata':workData

    }

    return render(request,'editResume.html',allDic)


def updateresume(request):
    if request.method=='POST':
        resumeID=request.POST.get('resumeID')


        resumeData=resumeModel.objects.get(id=resumeID)
        educationData=educationModel.objects.get(id=resumeID)
        workData=workModel.objects.get(id=resumeID)

        resumeData.FullName=request.POST.get('fullname')
        resumeData.Address=request.POST.get('address')
        resumeData.Phone=request.POST.get('phone')
        resumeData.Email=request.POST.get('email')
        resumeData.CareerObjective=request.POST.get('careerobjective')
        resumeData.Skills=request.POST.get('skills')
        resumeData.Certification=request.POST.get('certification')
        resumeData.Projects=request.POST.get('projects')
        resumeData.References=request.POST.get('references')

        if request.FILES.get('profilepicture'):
            resumeData.ProfilePicture=request.FILES.get('profilepicture')


        educationData.Degree=request.POST.get('degree')
        educationData.Institution=request.POST.get('institution')
        educationData.GraduationYear=request.POST.get('graduationyear')

        workData.Company=request.POST.get('company')
        workData.Position=request.POST.get('position')
        workData.StartDate=request.POST.get('startdate')
        workData.EndDate=request.POST.get('enddate')

        resumeData.save()
        educationData.save()
        workData.save()
        return redirect('resume')

    return redirect('resume')

def deleteresume(request,myid):
    resumeData=resumeModel.objects.get(id=myid)
    educationdata=educationModel.objects.get(id=myid)
    workdata=workModel.objects.get(id=myid)

    resumeData.delete()
    educationdata.delete()
    workdata.delete()

    return redirect('resume')

def viewresume(request,myid):
    resumeData=resumeModel.objects.get(id=myid)
    educationData=educationModel.objects.get(id=myid)
    workData=workModel.objects.get(id=myid)
    context={
        'resumeData':resumeData,
        'educationData':educationData,
        'workData':workData
    }
    return render(request,'viewResume.html',context)
