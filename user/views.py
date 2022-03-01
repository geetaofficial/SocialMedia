from venv import create
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login 
from .forms import SignupForm, CustomAuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.http import is_safe_url
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView, ListView
from django.core.exceptions import ImproperlyConfigured, PermissionDenied

# Create your views here.


class Home(TemplateView):
    """Home Template View"""
    template_name = 'home.html'


class CustomLoginView(LoginView):
    """User Custom Login View"""
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        keep_signin = form.cleaned_data['keep_signin']
        if not keep_signin:
            # clear session on browser close
            self.request.session.set_expiry(0)
    
        return HttpResponseRedirect(self.get_success_url())


class SignupView(CreateView):
    """User Sign-up View"""
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

    def get_next_url(self):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        if is_safe_url(redirect_path, request.get_host()):
            return redirect_path
        return self.success_url

    def form_valid(self, form, *args, **kwargs):
        form.save()
        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        password1 = form.cleaned_data['password1']
        user = authenticate(self.request, email=email, username=username, password=password1)

        login(self.request, user)
        messages.success(self.request, 'You have signed up successfully')
        # url = reverse_lazy('home')
        url = self.get_next_url()
        return HttpResponseRedirect(url)  

    # def form_invalid(self, form):
    #     """If the form is invalid, render the invalid form."""
    #     print(form)
    #     return self.render_to_response(self.get_context_data(form=form))
        

        next_path = self.get_next_url()
        
        return HttpResponseRedirect(next_path)
        # return CreateView.form_valid(self, form, *args, **kwargs)


class CustomLogoutView(LogoutView):
    """User Logout View"""
    pass


class ConfirmLogoutView(TemplateView):
    """User Logout View"""
    template_name = 'logout_confirm.html'


class AllProfiles(LoginRequiredMixin, ListView):

    template_name = 'profile_list.html'
    model = Profile
    paginate_by = 3


class ProfileDetail(LoginRequiredMixin, DetailView):

    template_name = 'profile_detail.html'
    model = Profile


class UpdateProfile(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Profile
    fields = ('profile_image', 'name', 'website', 'bio',)
    template_name = 'profile_form.html'
    success_url = reverse_lazy('all-profiles')
    success_message = "Profile was updated successfully"

    # def get_object(self, queryset=None):
    #     """
    #     Return the object the view is displaying.

    #     Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
    #     Subclasses can override this to return any object.
    #     """
    #     print('get object view called')
    #     curruent_object = UpdateView.get_object(self, queryset=None)
    #     if not curruent_object.user == self.request.user:
    #         messages.warning(self.request, 'You do not have permission')
    #         # raise PermissionDenied('You dont have permistion')
    #         return HttpResponseRedirect(self.success_url)
    #     # print(curruent_object.pk)
    #     return  curruent_object

    def dispatch(self, request, *args, **kwargs):
        print('dispatch hi deside karta hai k  kaha jana hai like get ya post ya put ya wahtever')
        obj = self.get_object()
        if not obj.user == self.request.user:
            messages.warning(self.request, 'You do not have permission')
            return HttpResponseRedirect(self.success_url)
        return UpdateView.dispatch(self, request, *args, **kwargs)

class DeleteProfile(DeleteView):

    model = Profile
    fields = '__all__'
    template_name = 'profile_del.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        print('dispatch hi deside karta hai k  kaha jana hai like get ya post ya put ya wahtever')
        obj = self.get_object()
        if not obj.user == self.request.user:
            messages.warning(self.request, 'You do not have permission')
            return HttpResponseRedirect(self.success_url)
        return UpdateView.dispatch(self, request, *args, **kwargs)
