from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView

from comic.models import Comic
from profiles.forms import RegisterForm

User = get_user_model()


class loginView(LoginView):
    template_name = 'login.html'


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(
            username=data['username'],
            password=data['password1'],
            email=data['email']
        )
        url = f"{reverse('register_ok')}?username={new_user.username}"
        from pprint import pprint;
        pprint(url)
        return redirect(url);


class SiteRegisterOk(TemplateView):
    template_name = "register_ok.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context


class SiteLogOut(LogoutView):
    template_name = 'logout.html'


def SiteOverView(request):
    object_view = Comic.objects.filter(name__in=['Dragon Ball'])

    return render(request, 'OverView.html', {
        'object_view': object_view,
        'nav': 'OverView'
    })


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'
    model = User
    fields = ['full_name', 'address', 'year_birth', 'about']
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user