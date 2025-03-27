from django.shortcuts import render

import  api


def dashboard(request):

    days, rates = api.get_rates(currencies=["USD"], days=30)
    return render(request,"index.html",context={"data": rates["USD"],
                                                "days_labels": days})