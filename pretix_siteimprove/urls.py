from django.conf.urls import url

from .views import siteimprove

urlpatterns = [
    url(r'^_pretix_siteimprove/siteimprove$', siteimprove, name='siteimprove'),
]
