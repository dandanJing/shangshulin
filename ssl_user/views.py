#encoding=utf-8
from django.shortcuts import render_to_response


# from django.template import RequestContext
# from django.core.context_processors import csrf

# Create your views here.
def checkUsername(request):
	print request.method
	return ""