#encoding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from home_page.models import ssl_users
#from django.core import serializers
import simplejson

# from django.template import RequestContext
# from django.core.context_processors import csrf

# Create your views here.
def checkUser(request):
	req = simplejson.loads(request.body)
	#print req

	filterResults = []
	if req.has_key('username'):
		username = req['username']
		filterResults = ssl_users.objects.filter(username=username)
	elif req.has_key('phone'):
		phone = req['phone']
		filterResults = ssl_users.objects.filter(mobilephone=phone)
	elif req.has_key('email'):
		email = req['email']
		filterResults = ssl_users.objects.filter(email=email)

	dict1 = {}
	#json_data = serializers.serialize("json", {"code":200,"msg":True})
	if len(filterResults)>0:
		dict1['code']= 200
		dict1['msg'] = False
	else:
		dict1['code']= 200
		dict1['msg'] = True
	json_data = simplejson.dumps(dict1)
	return HttpResponse(json_data,content_type="application/json")

def getUserByUsername(request):
	req = simplejson.loads(request.body)
	filterResults = []
	dict1 = {"phone":""}
	if req.has_key('username'):
		username = req['username']
		filterResults = ssl_users.objects.filter(username=username)
	if len(filterResults) > 0:
		dict1["phone"] = filterResults[0].mobilephone
	json_data = simplejson.dumps(dict1)
	return HttpResponse(json_data,content_type="application/json")

def regUserInfo(request):
	phone = None
	qq = None
	is_student = None
	errors=[]

	if request.method == 'POST':
		phone = request.POST.get('phone')
		qq = request.POST.get('qq')
		is_student = request.POST.get('is-student')
		
		if request.user.is_authenticated():
			print request.user
			request.user.mobilephone = phone
			request.user.qq = qq
			request.user.is_student = is_student
			request.user.save()	
			return render_to_response('reg/index.html',{'is_success':True})

	return render_to_response('reg/index.html')