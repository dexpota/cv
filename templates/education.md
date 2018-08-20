# Academic degrees
{% for degree in degrees -%}
	- {{degree.graduated_with}} {{degree.graduated_from}} {{degree.graduated_in}}
{% endfor %}  
