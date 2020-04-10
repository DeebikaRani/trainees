
from django.conf .urls import url,include

urlpatterns = [

    url('', include('core.urls', namespace="core")),

]

