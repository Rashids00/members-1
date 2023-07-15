from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MemberForm
from django.shortcuts import redirect



def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('allmembers.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def add_member_form(request):
    template = loader.get_template('add_member.html')
    form = MemberForm()
    return HttpResponse(template.render({"form": form}, request))

def save_member(request):
    
    newmember = MemberForm(request.POST)       
    newmember.save()
    return redirect('members')
