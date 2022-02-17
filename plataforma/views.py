import django
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django import forms
from django.utils import timezone

from .models import Album, Musica
from .forms import NovoAlbumForm, NovaMusicaForm

# Create your views here.


@login_required(login_url='/auth/login')
def home(request):
    # Mostrar todos os álbuns em ordem cronológica de upload
    albuns = Album.objects.all()
    return render(request, 'home.html', {'albuns': albuns})


@login_required(login_url='/auth/login')
def detalhe_perfil(request, username):
    # Mostrar todos os álbuns do artista
    albuns = get_object_or_404(User, username=username)
    albuns = albuns.albuns.all()
    return render(request, 'informacao_artista.html', {'albuns': albuns, 'username': username})


@login_required(login_url='/auth/login')
def adicionar_album(request, username):
    user = get_object_or_404(User, username=username)
    # Somente o usuário conectado no momento pode adicionar o álbum, senão será redirecionado para a página inicial.
    if user == request.user:
        if request.method == 'POST':
            form = NovoAlbumForm(request.POST, request.FILES)
            if form.is_valid():
                album = Album.objects.create(
                    logo_album = form.cleaned_data.get('logo_album'),
                    nome_album = form.cleaned_data.get('nome_album'),
                    genero_album = form.cleaned_data.get('genero_album'),
                    carregado_em = timezone.now(),
                    artista_album = request.user
                )
                return redirect('plataforma:detalhe_perfil', username=request.user)
        else:
            form = NovoAlbumForm()
        return render(request, 'criar_novo_album.html', {'form': form})
    else:
        return redirect('plataforma:detalhe_perfil', username=user)


@login_required(login_url='/auth/login')
def detalhe_album(request, username, album):
    # Mostre os detalhes do álbum aqui. detalhes do único álbum.
    album = get_object_or_404(Album, nome_album=album)
    musicas = get_object_or_404(User, username=username)
    musicas = musicas.albuns.get(nome_album=str(album))
    musicas = musicas.musicas.all()
    return render(request, 'informacao_album.html', {'musicas': musicas, 'album': album, 'username': username})
