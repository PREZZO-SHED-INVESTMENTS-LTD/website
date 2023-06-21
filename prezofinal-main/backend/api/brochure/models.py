from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brochure(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='brochures')
    pdf_file = models.FileField(upload_to='brochures/', null=True)


    def __str__(self):
        return self.title
