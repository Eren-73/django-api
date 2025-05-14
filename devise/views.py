from django.shortcuts import render

import  api


def dashboard(request, days_range = 5  , currencies = "CAD"):
    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)

    page_labels = {7:"Semaine", 30:"Mois", 365:"Année"}.get(days_range,"Personnalisée")
    
    return render(request,"index.html",context={"data": rates,
                                                "days_labels": days,
                                                "currencies":currencies,
                                                "page_label":page_labels})