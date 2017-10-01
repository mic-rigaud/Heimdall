from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from logging import getLogger

from Network_Analyst.task import scan
from Network_Analyst.task import demo_task

logger = getLogger(__name__)

# Create your views here.
@csrf_exempt
def tasks(request):
    scan_now()
    return redirect('home')

def scan_now():
    logger.debug('Scan creation de la tache')
    scan(schedule=1)
    # demo_task('bonjour', schedule=1)
    return redirect('home')


# def _repeat_tasks(message, request):
#     logger.debug('calling demo_task. message={0}'.format(message))
#     demo_task(message, repeat="60", repeat_until=None)
#     return render(request, 'Main_UI/home.html')
