from django import forms

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    username = forms.CharField(
        required=True, 
        label = "",
        widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'id':'id_username',
            'placeholder': "username",
            'label':''}))

    password = forms.CharField(
        label = "",
        widget=forms.PasswordInput(
        attrs={
            'class':'form-control', 
            'id':'id_password',
            'placeholder':'password',
            'label':''}))


    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        user_qs = User.objects.filter(username=username)
        if user_qs.count() == 1:
            user = user_qs.first()
        if not user:
            raise forms.ValidationError("This user does not exist")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password")

        if not user.is_active:
            raise forms.ValidationError("This user is no longer active")

        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):


    username = forms.CharField(
        required=True, 
        label = "",
        widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'id':'id_username',
            'placeholder': "username",
            'label':''}))


    email = forms.EmailField(
        label = "",
        widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'id':'id_email',
            'placeholder': "email",
            'label':''}))

    email2 = forms.EmailField(
        label = "",
        widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'id':'id_confirm_email',
            'placeholder': "confirm email",
            'label':''}))

    first_name = forms.CharField(
        label = "",
        widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'id':'id_first_name',
            'placeholder': "first name",
            'label':''
            }
        ))

    last_name = forms.CharField(
        label = "",
        widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'id':'id_last_name',
            'placeholder': "last name",
            'label':''
            }
        ))

    password = forms.CharField(
        label = "",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control', 
                'id':'id_password',
                'placeholder':'password',
                'label':''}
                ))


    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'email2',
            'password',
            ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:

            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already exists")
        return email