from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('invest/',views.invest),
    path('sip/',views.sip)
    # path('',views.expense)
]