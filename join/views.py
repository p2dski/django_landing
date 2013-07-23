# Create your views here.
from django.shortcuts import render_to_response, RequestContext
from django.core.mail import send_mail
from .models import Join
from .forms import JoinForm

def home(request):
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        new_join.save()
        send = send_mail('Joined From MVP Landing', 'Person: ' + new_join.full_name + '\n Email: ' + new_join.email + 'n\ Timestamp: ' + new_join.timestamp, str(new_join.email), ['mike@example.com'])
        if send:
            send_mail('Mail_sent', 'MVP WORKS', 'mike@example.com', ['mike2@example.com'])
    return render_to_response('join/home.html', locals(), context_instance=RequestContext(request))

