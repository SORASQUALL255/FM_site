from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post
from django.core.paginator import Paginator
from .forms import SigUpForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'myblog/bootstraptest.html'
        )

class ContactsView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'myblog/Contacts.html'
        )

class FMVView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'myblog/FMV.html'
        )

class BazaView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'myblog/Baza.html', context={
            'posts': posts
        })

class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SigUpForm()
        return render(request, 'myblog/signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SigUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'myblog/signup.html', context={
            'form': form,
        })