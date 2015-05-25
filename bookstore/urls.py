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
    url(r'^login', login),
    url(r'^errorLoginPage.html',TemplateView.as_view(template_name='errorLoginPage.html')),
    url(r'^register',register),
    url(r'^logout',logout),
]