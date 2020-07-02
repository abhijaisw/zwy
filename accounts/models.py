from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin




class UserProfileManager(BaseUserManager):
	"""Manager of user Profile"""
	use_in_migrations = True
	


	def create_user(self, email, first_name, last_name, password = None, **extra_fields):
		""""Create User Profile"""
		if not email:
			raise ValueError('User must have email address')
		if not first_name:
			raise ValueError('User must have first name')
		if not last_name:
			raise ValueError('User must have last name')
		email = self.normalize_email(email)
		user = self.model(email=email,first_name=first_name, last_name=last_name, **extra_fields)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, first_name, last_name, password, **extra_fields):
		"""Create and save a new super user"""
		user = self.create_user(email,first_name,last_name,password, **extra_fields)
		user.is_superuser = True
		user.is_staff =True
		user.save(using=self._db)

		return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""docstring for UserProfile"""
	email 			= 	models.EmailField(max_length=255, unique=True)
	first_name		=	models.CharField(max_length=255)
	last_name		=	models.CharField(max_length=255)
	is_active		=	models.BooleanField(default=True)
	is_staff		=	models.BooleanField(default=False)


	objects 	=	UserProfileManager()

	USERNAME_FIELD	= 'email'
	REQUIRED_FIELDS = ['first_name','last_name']


	def get_full_name(self):
		"""Retrieve full name of user"""
		return str(self.first_name+self.last_name)

	def short_name(self):
		"""Retrive short name of user"""
		return self.first_name 

	def __str__(self):
		"""Return string represent of  user"""
		return self.email