from django.shortcuts import render

# Create your views here.
def jinja_print1(request):
    d={'name':'yasmin','age':21}
    return render(request,'jinja_print1.html',context=d)

def jinja_first1(request):
    d={'name':'rasoolbee','age':45} 
    return render(request,'jinja_first1.html',context=d)   
