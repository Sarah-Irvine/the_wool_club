from django import template

register = template.Library()


@register.filter
def is_attending(user, workshop):
    return user.profile.attending.filter(id=workshop.id).exists()

