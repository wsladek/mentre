# mentre

to run this locally and test your work, you'll need python 3.6, and the latest vers of django.

you'll also need to open mentre/mentre/settings.py and put anything in for SECRET_KEY = ''

So: SECRET_KEY = '' ---> SECRET_KEY = 'anything'

in the top level 'mentre/' directory, run 'python manage.py runserver' and visit the address shown to view the current state of things

The CSS for the landing page lives in mentre/static/styles.css
The HTML for the landing page lives in mentre/landing/templates/landing/index.html
