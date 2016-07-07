# [redr](http://redr-0613.appspot.com/)
A project from Udacity's Full Stack Web Developer Nanodegree Program

#### Project Description
In this project you will be building a multi user blog(along the lines of Medium) where users can sign in and post blog posts as well as 'Like' and 'Comment' on other posts made on the blog. You will be hosting this blog on Google App Engine (GAE) and you will also be creating an authentication system for users to be able to register and sign in and then create blog posts!

#### Running the App Locally
###### Pre-requisites
* Install the GAE for Python SDK [here](https://cloud.google.com/appengine/downloads)
* Sign up for a GAE account ([instructions](https://sites.google.com/site/gdevelopercodelabs/app-engine/creating-your-app-engine-account))
* Clone the repo with ```git clone https://github.com/sharynneazhar/full-stack-webdev-nanodegree.git```
* ```cd P3-Blog``` into the blog directory

You may run the app in several ways:
* You can use the GAE launcher to run the app
 * Add the app as an existing project
 * Hit the ```Run``` button
 * View the blog site through your localhost
* If you are on a Windows OS:
 * Run ``` .\rundev.bat \path\to\P3-Blog ```
 * Note: This assumes that your GAE is installed under Program Files (x86)
* If you are on a Mac OS:
 * Run ``` dev_appserver.py \path\to\P3-Blog ```
 * Note: This assumes that you have created a symlink during the GAE installation

#### Deploying the App
You may deploy the app in several ways:
* You can use the GAE launcher to deploy the app
 * Hit the ```Deploy``` button
 * View the blog site on APP_NAME.appspot.com
* If you are on a Windows OS:
 * Run ``` .\deploy.bat \path\to\P3-Blog ```
 * Note: This assumes that your GAE is installed under Program Files (x86)
* If you are on a Mac OS:
 * Run ``` appcfg.py update \path\to\P3-Blog ```
 * Note: This assumes that you have created a symlink during the GAE installation
