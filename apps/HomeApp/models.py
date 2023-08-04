from django.db import models

class ViewHomeModels(models.Model):

    view=models.IntegerField()
    createdDate=models.DateField(auto_now_add=True)


    def __str__(self):


        return f"{self.createdDate}-->{self.view}"