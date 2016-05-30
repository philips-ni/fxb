from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from . import services
from . import forms

class SignInAndSignUp(generic.edit.FormMixin, generic.TemplateView):

    signin_form_class = forms.LoginForm
    signup_form_class = forms.SignupForm

    def get(self, request, *args, **kwargs):
        kwargs["form"] = 1
        if "signin_form" not in kwargs:
            kwargs["signin_form"] = self.signin_form_class()
        if "signup_form" not in kwargs:
            kwargs["signup_form"] = self.signup_form_class()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'sign_in' in request.POST:
            form = self.signin_form_class(**self.get_form_kwargs())
            if not form.is_valid():
                messages.add_message(request,
                                     messages.ERROR,
                                     "Unable login! "
                                     "Check username/password")
                return super().get(request,
                                   signup_form=self.signup_form_class(),
                                   signin_form=form)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(self.request, user)
            else:
                messages.add_message(request, messages.ERROR,
                                     "Unable to find given username!")
        if 'sign_up' in request.POST:
            form = self.signup_form_class(**self.get_form_kwargs())
            if not form.is_valid():
                messages.add_message(request,
                                     messages.ERROR,
                                     "Unable to register! "
                                     "Please retype the details")
                return super().get(request,
                                   signin_form=self.signin_form_class(),
                                   signup_form=form)
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            messages.add_message(request,
                                 messages.INFO,
                                 "{0} added sucessfully".format(
                                     username))
            # Login automatically
            user = authenticate(username=username, password=password)
            login(self.request, user)
        return redirect("home")


class LogoutView(generic.RedirectView):
    url = reverse_lazy("home")
    query_string = True
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            messages.add_message(self.request, messages.INFO,
                                 "Logout successful!")
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class AboutView(generic.TemplateView):
    template_name = "about.html"

class MyProjectsView(generic.TemplateView):
    form_class = forms.CompanyDetailsForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context["my_products"] = services.get_my_products(
                self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        kwargs["create_company_form"] = self.form_class()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class()
        if not form.is_valid():
            messages.add_message(request,
                                 messages.ERROR,
                                 "Failed to create project! "
                                 "Please check input")
            
            return super().get(request,
                               form=form)

        company_name = request.POST.get("company_name")
        company_description = request.POST.get("company_description")

        company_doc = { 'company_name': company_name,
                        'company_description': company_description}
        services.add_company(company_doc)
        messages.add_message(request,
                                 messages.INFO,
                                 "{0} added sucessfully".format(
                                     company_name))
        return redirect('/my_projects') # Redirect after POST
           

           