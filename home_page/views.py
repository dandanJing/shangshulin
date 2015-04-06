from django.shortcuts import render_to_response
from home_page.models import user_items_table
from home_page.models import ssl_table
from home_page.models import ssl_en_table
# Create your views here.
def index(request):
    booklist = ssl_table.objects.all()
    ssl_en_list = ssl_en_table.objects.all()
    return render_to_response('index.html',{'book_list':booklist,'ssl_en_list':ssl_en_list})
    # 

def reg(request):
	return render_to_response('reg/index.html')