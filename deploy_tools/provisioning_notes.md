## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:
	sudo apt-get install nginx git python3 python3-pip
	sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, beerbelly.ninja

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, beerbelly.ninja

## Folder structure:
Assume we have a user account at /home/username

/home/username
	- sites
		- SITENAME/source
			- database
			- app-folder
			- static
			- virtualenv

## I made a mistake with the application directory structure
## Ideally, SITENAME/source should be SITENAME
## and app-folder should be source