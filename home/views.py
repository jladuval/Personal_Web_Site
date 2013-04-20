from django.shortcuts import render_to_response
from django.template import RequestContext
from home.homeforms import ContactForm

def index(request):
    return render_to_response("home/index.html", context_instance=RequestContext(request))
    
def SendEmail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():            
            message = request.POST.get('message', '')
            email = request.POST.get('email', '')
            email_body = " Name: %s \n Message: \n %s " %( email, message )
            email = EmailMessage(
                'contact from %s' % email,
                email_body,
                to=['jladuval@outlook.com'],
                from_email='etpnoreply@gmail.com',
            )
            email.send(fail_silently=True)
            return HttpResponseRedirect('/about/')

    return HttpResponseRedirect("/")
