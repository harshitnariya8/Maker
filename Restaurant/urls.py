
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup', views.signup, name='signup'),
    path('signin',views.signin,name='signin'),
    path('<int:id>/createtable', views.createtable, name='createtable'),
    path('<int:id>',views.Menu,name='Menu'),
    path('<int:id>/createcategory', views.createcategory, name='createcategory'),
    path('<int:id>/createproduct', views.createproduct, name='createproduct'),
    path('restaurant_registration',views.restaurant_registration,name='restaurant_registration'),
    path('<int:id>/alltable',views.alltable,name='alltable'),
    path('<int:id>/allcategories',views.allcategories,name='allcategories'),
    path('<int:id>/allproduct',views.allproduct,name='allproduct'),

]
