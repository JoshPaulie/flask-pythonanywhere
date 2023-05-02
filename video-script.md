Hi! Today we'll discuss getting your simple Flask webapp onto PythonAnywhere

Difficulty: Easy - Intermediate

# What is PythonAnywhere?
- PythonAnywhere is a web-based Python development environment
- It offers an easy way for you to host many kinds of Python webapps
- Today we'll be utilizing their free (or "beginner") tier

# Requirements for this tutorial
- a basic understanding of
  - bash
  - git cli
  - tracking your repo with, cloning, and pulling from, GitHub
- an email-verified PythonAnywhere account
- a functional Flask app
  - <512mb in size
  - published to a public GitHub repo

# The small limitation of accessing your environment with the free tier
- To interact with your remote environment as a "virtual beginner," we must log into a virtual terminal from within your web browser
- From there, we can clone our webapp to "deploy" our files onto the server
- This is also how we will updating our web app

If your web app is greater than 512mb, or would require frequent updates, consider upgrading to the **Hacker** tier. This grants you SSH access, a much easier and flexible way to interact with your server.

# Understanding your web app
Before we create your web app on PyAny, we need to note a couple of things about your app structure

1. What is the name of your app script? Eg. `app.py`
2. What is the name of the instance you gave your app? Eg. `app`
3. What's the name of the repo tracking your app? Eg. `countdown-app`

# Creating your app on PythonAnywhere
1. Open the **web** tab
2. Click **create new web app**
3. Skip OR `/home/{username}/{repo_name}`
4. Visit your default app

# Cloning your app onto PyAny
1. Open the **consoles** tab
2. Start a new **bash** console
3. `git clone {repo_url}`
4. `rm -rf mysite ` (*optional*)

# Configure PyAny to serve your app
- Right now, the your PyAny page is still serving the default `mysite` it generated
- We need to make a couple of changes to configure our PyAny app to have it point to and serve the web app you cloned

1. Change the **source folder** path
2. Open the **WSGI** config Python file
3. Correct lines **11** & **TBD**
4. Save, reload app