from django.shortcuts import render
from django.http import HttpResponse


import json


# Create your views here.


def index(request):
    content=[{
        "username":"Smrat",
        "password":123456,
        "gender":u"男",
    },{
        "username":"LaLa",
        "password":123456,
        "gender":u"女",
    }
    ]
    # 返回发数据是json格式
    content=json.dumps(content)
    res=HttpResponse(content,content_type="application/json")
    return res
