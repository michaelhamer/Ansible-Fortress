from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import PlaybookForm, UserForm
from .models import Playbook

def index(request):
    return render(request, 'playbooks/index.html')

def playbooks(request):
    if not request.user.is_authenticated():
        return render(request, 'playbooks/login.html')
    else:
        playbooks = Playbook.objects.all() #TODO: filter by user
        #playbooks = Playbook.objects.filter(user=request.user)
        # query = request.GET.get("q")
        # if query:
        #     albums = albums.filter(
        #         Q(album_title__icontains=query) |
        #         Q(artist__icontains=query)
        #     ).distinct()
        #     song_results = song_results.filter(
        #         Q(song_title__icontains=query)
        #     ).distinct()
        #     return render(request, 'playbooks/index.html', {
        #         'albums': albums,
        #         'songs': song_results,
        #     })
        return render(request, 'playbooks/playbooks.html', {'playbooks': playbooks})


def create_playbook(request):
    if not request.user.is_authenticated():
        return render(request, 'playbooks/login.html')
    else:
        form = PlaybookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            playbook = form.save(commit=True)
            #playbook.playbook_text = request.
            # file_type = album.album_logo.url.split('.')[-1]
            # file_type = file_type.lower()
            # if file_type not in IMAGE_FILE_TYPES:
            #     context = {
            #         'album': album,
            #         'form': form,
            #         'error_message': 'Image file must be PNG, JPG, or JPEG',
            #     }
            #     return render(request, 'playbooks/create_playbook.html', context)
            # playbook.save()
            return render(request, 'playbooks/detail.html', {'playbook': playbook})
        context = {
            "form": form,
        }
        return render(request, 'playbooks/create_playbook.html', context)

def delete_playbook(request, playbook_id):
    #TODO: are you sure messagebox for user
    playbook = Playbook.objects.get(pk=playbook_id)
    playbook.delete()
    #playbooks = Playbook.objects.filter(user=request.user)
    playbooks = Playbook.objects.all() #TODO: filter by user
    return render(request, 'playbooks/playbooks.html', {'playbooks': playbooks})


def detail(request, playbook_id):
    if not request.user.is_authenticated():
        return render(request, 'playbooks/login.html')
    else:
        user = request.user
        playbook = get_object_or_404(Playbook, pk=playbook_id)
        return render(request, 'playbooks/detail.html', {'playbook': playbook, 'user': user})


def unsynced(request, host_id):
    # song = get_object_or_404(Song, pk=song_id)
    # try:
    #     if song.is_favorite:
    #         song.is_favorite = False
    #     else:
    #         song.is_favorite = True
    #     song.save()
    # except (KeyError, Song.DoesNotExist):
    #     return JsonResponse({'success': False})
    # else:
        return JsonResponse({'success': True})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'playbooks/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # albums = Album.objects.filter(user=request.user)
                # context = {'albums': albums}
                return render(request, 'playbooks/index.html')
            else:
                return render(request, 'playbooks/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'playbooks/login.html', {'error_message': 'Invalid login'})
    return render(request, 'playbooks/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # albums = Album.objects.filter(user=request.user)
                # context = {'albums': albums}
                return render(request, 'playbooks/index.html')
    context = {
        "form": form,
    }
    return render(request, 'playbooks/login.html', context) #TODO: edit for admin


def hosts(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'playbooks/login.html')
    else:
        # try:
        #     song_ids = []
        #     for album in Album.objects.filter(user=request.user):
        #         for song in album.song_set.all():
        #             song_ids.append(song.pk)
        #     users_songs = Song.objects.filter(pk__in=song_ids)
        #     if filter_by == 'favorites':
        #         users_songs = users_songs.filter(is_favorite=True)
        # except Album.DoesNotExist:
        #     users_songs = []
        # context = {'song_list': users_songs, 'filter_by': filter_by,}
        return render(request, 'playbooks/hosts.html')


