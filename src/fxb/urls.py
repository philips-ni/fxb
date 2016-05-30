from django.conf.urls import patterns, include, url
from django.contrib import admin
from profiles.views import SignInAndSignUp, LogoutView, AboutView, MyProjectsView


urlpatterns = patterns(
    '',
    url(r'^$', SignInAndSignUp.as_view(template_name='index.html'),
        name='home'),
    #     
    url(r'^about/$', AboutView.as_view(),
        name='about'),
    url(r'^my_projects$', MyProjectsView.as_view(template_name='myprojects.html'),
        name='my_projects'),
    #     url(r'^myfeed/$', MyFeedView.as_view(),
    #         name='myfeed'),
    url(r'^accounts/logout$', LogoutView.as_view(),
                 name='logout'),
    # 
    url(r'^admin/', include(admin.site.urls)),
)
