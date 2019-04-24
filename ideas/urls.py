"""
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    #url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    #url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    #url(r'^signup/$', views.signup, name='signup'),
]
"""


from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'ideas'
urlpatterns = [
	path('', views.ideas_view, name='ideas_home'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/signup', views.signup, name='signup'),
	path('<int:idea_id>/', views.detail, name='detail'),
	path('<int:idea_id>/upvote', views.upvote, name='upvote'),
	path('<int:idea_id>/downvote', views.downvote, name='downvote'),
	path('add_idea/', views.add_idea, name='add_idea'),
	path('add_info/', views.email_reqd, name='add_info'),
	path('<int:idea_id>/change_idea', views.change_idea, name='change_idea'),
	path('<int:idea_id>/delete_idea', views.delete_idea, name='delete_idea'),
]

