# Work experience

{% for experience in experiences -%}
	- {{experience.start}} {{experience.end}} {{experience.title}};
{% endfor %}
