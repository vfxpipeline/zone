from django.shortcuts import render
# Create your views here.


def renderbox_view(request):
    """
    Renderbox view
    :param request:
    :return:
    """
    return render(request, 'renderbox/renderbox.html')


def myjobs_view(request):
    """
    Renderbox view
    :param request:
    :return:
    """
    return render(request, 'renderbox/myjobs.html')
