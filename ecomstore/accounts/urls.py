from django.urls import path, re_path
from accounts import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('register/', views.register, name='register'),
    path('my_account/', views.my_account, name='my_account'),
    re_path(r'^order_details/(?P<order_id>[-\w]+)/$',
            views.order_details, name='order_details'),
    path('order_info/', views.order_info,  name='order_info'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logout.html'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password-change-form.html', success_url=reverse_lazy('password-change-done')), name='password-change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password-changed.html'), name='password-change-done'),
]
