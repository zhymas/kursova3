from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class HomeResponse(APIView):
    
    def get(self, request):
        return Response({"status": True, "message": "I reject your sadness"}, 
                        status=status.HTTP_200_OK)
