# from django import forms
# from django.contrib.auth import authenticate,login,get_user_model 
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from .models import User,EmailActivation 
# from django.db.models.signals import pre_save, post_save
# from django.utils.safestring import mark_safe
# from django.urls import reverse
# from .signals import user_logged_in
# from .models import User, Profile


# class ReactivateEmailForm(forms.Form):
#     email = forms.EmailField()

#     def clean_email(self):
#         email = self.cleaned_data["email"]
#         qs = EmailActivation.objects.email_exists(email)
#         if not qs.exists():
#             register_link = reverse("register")
#             msg = """ This Email Doesn't Exists.! Would you like to <a href="{link}">register</a>?
#             """.format(link=register_link)
#             raise forms.ValidationError(mark_safe(msg))
#         return email
    
    


# class UserAdminCreationForm(forms.ModelForm):
#     """
#     A form for creating new users. Includes all the required
#     fields, plus a repeated password.
#     """
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('email','first_name','last_name',)

#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2


#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserAdminCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class UserDetailChangeForm(forms.ModelForm):
#     first_name  = forms.CharField(label='First Name', required=False)
#     last_name   = forms.CharField(label='Last Name', required=False)
#     phone       = forms.CharField(label='Mobile Number', required=False)
#     # DOB         = forms.DateField(label='Date Of Birth', required=False)
#     # avatar      = forms.ImageField(label='Profile pic', required= False)
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','phone']


# class UserAdminChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = User
#         fields = ('email', 'password','first_name','last_name')

#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]


# class GuestForm(forms.Form):
#     email =forms.EmailField()


# class Loginform(forms.Form):
#     email = forms.EmailField(label='Email')
#     password =forms.CharField(widget=forms.PasswordInput) 

#     def __init__(self, request,*args, **kwargs):
#         self.request = request
#         super(Loginform, self).__init__(*args, **kwargs)
    
#     def clean(self):
#         request =self.request
#         data = self.cleaned_data
#         email = data.get("email")
#         password = data.get("password")
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             not_active = qs.filter(is_active=False)
#             if not_active.exists():
#                 link = reverse("account:resend-activation")
#                 reconfirm_msg = """Go to <a href='{resend_link}'>
#                 Resend Confirmation Email</a>.
#                 """.format(resend_link=link)
#                 confirm_email = EmailActivation.objects.filter(email=email)
#                 is_confirmable = confirm_email.confirmable().exists()
#                 if is_confirmable:
#                     msg1= "Please Check Your Email to Confirm Your Account." + reconfirm_msg
#                     raise forms.ValidationError(mark_safe(msg1))
#                 email_confirm_qs = EmailActivation.objects.email_exists(email).exists()
#                 if email_confirm_qs:
#                     msg2 ="Email Not Confirm. " + reconfirm_msg
#                     raise forms.ValidationError(mark_safe(msg2))
#                 if not is_confirmable and not email_confirm_qs.exists():
#                     raise forms.ValidationError("This User is inactive.")

                    


#         user = authenticate(request, username=email, password=password)
#         if user is None:
#             raise forms.ValidationError("Invalid Credentials")
#         login(request, user)
#         self.user = user
#         user_logged_in.send(user.__class__, instance=user, request=request)
#         try:
#             del request.session['guest_email_id']
#         except:
#             pass
#         return data
    
#     # def form_valid(self, form):
#     #     request = self.request
#     #     next_ =request.GET.get('next')
#     #     next_post=request.POST.get('next')
#     #     redirect_path=next_ or next_post or None

#     #     email = form.cleaned_data.get("email")
#     #     password = form.cleaned_data.get("password")
#     #     if user is not None:
#     #         if not user.is_active:
#     #             messages.error(request, "This user is InActive")
#     #             return super(Loginform, self).form_invalid(form)
#     #         login(request, user)
#     #         user_logged_in.send(user.__class__, instance=user, request=request)
#     #         try:
#     #             del request.session['guest_email_id']
#     #         except:
#     #             pass

#     #         if is_safe_url(redirect_path, request.get_host()):
#     #             return redirect(redirect_path)
#     #         else:
#     #             return redirect("/")
#     #     return super(Loginform, self).form_invalid(form)


# class Registerform(forms.ModelForm):
#     """
#     A form for creating new users. Includes all the required
#     fields, plus a repeated password.
#     """
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('first_name','last_name','email')

#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2


#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(Registerform, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         user.is_active = False
#         user.is_admin = False
#         user.is_staff = False
#         # obj = EmailActivation.objects.create(user=user)
#         # obj.send_activation()
#         if commit:
#             user.save()
#         return user