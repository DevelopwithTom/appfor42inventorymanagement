from django.conf.urls import url
from inventory_management_app import views
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from inventory_management_app.forms import CustomAuthForm





# Template Tagging
app_name = 'inventory_management_app'





urlpatterns = [


    # url(r'^login/$', auth_views.LoginView.as_view(),name = 'login'),

    url(r'^login/$', auth_views.login, name='login', kwargs={"authentication_form":CustomAuthForm}),





	url(r'^logout/$', auth_views.LogoutView.as_view(), name = 'logout'),



	# url(r'^dashboard', login_required(views.dashboard.as_view()), name = 'dashboard'),
	url(r'^all_assets', login_required(views.all_assets.as_view()), name = 'all_assets'),

	# url(r'^assets_by_project', login_required(views.dashboard.as_view()), name = 'assets_by_project'),


	url(r'^dashboard', views.dashboard, name = 'dashboard'),
	url(r'^assets_by_project', views.assets_by_project, name = 'assets_by_project'),


    url(r'^project_search_results/(?P<project_query>\D+)/$', views.project_search_results, name = 'project_search_results'),




	url(r'^manage_assets', views.manage_assets, name = 'manage_assets'),
	url(r'^search_results', views.search_results, name = 'search_results'),



	url(r'^assets_by_location', views.assets_by_location, name = 'assets_by_location'),
	url(r'^location_search_results/(?P<location_query>\D+)/$', views.location_search_results, name = 'location_search_results'),




    ]



    # 	url(r'^assets_by_project', login_required(views.dashboard.as_view()), name = 'assets_by_project'),
