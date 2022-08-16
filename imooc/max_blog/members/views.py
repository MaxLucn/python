from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from members.forms import SignUpForm, EditProfileForm, PasswordChangingForm


class UserRegisterView(generic.CreateView):
    """ 注册 """
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    """ 编辑个人信息 """
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('blog')

    def get_object(self, queryset=None):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    """ 修改密码 """
    form_class = PasswordChangingForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password_success')
    # success_url = reverse_lazy('blog')


def password_success(request):
    """ 密码修改成功跳转到这里 """
    return render(request, 'registration/password_success.html', {})


