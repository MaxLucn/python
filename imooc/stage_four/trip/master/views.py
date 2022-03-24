from django.shortcuts import render


# Create your views here.
def test(request):
    """ echarts 的使用 """
    return render(request, 'master/test.html')
