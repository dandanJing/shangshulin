from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ssl_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),  
    url(r'^reg/','home_page.views.reg'), 
    url(r'^regAction/','home_page.views.regAction'), 
    url(r'$','home_page.views.index'),
)
