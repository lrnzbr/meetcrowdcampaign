# KickStarter
Voting Website for Y2 Yearlong Group Projects

## Running Locally:

### Required Packages
All of the packages for this website can be installed using the pip installer.  

<ul>
<li>pandas(for database populating)
<li>flask</li>
<li>Flask-HTTPAuth
<li>Jinja2
<li>passlib
<li>python-dateutil
<li>requests
<li>SQLAlchemy
<li>psycopg2
<li>validate_email
<li>flask_mail
<li>flask_oauthlib
<li>pyDNS</li> 
</ul>


1.  fill in the values of secrets.json with your own credentials.

2. run python initializeDB.py
3. comment out lines 23 and 24 if you are using Python 3.

4.  in webapp.py toggle the comments on line 171 and line 172

5. run python webapp.py 

hopefully it should run on localhost:5000 without any problems.

Important files:  all html in templates folder all templates inherit from layout.html , all css files in static folder,

Ping me if you run into any problems.