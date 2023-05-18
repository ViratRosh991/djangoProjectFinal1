from django.http import HttpResponse;
import time
# Create your views here.
def f1(req):
    ct = time.ctime()
    print("Current Date & Time:",ct)
    ss = """
    <html>
    <head>
        <title>Project-HTML</title>
        <style>
            h1{color:'Red'}
        </style>
    </head>
    <body>
        <h1>Hello Users</h1>
        <hr color='Green' width = '50%'/>
        <h3>Server Date&Time:</h3>
        <center><h3 style='background-color:Blue;'>""", ct, """</h3></center>
    </body>
    </html>"""
    return HttpResponse(ss);
