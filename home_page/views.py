from django.shortcuts import render_to_response
from home_page.models import user_items_table
from home_page.models import ssl_table
from home_page.models import ssl_en_table
from home_page.models import ssl_users
# from django.template import RequestContext
# from django.core.context_processors import csrf

# Create your views here.
def index(request):
    booklist = ssl_table.objects.all()
    ssl_en_list = ssl_en_table.objects.all()
    return render_to_response('index.html',{'book_list':booklist,'ssl_en_list':ssl_en_list})
    # 

def reg(request):
	return render_to_response('reg/index.html')

def regAction(request):
	errors=[]
	username = None
	phone = None
	email = None
	password = None

	if request.method == 'post':
		if not request.POST.get('username'):
			errors.append('Please enter username')
		else:
			username = request.POST.get('username')
		if not request.POST.get('phone'):
			errors.append('Please enter mobilephone')
		else:
			phone = request.POST.get('phone')
		if not request.POST.get('email'):
			errors.append('Please enter email')
		else:
			email = request.POST.get('email')
		if not request.POST.get('password'):
			errors.append('Please enterpassword')
		else:
			password = request.POST.get('password')

		if username is not None and (email is not None or phone is not None)and password is not None:
			if email is not None:
				user = ssl_users.objects.create_user(email,password,email=email,nickname=username)
			else:
				user = ssl_users.objects.create_user(phone,password,mobilephone=phone,nickname=username)
			user.is_active = True
			user.save
			return HttpResponseRedirect('/login/')

	return render_to_response('index.html',errors)
