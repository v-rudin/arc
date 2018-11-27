from django.db import models
from django.urls import reverse



class DiadocDocument(models.Model):
    doc_brief = models.CharField(max_length=10)
    doc_type = models.CharField(max_length=10)
    doc_number = models.IntegerField()
    doc_date = models.DateField()
    doc_description = models.TextField()

    def __str__(self):
        return self.doc_brief

    def get_absolute_url(self):
        return reverse('diadocdocument-detail', args=[str(self.id)])

