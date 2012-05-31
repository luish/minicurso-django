from django.db import models

class ItemAgenda(models.Model):
	data = models.DateField()
	hora = models.TimeField()
	titulo = models.CharField(max_length=80)
	descricao = models.TextField()
	local = models.CharField(max_length=80)

	def __unicode__(self):
		return self.titulo
