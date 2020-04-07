# from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static
from django.urls import reverse

from jinja2 import Environment


print("===============",static)
print(reversed)


def environment(**options):
    env = Environment(**options)
    print("===============",env)
    env.globals.update({
        'static': static,
        'url': reverse,
    })
    return env


