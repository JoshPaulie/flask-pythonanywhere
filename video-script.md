# Getting your flask app on the internet with PythonAnywhere

## assumptions
- have a flask app, ready to deploy
  - the app should be simple
- understand git and tracking a repo on github
- basic understanding of bash

## what is PythonAnywhere?
- PythonAnywhere is a Python env in the cloud
- It's capable of hosting pretty much any Python web app you can think of
- There's predefined configs for Flask, Django, Bottle, & web2py, which we'll be using today

### $$$
- Free tier
  - 1 web app
  - Predefined domain
  - 512mb storage
  - Console for you to interact with your env
- Hacker tier
  - 1 web app
  - $5/month
  - Custom domain
  - 1gb storage
  - SSH access to your env
  - Higher traffic capacity
- Web Developer
  - $12/month
  - 2 web apps
  - 5gb storage
  - even higher traffic capacity

This tutorial will use the free tier, and will demonstrate how to easily get your app onto PythonAnywhere

## tutorial
1. Create your PythonAnywhere account
   1. verify your email
   2. if you have already created your first app and would like to deleted it to start over, follow the steps on screen
2. Create your app
   1. We'll use the flask preset
3. 