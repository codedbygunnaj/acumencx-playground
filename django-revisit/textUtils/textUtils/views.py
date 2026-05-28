# user built function

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("helloClient -- from Server!")
def homeWork1(request):
    return render(request,'homeWorkOne.html')
def exercise1(request):
    return render(request,'exercise1.html')
def tryBall(request):
    info = {'name':'Gunaj',
            'place':'Delhi'}
    return render(request,'tryBall.html',info)

#from here functions of project:
def homePage(request):
    return render(request, 'homePage.html')
def removePunc(request):
    text = request.GET.get('text','default') #default acting as a fallBack for 'text'
    print('Old text: ' , text)
    # processedText = [x for x in text if ('a' <= x <= 'z') or ('A' <= x <= 'Z')]
    processedText = ''.join([x for x in text if x.isalnum()])
    print('Processed text: ', processedText)
    return HttpResponse("helloClient -- from Server!")
def capFont(request):
    return HttpResponse("helloClient -- from Server!")
def removeNewL(request):
    return HttpResponse("helloClient -- from Server!")
def removeSpace(request):
    return HttpResponse("helloClient -- from Server!")
def charCount(request):
    return HttpResponse("helloClient -- from Server!")