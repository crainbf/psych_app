from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
import json
from website.models import TrialResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'website/home.html')


@csrf_exempt
def trial(request):
    #We're posting only with AJAX, so if it is not ajax, don't do anything
    if request.is_ajax():
        if request.method == 'POST':
            #The request.POST variable doesn't work so well when using JSON,
            #so we'll read the body of the request instead
            data = json.loads(request.body)
            #create the objects we want to insert into the database
            objects = []
            for obj in data:
                trial = TrialResponse(
                    stim_color=obj['stimulus_color'],
                    response_color=obj['response_color'],
                    reaction_time=obj['duration']
                )
                objects.append(trial)
            #create the objects in bulk, this saves a GREAT amount of time
            TrialResponse.objects.bulk_create(objects)

            return HttpResponse('Thank you.')

        else:
            #For now, this is just a view for POSTing data
            return HttpResponseNotAllowed(['POST'])
    else:
        return HttpResponse('Thank you.')
