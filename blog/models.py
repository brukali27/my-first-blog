from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class significa qu class Post(models.Model): -- esta linha define o nosso modelo (é um objeto). class é uma
# palavra-chave especial que indica que estamos definindo um objeto. models.Model significa que o Post é um modelo de
# Django, então o Django sabe ele que deve ser salvo no banco de dados. Agora definimos as propriedades que
# comentamos acima: title, text, created_date, published_date e author. Para fazer isso, é necessário definir um tipo
# para cada campo (É um texto? Um número? Uma data? Uma relação com outro objeto, por exemplo, um usuário?)
# models.CharField - é assim que definimos um texto com um número limitado de caracteres. models.TextField - este
# campo é para textos sem um limite fixo. Parece ideal para o conteúdo de um blog, né? models.DateTimeField - este é
# uma data e hora. models.ForeignKey - este é um link para outro modelo.
# verificar tipos de modelos do django: https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types
