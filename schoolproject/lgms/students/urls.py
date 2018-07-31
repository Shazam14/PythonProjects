from django.urls import path
from students.views import StudentBioList
from django.contrib.flatpages import views
from django.conf import settings
from django.conf.urls.static import static



from . import views

#name can be used for reverse function

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),

    path('testlist/', StudentBioList.as_view(), name='studentbiolist'),

    #this path worked
    # path('editprofile/', views.editprofile, name='editprofile'),

#studentbio in green is the path ! remember that!
#i need to change this to home - when i changed it became visible
    path('home/', views.slist, name='slist'),
    #path('studentbio/', views.studentcheck, name='studentcheck'),
#this is for editprofile
    path('editprofile/', views.editprofile, name='editprofile'),
#this is for editprofile
    path('changepassword/', views.changepassword, name='changepassword'),
#this worked when i linked the studentbio and added the integer id.
    path('home/<int:pk>', views.studentbioid, name="studentbioid"),

#this is for home
    #path("studentbio/<int:pk>", views.student, name="student"),

    #cheatsheet for getting primary key
    # path("<int:flight_id>", views.flight, name="flight"),
    # path("<int:flight_id>/book", views.book, name="book"),

    #not workin
    # path('home/', views.SubjectDetailView.as_view(), name="subject_detail_view"),

    #path('studentprofile/', StudentProfileView.as_view()),


    # path('studentprofile/', views.studentprofile, name='studentprofile'),

    #path('studentbioinfo/', views.DetailInfo.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
