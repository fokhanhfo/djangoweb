from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('register/',views.register,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('update_item/',views.updateItem,name='update_item'),
    path('search/',views.search,name='search'),
    path('category/<int:Category_id>/',views.category,name='category'),
    path('view/<int:Product_id>/',views.view,name='view'),
]