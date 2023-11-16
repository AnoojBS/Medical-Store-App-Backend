from django.urls import path
from.import views

urlpatterns = [

    path('register1',views.signup,name='register1'),
    path('loginapi1/',views.login,name='loginapi1'),
    path('logoutapi1/',views.logout,name='logoutapi1'),
    path('createapi1/',views.create_medicine,name='createapi1'),
    path('get1/',views.get_all_medicines,name='get1'),
    path('view/<int:pk>/',views.get_single_medicine,name='view'),
    path('updateapi1/<int:pk>/',views.update_medicine,name='updateapi1'),
    path('deleteapi1/<int:pk>/',views.delete_medicine,name='deleteapi1'),
    path('search1/medicine1/<str:name>/', views.search_medicine_by_name, name='search_medicine_by_name'),

 ]