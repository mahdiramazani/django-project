from apps.AcountApp.models import User
from .models import SendMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
import ghasedakpack
sms = ghasedakpack.Ghasedak("64543682f335e0527622ad84cea3dc33069017d8ec8f7618f5559f401635bc72")


@receiver(post_save, sender=SendMessage)
def create_profile(sender, instance, created, **kwargs):
    if created:

        print("testtt")

        for user in User.objects.all():

            print(instance.text)

            sms.send({'message': instance.text,
                      'receptor': user.phone,
                      'linenumber': 30005006008894})
