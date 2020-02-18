  from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^view_book/(?P<book_id>\d+)/$', views.view_book),
    url(r'^create_book/$', views.create_book),
    url(r'^add_author/$', views.add_author),

    url(r'^authors/$', views.authors),
    url(r'^view_author/(?P<author_id>\d+)/$', views.view_author),
    url(r'^create_author/$', views.create_author),
    url(r'^add_book/$', views.add_book),
]