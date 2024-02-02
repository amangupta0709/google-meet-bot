from django.shortcuts import render
from django.http import HttpResponse
import subprocess

def index(request):
    link = ''
    if request.method == "POST":
        link = request.POST.get('meetlink')
        if link != '':
            subprocess.run(["chmod", "+x", "./botserver/meetbot.py"]) 
            subprocess.run(['python3','./botserver/meetbot.py',link])

    return render(request,'index.html',context=None)


