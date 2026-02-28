
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

# 1. READ (List all notes)
def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

# 2. CREATE (Add a new note)
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

# 3. DELETE (Remove a note)
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})