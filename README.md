Cloud_Assignment1
===================

Problem Statement
------------------

- Developing Web-based application that runs on EC2 instance that takes processes a user input and gives result.


Built
-------------------
- Web Application that produces *Factors for a given Number*.


I followed the below steps :

Step 1 - Launch EC2 instance
-----------------------------

- I followed the steps mentioned here: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html
- I chose Ubuntu instance.
- Added a couple of security groups to enable traffic to my web application.

  ![image](../master/Security_Groups.PNG)

Step 2 - Developed the Modules and code 
------------------------------------------

- **Functionality** : Produce the factors of the Number provided by the user.

- **My Project Structure**:
	- flaskapp.py :: My Python code
	- templates
		- layout.html   :: My standard html files inherited across all the pages
		- my-form.html  :: html form handling the user input 
	- static
		- stylesheet.css:: Standard style sheet across all pages.
		
- **Using the Web Application** : Just enter the number and get the factors ! Simple!! :+1:

Step 3 - Enabled wsgi server behind Apache 
------------------------------------------ 		

- I followed the steps mentioned here: https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/.

References 
-------------
- I referred this link : https://aryaboudaie.com/python/technical/educational/web/flask/2018/10/17/flask.html while building the application.