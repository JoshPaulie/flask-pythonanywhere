# Get your flask app on the internet with PythonAnywhere

## assumptions
- have a flask app, already being tracked on github ready to deploy
  - because we'll be using the free tier, your app should require little maintenance and be smaller than 512mb in total
- understand git and tracking a repo on github
- basic understanding of bash

## what is PythonAnywhere?
- PythonAnywhere is a Python env in the cloud
- It's capable of hosting pretty much any Python web app you can think of
- There's predefined configs for Flask, Django, Bottle, & web2py, which we'll be using today

## tutorial
Let's see where I'll be starting from

1. Create your PythonAnywhere account
   1. verify your email
   2. if you have already created your first app and would like to deleted it to start over, follow the steps on screen
2. Add a new web app to your PythonAnywhere account
   1. We'll use the flask preset
   2. And not change this path just yet
3. Clone your app
4. Edit `WSGI` file
   1. Correct `project_home`
   2. Correct app name
5. Fix `source code` path