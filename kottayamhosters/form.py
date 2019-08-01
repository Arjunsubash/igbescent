from django import forms
from django.forms import ModelForm
from django.core.validators import validate_email
from kottayamhosters.models import Add_logo, Add_video, Add_design, Add_printart

class Loginform(forms.Form):    
    username = forms.CharField(label='username', max_length=100, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'Username'}),)
               
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput({'class': "form-control",'placeholder': 'Password'}))
    def clean(self):
        cleaned_data = super(Loginform, self).clean()
        username = cleaned_data.get('username') 
        password = cleaned_data.get('password')
        if len(username) < 3: 
            #raise forms.ValidationError("minimum 5 characters")
            msg="Minimum 3 characters required"
            self.add_error('username', msg)
        if len(password) < 3: 
            #raise forms.ValidationError("minimum 5 characters")
            msg="Minimum 3 characters required"
            self.add_error('password', msg) 
        return self.cleaned_data  

class Message_data(forms.Form):
    name = forms.CharField(label='name' ,max_length = 100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Name'}))
    Email_field = forms.EmailField(label='Email' ,max_length = 100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Email'}))
    Phno = forms.CharField(min_length = 5,max_length = 10,widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Your Phone number','size':'10'}),error_messages={'invalid':'Enter a valid phone number'})
    Text_area = forms.CharField(label='name' ,max_length = 100,widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Your Message'}))
    def clean(self):
        cleaned_data = super(Message_data, self).clean()
        name = cleaned_data.get('name') 
        Email_field = cleaned_data.get('Email_field')
        if len(name) <= 1: 
            msg="Enter a name"
            self.add_error('name', msg)
        V_data = validate_email(Email_field)
        if V_data == False:
            msg="Enter a valid email address"
            self.add_error('Email_field', msg)
        return self.cleaned_data  
class Logo_data(forms.ModelForm):
    name = forms.CharField(label='name' ,max_length = 100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Name'}))
    description_logo = forms.CharField(label='name' ,max_length = 100,widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Your Message'}))
    photo = forms.FileField()
    class Meta:
        model = Add_logo
        fields={
            "name","description_logo","photo"
         }
class video_data(forms.ModelForm):
    video_name = forms.CharField(label='name' ,max_length = 100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Name'}))
    video_description_logo = forms.CharField(label='name' ,max_length = 100,widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Your Message'}))
    video_photo = forms.FileField()
    class Meta:
        model = Add_video
        fields={
            "video_name","video_description_logo","video_photo"
         }
class design_data(forms.ModelForm):
    design_name = forms.CharField(label='name' ,max_length = 100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Name'}))
    design_description_logo = forms.CharField(label='name' ,max_length = 100,widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Your Message'}))
    design_photo = forms.FileField()
    class Meta:
        model = Add_design
        fields={
            "design_name","design_description_logo","design_photo"
         }
class printart_data(forms.ModelForm):
    printart_name = forms.CharField(label='name' ,max_length = 100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Name'}))
    printart_description_logo = forms.CharField(label='name' ,max_length = 100,widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Your Message'}))
    printart_photo = forms.FileField()
    class Meta:
        model = Add_printart
        fields={
            "printart_name","printart_description_logo","printart_photo"
         }