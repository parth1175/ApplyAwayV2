from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from demoapp.models import data
from demoapp.forms import UploadBookForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from bs4 import BeautifulSoup
from django.template import loader
from django.urls import reverse
from rest_framework import generics
from .serializers import BookSerializer
from .models import data

class BookList(generics.ListCreateAPIView):
    queryset = data.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = data.objects.all()
    serializer_class = BookSerializer
    

# # Create your views here.

# def update_data(request, data_id):
#     updata = data.objects.get(id=data_id)
#     template = loader.get_template('Update/update.html')
#     context = {
#         'updata': updata,
#     }

#     return HttpResponse(template.render(context, request))

# def updaterecord(request, data_id):
#     url = request.POST['url']
#     company = request.POST['company']
#     job = request.POST['job']
#     description = request.POST['description']
#     notes = request.POST['notes']
#     applied = request.POST['applied']
#     #date = request.POST['date']
#     data1 = data.objects.get(id=data_id)
#     data1.url = url
#     data1.Company = company
#     data1.Job = job
#     data1.Description = description
#     data1.Notes = notes
#     data1.Applied = applied
#     #data1.Date = date
#     data1.save()
#     return redirect('/')
#     #return HttpResponseRedirect(reverse('htmlcode'))

# def delete(request, id):
#   data2 = data.objects.get(id=id)
#   data2.delete()
#   return redirect('/')
#   #return HttpResponseRedirect(reverse('index'))

# def add(request):
#   template = loader.get_template('Add/add.html')
#   return HttpResponse(template.render({}, request))

# def addrecord(request):
#     username = request.user.username
#     url = request.POST['url']
#     website = request.POST['website']
#     company = request.POST['company']
#     job = request.POST['job']
#     description = request.POST['description']
#     notes = request.POST['notes']
#     applied = request.POST['applied']
#     data2 = data(user=username, Url=url, Website=website, Company=company, Job=job, Description=description, Notes=notes, Applied=applied)
#     data2.save()
#     return redirect('/')

# #def resume(request):
# #    template = loader.get_template('Resume/resume.html')
# #    return HttpResponse(template.render({}, request))

# #def BookUploadView(request):
# #    if request.method == 'POST':
# #        form = UploadBookForm(request.POST,request.FILES)
# #        if form.is_valid():
# #            form.save()
# #            return HttpResponse('The file is saved')
# #    else:
# #        form = UploadBookForm()
# #        context = {
# #            'form':form,
# #        }
# #    return render(request, 'Resume/resume.html', context)

# def privacy(request):
#     template = loader.get_template('Privacy/privacy.html')
#     return HttpResponse(template.render({}, request))