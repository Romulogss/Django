from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Person
from .forms import PersonForm


@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'clientes/person_list.html', {'persons': persons})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'clientes/person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'clientes/person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'clientes/person_confirm_delete.html', {'person': person})


class PersonList(ListView):
    model = Person


class PersonDetail(DetailView):
    model = Person

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['agora'] = timezone.now()
    #     return context


class PersonCreate(CreateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person_list')


class PersonUpdate(UpdateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person_list')
    template_name = 'clientes/person_form.html'


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('person_list')
