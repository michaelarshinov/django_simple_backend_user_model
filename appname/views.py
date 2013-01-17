from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext

from django.shortcuts import render_to_response

#https://docs.djangoproject.com/en/1.2/topics/auth/#other-authentication-sources
#http://stackoverflow.com/questions/9825630/login-required-decorator-in-django-1-1-and-template-name

#@login_required(redirect_field_name='my_redirect_field')
@login_required
def garbage_stat_info(request):
    template = loader.get_template('stat_info.html')
    context = Context({'is_auth': str(request.user.is_authenticated())})
    return HttpResponse(template.render(context))

@login_required
def stat_info(request):
    return render_to_response('stat_info.html',
        {'is_auth':request.user.is_authenticated()},
        context_instance=RequestContext(request))

@login_required
def mainmenu(request):
    return render_to_response('mainmenu.html',{},
        context_instance=RequestContext(request))