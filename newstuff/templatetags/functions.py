from django import template
from django.contrib import messages
from django.shortcuts import redirect 

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
def toggle_and_save_theme(context, cuser, request):
    
    if request.method == 'POST':
        cuser.is_dark_theme = not cuser.is_dark_theme
        cuser.save() 

    return context['request'].path