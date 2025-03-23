from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
import os
import subprocess
import logging

# Create your views here.
def index(request):
    return redirect(reverse(games))
def games(request):
    time_url = os.path.join(settings.BASE_DIR, '..', 'celkovy_cas.txt')
    with open(time_url, "r") as file:
        content = file.read().strip()
        time = float(content) if content else 0
    
    #převedení na hodiny:minuty(počítáno z sekund)
    hodiny = int(time // 3600)
    minuty = int((time % 3600) // 60)
    sekundy = int(time % 60)
    time = f"{hodiny} hod {minuty} min {sekundy} sec"

    return render(request, 'games/index.html', {
        'games': [
            {
                'name': 'Had',
                'url': 'had',
                'time': time
            },
        ],
    })



def game_url():

    return os.path.join(settings.BASE_DIR, '..', 'main.py')


def had(request):
    if settings.STATIC_ROOT:
        had_path = game_url()
        if os.path.exists(had_path):
            try:
                subprocess.run(
                    ["python", had_path],
                    shell=True,
                    cwd=os.path.dirname(had_path) 
                )
            except Exception as e:
                logging.error(f"Chyba při spuštění main.py ({had_path}) - {e}")
                return render(request, 'games/error.html', {'message': 'Chyba při spuštění main.py'})
        else:
            logging.error(f"Soubor nenalezen: {had_path}")
            return render(request, 'games/error.html', {'message': f'Soubor nenalezen: main.py ({had_path})'})
    else:
        return render(request, 'games/error.html', {'message': 'STATIC_ROOT není nastaven.'})
    return redirect(reverse(games))




def error(request):
    return render(request, 'games/error.html', {'message': 'Tato stránka neexistuje.'})