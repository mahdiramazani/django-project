from django.contrib import admin
from .models import ViewHomeModels,ZarinpallClass,SendMessage
from django.db.models.functions import TruncDay
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json


class WriterAdmin(admin.ModelAdmin):
    # change_list.html
    def changelist_view(self, request, extra_context=None):
        # Aggregate new authors per day
        chart_data = (
            ViewHomeModels.objects.annotate(date=TruncDay("createdDate"))
            .values("date")
            .annotate(y=Count("view"))
            .order_by("-date")
        )
        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)

        extra_context = extra_context or {"chart_data": as_json}
        # Call the superclass changelist_view to render the page

        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(ViewHomeModels, WriterAdmin)
admin.site.register(ZarinpallClass)
admin.site.register(SendMessage)
