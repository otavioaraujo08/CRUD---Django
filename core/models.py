from django.db import models
from stdimage.models import StdImageField

# Signal: Utilizado para realizar um processamento de dados antes de enviar para o BD
# Slugify é o título da "Matéria" para ser procurado na internet
from django.db.models import signals
from django.template.defaultfilters import slugify


# Classe utilizada para indicar a situação de uma informação
class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de modificação', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


# Classe Produto heradará as informações da classe Base
class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


# Função que antes de salvar ira analisar os dados com o Singal
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)
