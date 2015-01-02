# from django.conf.urls.defaults import patterns, url
from django.conf.urls import patterns, include, url

urlpatterns = patterns('authorizenet.views',
     url(r'^sim/payment/$', 'sim_payment', name="authnet_sim_payment"),
)
