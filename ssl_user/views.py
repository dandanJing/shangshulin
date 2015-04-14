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
	print req

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