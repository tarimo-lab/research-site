from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic.edit import CreateView




class LoginView(CreateView):
    success_url = reverse_lazy('home')
    template_name = 'registration/login.html'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(*args, **kwargs)