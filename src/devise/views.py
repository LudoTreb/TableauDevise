from django.shortcuts import render, HttpResponse
import api


# Create your views here.
def dashboard_view(request, days_range=60, currencies="USD"):

    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)

    context = {
        "data": rates,
        "days_labels": days,
    }

    return render(request, "devise/index.html", context=context)
