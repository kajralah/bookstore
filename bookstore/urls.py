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
    url(r'^add_book',add_book),
    url(r'^liked',num_of_liked_products),
    url(r'^newBook.html',TemplateView.as_view(template_name='newBook.html')),
    url(r'^categories',get_categories),
    url(r'^show_book',show_book),
    url(r'^showProduct',show_product),
    url(r'^books/$',TemplateView.as_view(template_name='books.html')),
    url(r'^likeProduct',like_book),
    url(r'^buyProduct',buy_book),
    url(r'^buyBook/$',TemplateView.as_view(template_name='buyingBook.html')),
    url(r'^is_supervisor',is_supervisor),
    url(r'^isLoggedUser',isLoggedUser),
    url(r'^changeProfile.html',TemplateView.as_view(template_name='changeProfile.html')),
    url(r'^changeProfile',changeProfile),
    url(r'^boughtBooks.html',TemplateView.as_view(template_name='boughtBooks.html')),
    url(r'^boughtBooks',boughtBooks),
]
