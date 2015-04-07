#encoding=utf-8
from django.shortcuts import render_to_response
from home_page.models import user_items_table
from home_page.models import ssl_table
from home_page.models import ssl_en_table
from home_page.models import ssl_users
from django.http import HttpResponseRedirect

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

def login(request):
	return render_to_response('login/index.html')

def regAction(request):
	errors=[]
	username = None
	phone = None
	email = None
	password = None

	if request.method == 'POST':
		if not request.POST.get('username'):
			errors.append('用户名无效')
		else:
			username = request.POST.get('username')

		if not request.POST.get('phone') and not request.POST.get('email'):
			errors.append('手机号码或邮箱有误')
		elif request.POST.get('phone'):
			phone = request.POST.get('phone')
		else:
			email = request.POST.get('email')


		if not request.POST.get('password'):
			errors.append('密码有误')
		else:
			password = request.POST.get('password')

		if username is not None and (email is not None or phone is not None)and password is not None:
			nametext = None
			if email is not None:
				nametext = email	
			else:
				nametext = phone
			filterResults = ssl_users.objects.filter(username=nametext)
			if len(filterResults)>0:
				errors.append('用户已存在')
				print errors
				return render_to_response('reg/index.html',{'errors':errors})
			user = ssl_users.objects.create_user(nametext,password,email=email,mobilephone=phone,nickname=username)
			user.is_active = True
			user.save
			return HttpResponseRedirect('/login/')

	print errors
	return render_to_response('reg/index.html',{'errors':errors})
