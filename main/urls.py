from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from .common import DefaultRouterWithSimpleViews
from api.employee.views import RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, EmployeeView
from api.room.views import RoomsViewSet
from api.reservation.views import RoomReservationsViewSet, GetRoomReservationsView, UpdateReservationsView
from reviews.views import ProductViewSet, ImageViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouterWithSimpleViews()
router.get_api_root_view().cls.__name__ = "Company Room Reservations API"
router.get_api_root_view().cls.__doc__ = "Below is the list of available APIs"
router.register(r'product', ProductViewSet, basename='Product')
router.register(r'image', ImageViewSet, basename='Image')
router.register(r'register', RegisterView, basename='Register')
router.register(r'login', TokenObtainPairView, basename='Login')
# router.register(r'change_password/<int:pk>/', ChangePasswordView, basename='Change Password')
# router.register(r'update_profile/<int:pk>/', UpdateProfileView, basename='Update Profile')
router.register(r'logout', LogoutView, basename='Logout')
router.register(r'employees', EmployeeView, basename='Get Employees')
router.register(r'rooms', RoomsViewSet, basename='Rooms')
router.register(r'rooms/<int:pk>/', RoomsViewSet, basename='Rooms id')
router.register(r'rooms/reservations/all', GetRoomReservationsView, basename='Get Reservations')
router.register(r'rooms/reservations/<int:pk>/', GetRoomReservationsView, basename='Get Reservations By Id')
router.register(r'rooms/reservations/create', RoomReservationsViewSet, basename='Create Reservations')
router.register(r'rooms/reservations/update', UpdateReservationsView, basename='Update Reservations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
