from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    return HttpResponse("Home page")

def hiname(request, username):
    return HttpResponse("Hi " + username)

def age(request, year):
    return HttpResponse("Age: " + str(year))

def hello_view(request):
    fourSeason = range(1, 5)
    p1={"name":"Amy","phone":"0912-345678","age":20}
    p2={"name":"Jack","phone":"0937-123456","age":25}
    p3={"name":"Nacy","phone":"0958-654321","age":17}
    persons=[p1,p2,p3]
    return render(request, 'hello_django.html', {
        'title':"樣板使用",
        'data':"Hello Django!",
        'seasons':fourSeason,
        'persons':persons,
        'now':datetime.now()
    })