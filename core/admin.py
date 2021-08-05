from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Valores obtidos do models na linha 11
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')