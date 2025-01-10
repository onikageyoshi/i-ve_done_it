from django.shortcuts import render

from rest_framework import permissions, response, status, views

from .serializers import NotificationSerializer
from .models import Notification
from drf_yasg.utils import swagger_auto_schema



class UserNotificationHistoryView(views.APIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = request.user
        notifications = Notification.objects.filter(user=user)
        serializer = NotificationSerializer(notifications, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    
    @swagger_auto_schema(request_body=NotificationSerializer)
    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Associate the loan transfer with the current user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

