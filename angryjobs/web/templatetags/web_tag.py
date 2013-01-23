# -*- encoding: utf-8 -*-

from django.core.urlresolvers import reverse
from django import template


register = template.Library()


@register.tag('match_url')
def do_match_url(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, page_url, _as_, var_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument"\
            % token.contents.split()[0])
    if not (page_url[0] == page_url[-1] and page_url[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be\
            in quotes" % tag_name)
    return MatchUrl(page_url[1:-1], var_name)


class MatchUrl(template.Node):

    def __init__(self, page_url, var_name):
        self.page_url = page_url
        self.var_name = var_name

    def render(self, context):
        request = context['request']
        if self.page_url == 'web.offer.detail':
            if 'offers' in request.path:
                context[self.var_name] = True
        elif self.page_url == 'web.index':
            context[self.var_name] = reverse(self.page_url) == request.path
        return ''
