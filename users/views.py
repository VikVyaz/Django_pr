from decouple import config
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .forms import UserRegisterFrom, UserUpdateForm
from .models import User


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterFrom
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_mail(user.email)
        return super().form_valid(form)

    def send_welcome_mail(self, user_email):
        subject = 'Добро пожаловать в Каталог'
        message = 'Спасибо, что зарегистрировались'
        from_email = 'mail.djan@yandex.com'
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/update.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('catalog:home')
