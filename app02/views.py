from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    entries = models.Entry.objects.all()

    return render(request,'home.html',{"entries":entries})


def home2(request):
    entries = models.Entry.objects.all()

    return render(request,'home2.html',{"entries":entries})









def intelligence(request):
    ###获取几天前的日期
    import datetime
    #获取今天日期
    today = datetime.datetime.now()
    #计算偏移量
    offset = datetime.timedelta(days=7)
    #获取想要的日期时间
    re_date = (today - offset).strftime('%Y-%m-%d')

    # infos = models.CtrImplied.objects.all()
    infosDatefilter = models.CtrImplied.objects.filter(Uptime__gte=re_date)
    #
    # return render(request,'infos.html',{"infos":infos})
    return render(request, 'infos.html', {"infos": infosDatefilter})
    # return render(request,'infos.html')