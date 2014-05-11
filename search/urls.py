from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from django.contrib import admin
admin.autodiscover()

from register import views

urlpatterns = patterns('',
    
    url(r'^_test_admin/', include(admin.site.urls)),

    
    url(r'^register/$',views.SingleRegister,name='single_register'),
    url(r'^thanks/$',views.thanks,name='thanks'),
    url(r'^login/$','django.contrib.auth.views.login',{'template_name':'search_login.html'},name='login'),
    url(r'^edit_profile/$',auth(views.EditProfile.as_view()),name='edit_profile',),
    url(r'^group_register/$',views.GroupRegister,name='group_register'),
    url(r'^(?:home/|)$', views.home,name='home',),
    url(r'^logout',views.user_logout,name='logout'),
    url(r'^help/$',views.help,name='helptext'),
    url(r'^start/$',views.home_start,name='start'),
    url(r'^edit_success/$',views.edit_success,name='edit_success'),
    url('^captcha/',include('captcha.urls')),
    url(r'^sousuodasai/$',views.home,),
)
