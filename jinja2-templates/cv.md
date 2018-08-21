---
title: Curriculum Vitae
author: Destro Fabrizio
colorlinks: True
---

# About

### Contacts

[destro.fabrizio@gmail.com](destro.fabrizio@gmail.com) --- [https://www.destro.me](https://www.destro.me) --- [https://github.com/dexpota](https://github.com/dexpota) --- [https://www.linkedin.com/in/fdestro/](https://www.linkedin.com/in/fdestro/)

# Skills
##  General skills

### Languages
{% for language in general_skills.languages -%}
	{{language}},
{% endfor %}

## Technical skills
### Programming languages
{% for language in technical_skills.programming_languages -%}
	{{language}},
{% endfor %}

### Markup languages
{% for language in technical_skills.markup_languages -%}
	{{language}},
{% endfor %}

{% for other in technical_skills.others %}
### {{other.title}}
{% for item in other["items"] -%}
	{{item}},
{% endfor %}
{% endfor %}

# Education

## Academic degrees
{% for degree in education.degrees -%}
	- {{degree.graduated_with}} {{degree.graduated_from}} {{degree.graduated_in}}
{% endfor %}

# Work experience

{% for experience in work_experience.experiences -%}
	- {{experience.start}} {{experience.end}} {{experience.title}};
{% endfor %}
