
from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    # getting input from form

    text = request.GET.get('text','default')
    capitalize = request.GET.get('capitalize','off')
    uppercase = request.GET.get('uppercase','off')
    lowercase = request.GET.get('lowercase','off')
    punctuations = request.GET.get('punctuations','off')
    blankspace = request.GET.get("blankspaces",'off')
    newline = request.GET.get('newline','off')

    # initializing variables
    check = False
    analyzed = text
    temp = ""
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


    # Capitalize
    if capitalize == "on":
        temp = ""
        check = True
        analyzed = analyzed.capitalize()
   
    if uppercase == "on":
        temp = ""
        for char in analyzed:
            temp = temp + char.upper()
        analyzed = temp

        check = True
    
    if lowercase == "on":
        analyzed = analyzed.lower()
        print(analyzed)
        check = True

    if punctuations == "on":
        temp = ""
        check = True
        for x in analyzed:
            if x not in punc:
                temp = temp + x
        analyzed = temp

    if blankspace == "on":
        check = True
        temp = analyzed.split()
        analyzed = ""   
        for i in temp:
            print(i)
            analyzed = analyzed + i + " "   
    
    if newline == "on":
        check = True
        analyzed.rstrip("\n")

    if not check:
        params = {"analyzed_text":"*You haven't selected any option*"}

    return render(request,"analyze.html",params)