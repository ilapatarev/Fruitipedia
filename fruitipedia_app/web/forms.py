from django import forms

from fruitipedia_app.web.models import Profile, Fruit


class ProfileCreateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields='first_name', 'last_name', 'email', 'password'

		widgets={
			'first_name': forms.TextInput(
				attrs={
					'placeholder': 'First Name',


				}),

			'last_name': forms.TextInput(
				attrs={
					'placeholder': 'Last Name',


				}
			),
			'email': forms.TextInput(
				attrs={
					'placeholder': 'Email',


				}
			),
			'password': forms.TextInput(
				attrs={
					'placeholder': 'Password',


				}
			),

		}
		labels = {
			'first_name': '',
			'last_name': '',
			'email': '',
			'password': '',
		}

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields='first_name', 'last_name', 'image_url', 'age'

class BaseFruitForm(forms.ModelForm):
	class Meta:
		model=Fruit
		fields='__all__'

class EditFruitForm(BaseFruitForm):
	pass

class CreateFruitForm(forms.ModelForm):
	class Meta:
		model =Fruit
		fields='__all__'
		widgets={
			'name': forms.TextInput(

				attrs={
					'placeholder': 'Fruit Name',


				}),
			'image_url': forms.TextInput(
				attrs={
					'placeholder': 'Fruit Image URL',

				}),
			'description': forms.Textarea(
				attrs={
					'placeholder': 'Fruit Description',

				}),
			'nutrition': forms.Textarea(
				attrs={
					'placeholder': 'Nutrition Info',

				}),
		}
		labels = {
			'name': '',
			'image_url': '',
			'description': '',
			'nutrition': '',
		}


class DeleteFruitForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__set_disabled_fields()

	def save(self, commit=True):
		if commit:
			self.instance.delete()
		return self.instance

	def __set_disabled_fields(self):
		for _, field in self.fields.items():
			field.widget.attrs['readonly'] = ['readonly']
	class Meta:
		model=Fruit
		fields='name', 'image_url', 'description'




