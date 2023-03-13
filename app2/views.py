from django.shortcuts import render

# Create your views here.
def jinja_print2(request):
    d={'name':'kalyani','age':20}
    return render(request,'jinja_print2.html',context=d)

def jinja_first2(request):
    d={'name':'ramalakshmamma','age':45} 
    return render(request,'jinja_first2.html',context=d)   
