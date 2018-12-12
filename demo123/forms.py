from django import forms

class ContactFrom(forms.Form):
    fname=forms.CharField(label='Firstname',widget=forms.TextInput(
                          attrs={'class':'form-control',
                                  'placeholder':'Enter your first name'}))

    lname=forms.CharField(label='LastName',widget=forms.TextInput(
                          attrs={'class':'form-control',
                                  'placeholder':'Enter your last name'}))

    username=forms.CharField(label='UserName',widget=forms.TextInput(
                          attrs={'class':'form-control',
                                  'placeholder':'Enter your user name'}))

    password=forms.CharField(label='Password',widget=forms.PasswordInput(
                             attrs={'class':'form-control',
                                    'placeholder':'Enter your Password'}))

    email = forms.EmailField(label='Email', widget=forms.EmailInput(
                             attrs={'class': 'form-control',
                             'placeholder': 'Enter your email'}))

    mobile = forms.IntegerField(label='Mobiile number', widget=forms.NumberInput(
                                attrs={'class': 'form-control',
                                'placeholder': 'Enter your Mobile number'}))

class LoginForm(forms.Form):
    username = forms.CharField(label='UserName', widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Enter your user name'}))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Enter your Password'}))