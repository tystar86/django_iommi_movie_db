from django.contrib import admin
from .models import Actor, Movie, Director, Category, Country


class ActorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date_of_birth",
        "date_of_death",
        "csfd_url",
        "imdb_url",
        "all_countries",
    )

    search_fields = ("countries",)
    list_filter = (("countries", admin.RelatedOnlyFieldListFilter),)

    def all_countries(self, obj):
        return "\n".join([c.name for c in obj.countries.all()])


admin.site.register(Actor, ActorAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "year",
        "duration",
        "csfd_url",
        "imdb_url",
        "all_countries",
        "all_categories",
        "all_actors",
        "all_directors",
    )
    search_fields = (
        "year",
        "countries",
        "categories",
        "actors__name",
        "directors__name",
    )
    list_filter = (
        ("countries", admin.RelatedOnlyFieldListFilter),
        ("categories", admin.RelatedOnlyFieldListFilter),
        "year",
    )

    def all_countries(self, obj):
        return "\n".join([c.name for c in obj.countries.all()])

    def all_categories(self, obj):
        return "\n".join([c.name for c in obj.categories.all()])

    def all_actors(self, obj):
        return "\n".join([c.name for c in obj.actors.all()])

    def all_directors(self, obj):
        return "\n".join([c.name for c in obj.directors.all()])


admin.site.register(Movie, MovieAdmin)


class DirectorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date_of_birth",
        "date_of_death",
        "csfd_url",
        "imdb_url",
        "all_countries",
    )

    search_fields = ("countries",)
    list_filter = (("countries", admin.RelatedOnlyFieldListFilter),)

    def all_countries(self, obj):
        return "\n".join([c.name for c in obj.countries.all()])


admin.site.register(Director, DirectorAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Category, CategoryAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Country, CountryAdmin)
