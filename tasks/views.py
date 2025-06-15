from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import AndroidApp
from .serializers import AndroidAppSerializer

class AndroidAppViewSet(viewsets.ModelViewSet):
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer
    permission_classes = [IsAuthenticated]
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import Task

@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_screenshot(request):
    task_id = request.POST.get('task_id')
    screenshot_file = request.FILES.get('file')  # Dropzone sends it with key `file`

    if task_id and screenshot_file:
        try:
            task = Task.objects.get(id=task_id)
            task.screenshot = screenshot_file
            task.save()
            return Response({'message': 'Screenshot uploaded successfully'})
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=404)
    return Response({'error': 'Invalid data'}, status=400)

from django.shortcuts import render, get_object_or_404
from .models import Task

def upload_screenshot_page(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/upload_screenshot.html', {'task': task})

