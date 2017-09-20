from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.db import transaction
from django.shortcuts import redirect
from django.contrib import messages


# authenticate() проверяет учетные данные пользователя и возвращает user объект в случае успеха;
# login() задает пользователя в текущей сессии.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Аутентификация прошла успешно.')
                else:
                    return HttpResponse('Учетная запись отключена.\n, Обратитесь к администратору.')
            else:
                return HttpResponse('Неверный логин.')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


# Мы используем декоратор login_required, так как пользователи должны
# авторизоваться для редактирования своего профиля
@login_required
@transaction.atomic
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            photo = request.user.profile.photo
            messages.success(request, 'Ваш профиль успешно обновлён.')
            # return redirect('settings:profile')
        else:
            messages.error(request, 'Ошибка при обновлении профиля!')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    # print("----------------------------")
    # print(request.user.profile.photo)
    # print(photo)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form, 'photo': request.user.profile.photo})


# декоратор login_required authentication framework. Декоратор login_required
# проверяет, прошел ли текущий пользователь аутентификацию.
# Если пользователь прошел аутентификацию, представление выполнится; Если пользователь не прошел
# аутентификацию, он будет перенаправлян на страницу входа.
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
