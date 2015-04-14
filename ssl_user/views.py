#encoding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from home_page.models import ssl_users
#from django.core import serializers
import simplejson

# from django.template import RequestContext
# from django.core.context_processors import csrf

# Create your views here.
def checkUsername(request):
	req = simplejson.loads(request.body)
	username = req['username']
	filterResults = ssl_users.objects.filter(username=username)
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