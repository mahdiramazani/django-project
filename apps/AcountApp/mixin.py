from django.shortcuts import redirect


class CheckLoginMixinMixin:

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect("HomeApp:HomeApp")

        else:

            return super().dispatch(request, *args, **kwargs)