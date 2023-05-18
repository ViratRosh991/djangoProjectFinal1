from django.http import HttpResponse

# Create your views here.
def f2(req):
    print("Hello")
    ss = """<h2 style='color:Green;'>Hello ser</h2>"""
    return HttpResponse(ss);