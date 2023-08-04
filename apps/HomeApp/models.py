from django.db import models

class ViewHomeModels(models.Model):

    view=models.IntegerField()
    createdDate=models.DateTimeField(auto_now_add=True)