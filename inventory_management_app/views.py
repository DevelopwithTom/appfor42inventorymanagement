from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView
from django.db.models import Q
from inventory_management_app.models import Project, Location, Box, UserQueryHistory
from inventory_management_app import models

# from django.template import RequestContext

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

import datetime

from django.db.models import Count

# from .forms import LoginForm

from django.contrib import messages











def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('index')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')

    else:
        form = AuthenticationForm()
    return render(request, 'todo/login.html', {'form': form})





@login_required
def dashboard(request):
    queries = UserQueryHistory.objects.filter(user=request.user).order_by('-date_searched')[:7]

    project_data = Project.objects.exclude(box__isnull=True)
    project_data_full = Project.objects.all()


    # box_content_history = Box.history.filter(history_type='-').order_by('-history_date')

    box_content_history = Box.history.all().order_by('-history_date')



    number_of_projects = Project.objects.exclude(box__isnull=True)

    location_data = Location.objects.values('loc_room').distinct()

    box_data = Box.objects.all()







    Vacant_location_data = list(Location.objects.values('loc_room'
     ).filter(box__isnull=True).annotate(nempty=Count('id')).order_by('loc_room'))



    Occupied_location_data = list(Location.objects.values('loc_room'
    ).filter(box__isnull=False).annotate(nempty=Count('id')).order_by('loc_room'))


    if Occupied_location_data:
        for i, vacant in enumerate(Vacant_location_data):
            vacant['occupied'] = Occupied_location_data[i]['nempty']



    return render(request, 'inventory_management_app/dashboard.html', {"queries":queries,
                                                        "project_data":project_data,
                                                        "box_content_history":box_content_history,
                                                        "number_of_projects":number_of_projects,
                                                        "box_data":box_data,
                                                        "location_data":location_data,
                                                        "Vacant_location_data":Vacant_location_data,
                                                        "Occupied_location_data":Occupied_location_data,})









class all_assets(TemplateView):
    template_name = 'inventory_management_app/all_assets.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['box_data'] = Box.objects.all()
        return context

#Transfer to class ListView for above



@login_required
def manage_assets(request):
    return render(request, admin_index)



"""
class assets_by_Project(ListView):
    context_object_name = 'Project_data'
    model = models.Project




"""
@login_required
def assets_by_project(request):
    project_data = Project.objects.all()
    return render(request, 'inventory_management_app/assets_by_project.html', { "project_data":project_data })

##Transfer to class ListView for above






@login_required
def project_search_results(request, project_query):
    query = project_query
    results = Box.objects.filter(Q(project_assigned_to__project_name__icontains=query))
    return render(request, 'inventory_management_app/project_search_results.html', {'query':query,'results':results})

#Transfer to class ListView for above


@login_required
def assets_by_location(request):
    location_data = Location.objects.values('loc_room').distinct('loc_room')
    return render(request, 'inventory_management_app/assets_by_location.html', {"location_data":location_data})


@login_required
def location_search_results(request, location_query):
    query = location_query
    results = Box.objects.filter(Location__loc_room__icontains=query)
    return render(request, 'inventory_management_app/location_search_results.html', {'query':query,'results':results})




@login_required
def search_results(request):
    query = request.GET.get('q')
    results = Box.objects.filter(box_contents__icontains=query)
    UserQueryHistory.objects.create(user=request.user, query=query)

    return render(request, 'inventory_management_app/search_results.html', {"results":results})


















@login_required
def user_log_off(request):
    my_dict = {'insert_me': 'hello, I am from view.py. THIS IS A TEST'}
    return render(request, 'inventory_management_app/user_log_off.html' , context = my_dict)
