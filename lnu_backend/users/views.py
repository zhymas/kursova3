from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from .permission import AzurePermission
from django.contrib.sessions.models import Session

ms_identity_web = settings.MS_IDENTITY_WEB

class HomeResponse(APIView):
    
    permission_classes = [AzurePermission,]
    
    def get(self, request):
        return Response({"status": True, "message": "Deploy check"}, 
                        status=status.HTTP_200_OK)


class Claims(APIView):
    
    permission_classes = [AzurePermission,]
    
    def get(self, request):
        session_data = request.session
        return Response({
            "status": True, "message": "Successfully claims user_info", "data": session_data['identity_context_data']
        }, status=status.HTTP_200_OK)