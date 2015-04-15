#encoding=utf-8
from django.shortcuts import render_to_response
from home_page.models import user_items_table
from home_page.models import ssl_table
from home_page.models import ssl_images_table
from home_page.models import ssl_en_table
from home_page.models import ssl_users
from django.http import HttpResponseRedirect
from datetime import datetime
from datetime import time
from django.contrib import auth
from wtforms import Form, BooleanField, TextField, PasswordField, validators

# from django.template import RequestContext
# from django.core.context_processors import csrf

# Create your views here.
def index(request):
    good_booklist = ssl_table.objects.all()
    ssl_en_list = ssl_en_table.objects.all()
    if request.user.is_authenticated():
    	#print 'authenticate'
    	return render_to_response('index.html',{'good_book_list':good_booklist,'ssl_en_list':ssl_en_list,'login_user':request.user.username})
    else:
    	#print 'logout'
    	auth.logout(request)
    	return render_to_response('index.html',{'good_book_list':good_booklist,'ssl_en_list':ssl_en_list})
    # 

def reg_index(request):
	return render_to_response('reg/index.html')

def regAction(request):
	errors=[]
	username = None
	phone = None
	email = None
	password = None
	cpassword = None

	# print request.method
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

		if not request.POST.get('cpassword'):
			errors.append('确认密码输入有误')
		else:
			cpassword = request.POST.get('cpassword')

		if username is not None and (email is not None or phone is not None)and password is not None and len(errors) == 0:
			filterResults = ssl_users.objects.filter(username=username)
			if len(filterResults)>0:
				errors.append('用户名已存在')
				print errors
				return render_to_response('reg/index.html',{'errors':errors})
			
			filterResults = ssl_users.objects.filter(email=email)
			if len(filterResults)>0:
				errors.append('该邮箱已注册')
				print errors
				return render_to_response('reg/index.html',{'errors':errors})

			filterResults = ssl_users.objects.filter(mobilephone=phone)
			if len(filterResults)>0:
				errors.append('该手机号已注册')
				print errors
				return render_to_response('reg/index.html',{'errors':errors})

			# user input verify
			print username
			print phone
			user = ssl_users.objects.create_user(username=username,password=password,email=email,nickname=username)
			if phone is not None:
				user.mobilephone = phone
			user.is_active = True
			user.save()
			request.user = user
			return index(request)

	print errors
	return render_to_response('reg/index.html',{'errors':errors})

def login_index(request):
	return render_to_response('login/index.html')

def loginAction(request):
	errors = []
	user = None
	result = False

	if request.method=='POST':
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		print "login-username:"+username
		user = auth.authenticate(username=username,password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			result = True
		elif user is None:
			filterResults = ssl_users.objects.filter(mobilephone=username)
			if len(filterResults) == 0:
				filterResults = ssl_users.objects.filter(email=username)
			
			if len(filterResults) > 0:	
				user = filterResults[0]	      
			if user is not None and user.check_password(password) and user.is_active:
				print user
				user = auth.authenticate(username=user.username,password=password)
				auth.login(request, user)
				result = True
        if result:
			print 'login success'
			return HttpResponseRedirect("/index.html")
	errors.append('用户名或密码错误')
	return render_to_response('login/index.html',{"errors":errors})

def logoutAction(request):
	auth.logout(request)
	return index(request)

def show_item_detail(request):
	if request.method=='GET':
		itemid = request.GET.get('id','')
		item_data = ssl_table.objects.filter(itemid = itemid)
		item_images = ssl_images_table.objects.filter(itemid = itemid)
		if request.user.is_authenticated():
			user = request.user
		else:
			user = None
		if len(item_data) > 0:
			item_data[0].lookCount=item_data[0].lookCount+1
			item_data[0].save()
			seller = ssl_users.objects.filter(username=item_data[0].username)
			return render_to_response('show_items/item_detail.html',{'item_detail':item_data,'login_user':user,'seller':seller,'mobilephone':int(seller[0].mobilephone)/10000,'item_images':item_images})
	return render_to_response('index.html')

class RegistrationForm(Form):
	username = TextField('username', [validators.Length(min=4, max=20)])
	email = TextField('email', [validators.Length(min=6, max=35),validators.Email("invalid email")])
	password = PasswordField('password', [validators.Required(),validators.EqualTo('confirm', message='Passwords must match')])
	confirm = PasswordField('cpassword')
	phone = TextField('phone', [validators.Length(min=11, max=11)])