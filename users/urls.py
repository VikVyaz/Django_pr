from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, UserUpdateView
from .forms import CustomAuthForm

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', authentication_form=CustomAuthForm,
                                     next_page='catalog:home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
]
