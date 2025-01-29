from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from myapp.models import student
from django.http import Http404
from django.db import connection
import pandas as pd
from django.contrib import auth

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

def getOneByName(request, username):
    title = "顯示一筆資料"
    try:
        unit = student.objects.get(cName=username)
    except student.DoesNotExist:
        raise Http404("查無此學生")
    except Exception as e:
        print(f"讀取錯誤: {e}")
        raise Http404("讀取錯誤")
    return render(request, 'listone.html', locals())    # locals() 可將所有區域變數轉為字典

def getAll(request):
    title = "顯示全部資料"
    try:
        students = student.objects.all()
    except student.DoesNotExist:
        raise Http404("查無學生資料")
    except Exception as e:
        print(f"讀取錯誤: {e}")
        raise Http404("讀取錯誤")
    return render(request, 'listall.html', locals())

def getAll_pd(request):
    title = "顯示全部資料"
    try:
        query = "SELECT * FROM myapp_student"
        df = pd.read_sql_query(query, connection)
        students = df.to_dict(orient='records')  # 將 DataFrame 轉換為列表字典
    except Exception as e:
        print(f"讀取錯誤: {e}")
        raise Http404("讀取錯誤")
    return render(request, 'listall.html', locals())

# 模板繼承範例
def main(request):
    pageTitle="子網頁繼承"
    mainTitle="段落標題"
    mainContent="段落內文"
    artitle1={"aTitle":"文章標題","aContent":"文章1內文"}
    artitle2={"aTitle":"文章標題","aContent":"文章2內文"}
    artitles=[artitle1, artitle2]
    return render(request, 'index.html', locals())

# 表單範例
def login(request):
    # GET -> 登入頁面
    if request.method == 'GET':
        return render(request, 'login.html')
    # POST -> 驗證
    elif request.method == 'POST':
        uName = request.POST.get('uName') # login.html 傳來的變數
        uPass = request.POST.get('uPass') # login.html 傳來的變數

        # 以 Django 內建的管理者帳密判斷有效性
        user = auth.authenticate(username=uName, password=uPass)
        if user is not None:
            auth.login(request, user)
            return HttpResponse("已登入")
        else:
            return redirect('/myapp/login/')  # 重定向
