
from django.urls import path,include
from . import views as a



urlpatterns = [
   path('create/', a.UserCreateListView.as_view(), name='user_create'),
   path('detail/<int:id>/', a.UserDetailView.as_view(),name='detail_user'),
]