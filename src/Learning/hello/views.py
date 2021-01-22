from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cookieCount(request):
    num_visits = request.session.get('num_visits', 0) + 1
    html = HttpResponse("<h1>Here is dj4e cookie</h1>")
    html.set_cookie('dj4e_cookie', '7f018eb7', max_age=1000)
    request.session['num_visits'] = num_visits
    if num_visits > 4: del (request.session['num_visits'])
    return HttpResponse('view count=' + str(num_visits))