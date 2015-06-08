from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from bookstore.python_app.views import *

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/doc', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index.html', TemplateView.as_view(template_name='index.html')),
    url(r'^errorLoginPage.html', TemplateView.as_view(template_name='errorLoginPage.html')),
    url(r'^login', login),
    url(r'^register', register),
    url(r'^logout', logout),
    url(r'^profile-settings.html',TemplateView.as_view(template_name='profile-settings.html')),
    url(r'^profile', profile),
    url(r'^liked',num_of_liked_products)
]
