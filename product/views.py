from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.checks import messages
from django.db.models import F, Q
from django.forms import forms
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from .models import product, category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse, reverse_lazy
from django.db.models import Count
import random
import os
#from twilio.rest import Client

def index(request):
    context = {
        'category': category.objects.all()
    }
    return render(request, 'index.html', context)

"""def tataset(request):
    context = {
        'category': category.objects.all(),
        'product': product.objects.order_by('-create'),
        'posts': post.objects.order_by('-date_posted')
    }
    return render (request, 'setting.html', context)"""


def category_view(request, id):
    obj1 = get_object_or_404(category, id=id)
    title = category.objects.filter(id=id).only("name")
    abcd = title[0]
    context = {
        "obj": product.objects.filter(category=abcd).order_by('-nbr_achat')[:10],
        "abcd": abcd,
        "category": category.objects.all()
    }
    return render(request, "category.html", context)


def about(request):
    context = {
        'category': category.objects.all()
    }
    return render(request, 'about.html',context)
#added

def politique(request):
    context = {
        'category': category.objects.all()
    }
    return render(request, 'politique.html', context)

def livraison(request):
    context = {
        'category': category.objects.all()
    }
    return render(request, 'livraison.html', context)