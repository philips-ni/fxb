from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from . import services

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline navbar-form pull-right'
        self.helper.form_id = 'signin-form'
        self.helper.form_show_labels = False
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            Field('username', placeholder="Username", autofocus=""),
            Field('password', placeholder="Password"),
            Submit('sign_in', 'Sign in', css_class="btn-sm btn-success"),
            )


class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'signup-form'
        #self.helper.form_class = 'form-inline navbar-form pull-right'
        self.helper.form_show_labels = False
        self.helper.form_show_errors = False
        self.helper.help_text_inline = False
        self.helper.layout = Layout(
            Field('username', placeholder="Username"),
            Field('password1', placeholder="Password"),
            Field('password2', placeholder="Re-type Password"),
            Submit('sign_up', 'Sign up', css_class="btn-warning"),
            )

class CompanyDetailsForm(forms.Form):
    company_name = forms.CharField(max_length=100)
    company_description = forms.CharField(max_length=100)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_show_errors = False
        self.helper.help_text_inline = False
        self.helper.form_id = 'create_company_form'    
        self.helper.layout = Layout(
            Field('company_name', placeholder="Company Name"),
            Field('company_description', placeholder="Company Description"),
            Submit('create', 'Create', css_class="btn-warning"),
            )
        
    def is_valid(self):
        return True
