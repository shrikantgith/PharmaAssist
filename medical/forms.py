from django import forms
from .models import Medicine,Patient
a= Medicine.objects.all()
#print(a[0])
#print(a[2])
#heres how we search Patients according to name of medicine
'''
c = Patient.objects.filter(medicine__name="Chrosine")
print(c)
'''
Medicine_ch = [  ]
for i in range(len(a)):
    add_tuple=(a[i].name,a[i].name)
    Medicine_ch.insert(i,add_tuple)

'''
for i in range(len(a)):
    Medicine_ch[a[i].name] = a[i].name
    print(a[i].name)
'''
#print(Medicine_ch)


class PatientForm(forms.Form):
#    auto_reco = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'input inp','data-toggle':'toggle','data-style':'ios'}))
    Patient_Name = forms.CharField(max_length=30,label_suffix="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Patient name'}))
    Medicine = forms.CharField(label_suffix='',widget=forms.Select(attrs={'class':'form-control'},choices=Medicine_ch))
    Address = forms.CharField(max_length=50,label_suffix="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}))
    City = forms.CharField(max_length=30,label_suffix="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City '}))
    Doctor= forms.CharField(max_length=30,label_suffix="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Doctor '}))
    Phno_NO= forms.CharField(max_length=10,min_length=10, label_suffix="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone NO '}))

class AccountSettingForm(forms.Form):
    Phno_NO = forms.CharField(max_length=10,min_length=10, label_suffix="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone NO '}))
    Email_address = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    Password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone No'}))
    Email_noti=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'input inp','data-toggle':'toggle','data-style':'ios'}))
    SMS_noti=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'input inp','data-toggle':'toggle','data-style':'ios'}))

class AccountProfileForm(forms.Form):
    pass

class ReaminderForm(forms.Form):
    task =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone NO '}))
    date =forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'form-control', 'placeholder': 'To do at ?'}))
    SMS_noti=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'input inp','data-toggle':'toggle','data-style':'ios'}))

class MedicineForm(forms.Form):
    nam=forms.CharField( label_suffix=" ", max_length=10,min_length=5,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name '}))
    quantity=forms.IntegerField( label_suffix="", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Quantity '}))
    purchase_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'form-control', 'placeholder': 'Purchase Date'}))
    expiration_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'form-control', 'placeholder': 'Expiration_Date'}))
#    auto_reco=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'input inp','data-toggle':'toggle','data-style':'ios'}))

class MessageForm(forms.Form):
    form = forms.CharField( label_suffix=" ",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Sender email'}))
    to = forms.CharField( label_suffix=" ",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Reciver email'}))
    subject =forms.CharField( label_suffix=" ",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject '}))
    body =forms.CharField( label_suffix=" ",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Body '}))