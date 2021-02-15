from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


# Create your models here.
class Customer(models.Model):
    Name = models.CharField(max_length=50)
    Code = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def _def_(self):
        return self.title


class Order(models.Model):
    item = models.CharField(max_length=50)
    amount = models.CharField(max_length=100)
    date = models.TimeField(auto_now_add=True)

    def _def_(self):
        return self.title
