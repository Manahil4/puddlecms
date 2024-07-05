from django.shortcuts import render
myitems=['portfolio','df','fe']
# Create your views here.
def index(request):
    return render(request, "myitems/index.html",{
        'myitems':myitems})