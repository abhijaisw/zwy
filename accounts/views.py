# from django.views.generic import CreateView, FormView
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model,logout,authenticate,login
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib import messages
# from django.utils.http import is_safe_url
# from django.utils.decorators import method_decorator
# from django.views.generic import DetailView , View, UpdateView
# from django.views.generic.edit import FormMixin
# from django.urls import reverse
# from django.utils.safestring import mark_safe
# from .models import GuestEmail,EmailActivation
# from .forms import Loginform, Registerform, GuestForm, ReactivateEmailForm, UserDetailChangeForm
# from .signals import user_logged_in
# from shopw.mixins import NextUrlMixin,RequestFormAttachMixin



# @login_required
# def account_home_view(request):
#     return render(request, "accounts/home.html" , context)

# # LoginRequiredMixin
# class AccountHomeView(LoginRequiredMixin,DetailView):
#     template_name="accounts/home.html"
#     def get_object(self):
#         return self.request.user
    

# class AccountEmailActivateView(FormMixin, View):
#     success_url = "/login/"
#     form_class = ReactivateEmailForm
#     key = None
#     def get(self, request, key=None,*args, **kwargs):
#         self.key = key
#         if key is not None:
#             qs = EmailActivation.objects.filter(key__iexact=key)
#             confirm_qs = qs.confirmable() 
#             if confirm_qs.count() == 1:
#                 obj = confirm_qs.first()
#                 obj.activate()
#                 messages.success(request, "Your email has been confirmed. please Login.")
#                 return redirect("login")
#             else:
#                 activated_qs = qs.filter(activated=True)
#                 if activated_qs.exists():
#                     reset_link = reverse("password_reset")
#                     msg = """ Your email has already been confirmed
#                     Do you need to <a href="{link}">reset your password</a>?
#                     """.format(link=reset_link)
#                     messages.success(request, mark_safe(msg))
#                     return redirect("login")
#         context = {'form': self.get_form(),'key':key}
#         return render(request, 'registration/activation-error.html', context)
    

#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         msg = """ Activation link sent, Please Check your email."""
#         request = self.request
#         messages.success(request, msg)
#         email = form.cleaned_data.get("email")
#         obj = EmailActivation.objects.email_exists(email).first()
#         user = obj.user
#         new_activation = EmailActivation.objects.create(user=user, email=email)
#         new_activation.send_activation()
#         return super(AccountEmailActivateView, self).form_valid(form)

#     def form_invalid(self, form):
#         context = {'form': form, 'key':self.key}
#         return render(self.request, 'registration/activation-error.html', context)


# def guest_register_view(request):
#     form = GuestForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     next_ =request.GET.get('next')
#     next_post=request.POST.get('next')
#     redirect_path=next_ or next_post or None
#     if form.is_valid():
#         email    = form.cleaned_data.get("email")
#         new_guest_email = GuestEmail.objects.create(email=email)
#         request.session['guest_email_id'] = new_guest_email.id
#         if is_safe_url(redirect_path, request.get_host()):
#             return redirect(redirect_path)
#         else:    
#             return redirect("/register/")    
#     return render(request, '/register/', context)


# class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
#     form_class = Loginform
#     template_name = 'accounts/login.html'
#     success_url = '/'
#     default_next = '/'
    
#     def form_valid(self, form):
#         next_path = self.get_next_url()
#         return redirect(next_path)


# class RegisterView(CreateView):
#     form_class = Registerform
#     template_name  = 'accounts/register.html'
#     success_url ='/login/'


# def log_out(request):
#     logout(request)
#     return redirect("/")

# class UserDetailUpdateView(LoginRequiredMixin, UpdateView):
#     form_class = UserDetailChangeForm
#     template_name = 'accounts/account-update-view.html'
#     success_url = '/account/'

#     def get_object(self):
#         return self.request.user
    
#     def get_context_data(self, *args, **kwargs):
#         context = super(UserDetailUpdateView, self).get_context_data(*args, **kwargs)
#         context['title'] = 'Change Your Account Details'
#         return context

#     def get_success_url(self):
#         return reverse("account:Home")
