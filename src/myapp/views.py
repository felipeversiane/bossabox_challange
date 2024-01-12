from rest_framework import viewsets
from myapp.myapp_models.ToolModel import *
from .permissions import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action



'''

Tool View Set

'''

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            tag_param = self.request.query_params.get('tag', None)
            if tag_param:
                return self.queryset.filter(tags__icontains=tag_param)
        return self.queryset
