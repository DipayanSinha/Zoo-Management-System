from django import forms
from .models import Department,Exhibit,Animal,Staff
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import User

class ChangePassword(PasswordChangeForm):
    '''error_css_class = 'has-error'''''
    '''error_messages = {'password_incorrect':
                          "Το παλιό συνθηματικό δεν είναι σωστό. Προσπαθείστε   ξανά."}'''
    old_password = forms.CharField(required=True, label='Old password',
                             widget=forms.PasswordInput(attrs={
                                 'class': 'form-control','placeholder':'Old password'}),
                             )

    new_password1 = forms.CharField(required=True, label='New Password',
                              widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter Password'}))
    new_password2 = forms.CharField(required=True, label='Re-enter New Password',
                              widget=forms.PasswordInput(attrs={
                                  'class': 'form-control','placeholder':'Enter Password'}),
                              )
    class Meta:
        model=User
        fields = ('old_password','new_password1','new_password2')

    def __init__(self,*args,**kwargs):
        super(ChangePassword,self).__init__(*args,**kwargs)

        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].label = ""
        self.fields['old_password'].widget.attrs['placeholder'] = 'Enter your Username'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].label = ""
        self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li> ' \
                                    '<li>Your password can\'t be a commonly used password.</li> <li>Your password can\'t be entirely numeric.</li> ' \
                                    ' </ul>'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Enter your Password'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].label = ""
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Re-enter your Password'
        self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class DepartmentForm(forms.ModelForm):
    id = forms.CharField(max_length=4, label="Department ID",
                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department ID'}))
    name = forms.CharField(max_length=45, label="Department Name",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department Name'}))
    class Meta:
        model = Department
        fields = ['id','name']

class ExhibitForm(forms.ModelForm):
    id = forms.CharField(max_length=4, label="Exhibit ID",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Exhibit ID'}))
    name = forms.CharField(max_length=45, label="Exhibit Name",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Exhibit Name'}))
    doo = forms.DateField(label="Date of Opening",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Opening'}))
    noofvisitors = forms.IntegerField(label="No. of Visitors",widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'No. of Visitors','type':'number'}))
    class Meta:
        model = Exhibit
        fields = ['id', 'name','doo','noofvisitors']

class AnimalForm(forms.ModelForm):
    id = forms.CharField(max_length=4, label="Animal ID",
                         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Animal ID'}))
    commonname = forms.CharField(max_length=45, label="Common Name",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Common Name'}))
    scientificname = forms.CharField(max_length=45, label="Scientific Name",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Scientific Name'}))
    dob = forms.DateField(label="Date of Birth",
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}))
    class_field = forms.CharField(max_length=45, label="Class",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Common Name'}))
    dod = forms.DateField(label="Date of Death",required=False,
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Death'}))
    edscore = forms.FloatField(label="ED Score",required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ED Score'}))
    height = forms.FloatField(label="Height",
                               widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'height'}))
    weight = forms.FloatField(label="Weight",
                               widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'weight'}))
    healthstatus = forms.CharField(max_length=45, label="Health Status",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Health Status'}))

    class Meta:
        model = Animal
        fields = ['id', 'commonname','scientificname','dob','class_field','dod','edscore','height','weight','healthstatus']

class StaffForm(forms.ModelForm):
    id = forms.CharField(max_length=4, label="Staff ID",
                         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Staff ID'}))
    firstname = forms.CharField(max_length=45, label="First Name",
                         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    middlename = forms.CharField(max_length=45, label="Middle Name",required=False,
                         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}))
    lastname = forms.CharField(max_length=45, label="Last Name",
                         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    dob = forms.DateField(label="Date of Birth",
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}))
    doorno = forms.CharField(max_length=45, label="Door No",required=False,
                         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Door No'}))
    housename = forms.CharField(max_length=45, label="House Name",required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'House Name'}))
    streetname = forms.CharField(max_length=45, label="Street Name",required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Name'}))
    gender = forms.CharField(max_length=1, label="Gender",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender'}))
    contactno = forms.CharField(max_length=10, label="Contact No",
                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact No'}))

    class Meta:
        model = Staff
        fields = ['id', 'firstname','middlename','lastname','dob','doorno','housename','streetname','gender','contactno']