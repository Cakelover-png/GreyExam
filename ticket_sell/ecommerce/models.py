from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ticket(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Ticket name'))
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    code = models.CharField(max_length=20, verbose_name=_('Ticket code'), unique=True)

    def __str__(self):
        return f"{self.code}"


class Order(models.Model):
    ticket = models.OneToOneField(
        to='ecommerce.Ticket', on_delete=models.CASCADE)
    user = models.ForeignKey(to='user.User', on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.user} | {self.ticket}"
