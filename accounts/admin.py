# from django.contrib import admin
# from .models import GuestEmail, Profile, User, EmailActivation
# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .forms import UserAdminChangeForm,UserAdminCreationForm

# # Register your models here.

# class UserAdmin(BaseUserAdmin):
# 	form = UserAdminChangeForm
# 	add_form = UserAdminCreationForm
	
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
# 	list_display = ['email','first_name','last_name']
# 	fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name','avatar','phone')}),
#         ('Permissions', {'fields': ('is_staff','is_admin','is_active')}),
#     )
# 	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
# 	add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2')}
#         ),
#     )
# 	search_fields = ('email',)
# 	ordering = ('email',)
# 	filter_horizontal = ()

# admin.site.register(User, UserAdmin)


# class ProfileAdmin(admin.ModelAdmin):	
# 	list_display = ['__str__','phone','DOB']

# admin.site.register(Profile,ProfileAdmin)


# class EmailActivationAdmin(admin.ModelAdmin):
#     list_display =['__str__','activated','forced_expired','expires']

# admin.site.register(EmailActivation,EmailActivationAdmin)


# class GuestEmailAdmin(admin.ModelAdmin):
# 	search_fields =['email']
# 	list_display = ['__str__','active']

# admin.site.register(GuestEmail,GuestEmailAdmin)