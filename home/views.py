from django.shortcuts import render_to_response
from django.template import RequestContext
from home.homeforms import ContactForm
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect

def index(request):
    return render_to_response("home/index.html", context_instance=RequestContext(request))

def resume(request):
    return render_to_response("home/resume.html", context_instance=RequestContext(request))
    
def SendEmail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print form
        if form.is_valid():
            print request.POST
            message = request.POST.get('Message', '')
            email = request.POST.get('Email', '')
            email_body = " Name: %s \n Message: \n %s " %( email, message )
            email = EmailMessage(
                'contact from %s' % email,
                email_body,
                to=['jladuval@outlook.com'],
                from_email='jladuval@gmail.com',
            )
            email.send(fail_silently=True)
            return HttpResponseRedirect('/')

    return HttpResponseRedirect("/")
