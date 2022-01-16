from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):

	def create_user(self, phone, password=None, **other_fields):
		if not phone:
			raise ValueError("Mobile is required...!")

		user = self.model(phone=phone, **other_fields)
		user.set_password(password) 
		user.save()
		return user

	def create_superuser(self, phone, password=None, **other_fields):
		other_fields.setdefault('is_staff', True)
		other_fields.setdefault('is_superuser', True)
		other_fields.setdefault('is_active', True)

		if other_fields.get('is_staff') is not True:
			raise ValueError('Superuser muse have is_staff=True')
		if other_fields.get('is_superuser') is not True:
			raise ValueError('Superuser muse have is_superuser=True')
		return self.create_user(phone, password, **other_fields)