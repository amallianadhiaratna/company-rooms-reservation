from django.urls import include, path
from rest_framework import routers
from reservation.views import RoomReservationsViewSet, GetRoomReservationsView, UpdateReservationsSerializer
from room.views import RoomsViewSet
from employee.views import RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, LogoutAllView, EmployeeView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

# router = routers.DefaultRouter()
# router.register(r'rooms', views.RoomReservationsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('register/', RegisterView.as_view(), name='auth_register'),
#     path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
#     path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
#     path('logout/', LogoutView.as_view(), name='auth_logout'),
#     path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
#     path('employees/', EmployeeView.as_view(), name='get_employees'),
    
#     path('rooms/', RoomsViewSet, name='create_room'),
#     # path('rooms/reservations/', GetRoomReservationsView, name='get_reservations'),
#     path('rooms/reservations/create/', RoomReservationsViewSet, name='create_reservations'),
#     path('rooms/reservations/update/', UpdateReservationsSerializer, name='update_reservations'),
# ]