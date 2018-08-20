# Programming Languages
{% for language in programming_languages -%}
	- {{language}}
{% endfor %}

# Markup Languages
{% for language in markup_languages -%}
	- {{language}}
{% endfor %}

{% for other in others %}
# {{other.title}}
{% for item in other["items"] -%}
	- {{item}}
{% endfor %}
{% endfor %}
