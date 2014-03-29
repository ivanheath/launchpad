from django import template

register = template.Library()

def include_external(url):
    import urllib2
    return urllib2.urlopen(url).read()

register.simple_tag(include_external)

