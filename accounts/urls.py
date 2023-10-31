from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginuser), 
    path('', views.startScreen,name="startscreen"), 
    path('tender', views.placetender,name="tender"), 
    path('map', views.AddressView.as_view(), name='mapMain'),
    path('getMe',views.grtCord , name='getMe'),
    path('onBoarding',views.vendorOnboarding,name='onBoarding'),
    path('vendorshop',views.vendorshop,name='vendorshop',), 
    path("reg",views.afterLogin,name="afterLogin"),
    path("quotation",views.getTender,name="getTender"),
    path('customerPage',views.customerPage,name="customerPage"),
    path('viewTenders',views.viewTenders,name="viewTenders"),
    path('giveQuat/<str:id>',views.giveQuat,name="giveQuat"),
    path('pendingQuat',views.pendingQuat,name="pendingQuat"),
    path('logoutUser',views.logoutUser,name="logoutUser"),
    path('loadLocation',views.loadLocation,name="loadLocation")

    
]
