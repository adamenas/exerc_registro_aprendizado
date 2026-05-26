from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    # cadastro novo
    if request.method != 'POST':
        # exibe form em branco
        form = UserCreationForm()
    else:
        # processa form preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # faz login e vai pra home
            login(request, new_user)
            return redirect('learning_logs:index')
    
    # exibe form em branco ou inválido
    context = {'form': form}
    return render(request, "registration/register.html", context)