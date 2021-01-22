from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class OwnerListView(ListView):
    '''This will simply inherit ListView'''

class OwnerDetailView(DetailView):
    "THis will inherit the Detail View"

class OwnerCreateView(LoginRequiredMixin, CreateView):
    """
        Sub-class of the CreateView to automatically pass the Request to the Form
        and add the owner to the saved object.
        """
    def form_valid(self, form):
        print('form_valid called')
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(OwnerCreateView, self).form_valid(form)

class OwnerUpdateView(LoginRequiredMixin,UpdateView):
    """
        Sub-class the UpdateView to pass the request to the form and limit the
        queryset to the requesting user.
        """
    def get_queryset(self):
        print("Update called get_queryset()")
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerDeleteView(LoginRequiredMixin,DeleteView):

    def get_queryset(self):
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)





# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.form_valid

# https://stackoverflow.com/questions/862522/django-populate-user-id-when-saving-a-model

# https://stackoverflow.com/a/15540149

# https://stackoverflow.com/questions/5531258/example-of-django-class-based-deleteview