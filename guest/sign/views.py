from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required  # 导入限制某个视图函数登录才能访问的装饰器
from sign.models import Event, Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.


def index(request):
    return render(request, "index.html")

# 登录动作


def login_action(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # if username == 'admin' and password == 'admin123':
        #     response = HttpResponseRedirect('/event_manage/')
        user = auth.authenticate(
            username=username, password=password)  # 后台配置了账号才能登录成功
        if user is not None:
            auth.login(request, user)  # 登录
            # response.set_cookie('user',username,3600) #添加浏览器cookie,3600是设置保存的时间，单位为秒
            request.session['user'] = username  # 将session 信息记录在浏览器里面
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, "index.html", {'error': u'用户名或者密码错误!'})

# 发布会管理


@login_required  # 限制某个视图函数登录才能访问的装饰器
def event_manage(request):
    # username = request.COOKIES.get('user','') #读取浏览器的cookie
    event_list = Event.objects.all()  # 查询所有发布会的对象
    username = request.session.get('user', '')  # 读取浏览器的session
    return render(request, "event_manage.html", {"user": username, "events": event_list})

# 搜索发布会


@login_required
def search_name(request):
    username = request.session.get('user', '')  # 读取浏览器的session
    search_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=search_name)  # 查询要搜索的对象
    return render(request, "event_manage.html", {"user": username, "events": event_list})

# 嘉宾管理


@login_required
def guest_manage(request):
    username = request.session.get('user', '')  # 读取浏览器的session
    guest_list = Guest.objects.all()  # 查询所有嘉宾
    paginator = Paginator(guest_list,2) #划分每页显示2条数据
    page = request.GET.get('page') #获取当前要显示第几页数据
    try:
        contacts = paginator.page('page')
    except PageNotAnInteger:
        #如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        #如果page不在范围，取最后一页数据
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})

# 搜索嘉宾


@login_required
def search_guest_name(request):
    username = request.session.get('user', '')  # 读取浏览器的session
    search_name = request.GET.get("realname", "")
    guest_list = Event.objects.filter(name__contains=search_name)  # 查询要搜索的对象
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})
