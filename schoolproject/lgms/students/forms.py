from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, PresentCondition, IllnessInfo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.models import User
from django.forms import ModelForm





class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'name','fathersname','guardiansname', 'address', 'dateofbirth','applicationtype','studentname', 'mobilenumber', 'homenumber', 'civilstatus', 'religion')

        fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Personal info', {'email': ('studentname',)}),
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'address')



class EditProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','email', 'first_name', 'last_name', 'dateofbirth', 'studentname', 'address', 'dateuserjoined', 'mobilenumber', 'profilepic', 'religion')


class PresentConditionForm(ModelForm):
    class Meta:
        model = PresentCondition
        fields = ('user', 'name', 'currentcondition', 'conditiondetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness' )


class IllnessInfoForm(ModelForm):
    class Meta:
        model = IllnessInfo
        fields = ('user', 'name', 'illnessinfo', 'illnessdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness')



###########################

###########################
