# Get your simple flask app on the internet with PythonAnywhere

## what is PythonAnywhere?
- PythonAnywhere is a web app hosting service for literally anything Python
- It's capable of hosting pretty much any Python web app you can think of
- & and the popular frameworks have have preconfigs, one of which we'll be using today
- We'll be using their free tier, which gives us 512mb of storage and a virtual console for us to interact with our server through

## assumptions
- have a flask app
- app should be low maintanace and small 
- already being tracked on github ready to deploy
- understand git and tracking a repo on github
- basic understanding of bash

## tutorial
Let's see where I'll be starting from

### Getting your app onto PythonAnywhere
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