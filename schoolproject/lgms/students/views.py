from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from django.views import generic
from django.template import loader
from django.db import transaction
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
#for session
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import StudentBio, CustomUser, IllnessInfo, PresentCondition, HospitalInfo, ImmunisationInfo, AccidentInfo
from .forms import CustomUserCreationForm, EditProfileForm, CustomUserChangeForm, PresentConditionForm

from django.contrib import messages


def slist(request):

    context = {
        "studentbios": StudentBio.objects.all()
    }
    return render(request, "students/home.html", context)


def ucheck(request):

    context = {
        "userbio": Users.objects.all()
    }
    return render(request, "students/home.html", context)

    #original
    #return render(request, "students/studentbio.html", context)
#studentbio id is the variable

def studentbioid(request, pk):
    try:
        studentcheck = StudentBio.objects.get(pk=pk)
        subjectlist = StudentBio.objects.filter(subjects__pk=pk)

    except StudentBio.DoesNotExist:
        raise Http404("Student does not exist")
    context = {
        "studentcheck" : studentcheck,
        "subjectlist" : subjectlist
    }
    #return render(request, "students/home.html", context)
    #original code
    return render(request, "students/home.html", context)


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#@login_required
class StudentBioList(ListView):
    model = StudentBio
    paginate_by = 10



############################## MEDICAL FORM ####################################


class PresentConditionCreate(CreateView):
    model = PresentCondition
    fields = ['user', 'name', 'currentcondition', 'conditiondetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']


class PresentConditionUpdate(UpdateView):
    model = PresentCondition
    fields = ['user', 'name', 'currentcondition', 'conditiondetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']


