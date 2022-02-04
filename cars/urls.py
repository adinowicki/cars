from rest_framework import routers

from cars_app import views

router = routers.SimpleRouter()
router.register(
    r"cars",
    views.CarViewSet,
)
router.register(
    r"rate",
    views.RateViewSet,
    basename="rate",
)
router.register(
    r"popular",
    views.PopularViewSet,
)
urlpatterns = router.urls
