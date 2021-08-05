from django import forms
from django.core.mail.message import EmailMessage

from .models import Produto


# Detalhes necessários para se enviar um email
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    # Função para enviar os detalhes recebidos do formulário acima
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}.\nEmail: {email}.\nAssunto: {assunto}.\nMensagem: {mensagem}'

        mail = EmailMessage(
            # Conteúdo que será enviado pelo Django
            subject='Email enviado pelo sistema Django',
            body=conteudo,
            from_email='contato@gmail.com',
            to=['otavioaraujo490@gmail.com'],
            headers={'Reply-To': email}
        )
        # Função para enviar o Email
        mail.send()


# Classe Model Form: Responsável por
class ProdutoModelForm(forms.ModelForm):
    class Meta:
        # Metadados - Informações
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']