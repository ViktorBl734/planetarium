from django.urls import path, include
from rest_framework import routers

from planetarium.views import ShowThemeViewSet, PlanetariumDomeViewSet, AstronomyShowViewSet, ShowSessionViewSet, \
    ReservationViewSet

router = routers.DefaultRouter()
router.register("show_themes", ShowThemeViewSet)
router.register("planetarium_domes", PlanetariumDomeViewSet)
router.register("astronomy_shows", AstronomyShowViewSet)
router.register("show_sessions", ShowSessionViewSet)
router.register("reservations", ReservationViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "planetarium"