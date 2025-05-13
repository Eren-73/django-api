from django.shortcuts import render

import  api


def dashboard(request, days_range = 5  , currencies = "CAD"):
    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)


    
    return render(request,"index.html",context={"data": rates[currencies],
                                                "days_labels": days})