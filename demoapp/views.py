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





# @csrf_exempt
# def home(request):
#     num1=0
#     num2=0
#     company = ""
#     job = ""
#
#     if request.method == 'POST':
#         reqs = request.body.decode('utf-8')
#         try:
#             reqs[:5]
#
#             status = reqs.split('\n', 1)[0]
#             print(status)
#             rest = reqs.split('\n', 1)[1]
#
#             username = rest.split('\n', 1)[0]  #######################################
#             print(username)
#             rest2 = rest.split('\n', 1)[1]
#
#             url = rest2.split('\n', 1)[0]  #############################
#             print(url)
#             textNotes = rest2.split('\n', 1)[1]
#
#             notes = textNotes.split('\n', 1)[0]  #############################
#             print(notes)
#             text = textNotes.split('\n', 1)[1]
#
#
#             rawSite = re.search("^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/?\n]+)", url)
#             SiteName = rawSite.group(1)
#
#             # LINKEDIN TAGS
#             linkedin_identifier = "linkedin-logo"
#             link_root_2 = "Jobs based on your Profile"
#             link_root_3 = "Search all Jobs"
#             # HANDSHAKE TAGS
#             handshake_identifier = "handshake-production-cdn"
#             # OTHER TAGS
#             zip_identifier = "www.ziprecruiter.com"
#             indeed_identifier = "indeed_gnav"
#             meta_identifier = "About Meta"
#             amazon_identifier = "Amazon.jobs"
#             ibm_identifier = '"name": "IBM"'
#             tesla_identifier =  "tesla-talent"
#             jpmorganint_identifier = "careers.jpmorgan"
#             arthrex_identifier = 'arthrex'
#             deloitte_identifier = 'deloitte'
#             blackrock_identifier = 'blackrock'
#             accenture_identifier = 'accenture'
#             kpmg_identifier = 'kpmg'
#             citi_identifier = 'citi'
#             morganstanley_identifier = 'Morgan Stanley'
#             bofa_identifier = 'BofA_Careers'
#             tigerjoblink_identifier = "csm.symplicity"
#
#
#             if linkedin_identifier in text:
#                 num1 = text.find('<!----> <span>')
#                 num2 = text.find('<!----> </span>')
#                 if link_root_2 in text:
#                     job = re.search('<div aria-label="(.*)" class="jobs-search', text)
#                     jobtitle = job.group(1)
#                     comp = re.search('<div class="t-14 truncate">\n<span>(.*)</span>', text)
#                     companyname = comp.group(1)
#                 elif link_root_3 in text:
#                     job = re.search('<div aria-label="(.*)" class="jobs-search', text)
#                     jobtitle = job.group(1)
#                     comp = re.search('<div class="t-14 truncate">\n<span>(.*)</span>', text)
#                     companyname = comp.group(1)
#                 else:
#                     jah = re.search('<title>(.*)| LinkedIn</title>', text)
#                     jobjob = jah.group(1)
#                     left = ') '
#                     right = ' |'
#                     jobtitle = jobjob[jobjob.index(left)+len(left):jobjob.index(right)]
#                     comp = re.search('class="ember-view t-black t-normal">\n(.*)\n</a>', text)
#                     companyname = comp.group(1)
#                 print(jobtitle)
#                 print(companyname)
#
#             elif handshake_identifier in text:
#                 peer_exp = '<h2 class="style__heading___3liBJ style__heading___29i1Z style__large___15W-p">Ask a peer about their experience'
#                 if peer_exp in text:
#                     num1 = text.find('<h2 class="style__role-description-title___2aHXu style__heading___29i1Z style__large___15W-p">')
#                     num2 = text.find(peer_exp)
#                 else:
#                     num1 = text.find('<h2 class="style__role-description-title___2aHXu style__heading___29i1Z style__large___15W-p">')
#                     num2 = text.find('class="style__container___L2N8n"><h2 class="style__title___1Smoz style__heading___29i1Z style__large___15W-p">')
#                 result = re.search('<title>(.*)| Handshake</title>', text)
#                 try:
#                     companyJob = result.group(1)
#                     companyJob = companyJob[4:]
#                     companyJob = companyJob[:-20]
#                 except AttributeError:
#                     companyJob = result
#                 job = (companyJob.split('|', 1)[0])[:-1]
#                 company = (companyJob.split('|', 1)[1])[1:]
#                 print(job)
#                 print(company)
#
#             elif zip_identifier in text:
#                 num1 = text.find('<div class="jobDescriptionSection">')
#                 num2 = text.find('<p class="report_job">')
#                 result = re.search('"hiring_company_text t_company_name">(.*) </span>', text)
#                 soup = BeautifulSoup(result.group(1), 'html.parser')
#                 company = (soup.get_text('\n','\n\n')).replace('\n', ' ')
#                 print(company)
#                 dragondese = re.search("name: '(.*)',\nlocation:", text)
#                 job = dragondese.group(1)
#                 print(job)
#
#             elif meta_identifier in text:
#                 num1 = text.find('<div class="_3gel _3gfe _3gef _3gee _8lfv _3-8p _8lfv _3-8p"><div class="_25x1 _25x7 _25xj _1ilv _1iot _38g3 _3geg _38g4 _38g5" style="background-color: ">')
#                 num2 = text.find('<div class="_97fe _1n-z _6hy- _8lfs">Locations')
#                 result = re.search('<meta property="og:title" content="(.*)"><meta property="og:description"', text)
#                 soup = BeautifulSoup(result.group(1), 'html.parser')
#                 job = (soup.get_text('\n','\n\n')).replace('\n', ' ')
#                 print(job)
#                 company = "Meta"
#                 print(company)
#
#             elif amazon_identifier in text:
#                 num1 = text.find('<div class="section"><h2>DESCRIPTION')
#                 num2 = text.find('<div class="sidebar">')
#                 result = re.search('jobTitle: "(.*)",\njobTeam', text)
#                 soup = BeautifulSoup(result.group(1), 'html.parser')
#                 jobtitle = (soup.get_text('\n','\n\n')).replace('\n', ' ')
#                 print(jobtitle)
#                 company = "Amazon"
#                 print(company)
#
#             elif tesla_identifier in text:
#                 num1 = text.find('<div class="style_descriptionItem__JMSKp">')
#                 num2 = text.find('<p>Tesla is an Equal Opportunity / Affirmative Action employer committed to diversity in the workplace. All qualified applicants will receive consideration for employment without regard to race, color, religion, sex, sexual orientation, age, national origin, disability, protected veteran status, gender identity or any other factor protected by applicable federal, state or local laws.</p>')
#                 result = re.search('<h1 class="tds-text--h1-alt">(.*)</h1>', text)
#                 soup = BeautifulSoup(result.group(1), 'html.parser')
#                 jobtitle = (soup.get_text('\n','\n\n')).replace('\n', ' ')
#                 print(jobtitle)
#                 company = "Tesla"
#                 print(company)
#
#             elif jpmorganint_identifier in text:
#                 slay = '<div class="col-12">'
#                 idt = text.count('<div class="col-12">')
#                 print(idt)
#                 i = 0
#                 t = []
#                 occurence = text.find(slay)
#                 print(occurence)
#                 while i < 4:
#                     for idt[i] in text:
#                         num_1 = text.find('<div class="col-12">')
#                         num_2 = text.find('<div class="row jpmc-grid">')
#                         soop = BeautifulSoup(text[num_1:num_2], 'html.parser')
#                         st = (soop.get_text('\n','\n\n')).replace('\n', ' ')
#                     t = t + st
#                     i = i + 1
#                 if i == 4:
#                     num_1 = text.find('<div class="col-12">')
#                     num_2 = text.find('<div class="row jpmc-grid">')
#                     soop = BeautifulSoup(text[num_1:num_2], 'html.parser')
#                     st = (soop.get_text('\n','\n\n')).replace('\n', ' ')
#                 t = t + st
#                 print(t)
#
#             elif arthrex_identifier in text:
#                 num1 = text.find('<td><b>Division:</b></td>')
#                 num2 = text.find('About Arthrex</span></span></b></span></span></span></p>')
#                 result = re.search('<title(.*)</title>', text)
#                 soup = BeautifulSoup(result.group(1), 'html.parser')
#                 jobtitle = (soup.get_text('\n','\n\n')).replace('\n', ' ')
#                 print(jobtitle)
#                 company = "Arthrex"
#                 print(company)
#
#             elif deloitte_identifier in text:
#                 num1 = text.find('<h3 class="article__header__text__title article__header__text__title--3">\nPosition Summary')
#                 num2 = text.find('<h3 class="article__header__text__title article__header__text__title--2">\nRecruiting tips </h3>')
#                 result = re.search('Check out this job at Deloitte, (.*)">', text)
#                 soup = BeautifulSoup(result.group(1), 'html.parser')
#                 jobtitle = (soup.get_text('\n','\n\n')).replace('\n', ' ')
#                 print(jobtitle)
#                 company = "Deloitte"
#                 print(company)
#
#             elif blackrock_identifier in text:
#                 num1 = text.find('<div class="collapse in" id="viewjobdetail" aria-expanded="true">\n<div data-field="responsibilities" class="jd-responsibilities"><strong>Description</strong><p></p>')
#                 num2 = text.find('<p></p>\n<p></p>\n<p><b>About BlackRock</b></p>\n<p></p>')
#                 result = re.search('<title>(.*) | BlackRock</title>', text)
#                 soup = BeautifulSoup(result.group(1), 'html.parser')
#                 jobtitle = (soup.get_text('\n','\n\n')).replace('\n', ' ')
#                 print(jobtitle)
#                 company = "BlackRock"
#                 print(company)
#
#
#             elif accenture_identifier in text:
#                 num1 = text.find('<h2 class="section-title">Job Description</h2>')
#                 num2 = text.find('<div id="job-location" class="col-xs-12 module location">')
#                 result = re.search('"JobPosting","title":"(.*)","jobLocation"', text)
#                 soup = BeautifulSoup(result.group(1), 'html.parser')
#                 jobtitle = (soup.get_text('\n','\n\n')).replace('\n', ' ')
#                 print(jobtitle)
#                 company = "Accenture"
#                 print(company)
#
#
#             elif kpmg_identifier in text:
#                 num1 = text.find('<div class="subDesc"><p>Known for being a great place to work and build a career, KPMG provides audit, tax and advisory services for organizations in today’s most important industries. Our growth is driven by delivering real results for our clients. It’s also enabled by our culture, which encourages individual development, embraces an inclusive environment, rewards innovative excellence and supports our communities. With qualities like those, it’s no wonder we’re consistently ranked among the best companies to work for by Fortune Magazine, Consulting Magazine, Working Mother Magazine, Diversity Inc. and others. If you’re as passionate about your future as we are, join our team.</p></div>')
#                 num2 = text.find('<div class="subDesc"><p>KPMG LLP (the U.S. member firm of KPMG International) offers')
#                 result = re.search('content="https://us-jobs.kpmg.com/portal/27/images/logoKPMG.jpg">\n<title>(.*) - KPMG Careers</title>', text)
#                 soup = BeautifulSoup(result.group(1), 'html.parser')
#                 jobtitle = (soup.get_text('\n','\n\n')).replace('\n', ' ')
#                 print(jobtitle)
#                 company = "KPMG"
#                 print(company)
#
#
#             elif citi_identifier in text:
#                 num1 = text.find('<div class="ats-description" itemprop="description">')
#                 num2 = text.find('<a class="button job-apply bottom" ')
#                 result = re.search('content="Learn more about and apply for the (.*) at Citi here.">', text)
#                 soup = BeautifulSoup(result.group(1), 'html.parser')
#                 jobtitle = (soup.get_text('\n','\n\n')).replace('\n', ' ')
#                 print(jobtitle)
#                 company = "CITI Group"
#                 print(company)
#
#
#             elif morganstanley_identifier in text:
#                 num1 = text.find('<span class="hform_lbl_text">Job description</span>')
#                 num2 = text.find('<span class="hform_lbl_text">Job Level</span>')
#                 result = re.search('<title>(.*) - Morgan Stanley Campus</title>\n<meta http-equiv="Content-Type" content="text/html;charset=utf-8">', text)
#                 soup = BeautifulSoup(result.group(1), 'html.parser')
#                 jobtitle = (soup.get_text('\n','\n\n')).replace('\n', ' ')
#                 print(jobtitle)
#                 company = "Morgan Stanley"
#                 print(company)
#
#
#             elif tigerjoblink_identifier in text:
#                 num1 = text.find('<div class="job_description widget">')
#                 num2 = text.find('<div class="xlate-form-w"></div>')
#                 result = re.search('title="Add (.*) to your favorites" href="', text)
#                 soup = BeautifulSoup(result.group(1), 'html.parser')
#                 jobtitle = (soup.get_text('\n','\n\n')).replace('\n', ' ')
#                 print(jobtitle)
#                 employer = re.search('Employer</td><td>(.*)</td>', text)
#                 soop = BeautifulSoup(employer.group(1), 'html.parser')
#                 company = (soop.get_text('\n','\n\n')).replace('\n', ' ')
#                 print(company)
#
#
#
#             soup = BeautifulSoup(text[num1:num2], 'html.parser')
#             subtext = (soup.get_text('\n','\n\n')).replace('\n', ' ')
#             print(subtext)
#             shortened_subtext = subtext[:200] + "..."
#             print(subtext[:100])
#
#
#             p = data(user=username, Website=SiteName, Notes =notes, Url=url, Company=company, Description=shortened_subtext, Job = job, Applied = status)
#             p.save()
#
#             return JsonResponse(
#                 {
#                 "success":True,
#                 "url": reqs[:5]
#                 }
#             )
#         except KeyError:
#             print("wrong!")
#             #raise JsonInvalidError
#
#     else:
#         datas = data.objects.all()
#
#         # return render(request,'demoapp/htmlcode.html',{'datas':datas})
#         return 0





