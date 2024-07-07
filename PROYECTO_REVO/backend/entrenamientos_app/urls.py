from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DatosFisicosViewSet, RutinaViewSet, CoachViewSet
from .views import get_datos_fisicos, get_rutinas, get_coaches , get_user_id

router = DefaultRouter()
router.register(r'datos_fisicos', DatosFisicosViewSet)
router.register(r'rutinas', RutinaViewSet)
router.register(r'coaches', CoachViewSet)

urlpatterns = [
    path('user_id/', get_user_id, name='get_user_id'),
    path('datos_fisicos/<int:user_id>/', get_datos_fisicos, name='get_datos_fisicos'),
    path('rutinas/<int:user_id>/', get_rutinas, name='get_rutinas'),
    path('coaches/<int:user_id>/', get_coaches, name='get_coaches'),
    path('', include(router.urls)),
]
