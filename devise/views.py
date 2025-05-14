from django.shortcuts import render, redirect
import api

# Toutes les devises disponibles (tu peux les définir toi-même ou les récupérer depuis l'API)
ALL_CURRENCIES = [
    "USD", "EUR", "GBP", "CAD", "JPY", "AUD", "CHF", "CNY", "ZAR", "INR"
]

def index(request):
    return redirect("home", days_range=7, currencies="USD")


def dashboard(request, days_range=7, currencies="USD"):

    days_range = int(request.GET.get("days_range", days_range))
    currencies = request.GET.get("currencies", currencies)

    # On découpe la chaîne des devises
    currency_list = currencies.split(",")  # ⬅️ Transforme la chaîne en liste
    # Appel à ton API
    days, rates = api.get_rates(currencies=currency_list, days=days_range)

    # Détermination du libellé de la période
    page_labels = {7: "Semaine", 30: "Mois", 365: "Année"}.get(days_range, "Personnalisée")

    context = {
        "data": rates,
        "days_range": days_range,
        "currencies": currencies,
        "page_label": page_labels,
        "currency_list": currency_list,
        "days_labels": days ,
        "all_currencies": ALL_CURRENCIES  # Pour la liste déroulante
    }

    return render(request, "index.html", context)
