from rest_framework import viewsets
from myapp.myapp_models.ToolModel import *
from myapp.myapp_models.UserModel import *
from .permissions import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated



@permission_classes([IsAuthenticated])
class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            tag_param = self.request.query_params.get('tag', None)
            if tag_param:
                return self.queryset.filter(tags__icontains=tag_param)
        return self.queryset

class SignupViewSet(viewsets.ViewSet):
    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None :
            return Response({'message':'Digit a valid username'},status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'message': 'This username is already in use.'}, status=status.HTTP_400_BAD_REQUEST)
        if not re.match(PASSWORD_REGEX, password):
            return Response({
                'message': 'Password does not meet the requirements.'
            }, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        if user:
         return Response({'message':'Sucessfully created'},status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'An error occurred while registering the user.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)