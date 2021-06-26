from django.urls import path


from testApp import views

urlpatterns = [
    path('', views.retrieve_view,name='retrive_view'),
    path('create/', views.create_view,name='create'),
    path('delete/<int:id>/', views.delete_view,name='delete'),
    path('update/<int:id>/', views.update_view,name='update'),
    path('logout/', views.logoutview,name='logoutview'),
    path('signup/', views.signup,name='sign_up'),
    ]
