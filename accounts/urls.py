from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    

    # login and logout and signup with API ->
    path('api/v1/',include('accounts.api.v1.urls')),
    # to update the API section ->
    # path('api/v2/', include('djoser.urls')),
    # path('api/v2/', include('djoser.urls.jwt')),

    
    # test ->
    # path('send-email/', views.send_email, name='send-email'),
    # path('test/', views.test, name='test'),
]

