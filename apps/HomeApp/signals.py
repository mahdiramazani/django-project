from apps.AcountApp.models import User
from .models import SendMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
import ghasedakpack
sms = ghasedakpack.Ghasedak("091fd79dad29615b1b1ca22a91beac3c83db83baba36b25e28ef054650d7d71e")


@receiver(post_save, sender=SendMessage)
def create_profile(sender, instance, created, **kwargs):
    if created:

        print("testtt")

        for user in User.objects.all():

            print(instance.text)

            sms.send({'message': instance.text,
                      'receptor': user.phone,
                      'linenumber': 300002525})
