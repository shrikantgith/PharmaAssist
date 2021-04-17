"""PharmaAssistant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='home'),
    path("hall", views.hall,name='hall'),
    path("plans", views.plans, name="plans"),
    path("patientdb", views.patientdb, name="patientdb"),
    path("account",views.account,name='account'),
    path("profilesetting",views.profilesetting,name='profilesetting'),
    path("medicine",views.Medicinee,name='Medicine'),
    path("customer", views.customer,name='customer'),
    path("reminder", views.reminder,name='reminder'),
    path("seetask", views.seetask, name='seetask'),
    path("message", views.message,name='message'),
    path("inbox", views.inbox, name='inbox'),
]

