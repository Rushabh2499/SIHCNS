from django.shortcuts import render
from login import models as models

def pie_chart(request):
    labels = []
    data = []

    queryset = DgmReports.objects.order_by('-r_count')
    for datisd in queryset:
        labels.append(datisd.r_status)
        data.append(datisd.r_count)

    return render(request, 'dgm.html', {
        'labels': labels,
        'data': data,
    })