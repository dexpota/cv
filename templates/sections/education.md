# Academic degrees
{% for degree in education.degrees -%}
	- {{degree.graduated_with}} {{degree.graduated_from}} {{degree.graduated_in}}
{% endfor %}  
