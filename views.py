def index(request)
        return HttpResponse("CSDN读者你好啊")
def login(request)
        return redirect("/index")
