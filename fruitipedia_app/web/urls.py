from django.urls import path
from fruitipedia_app.web import views


urlpatterns=[
	path('', views.index, name='index'),
	path('dashboard/', views.dashboard, name='dasboard'),
	path('create/', views.create_fruit, name='create-fruit'),
	path('fruit/details/<int:pk>', views.fruit_details, name='fruit-details'),
	path('fruit/edit/<int:pk>', views.edit_fruit, name='edit-fruit'),
	path('fruit/delete/<int:pk>', views.delete_fruit, name='delete-fruit'),
	path('profile/create/', views.create_profile, name='create-profile'),
	path('profile/details/', views.profile_details, name='profile-details'),
	path('profile/edit', views.edit_profile, name='edit-profile'),
	path('profile/delete', views.delete_profile, name='profile-delete'),
]