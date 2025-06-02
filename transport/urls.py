from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookingViewSet,
    MyTokenObtainPairView,
    StudentTransportListView,
    OrganizerDashboardView,
    AdminTransportApprovalView,
    BookingCreateView,
    AvailableTransportOptionsView,
    OrganizerTransportListView,
    TransportOptionCreateView,
    ApproveTransportOptionView,
    root_view
)
from rest_framework_simplejwt.views import TokenRefreshView

# DRF router for ViewSets
router = DefaultRouter()
router.register(r'bookings', BookingViewSet)

# URL patterns
urlpatterns = [
    path('', root_view),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Student APIs
    path('student/book/', BookingCreateView.as_view(), name='book-ride'),
    path('student/options/', AvailableTransportOptionsView.as_view(), name='view-options'),
    path('student/transports/', StudentTransportListView.as_view(), name='student-transports'),

    # Organizer APIs
    path('organizer/options/', OrganizerTransportListView.as_view(), name='organizer-options'),
    path('organizer/create/', TransportOptionCreateView.as_view(), name='create-option'),
    path('organizer/dashboard/', OrganizerDashboardView.as_view(), name='organizer-dashboard'),

    # Admin APIs
    path('admin/approvals/', AdminTransportApprovalView.as_view(), name='admin-approvals'),
    path('admin/approve/<int:pk>/', ApproveTransportOptionView.as_view(), name='approve-transport-option'),


    # Include router-generated URLs (trips and bookings)
    path('', include(router.urls)),
]
