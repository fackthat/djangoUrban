from django.shortcuts import render
from task5.forms import UserRegister
# Create your views here.
users = ['user1', 'admin', 'testuser']

def sign_up_by_django(request):
    global users
    info = {'form': UserRegister()}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                return render(request, 'registration_page.html', {'message': f'Приветствуем, {username}!'})
        else:
            info['form'] = form

    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    global users
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        try:
            age = int(age)
        except ValueError:
            info['error'] = 'Некорректный возраст'
        else:
            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                users.append(username)
                return render(request, 'registration_page.html', {'message': f'Приветствуем, {username}!'})

    return render(request, 'registration_page.html', info)
    print(users)