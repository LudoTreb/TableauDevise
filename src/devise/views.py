from django.shortcuts import render, HttpResponse
import api


# Create your views here.
def dashboard_view(request, days_range=60, currencies="USD"):

    days, rates = api.get_rates(currencies=currencies.upper().split(","), days=days_range)

    page_label = {7: "Semaine", 30: "Mois", 365: "Année"}.get(days_range, "Personnalisé")

    context = {
        "data": rates,
        "days_labels": days,
        "currencies": currencies,
        "page_label": page_label,
    }

    return render(request, "devise/index.html", context=context)
