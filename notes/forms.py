# notes/forms.py
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your note...', 'rows': 4}),
        }

# notes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_create(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'form': form, 'action': 'Create'})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'form': form, 'action': 'Update'})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
