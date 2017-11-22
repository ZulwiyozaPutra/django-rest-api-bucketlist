from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(
        regex=r'^auth/',
        view=include(
            arg='rest_framework.urls',
            namespace='rest_framework'
        )
    ),
    url(
        regex=r'^bucketlists/$',
        view=CreateView.as_view(),
        name="create"
    ),
    url(
        regex=r'^bucketlists/(?P<pk>[0-9]+)/$',
        view=DetailsView.as_view(),
        name="details"
    ),
    url(
        regex=r'^sign-in/',
        view=obtain_auth_token
    ),
}

urlpatterns = format_suffix_patterns(urlpatterns)
