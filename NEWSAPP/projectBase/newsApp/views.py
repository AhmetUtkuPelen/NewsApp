from django.shortcuts import render,redirect
from .models import*
import requests
from django.contrib.auth.decorators import login_required
from .forms import*

# Create your views here.

# !training dummy function ! #

# def index(request):
#     return render(request,'newsApp/index.html')


# ! beautiful soup ajax function for weather ! #

def get_html_content(request):
    import requests
    city = request.GET.get('city')
    city = city.replace(" ", "+")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.google.com/search?q=weather+{city}').text
    return html_content


# ! landing page function ! #

def index(request):
    context = {}
    
    context["result"] = None
    
    if request.user.is_authenticated:
        if 'city' in request.GET:
    # fetch the weather from Google.
            html_content = get_html_content(request)
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            result = dict()
    # extract region
            result['region'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
    # extract temperature now
            result['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
    # get the day, hour and actual weather
            result['dayhour'], result['weather_now'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split('\n')
        context["readadminnews"] = CreateNews.objects.all()
    
    else:
        return redirect('register')
    
    return render(request, 'newsApp/index.html', context)


# ! GLOBAL NEWS API KEY ! #

API_KEY = '9018c98f43cc4f5f8a7a42207ae84947'


# ! GLOBAL NEWS FUNCTION ! #
def globalNews(request):
    category = request.GET.get('category')
    url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
        
    articles = data['articles']
    
    context = {
        'articles':articles
    }
    return render(request,'newsApp/globalnews.html',context)


def readadminnews(request,nid):
    read_news = CreateNews.objects.filter(id=nid)
    return render(request,'newsApp/readadminnews.html',{"readnews":read_news})

# ! PROFILE PAGE FOR USERS TO CREATE THEIR OWN NEWS ! #

@login_required
def profile(request):
    context = {}
     
    context['form'] = CreateUserNewsForm
    if request.method == "POST":
        
        form = CreateUserNewsForm(request.POST,request.FILES)
        
        if form.is_valid():
            form = form.save(commit = False)
            form.owner = request.user
            form.save()
            return redirect('usernews')
    else:
        return render(request,'newsApp/profile.html',context)


# ! HTML PAGE FUNCTION FOR USERS TO READ ALL USERS' NEWS ! #

def user_news(request):
        
    context = {}
    
    context['create_form'] = UserCreateNews.objects.all().order_by("-creation_date")
    
    return render(request,'newsApp/usernews.html',context)



# ! SPESIFIC USER NEWS READ HTML PAGE FUNCTION ! #

def read_user_news(request,newsId):
    context = {}
    
    context['read_news'] = UserCreateNews.objects.filter(id=newsId)
    
    return render(request,'newsApp/readusernews.html',context)

































# def create_user_news(request,id):
#     context = {}
    
#     context['form'] == CreateUserNewsForm
#     if request.method == "POST":
#         form = CreateUserNewsForm(request.POST,request.FILES)
        
#         if form


     # if request.user.is_authenticated:

    # else:
    #     return render(request,'user/login.html')
    
    
    
    #     context = {}
    
    # context["result"] = None
    
    # if request.user.is_authenticated:
    #     if 'city' in request.GET:
    # # fetch the weather from Google.
    #         html_content = get_html_content(request)
    #         from bs4 import BeautifulSoup
    #         soup = BeautifulSoup(html_content, 'html.parser')
    #         result = dict()
    # # extract region
    #         result['region'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
    # # extract temperature now
    #         result['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
    # # get the day, hour and actual weather
    #         result['dayhour'], result['weather_now'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split('\n')
    #     context["readadminnews"] = CreateNews.objects.all()