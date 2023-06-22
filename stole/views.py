from dataclasses import dataclass
from typing import Self, Union, Any
from django.urls.base import reverse
from django.views.generic.base import View
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .models import IPModel





@dataclass
class UserAccessType:
    access: str = 'Accessed'
    no_access: str = 'Access Denied'





class IndexView(View):
    def get(self: Self, request: HttpRequest) -> Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]:
        ip: Any = request.META['HTTP_X_FORWARDED_FOR']
        system: Any = str(request.META['HTTP_USER_AGENT']).split(sep=' ')
        
        if (ip is not None):
            ip: str = str(ip).split(sep=',')[0]
            try:
                if (IPModel.objects.get(ip=ip).limit == False):
                    pass
                else:
                    return redirect(to=reverse(viewname='limit'))
            except:
                IPModel.objects.create(
                    user_agent=system,
                    ip=ip,
                    limit=False,
                )
        
        return render(
            request=request,
            template_name='index.html',
            context={
                'title': UserAccessType.access,
                'ip': ip,
                'access': UserAccessType.access,
                'system_windows': str(system[1]).replace("(", ""),
                'system_other': str(system[2]).replace(';', ''),
            },
        )
        





class LimitView(View):
    def get(self: Self, request: HttpRequest) -> HttpResponse:
        return render(
            request=request,
            template_name='limit.html',
            context={
                'title': UserAccessType.no_access,
                'access': UserAccessType.no_access,
            },
        )