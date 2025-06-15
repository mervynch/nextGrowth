from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AndroidAppViewSet
from .views import upload_screenshot
from .views import upload_screenshot_page
router = DefaultRouter()
router.register(r'android-apps', AndroidAppViewSet, basename='androidapp')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', upload_screenshot, name='upload-screenshot'),
    path('upload-page/<int:task_id>/', upload_screenshot_page, name='upload-screenshot-page'),
]

