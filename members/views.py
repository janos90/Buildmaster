from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from members.forms import RepForm, PasswordChangingForm, EditUserForm, SignUpForm, SupplierForm
from members.models import Rep, Supplier
from submissionform.models import Job


class CreateUserView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/sign-up.html'
    success_url = reverse_lazy('login')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class EditUserView(UpdateView):
    form_class = EditUserForm
    template_name = 'registration/edit-settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


class CreateRepView(CreateView):
    model = Rep
    form_class = RepForm
    template_name = 'create-rep.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateSupplierView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'create-supplier.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DisplayRepView(DetailView):
    model = Rep
    template_name = 'rep-profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Rep.objects.all()
        context = super(DisplayRepView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Rep, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


class DisplaySupplierView(DetailView):
    model = Supplier
    template_name = 'supplier-profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Rep.objects.all()
        context = super(DisplaySupplierView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Supplier, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


class EditRepView(UpdateView):
    model = Rep
    template_name = 'edit_rep_page.html'
    fields = ['image', 'bio', 'phone']
    success_url = reverse_lazy('home')


class EditSupplierView(UpdateView):
    model = Supplier
    template_name = 'edit_supplier_page.html'
    fields = ['image', 'bio', 'phone']
    success_url = reverse_lazy('home')
