from django.urls import path,include
from rest_framework import routers
from myapi.views import *

router = routers.DefaultRouter()
router.register(r'students',Studentlist)
# router.register(r'deleteStudent',deleteStudent)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('Studentdelete/<id>',deleteStudent),
    path('Studentupdate/<id>',updateStudent),
]