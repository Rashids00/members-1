from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('members/addmember/', views.add_member_form, name='addmember'),
    path('members/savemember/', views.save_member, name='savemember')
]