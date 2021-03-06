from django.http import HttpResponse, HttpResponseNotAllowed
from django.middleware.csrf import get_token
from django.shortcuts import render
from website.models import TrialResponse
import json


def home(request):
    return render(request, 'website/home.html')


def disclaimer(request):
    return render(request, 'website/disclaimer.html')


def thanks(request):
    #We're posting only with AJAX, so if it is not ajax, don't do anything
    if request.is_ajax():
        if request.method == 'POST':
            #The request.POST variable doesn't work so well when using JSON,
            #so we'll read the body of the request instead
            data = json.loads(request.body)
            #create the objects we want to insert into the database
            objects = []
            try:
                participant_number = TrialResponse.objects.order_by('-participant_id')[0].participant_id + 1
            except IndexError:
                participant_number = 1
            for obj in data:
                trial = TrialResponse(
                    participant_id=participant_number,
                    stim_color=obj['stimulus_color'],
                    stim_word=obj['stimulus_word'],
                    response_color=obj['response_color'],
                    reaction_time=obj['duration'],
                    session_number=obj['session_number'],
                )
                objects.append(trial)
            #create the objects in bulk, this saves a GREAT amount of time
            TrialResponse.objects.bulk_create(objects)

            return HttpResponse('{"status": true}', content_type='application/json')

        else:
            #For now, this is just a view for POSTing data
            return HttpResponseNotAllowed(['POST'])
    else:
        return HttpResponse('Success. This is so AWESOME!')


def csrf(request):
    get_token(request)
    return HttpResponse('')


def break_screen(request):
    #We're posting only with AJAX, so if it is not ajax, don't do anything
    if request.is_ajax():
        if request.method == 'POST':
            #The request.POST variable doesn't work so well when using JSON,
            #so we'll read the body of the request instead
            data = json.loads(request.body)
            #create the objects we want to insert into the database
            objects = []
            try:
                participant_number = TrialResponse.objects.order_by('-participant_id')[0].participant_id + 1
            except IndexError:
                participant_number = 1

            for obj in data:
                trial = TrialResponse(
                    participant_id=participant_number,
                    stim_color=obj['stimulus_color'],
                    stim_word=obj['stimulus_word'],
                    response_color=obj['response_color'],
                    reaction_time=obj['duration'],
                    session_number=obj['session_number'],
                )
                objects.append(trial)
            #create the objects in bulk, this saves a GREAT amount of time
            TrialResponse.objects.bulk_create(objects)

            return HttpResponse('{"status": true}', content_type='application/json')

        else:
            #For now, this is just a view for POSTing data
            return HttpResponseNotAllowed(['POST'])
    else:
        return render(request, 'website/break.html')
