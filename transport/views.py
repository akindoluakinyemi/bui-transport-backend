from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework import generics
from .models import TransportOption
from .serializers import TransportOptionSerializer
from .permissions import IsStudent, IsOrganizer, IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer
from .models import TransportOption
from .serializers import TransportOptionSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

def root_view(request):
    return HttpResponse("🎉 Welcome to Akin's BUI Transport Backend API!")

class OrganizerTransportListView(generics.ListAPIView):
    serializer_class = TransportOptionSerializer
    permission_classes = [IsAuthenticated, IsOrganizer]

    def get_queryset(self):
        return TransportOption.objects.filter(organizer=self.request.user)
    
class TransportOptionCreateView(generics.CreateAPIView):
    serializer_class = TransportOptionSerializer
    permission_classes = [IsAuthenticated, IsOrganizer]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class AvailableTransportOptionsView(generics.ListAPIView):
    queryset = TransportOption.objects.filter(approved=True)
    serializer_class = TransportOptionSerializer
    permission_classes = [IsAuthenticated]


class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def perform_create(self, serializer):
        booking = serializer.save(student=self.request.user)

        if booking.payment_method == 'cash':
            booking.is_paid = False
            booking.save()
        else:
            # Integrate with Paystack/Flutterwave — we'll cover this
            pass
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


# ✅ Only students can view available transport
class StudentTransportListView(generics.ListAPIView):
    queryset = TransportOption.objects.all()
    serializer_class = TransportOptionSerializer
    permission_classes = [IsStudent]

# ✅ Only organizers can see their dashboard
class OrganizerDashboardView(generics.ListAPIView):
    queryset = TransportOption.objects.all()
    serializer_class = TransportOptionSerializer
    permission_classes = [IsOrganizer]

# ✅ Only admins can approve or review
class AdminTransportApprovalView(generics.ListAPIView):
    queryset = TransportOption.objects.filter(organizer__transportorganizer__approved=False)
    serializer_class = TransportOptionSerializer
    permission_classes = [IsAdmin]

class ApproveTransportOptionView(generics.UpdateAPIView):
    queryset = TransportOption.objects.all()
    serializer_class = TransportOptionSerializer
    permission_classes = [IsAdmin, IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        option = self.get_object()
        option.approved = True
        option.save()
        return Response({'detail': 'Transport option approved.'}, status=status.HTTP_200_OK)



# Create your views here.