@csrf_exempt
def home(request):
    num1=0
    num2=0
    company = ""
    job = ""

    if request.method == 'POST':
        reqs = request.body.decode('utf-8')
        try:
            reqs[:5]

            status = reqs.split('\n', 1)[0]
            print(status)
            rest = reqs.split('\n', 1)[1]

            username = rest.split('\n', 1)[0]  #######################################
            print(username)
            rest2 = rest.split('\n', 1)[1]

            url = rest2.split('\n', 1)[0]  #############################
            print(url)
            textNotes = rest2.split('\n', 1)[1]

            notes = textNotes.split('\n', 1)[0]  #############################
            print(notes)
            text = textNotes.split('\n', 1)[1]


            rawSite = re.search("^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/?\n]+)", url)
            SiteName = rawSite.group(1)

            handshake_identifier = "handshake-production-cdn"
            linkedin_identifier = "linkedin-logo"
            zip_identifier = "www.ziprecruiter.com"
            indeed_identifier = "indeed_gnav"
            meta_identifier = "About Meta"

            if linkedin_identifier in text:
                num1 = text.find('<!----> <span>')
                print("num1")
                print(num1)
                num2 = text.find('<!----> </span>', num1)
                print("num2")
                print(num2)
                result = re.search('<title>(.*)| LinkedIn</title>', text)
                try:
                    companyJob = result.group(1)
                    companyJob = companyJob[6:]
                    companyJob = companyJob[:-18]
                except AttributeError:
                    companyJob = result
                job = (companyJob.split('|', 1)[0])[:-1]  ################################
                company = (companyJob.split('|', 1)[1])[1:]
                print(companyJob)

            elif handshake_identifier in text:
                peer_exp = '<h2 class="style__heading___3liBJ style__heading___29i1Z style__large___15W-p">Ask a peer about their experience'
                if peer_exp in text:
                    num1 = text.find('<h2 class="style__role-description-title___2aHXu style__heading___29i1Z style__large___15W-p">')
                    num2 = text.find(peer_exp)
                else:
                    num1 = text.find('<h2 class="style__role-description-title___2aHXu style__heading___29i1Z style__large___15W-p">')
                    num2 = text.find('class="style__container___L2N8n"><h2 class="style__title___1Smoz style__heading___29i1Z style__large___15W-p">')
                result = re.search('<title>(.*)| Handshake</title>', text)
                try:
                    companyJob = result.group(1)
                    companyJob = companyJob[4:]
                    companyJob = companyJob[:-20]
                except AttributeError:
                    companyJob = result
                job = (companyJob.split('|', 1)[0])[:-1]
                company = (companyJob.split('|', 1)[1])[1:]
                print(job)
                print(company)

            elif zip_identifier in text:
                num1 = text.find('<div class="jobDescriptionSection">')
                num2 = text.find('<p class="report_job">')
                result = re.search('"hiring_company_text t_company_name">(.*) </span>', text)
                soup = BeautifulSoup(result.group(1), 'html.parser')
                company = (soup.get_text('\n','\n\n')).replace('\n', ' ')
                print(company)
                dragondese = re.search("name: '(.*)',\nlocation:", text)
                job = dragondese.group(1)
                print(job)

            elif meta_identifier in text:
                num1 = text.find('<div class="_3gel _3gfe _3gef _3gee _8lfv _3-8p _8lfv _3-8p"><div class="_25x1 _25x7 _25xj _1ilv _1iot _38g3 _3geg _38g4 _38g5" style="background-color: ">')
                num2 = text.find('<div class="_97fe _1n-z _6hy- _8lfs">Locations')
                result = re.search('<meta property="og:title" content="(.*)"><meta property="og:description"', text)
                soup = BeautifulSoup(result.group(1), 'html.parser')
                job = (soup.get_text('\n','\n\n')).replace('\n', ' ')
                print(job)
                company = "Meta"
                print(company)



            soup = BeautifulSoup(text[num1:num2], 'html.parser')
            subtext = (soup.get_text('\n','\n\n')).replace('\n', ' ')
            print(subtext)
            shortened_subtext = subtext[:200] + "..."
            print(subtext[:100])


            p = data(user=username, Website=SiteName, Notes =notes, Url=url, Company=company, Description=shortened_subtext, Job = job, Applied = status)
            p.save()

            return JsonResponse(
                {
                "success":True,
                "url": reqs[:5]
                }
            )
        except KeyError:
            print("wrong!")
            #raise JsonInvalidError

    else:
        datas = data.objects.all()

        # return render(request,'demoapp/htmlcode.html',{'datas':datas})
        return 0;






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
