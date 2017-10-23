from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'log' in request.session:
        request.session['log'] = 0
    data = {}
    data['gold'] = request.session['gold']
    data['log'] = request.session['log']
    return render_template('index.html', data=data)

def process(request):
    if 'location' not in request.POST:
        location = request.POST['location']

    if location == 'Farm':
        rand = randrange(10, 21)
        message = "You went to the farm and earned ", rand, " gold."
    elif location == 'Cave':
        rand = randrange(5, 11)
        message = "You went to the cave and earned ", rand, " gold."
    elif location == 'House':
        rand = randrange(2, 6)
        message = "You went to the house and earned ", rand, " gold."
    elif location == 'Casino':
        rand = randrange(-50, 51)
        message = "You went to the casino and earned ", rand, " gold."
    
    log = request.session['log']
    request.session['log'] = message, log
    request.session['gold'] += rand
    return redirect('/')

def reset(request):
	request.session['gold'] = 0
	request.session['log'] = ''
	return redirect('/')