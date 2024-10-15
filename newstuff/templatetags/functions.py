from django import template
from django.contrib import messages
from django.shortcuts import redirect 
from django.urls import reverse 
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def send_message(context, message):
    """
    {% send_message "Your message here" %}
    """
    request = context['request']
    messages.success(request, message)
    return ''

@register.simple_tag(takes_context=True)
def dashboardreturn(context):
    """
    {% dashboardreturn %}
    """
    request = context['request']
    return redirect('homeapp:dashboard')

@register.simple_tag(takes_context=True)
def isuserloggedin(context, request, siteon):
    """
    {% isuserloggedin request "site" %}
    """
    if request.user.is_authenticated and siteon == 'welcomepage':
        # User is authenticated, redirect to the dashboard
        url = reverse('homeapp:dashboard')  # Get the dashboard URL
        return mark_safe(f'<a class="redirectcheck" name="gotodashboard" data-url="{url}"></a>')
    elif not request.user.is_authenticated and siteon != 'welcomepage':
        # User is not authenticated, redirect to welcome page
        url = reverse('welcomeapp:welcomepage')  # Get the welcome page URL
        return mark_safe(f'<a class="redirectcheck" name="gowelcomepage" data-url="{url}"></a>')
    else:
        # No redirection needed
        return mark_safe('<a class="redirectcheck" name="allgood"></a>')

@register.simple_tag(takes_context=True)
def toggle_and_save_theme(context, cuser, request):
    """
    {% toggle_and_save_theme cuser request %}
    """
    if request.method == 'POST':
        cuser.is_dark_theme = not cuser.is_dark_theme
        cuser.save() 

    return context['request'].path