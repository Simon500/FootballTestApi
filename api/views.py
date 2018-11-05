from django.shortcuts import render
import requests, datetime
from datetime import datetime, date, time,timedelta

def index(request):
    url ='https://api.sportradar.us/soccer-xt3/other/en/schedules/{}/schedule.json?api_key=gq8tkgwrfz4wv3dzhg2pzq6u'
    d = date.today()
    results = requests.get(url.format(d)).json()
    fixtures = []
    
    for sportevent in results['sport_events']:
        daily ={
            
            'id': sportevent['id'],
            'scheduled': sportevent['scheduled'],
            'tournamentround': sportevent['tournament_round'],
            'season': sportevent['season'],
            'tournament': sportevent['tournament'],
            'hometeam':sportevent['competitors'][0],
            'awayteam':sportevent['competitors'][1],                 
        }
        fixtures.append(daily)
    
    context = {'fixtures': fixtures}
    return render(request, 'schedule/index.html', context)
