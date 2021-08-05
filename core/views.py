# Bibliotecas importadas do django com funções específicas
# Render = Faz a rendirazação do site// Messages = Retorna mensagens para o público
# Redirect = Redireciona para determinado local
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

# Páginas importadas com o intuito de criar contexto com as views principais
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


# Função para direcionar a página inicial como 'Index.html'
def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


# Função responsável por receber os valóres de token e variáveis, podendo aparecer no terminal.
def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        # Inserindo as variáveis necessárias para o formulário ser validado
        if form.is_valid():
            form.send_mail()

            # Caso funcione, ira ser gerado um token dizendo que foi sucesso.
            messages.success(request, 'Email enviado com Sucesso!')
            form = ContatoForm()
        else:
            # Caso contrário, ira retornar um token inválido
            messages.error(request, 'Erro ao enviar Email!')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


# Função que retorna a página produto - A Página será renderizada com os produtos e informações abaixo.
def produto(request):
    # Verificando se o usuário que entrar é anônimo ou usuário do servidor para liberar a página.
    if str(request.user) != 'AnonymousUser':
        # Validando se as informações recebidas são reais.
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            # Se ele for válido
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto Salvo com Sucesso.')
                form = ProdutoModelForm
            # Caso não seja válido.
            else:
                messages.error(request, 'Erro ao Salva Produto.')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')
