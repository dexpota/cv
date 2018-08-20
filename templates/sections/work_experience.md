# Work experience

{% for experience in work_experience.experiences -%}
	- {{experience.start}} {{experience.end}} {{experience.title}};
{% endfor %}
