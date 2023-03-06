from django.shortcuts import render

# Create your views here.
def mypageone(request):
    return render(request,'mypage.html')
def secondpage(request):
    return render(request,'show.html')


