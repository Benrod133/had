from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import os
import subprocess
import logging

# Create your views here.
def index(request):
    return render(request, 'games/index.html', {
        'games': [
            {
                'name': 'Had',
                'url': 'had',
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
    return index(request)



def error(request):
    return render(request, 'games/error.html', {'message': 'Tato stránka neexistuje.'})