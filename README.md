# linux-captainduckduck-python-example
DO Docker instance with Captain Duck Duck App installer. (Heroku similar app management)

Python - Flask based working example app with "Captain Duck Duck" setting file.
https://github.com/githubsaturn/captainduckduck

To set up domain:

	In your domain registrar (and Digital Ocean etc...) settings there should be 2 records;
	A Record - subdomain - ip
	A Record - *.subdomain - ip


Application deployment methods are described here:
https://github.com/githubsaturn/captainduckduck/wiki/Deployment-Methods

To start application with gunicorn "captain-definition" file should be used (default).

  	"CMD gunicorn --bind 0.0.0.0:80 wsgi:fapp"

To start application with Flask web server "captain-definition.1" should be used (after renaming file to captain-definition)

	"ENTRYPOINT [\"python\"]",
	"CMD [\"app.py\"]",	
