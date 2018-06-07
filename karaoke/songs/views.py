from django.shortcuts import get_object_or_404, render

from .models import Song, Performer

def performer_detail(request, pk):
    performer = get_object_or_404(Performer, pk=pk)
    return render(request, 'songs/performer_detail.html', {'performer': performer})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'songs/song_detail.html', {'song': song})

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})
