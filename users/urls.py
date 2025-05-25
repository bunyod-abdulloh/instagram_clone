from django.urls import path

from .views import CreateUserView, VerifyAPIView, GetNewVerificationView, ChangeUserInformationView, ChangeUserPhotoView

urlpatterns = [
    path('signup/', CreateUserView.as_view()),
    path('verify/', VerifyAPIView.as_view(), ),
    path('new-verify/', GetNewVerificationView.as_view(), ),
    path('change-user/', ChangeUserInformationView.as_view(), ),
    path('change-user-photo/', ChangeUserPhotoView.as_view(), ),
]
