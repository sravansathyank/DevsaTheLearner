from django.contrib import admin
from django.urls import path
from Devsa import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('quote/', views.quote, name='quote'),
    path('main/', views.main, name='main'),
    path('it/', views.it_page, name='it_page'),
    path('ele/', views.ele_page, name='ele_page'),
    path('passive/', views.passive_page, name='passive_page'),
    path('', LoginView.as_view(template_name='login.html'), name='home'),
    path('quantum-computing/', views.quantum_computing_page, name='quantum_computing_page'),
     path('block/', views.block_page, name='block_page'),
    path('augmented/', views.augmented_page, name='augmented_page'),
    path('smart_grids/', views.smart_grids_page, name='smart_grids_page'),
    path('robotics/', views.robotics_page, name='robotics_page'),
    path('certificate/', views.certificate_page, name='certificate_page'),
    path('awards/', views.awards_page, name='awards_page'),
    path('owners/',views.owner_page,name='owner_page'),
    path('send-email/', views.send_email, name='send_email'),
]
