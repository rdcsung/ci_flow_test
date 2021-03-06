from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^dl', hello.views.dl, name='dl'),
    url(r'^learn', hello.views.learn, name='learn'),
    url(r'^get_name', hello.views.get_name, name='get_name'),
    url(r'^your_name', hello.views.your_name, name='your_name'),
    url(r'^admin/', include(admin.site.urls)),
]
