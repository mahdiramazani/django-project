from django import forms
from apps.AcountApp.models import User

class EditProfileForm(forms.ModelForm):

    class Meta:
        model=User

        fields=("fullname","image","bio")

        widgets={
            "fullname":forms.TextInput(
                attrs={
                    "class":"input-namefirst-checkout form-control"
                }
            ),
            "image":forms.FileInput(attrs={
                "class":"input-namefirst-checkout form-control"
            }),
            "bio":forms.Textarea(attrs={
                "class":"input-namefirst-checkout form-control summernote"
            })
        }
