from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
# Create your views here.


class IndexPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class RegisterPageView(TemplateView, generic.FormView):
    form_class = UserCreationForm
    template_name = "registration.html"
    success_url = "/"



    def get(self, request, **kwargs):
        the_form = UserCreationForm()

        return render(request, self.template_name, context={"form": the_form})

    def post(self, request, *args, **kwargs):
        the_form = UserCreationForm(data=request.POST)
        if the_form.is_valid():
            u = the_form.save()
            u.save()
            return redirect('index')
        else:
            return render(request, self.template_name, context={"form": the_form})
