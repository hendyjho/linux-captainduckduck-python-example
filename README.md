# linux-captainduckduck-python-example
Setting up Digital Ocean Docker instance with Captain Duck Duck App installer. (Heroku similar app management)
Repository contains Python - Flask based working example app with "Captain Duck Duck" setting file.

After starting instance, npm and node should be installed. (apt install npm & node)

	curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
	sudo apt-get install -y nodejs
	sudo apt-get install npm


Captain setup
	https://github.com/githubsaturn/captainduckduck
	https://github.com/githubsaturn/captainduckduck/wiki/Getting-Started


<b>To set up domain:</b>

	In your domain registrar (and Digital Ocean (etc...) domain settings also) settings there should be 2 records;
	A Record - subdomain - ip
	A Record - *.subdomain - ip

Other details on setting custom domain
	
	https://github.com/githubsaturn/captainduckduck/issues/138


Application <b>deployment</b> methods are described here:

	https://github.com/githubsaturn/captainduckduck/wiki/Deployment-Methods


<b>Other settings</b> needs to attension:

To start application with <u>gunicorn</u> "captain-definition" file should be used (default).

  	"CMD gunicorn --bind 0.0.0.0:80 wsgi:fapp"

To start application with <u>Flask web server</u> "captain-definition.1" should be used (after renaming file to captain-definition)

	"ENTRYPOINT [\"python\"]",
	"CMD [\"app.py\"]",	

<u>No need to change port settings.</u> Captain expects default Docker container port as 80.
If it is necessery to change (app exposed on different port over Docer) Nginx settings should be arranged as well in Captain application app settings as follows

	set $upstream http://<%-s.localDomain%>:8080;
	

Other things to consider:

-There is no gracefull reload or Blue/Green deployment option.
