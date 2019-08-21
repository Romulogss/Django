from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
)
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

    return render(request, 'clientes/person_delete_confirm.html', {'person': person})


class PersonList(ListView):
    model = Person


class PersonDetail(DetailView):
    model = Person