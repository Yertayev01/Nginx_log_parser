from rest_framework.routers import DefaultRouter
from django.urls import path, include
from logparser.views import LogEntryViewSet

router = DefaultRouter()
router.register(r'logentries', LogEntryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]