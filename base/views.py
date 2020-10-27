from django.shortcuts import get_object_or_404
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from iommi import Column, Form, Page, Table, html

from .models import Actor, Category, Country, Director, Movie


#  We had these arguments: page, traversable, request, table, cells, row, column
# class ActorTable(Table):
#     name = Column(
#         cell__value=lambda row, **_: f"{row.last_name} {row.first_name}",
#     )
#     date_of_birth = Column()
#     date_of_death = Column()
#     csfd_url = Column(
#         cell__url=lambda row, **_: row.csfd_url,
#         cell__url_title="go to csfd.cz",
#     )
#     imdb_url = Column(
#         cell__url=lambda row, **_: row.imdb_url,
#         cell__url_title="go to imdb.com",
#     )
#     countries = Column()

#     class Meta:
#         title = "Actors"
#         rows = Actor.objects.all()

# def get_absolute(self):
#     breakpoint()
#     return f"/actors/{self}/"


# def edit_movie(request, actor, movie):
#     movie = get_object_or_404(movie, name=movie, artist__name=actor)
#     return Form.edit(auto__instance=movie)


# def delete_movie(request, actor, movie):
#     movie = get_object_or_404(movie, name=movie, artist__name=actor)
#     return Form.delete(auto__instance=movie)


# def actors_page(request, id):
#     actor = get_object_or_404(Actor, id=id)

#     class ActorPage(Page):
#         title = html.h1(actor.name)

#         movies = Table(
#             auto__rows=Movie.objects.filter(actors=actor),
# columns__title__cell__url=lambda row, **_: row.get_absolute(),
# columns__edit=Column.edit(),
# columns__delete=Column.delete(),
#         )

#     return ActorPage()


# class DirectorTable(Table):
#     name = Column(
#         cell__value=lambda row, **_: f"{row.last_name} {row.first_name}",
#     )
#     date_of_birth = Column()
#     date_of_death = Column()
#     csfd_url = Column(
#         cell__url=lambda row, **_: row.csfd_url,
#         cell__url_title="go to csfd.cz",
#     )
#     imdb_url = Column(
#         cell__url=lambda row, **_: row.imdb_url,
#         cell__url_title="go to imdb.com",
#     )
#     countries = Column()

#     class Meta:
#         title = "Directors"
#         rows = Director.objects.all()


# class MoviesTable(Table):
#     title = Column()
#     year = Column()
#     duration = Column()
#     csfd_url = Column(
#         cell__url=lambda row, **_: row.csfd_url,
#         cell__url_title="go to csfd.cz",
#     )
#     imdb_url = Column(
#         cell__url=lambda row, **_: row.imdb_url,
#         cell__url_title="go to imdb.com",
#     )
#     categories = Column()
#     actors = Column()
#     directors = Column()
#     countries = Column()

#     class Meta:
#         title = "Movies"
#         rows = Movie.objects.all()


# class HomePage(Page):
#     title = html.h1("TMDB")
#     welcome_text = "Welcome to my TMDB site..."

#     actors = ActorTable(
#         page_size=5,
# columns__name__cell__format=lambda value, **_: format_html(f'<a href="/actors/{value}/">{value}</a?'),
# columns__name__cell__url=lambda value, **_: value.get_absolute(),
# )
# directors = DirectorTable(page_size=5)
# movies = MoviesTable(page_size=5)


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
# -------------------------------------------------------------------
#  We had these arguments: page, traversable, request, table, cells, row, column
# We had these arguments: row, value, page, traversable, request, table, column
# 'Cell' object has no refinable attribute(s): call_target.
# Available attributes:
#     attrs
#     contents
#     format
#     link
#     tag
#     template
#     url
#     url_title
#     value


