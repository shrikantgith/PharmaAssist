from django.shortcuts import render
from .forms import PatientForm,AccountSettingForm,ReaminderForm,MedicineForm,MessageForm
from .models import Medicine,Patient

# Create your views here

#from .form import dmeoform,demo2form,demo3form,demo4form
# Create your views here.
def home(request):

    return render(request,'landingpage.html')
def hall(request):
    a = Medicine.objects.all()

    return render(request,'Hall.html',{'a':a})

def patientdb(request):
    a =Patient.objects.all()
    return render(request,'patientdb.html',{'a':a})

def profilesetting(request):
    return render(request,'profilesetting.html')

def plans(request):
    return render(request,'plans.html')

def account(request):

    if request.method =="POST":
        form=AccountSettingForm(request.POST)
        if form.is_valid():
            return render(request,'account.html',{'form':form})
    else:
        form=AccountSettingForm(auto_id=False)

    return render(request,'account.html',{'form':form})

def Medicinee(request):
    if request.method == "POST":
        form=MedicineForm(request.POST)
        print("This is Post req")
        if form.is_valid():
            name= form.cleaned_data['nam']
            quantity= form.cleaned_data['quantity']
            purchase_date=form.cleaned_data['purchase_date']
            expiration_date=form.cleaned_data['expiration_date']
            #print("name"+str(name))
            #print("quantity" + str(quantity))
            #print("purchase_data" + str(purchase_date))
            #print("expiration_data" + str(expiration_date))
            a =Medicine(name=name,quantity=quantity,purchase_date=purchase_date, expiration_date=expiration_date)
            a.save()
            return render(request, 'Medicine.html', {'form': form, 'msg': 1, 'name': name})


        return render(request,'Medicine.html',{'form':form,'msg':2})
    else:
        form=MedicineForm(auto_id=False)
    return render(request,'Medicine.html',{'form':form})

def customer(request):
    if request.method == 'POST':
        form=PatientForm(request.POST)
        print("this is post")
        if form.is_valid():
            print("This is validation")
            Patient_Name=form.cleaned_data['Patient_Name']
            medicines=form.cleaned_data['Medicine']
            Address=form.cleaned_data['Address']
            City=form.cleaned_data['City']
            Doctor=form.cleaned_data['Doctor']
            Phno_NO=form.cleaned_data['Phno_NO']
            print("This is medicine"+ str(medicines))
            a = Patient(Patient_Name=Patient_Name,Address=Address,City=City,Doctor=Doctor, Phno_NO=Phno_NO)
            a.save()
            b = Medicine.objects.filter(name=medicines)
            a.medicine.add(b[0])
            return render(request,'customer.html',{'form':form,'msg':1,'Patient_Name':Patient_Name})
        else:
            return render(request, 'customer.html', {'form': form, 'msg': 2})
    else:
        form =PatientForm(auto_id=True)
    return render(request,'customer.html',{'form':form})

def reminder(request):
    if request.method=='POST':
        form=ReaminderForm(request.POST)
        if form.is_valid():
            return render(request,'reminder.html',{'form':form})
    else:
        form =ReaminderForm(auto_id=True)
    return render(request,'reminder.html',{'form':form})

def seetask(request):
    return render(request,'seetask.html')

def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            return render(request, 'message.html', {'form': form})
    else:
        form = MessageForm(auto_id=True)

    return render(request,'message.html',{'form':form})

def inbox(request):
    return render(request,'Inbox.html')
'''
from twilio.rest import Client

account_sid = 'ACb3cc37d304c5d89096b49be05aa5d88a'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+19388008469',
    body='dammm!',
    to='+917972168543'
)

print(message.sid)
'''