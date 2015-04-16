from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ssl_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),  
    url(r'^reg/','home_page.views.reg_index'), 
    url(r'^login/','home_page.views.login_index'),
    url(r'^regAction/','home_page.views.regAction'),
    url(r'^loginAction/','home_page.views.loginAction'),
    url(r'^loginout/','home_page.views.logoutAction'),
    url(r'^check-user','ssl_user.views.checkUser'),
    url(r'^show_item_detail','home_page.views.show_item_detail'),
    url(r'^get-user-for-username','ssl_user.views.getUserByUsername'),
    url(r'$','home_page.views.index'),
)
