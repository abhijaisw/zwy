from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views


app_name=''

urlpatterns = [
    # path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html'),),
    path('password/change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), {'post_reset_redirect' : '/accounts/password/change/done/'}, name="password_change"),
    path('password/change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name="password_change_done"),
    path('password/reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_confirm.html'), {'post_reset_redirect' : '/accounts/password/reset/done/'}, name="password_reset"),
    path('password/reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password/reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    
]
