from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from trail.models import *
from django.urls import reverse
from trail.forms import CompanyForm, AgentForm, MaterialsFormset
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# This function created for login purpose  
def user_login(request):
    # creation of blank context
    context={}
    # checking for a method here it is post
    if request.method == "POST":
        # getting username and password in parameter request.POST
        username = request.POST['username']
        password = request.POST['password']
        # this authenticate method check for the username and password are correct
        user=authenticate(request, username=username,password=password)
        if user:
            # login method
            login(request, user)
            if request.GET.get('next',None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('company_list'))
        else:
            context["error"]=" provide valid credentials"
            # rendering to the page
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)
# login_required is the decorator used to restrict the user
@login_required(login_url="/login/")
# This fuction is to get list of companies
def company_list(request):
  
    context={}
    # Company.objects.all() gives all the objects 
    context['companies'] = Company.objects.all()
    context['title'] = 'Companies'
    return render(request, 'index.html',context)

@login_required(login_url="/login/")
# # This fuction is to get details of companies
def company_details(request, id=None):
    context = {}
    context['company'] = get_object_or_404(Company, id=id)
    return render(request, 'details.html', context)

@login_required(login_url="/login/")
# This fuction is to  add the companies
def company_add(request):
    context = {}
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            comp_obj = form.save()
            formset = MaterialsFormset(request.POST, instance=comp_obj)
            if formset.is_valid():
                formset.save()
                return redirect('company_list')
    else:
        context['form'] = CompanyForm()
        context['formset'] = MaterialsFormset()
        return render(request, 'add.html', context)


@login_required(login_url="/login/")
# This fuction is to edit the details of companies
def company_edit(request, id=None):
    context={}
    company = get_object_or_404(Company, id=id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        # validating the form
        if form.is_valid():
            # saving the form
            comp1_obj = form.save()
            #to acess the child class fiels materialformset is used
            formset = MaterialsFormset(request.POST, instance=comp1_obj)
            if formset.is_valid():
                formset.save()
                return redirect('company_list')
    else:
        context['form'] = CompanyForm(instance=company)
        context['formset'] = MaterialsFormset(instance=company)
        return render(request, 'edit.html', context)


@login_required(login_url="/login/")
# This fuction is to delete the companies
def company_delete(request, id=None):
    company = get_object_or_404(Company, id=id)
    if request.method == 'POST':
        company.delete()
        return HttpResponseRedirect(reverse('company_list'))
    else:
        context = {}
        context['company'] = company
        return render(request, 'delete.html', context)

#This method to get the details of child class
def agent_details(request, id=None):
    comp=Company.objects.get(id=id)
    details=comp.agent_set.all()

    return render(request, 'agent_details.html', {'details':details})

#This method to edit  the  child class
def agent_edit(request, id=None):
    agent = Agent.objects.get(id=id)
    a_form = AgentForm(instance=agent)
    if request.method == 'POST':
        a_form = AgentForm(request.POST, instance=agent)
        if a_form.is_valid():
            a_form.save()    
            return redirect('agent_list', id=agent.company.id)
    else:
        return render(request, 'agent_edit.html', {'a_form': a_form})

#This method to  delete the child class
def agent_delete(request, id=None):
    agent = Agent.objects.get(id=id)
    if request.method == 'POST':
        agent.delete()
        return redirect('agent_list', id=agent.company.id)
    else:
        return render(request, 'agent_delete.html', {'agent': agent })
