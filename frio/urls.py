# ---> move to views.py when finished ---------------------------------------------------
from datetime import datetime, timedelta

from django.shortcuts import render
from django.urls import path

from .models import Camaras, Registros, Umbrales

# from django.contrib import admin

# from . import views

# from .views import fichada_list
# from .views import fichada_flat_list
# from .views import presentes_CC_list
# from .views import formacion_list
# from .views import detalle_list
# from .views import checkrelo
# from .views import ahora_list


# @login_required
def tsttemps(request):

    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    # canales_con_datos = Registros.objects.all().order_by("ts")
    temps = Registros.objects.filter(ts__gte="2024-06-28 00:00:00").filter(tipo__exact="T").order_by("ix", "ts")
    # canales = set([x.ix for x in temps])
    data = {}
    # data = {x: temps.filter(ix__exact=x) for x in canales}
    l_ts = []
    l_temp = []
    c = None
    for r in temps:
        if c and r.ix != c:
            data[c] = {"ts": l_ts, "temp": l_temp}
            l_ts = []
            l_temp = []
        c = r.ix
        l_ts.append(f"{r.ts:%H:%M}")
        # l_ts.append(f"{r.ts}")
        l_temp.append(float(r.temp))
    if c:
        data[c] = {"ts": l_ts, "temp": l_temp}

    return render(request, "graficos.html", {"data": data})


def tsttemps4(request):

    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    return render(request, "graficos4.html")


def tsttemps5(request):

    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    return render(request, "graficos5.html")


def tstalpine(request):

    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    return render(request, "tstalpine.html")


def tsttemps2(request):

    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    # canales_con_datos = Registros.objects.all().order_by("ts")
    temps = Registros.objects.filter(ts__gte="2024-06-27 00:00:00").filter(tipo__exact="T").order_by("ix", "ts")
    # canales = set([x.ix for x in temps])
    data = {}
    # data = {x: temps.filter(ix__exact=x) for x in canales}
    l_ts = []
    l_temp = []
    l_data = []
    c = None
    series = []
    for r in temps:
        if c and r.ix != c:
            data[c] = {"ts": l_ts, "temp": l_temp, "data": l_data}
            series.append({"name": f"Canal {c}", "data": l_data})
            l_ts = []
            l_temp = []
            l_data = []
        c = r.ix
        l_ts.append(f"{r.ts:%H:%M}")
        # l_ts.append(f"{r.ts}")
        l_temp.append(float(r.temp))
        l_data.append([int((r.ts - timedelta(hours=3)).timestamp() * 1000), float(r.temp)])
    if c:
        data[c] = {"ts": l_ts, "temp": l_temp, "data": l_data}
        series.append({"name": f"Canal {c}", "data": l_data})

    return render(request, "graficos2_2.html", {"data": data, "series": series})


from django.http import JsonResponse
from django.views.decorators.gzip import gzip_page


@gzip_page
def jsontemps(request):

    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    chans = Camaras.objects.all()
    # canales = [x.__str__() for x in chans]
    canales = {x.ix: x.__str__() for x in chans}

    # canales_con_datos = Registros.objects.all().order_by("ts")
    temps = Registros.objects.filter(ts__gte="2024-07-04 00:00:00").filter(tipo__exact="T")  # .order_by("ix", "ts")
    # viene ordenado por ts, ix

    # chans = set()
    # series = [ { name: x, data:[] } for x in chans]
    dser = {}
    for r in temps:
        if r.ix not in dser:
            # dser[r.ix] = {"name": r.ix, "data": []}
            dser[r.ix] = {"name": canales[r.ix], "data": []}
        dser[r.ix]["data"].append([int((r.ts - timedelta(hours=3)).timestamp() * 1000), float(r.temp)])

    canales_keys = sorted(dser.keys())

    data = {
        "canales": [canales[i] for i in canales_keys],
        # "canales": canales_keys,
        # "labels": [f"Temperaturas canal {k}" for k in dser.keys()],
        "series": [dser[i] for i in canales_keys],
    }

    return JsonResponse(data, safe=True)


def tsttemps3(request):

    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    # canales_con_datos = Registros.objects.all().order_by("ts")
    temps = Registros.objects.filter(ts__gte="2024-07-04 00:00:00").filter(tipo__exact="T").order_by("ix", "ts")
    # canales = set([x.ix for x in temps])
    data = {}
    # data = {x: temps.filter(ix__exact=x) for x in canales}
    l_ts = []
    l_temp = []
    c = None
    for r in temps:
        if c and r.ix != c:
            data[c] = {"ts": l_ts, "temp": l_temp}
            l_ts = []
            l_temp = []
        c = r.ix
        l_ts.append(f"{r.ts:%H:%M}")
        # l_ts.append(f"{r.ts}")
        l_temp.append(float(r.temp))
    if c:
        data[c] = {"ts": l_ts, "temp": l_temp}

    return render(request, "graficos3.html", {"data": data})


# -----------------------------------------------------------------------------------------

urlpatterns = [
    path("tst/", tsttemps, name="tsttemps"),
    path("tst2/", tsttemps2, name="tsttemps2"),
    path("tst3/", tsttemps3, name="tsttemps2"),
    path("series/", jsontemps, name="jsontemps"),
    path("tst4/", tsttemps4, name="tsttemps4"),
    path("tst5/", tsttemps5, name="tsttemps5"),
    path("tsta/", tstalpine, name="tstalpine"),
    # path('',            ahora_list ,        name='homepage')
]
# path('lista/', fichada_flat_list , name='flat'), #views.consulta)
