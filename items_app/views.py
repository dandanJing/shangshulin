from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from home_page.models import ssl_users
from django.http import HttpResponseRedirect

# Create your views here.
def publish_item(request):
    if request.user.is_authenticated():
        return render_to_response('publish/pub_index.html')
    else:
        return HttpResponseRedirect("/login/")