from django.shortcuts import render
from .models import Psycho

def filter_psychologists(request):
    specialization = request.GET.get('specialization', '')
    location = request.GET.get('location', '')
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)

    # Base query
    psychologists = Psycho.objects.all()

    # Apply filters
    if specialization:
        psychologists = psychologists.filter(specialization__icontains=specialization)
    if location:
        psychologists = psychologists.filter(work_location__icontains=location)
    if min_price:
        psychologists = psychologists.filter(price__gte=min_price)
    if max_price:
        psychologists = psychologists.filter(price__lte=max_price)

    return render(request, 'fip_app/filter_psychologists.html', {
        'psychologists': psychologists,
    })
