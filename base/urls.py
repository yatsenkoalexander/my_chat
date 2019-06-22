from sys import path

from .views import BasePageView

urlpatterns = [
    path('', BasePageView.as_view()),
]