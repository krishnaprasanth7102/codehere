from django.shortcuts import render, HttpResponse

def index(request):    
    return render(request,'index.html')
    #return HttpResponse('This is home page')

    #return HttpResponse('This is contact this site')
def mos(request):
    return render(request,'mos.html')
   

def bot(request):
    return render(request,'bot.html')





