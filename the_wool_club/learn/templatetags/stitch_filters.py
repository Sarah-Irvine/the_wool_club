from django import template

register = template.Library()


@register.filter
def is_saved(user, stitch):
    return user.profile.saved.filter(id=stitch.id).exists()


