from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.filter
def highlight_search(text, search):
    highlighted = text.replace(search, '<span class="highlight">{}</span>'.format(search))
    # highlighted = re.sub(search, '<span class="highlight">{}</span>'.format(search), text, re.IGNORECASE)

    return mark_safe(highlighted)


# <h2><a class="article-title" href="{% url 'post-detail' post.slug %}">{{ post.title|highlight_search:query }}</a></h2>
# <p class="card-text">{{post.content|slice:":200"|highlight_search:query}}</p>
