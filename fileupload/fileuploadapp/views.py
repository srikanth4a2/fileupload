from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .models import UserSong
from .forms import UserSongForm

def login(request):
    if request.POST:
        #import pdb; pdb.set_trace()
		user = request.POST['user']
		password = request.POST['password']
		user = authenticate(username=user, password=password)
		if user:
			user = authenticate()
		
		#user.save()
    return render_to_response("login.html",context_instance=RequestContext(request))

def signup(request):
	if request.POST:
		username = request.POST['username']
		firstname = request.POST['firstname']
		email = request.POST['email']
		password = request.POST['password']

		user = User.objects.create_user(username, email, password)
		user.save()
	return render_to_response("signup.html",context_instance=RequestContext(request))

def upload_file(request):
    if request.method == 'POST':
        form = UserSongForm(request.POST, request.FILES)
        if form.is_valid():
            # If we are here, the above file validation has completed
            # so we can now write the file to disk
            file_upload = form.save(commit=False)
            file_upload.save()
            return HttpResponse('File uploaded')
    else:
        form = UserSongForm()
    
    return render_to_response('upload.html', {'form': form})