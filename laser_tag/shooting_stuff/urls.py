from . import views
from django.conf.urls import url
app_name = 'laser_tag'

urlpatterns = [
    url(r'^player(?P<user_id>[0-9]+)', views.shoot, name='shoot'),
]
