from iommi import (
    Page,
    html,
    Table,
    Column,
    Form,
)
from .models import Actor, Movie, Director, Country, Category
from django.shortcuts import get_object_or_404
from django.utils.html import format_html


class ActorTable(Table):
    name = Column(
        cell__value=lambda row, **_: f"{row.last_name} {row.first_name}",
    )
    date_of_birth = Column()
    date_of_death = Column()
    csfd_url = Column(
        cell__url=lambda row, **_: row.csfd_url,
        cell__url_title="go to csfd.cz",
    )
    imdb_url = Column(
        cell__url=lambda row, **_: row.imdb_url,
        cell__url_title="go to imdb.com",
    )
    countries = Column()

    class Meta:
        title = "Actors"
        rows = Actor.objects.all()

    # def get_absolute(self):
    #     breakpoint()
    #     return f"/actors/{self}/"


def edit_movie(request, actor, movie):
    movie = get_object_or_404(movie, name=movie, artist__name=actor)
    return Form.edit(auto__instance=movie)


def delete_movie(request, actor, movie):
    movie = get_object_or_404(movie, name=movie, artist__name=actor)
    return Form.delete(auto__instance=movie)


def actors_page(request, id):
    actor = get_object_or_404(Actor, id=id)

    class ActorPage(Page):
        title = html.h1(actor.name)

        movies = Table(
            auto__rows=Movie.objects.filter(actors=actor),
            # columns__title__cell__url=lambda row, **_: row.get_absolute(),
            # columns__edit=Column.edit(),
            # columns__delete=Column.delete(),
        )

    return ActorPage()


class DirectorTable(Table):
    name = Column(
        cell__value=lambda row, **_: f"{row.last_name} {row.first_name}",
    )
    date_of_birth = Column()
    date_of_death = Column()
    csfd_url = Column(
        cell__url=lambda row, **_: row.csfd_url,
        cell__url_title="go to csfd.cz",
    )
    imdb_url = Column(
        cell__url=lambda row, **_: row.imdb_url,
        cell__url_title="go to imdb.com",
    )
    countries = Column()

    class Meta:
        title = "Directors"
        rows = Director.objects.all()


class MoviesTable(Table):
    title = Column()
    year = Column()
    duration = Column()
    csfd_url = Column(
        cell__url=lambda row, **_: row.csfd_url,
        cell__url_title="go to csfd.cz",
    )
    imdb_url = Column(
        cell__url=lambda row, **_: row.imdb_url,
        cell__url_title="go to imdb.com",
    )
    categories = Column()
    actors = Column()
    directors = Column()
    countries = Column()

    class Meta:
        title = "Movies"
        rows = Movie.objects.all()


class HomePage(Page):
    title = html.h1("TMDB")
    welcome_text = "Welcome to my TMDB site..."

    actors = ActorTable(
        page_size=5,
        # columns__name__cell__format=lambda value, **_: format_html(f'<a href="/actors/{value}/">{value}</a?'),
        # columns__name__cell__url=lambda value, **_: value.get_absolute(),
    )
    directors = DirectorTable(page_size=5)
    movies = MoviesTable(page_size=5)


# def home_view(request):
#     class MyPage(Page):
#         title = html.h1('TMDB')
#         body_text = 'Welcome to my TMDB site...'
#         actors = Table(
#             auto__model=Actor,
#             columns__name=Column(
#                 cell__value=lambda row, **_: f"{row.last_name} {row.first_name}",
#             ),
#             columns__date_of_birth__after='name',
#             columns__last_name__filter__include=True,
#             columns__created__include=False,
#             columns__modified__include=False,
#             columns__first_name__include=False,
#             columns__last_name__include=False,
#             columns__csfd_url=Column(
#                 cell__url=lambda row, **_: row.csfd_url,
#                 cell__url_title='go to csfd.cz',
#             ),
#         )
#         movies = Table(
#             auto__model=Movie,
#             columns__created__include=False,
#             columns__modified__include=False,
#             columns__csfd_url=Column(
#                 cell__url=lambda row, **_: row.csfd_url,
#                 cell__url_title='go to csfd.cz',
#             ),
#         )
#         directors = Table(
#             auto__model=Director,
#             columns__name=Column(
#                 cell__value=lambda row, **_: f"{row.last_name} {row.first_name}",
#             ),
#             columns__date_of_birth__after='name',
#             columns__last_name__filter__include=True,
#             columns__created__include=False,
#             columns__modified__include=False,
#             columns__first_name__include=False,
#             columns__last_name__include=False,
#             columns__csfd_url=Column(
#                 cell__url=lambda row, **_: row.csfd_url,
#                 cell__url_title='go to csfd.cz',
#             ),
#         )
#         countries = Table(
#             auto__model=Country,
#             columns__created__include=False,
#             columns__modified__include=False,
#         )
#         categories = Table(
#             auto__model=Category,
#             columns__created__include=False,
#             columns__modified__include=False,
#         )

#     return MyPage()
