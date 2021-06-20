from django.urls import path
from . import views
app_name = 'comportal'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('section/', views.AdminView.as_view(), name='admin-sec'),
    path('<int:pk>/', views.detailViewNew, name='detail'),
    path('<int:pk>/prioritize', views.prioritize, name='prioritize'),
    path('<int:pk>/pdf', views.pdf, name='complain-pdf'),
    path('<int:pk>/statusupdate', views.statusupdate, name='status-update'),
    path('add/', views.CreateComplain.as_view(), name='newcomplain'),
    path('lodged/', views.LodgedComplain.as_view(), name='lodged-complains'),
    path('<int:pk>/process', views.process, name='process'),
    path('<int:pk>/done', views.done, name='done'),
    path('update/<int:pk>/', views.UpdateComplain.as_view(), name='update-complain'),
    path('delete/<int:pk>/', views.DeleteComplain.as_view(), name='delete-complain'),
    path('user/<str:username>', views.UserComplains.as_view(), name='user-complains'),
    path('recents/',views.RecentView.as_view(),
         name='index-recents'),
    path('last/',views.LastView.as_view(),
         name='index-last'),
    path('unprocessed/', views.UnprocessedView.as_view(),
         name='index-unprocessed'),
    path('processing/',views.ProcessingView.as_view(),
         name='index-processing'),
    path('resolved/', views.ResolvedView.as_view(),
         name='index-resolved'),
    path('priority/',views.PriorityView.as_view() ,
         name='index-priority'),

]
