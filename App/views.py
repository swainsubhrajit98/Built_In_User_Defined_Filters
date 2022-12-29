from django.shortcuts import render

# Create your views here.
def Built_Filter(request):
    d={'data':'HaI PytHOn aNd DjaNGo WeLCoME'}
    return render(request,'Built_Filter.html',d)

def Date_Filter(request):
    import datetime
    dt=datetime.date.today()
    d={'dt':dt,'c':1,'m':2}
    return render(request,'Date_Filter.html',d)
    
def UserDefineFilter(request):
    d={'data':'HI Python AnD DjanGO HoW aRe yoU TeLL Me What AbOuT ToDay'}
    return render(request,'UserDefineFilter.html',d)