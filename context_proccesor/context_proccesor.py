from datetime import datetime

import jdatetime


def get_time(request):

    return {
        "time":datetime.now().strftime("%H:%M:%S"),
        "date":jdatetime.date.today()
    }