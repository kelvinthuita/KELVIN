from django.urls import  path
from . import views

app_name = 'afriqapp'

urlpatterns = [
    path('',views.MemberListview.as_view(), name='index'),
    path('add-member', views.MembersCreateView.as_view(), name='add-member'),
    path('<int:pk>/update', views.MembersUpdateView.as_view(), name='update-member'),
    path('<int:pk>/delete', views.MembersDeleteView.as_view(), name='delete-member'),

]