class PresentConditionDelete(DeleteView):
    model = PresentCondition
    fields = ['user', 'name', 'currentcondition', 'conditiondetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    success_url = reverse_lazy('students/home')
##############################ILLNESS FORM ####################################
class IllnessInfoCreate(CreateView):
    model = IllnessInfo
    fields = ['user', 'name', 'illnessinfo', 'illnessdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']

class IllnessInfoUpdate(UpdateView):
    model = IllnessInfo
    fields = ['user', 'name', 'illnessinfo', 'illnessdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']

class IllnessInfoDelete(DeleteView):
    model = IllnessInfo
    fields = ['user', 'name', 'illnessinfo', 'illnessdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    success_url = reverse_lazy('students/home')

##############################ILLNESS FORM ####################################


##############################HOSPITAL FORM ####################################

class HospitalInfoCreate(CreateView):
    model = HospitalInfo
    fields = ['user', 'name', 'reasonforhospital', 'hospitalisationdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']

class HospitalInfoUpdate(UpdateView):
    model = HospitalInfo
    fields = ['user', 'name', 'reasonforhospital', 'hospitalisationdetails', 'treatmentdetails',  'startperiodofillness', 'endperiodillness']

class HospitalInfoDelete(DeleteView):
    model = HospitalInfo
    fields = ['user', 'name', 'reasonforhospital', 'hospitalisationdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    success_url = reverse_lazy('students/home')

##############################HOSPITAL FORM ####################################

##############################ACCIDENT FORM ####################################

class AccidentInfoCreate(CreateView):
    model = AccidentInfo
    fields = ['user', 'name', 'accidentdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']

class AccidentInfoUpdate(UpdateView):
    model = AccidentInfo
    fields = ['user', 'name', 'accidentdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']

class AccidentInfoDelete(DeleteView):
    model = HospitalInfo
    fields = ['user', 'name', 'accidentdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    success_url = reverse_lazy ('students/home')

##############################ACCIDENT FORM ####################################


##############################IMMUNE FORM ####################################
class ImmunisationInfoCreate(CreateView):
    model = ImmunisationInfo
    fields = ['user','name', 'immunedetails', 'treatmentdetails', 'startperiodofimmune', 'endperiodimmune']

class ImmunisationInfoUpdate(UpdateView):
    model = ImmunisationInfo
    fields = ['user', 'name', 'immunedetails', 'treatmentdetails', 'startperiodofimmune', 'endperiodimmune']

class ImmunisationInfoDelete(DeleteView):
    model = ImmunisationInfo
    fields = ['user', 'name', 'immunedetails', 'treatmentdetails', 'startperiodofimmune', 'endperiodimmune']
    success_url = reverse_lazy ('students/home')



##############################IMMUNE FORM ####################################
class DetailView(generic.DetailView):
    model = StudentBio
    template_name = 'students/studentbiodetail.html'

class ResultsView(generic.DetailView):
    model = StudentBio
    temaplate_name = 'students/studentbioresults.html'


def editprofile(request):
    try:
        profile = request.user.id
    except User.DoesNotExist:
        profile = CustomUser(user=request.user)
    if request.method == 'POST':
        profileform = EditProfileForm(request.POST, instance=request.user)
        if profileform.is_valid():
            profileform.save()
            update_session_auth_hash(request, form.users)
            return redirect('home')
        else:
            message.error(request, ('ERROR ON UPDATING PROFILE!'))
    else:
        profileform = EditProfileForm(instance=request.user)
        return render (request, 'students/editprofile.html', {'profileform': profileform})


##############################PRESENT CONDITION FORM####################################
def presentcondition(request):
    try:
        profile = request.user.id
    except User.DoesNotExist:
        profile = CustomUser(user=request.user)
    if request.method == 'POST':
        medicalform = PresentConditionForm(request.POST, user=request.user)
        if medicalform.is_valid():
            medicalform.save()
            update_session_auth_hash(request, form.users)
            return redirect('home')
        else:
            message.error(request, ('FORM INCOMPLETE'))
    else:
        medicalform = PresentConditionForm(instance=request.user)
        return render (request, 'students/medicalform.html', {'medicalform' : medicalform })




##############################CHANGE PASSWORD####################################
def changepassword(request):
    try:
        passwordprofile = request.user.id
    except User.DoesNotExist:
        passwordprofile = CustomUser(user=request.user)
    if request.method == 'POST':
        passwordchangeform = PasswordChangeForm(data=request.POST, user=request.user)

        if passwordchangeform.is_valid():
           passwordchangeform.save()
           update_session_auth_hash(request, passwordchangeform.user)
           return redirect('home')

        else:
           messages.error(request, ('ERROR IN CHANGING YOUR PASSWORD!'))
    else:
        passwordchangeform = PasswordChangeForm(user=request.user)
        return render(request, 'students/changepassword.html', {'passwordchangeform' : passwordchangeform})





def latestsubjects(request):

    latest_subjects = Subjects.objects.order_by('id')
    context = { 'latest_subjects': latest_subjects }
    return render(request, 'students/latestsubjects.html', context)





#! remember ! this is the code I based for the editprofile to work - will get back into this.
# try:
#         profile = request.user.profile
#     except Profile.DoesNotExist:
#         profile = Profile(user=request.user)
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(
#             request.POST or None, instance=profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(
#                 request, ('your profile was successfully updated!'))
#             return redirect('products:profile')
#         else:
#             messages.error(
#                 request, ('There was an error updating your profile'))
#     else:s
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'dashboard/company/profile.html', {'user_form': user_form, 'profile_form': profile_form})






    # def flight(request, flight_id):
    #     try:
    #         flight = Flight.objects.get(pk=flight_id)
    #     except Flight.DoesNotExist:
    #         raise Http404("Flight does not exist")
    #     context = {
    #         "flight": flight,
    #         "passengers": flight.passengers.all(),
    #         "non_passengers": Passenger.objects.exclude(flights=flight).all()
    #     }
    #     return render(request, "flights/flight.html", context)

#
# class StudentBioView(TemplateView):
#     model = StudentBio
#     template_name = 'home.html'
#
# #getting records
#     def get(self, request):
#         studentrecords = StudentBio.objects.all()
#         print(studentrecords)
#         args = {'studentrecords' : studentrecords}
#         return render(request, self.template_name, args)


# class MedicalRecordsView(TemplateView):
#     template_name = 'home.html'
#
#     def get_info(self, request):
#         if request.method == 'POST':
#             form = MedicalForm(request.POST)
#             if form.is_valid():
#                 text = form.cleaned_data['post_info']
#                 return HttpResponseRedirect('home.html')
#         else:
#             form = MedicalForm()
#         args = {'form': form, 'text' : text}
#         return render(request, self.template_name, args)


#
# def login_view():
#     if request.method == 'POST':
#                 #what is this form?? but noramlly you put UserCreationForm or whatever form you did.
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#         return redirect('')
#     else:
#         form = AuthenticationForm()
#

#medical form -- test
# from students.forms import PresentConditionForm

# Create your views here.

##testing of students

# class HomeView(g)
#
# view profile with primary key



#
# class SubjectDetailView(generic.DetailView):
#     model = StudentBio
#     template_name = 'home.html'


# ###this is a test for studentview lists...
# def studentprofile(request):
#     args = {'studentbio': request.studentbio.id }
#     return render(request, 'studentprofileview.html', args)

#edit profile not working
#this worked code - will check!
#from user(blue parameters - i changed it to CustomUser and it worked)
#i also experimented to change the form name to profile form then change the name in html template
