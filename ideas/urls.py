
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
	path('<int:idea_id>/share', views.share_idea, name='share_idea'),
	path('<int:idea_id>/downvote', views.downvote, name='downvote'),
	path('<int:idea_id>/add_comment', views.add_comment, name='add_comment'),
	path('add_idea/', views.add_idea, name='add_idea'),
	path('add_info/', views.add_info, name='add_info'),
	path('<int:idea_id>/change_idea', views.change_idea, name='change_idea'),
	path('<int:idea_id>/delete_idea', views.delete_idea, name='delete_idea'),
]

