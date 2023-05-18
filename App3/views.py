from django.shortcuts import render
import time
# Create your views here.
def f3(req):
    cd = time.ctime()
    return render(req,'App3/time.html',{"cd":cd})