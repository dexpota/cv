# Programming Languages
{% for language in technical_skills.programming_languages -%}
	- {{language}}
{% endfor %}

# Markup Languages
{% for language in technical_skills.markup_languages -%}
	- {{language}}
{% endfor %}

{% for other in others %}
# {{other.title}}
{% for item in technical_skills.other["items"] -%}
	- {{item}}
{% endfor %}
{% endfor %}
