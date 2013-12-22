# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext 
from django.contrib.auth import logout

def index(request):
    if request.GET.has_key('next'):
        print request.GET['next']
    return render_to_response('login/index.html', {'next':request.GET['next']}, context_instance=RequestContext(request))

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            if request.POST.has_key('next'):
                return redirect(request.POST['next'])
            return render_to_response('login/response.html', {'result':1}, context_instance=RequestContext(request))
        else:
            return render_to_response('login/response.html', {'result':2}, context_instance=RequestContext(request))
    else:
        return render_to_response('login/response.html', {'result':3}, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('/polls')
 