class IndexPage(Page):
    title = html.h1("TMDB")
    welcome_text = "Welcome to my TMDB!"

    actors = Table(
        auto__model=Actor,
        page_size=5,
        columns__name=Column(
            cell__value=lambda row, **_: f"{row.last_name} {row.first_name}",
        ),
        columns__created__include=False,
        columns__modified__include=False,
        columns__first_name__include=False,
        columns__last_name__include=False,
        columns__countries__cell__format=lambda row, **_: mark_safe(
            "".join(
                format_html(f'<a href="{country.get_absolute_url()}">{country}</a><br>')
                for country in row.countries.all()
            )
        ),
    )
    movies = Table(
        auto__model=Movie,
        page_size=5,
        columns__created__include=False,
        columns__modified__include=False,
        columns__actors__cell__format=lambda row, **_: mark_safe(
            "".join(
                format_html(f'<a href="{actor.get_absolute_url()}">{actor}</a><br>')
                for actor in row.actors.all()
            )
        ),
        columns__directors__cell__format=lambda row, **_: mark_safe(
            "".join(
                format_html(
                    f'<a href="{director.get_absolute_url()}">{director}</a><br>'
                )
                for director in row.directors.all()
            )
        ),
        columns__countries__cell__format=lambda row, **_: mark_safe(
            "".join(
                format_html(f'<a href="{country.get_absolute_url()}">{country}</a><br>')
                for country in row.countries.all()
            )
        ),
        columns__categories__cell__format=lambda row, **_: mark_safe(
            "".join(
                format_html(
                    f'<a href="{category.get_absolute_url()}">{category}</a><br>'
                )
                for category in row.categories.all()
            )
        ),
    )
    directors = Table(
        auto__model=Director,
        page_size=5,
        columns__name=Column(
            cell__value=lambda row, **_: f"{row.last_name} {row.first_name}",
        ),
        columns__created__include=False,
        columns__modified__include=False,
        columns__first_name__include=False,
        columns__last_name__include=False,
        columns__countries__cell__format=lambda row, **_: mark_safe(
            "".join(
                format_html(f'<a href="{country.get_absolute_url()}">{country}</a><br>')
                for country in row.countries.all()
            )
        ),
    )


def actor_page(request, id):
    actor = get_object_or_404(Actor, id=id)

    class ActorPage(Page):
        title = html.h1(actor.name)

        movies = Table(
            auto__rows=Movie.objects.filter(actors=actor),
            columns__created__include=False,
            columns__modified__include=False,
        )

    return ActorPage()


def director_page(request, id):
    director = get_object_or_404(Director, id=id)

    class DirectorPage(Page):
        title = html.h1(director.name)

        movies = Table(
            auto__rows=Movie.objects.filter(directors=director),
            columns__created__include=False,
            columns__modified__include=False,
        )

    return DirectorPage()


def category_page(request, id):
    category = get_object_or_404(Category, id=id)

    class CategoryPage(Page):
        title = html.h1(category.name)

        movies = Table(
            auto__rows=Movie.objects.filter(categories=category),
            columns__created__include=False,
            columns__modified__include=False,
        )

    return CategoryPage()


def country_page(request, id):
    country = get_object_or_404(Country, id=id)

    class CountryPage(Page):
        title = html.h1(country.name)

        movies = Table(
            auto__rows=Movie.objects.filter(countries=country),
            columns__created__include=False,
            columns__modified__include=False,
        )
        actors = Table(
            auto__rows=Actor.objects.filter(countries=country),
            columns__created__include=False,
            columns__modified__include=False,
        )
        directors = Table(
            auto__rows=Director.objects.filter(countries=country),
            columns__created__include=False,
            columns__modified__include=False,
        )

    return CountryPage()


def movie_page(request, id):
    movie = get_object_or_404(Movie, id=id)

    class MoviePage(Page):
        title = html.h1(movie.name)

        actors = Table(
            auto__rows=Actor.objects.filter(movies=movie),
            columns__created__include=False,
            columns__modified__include=False,
        )
        directors = Table(
            auto__rows=Director.objects.filter(movies=movie),
            columns__created__include=False,
            columns__modified__include=False,
        )

    return MoviePage()
