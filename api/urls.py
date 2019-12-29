from django.urls import path

from .views import QuoteAPIView
from .views import QuoteCategoryAPIView
from .views import QuoteAPIDetailView
from .views import QuoteAPINewView
from .views import QuoteAPISpecificView

urlpatterns = [
    path('', QuoteCategoryAPIView.as_view()),
    path('GET/values/', QuoteAPIView.as_view()),
    path('GET/values/<int:pk>/', QuoteAPISpecificView.as_view()),
    path('POST/values/', QuoteAPINewView.as_view()),
    path('PATCH/values/<int:pk>/', QuoteAPIDetailView.as_view()),
]