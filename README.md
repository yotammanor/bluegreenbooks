# bluegreenbooks
A demo implementation of an Application-based Blue/Green Migration in Django.
This project is the companion of [this talk](https://github.com/yotammanor/bluegreenbooks/blob/master/PyWebIL%20-%20App%20Based%20Blue%20Green%20Migrations%20With%20Django.pptx), although both are
standalone, and each can (hopefully) be understood without the other.

This implementation heavily draws on https://github.com/jazzband/django-hosts, and on
[work done](https://github.com/masschallenge/standards/blob/master/blue_green_transitions.md)
by my team and I at MassChallenge Inc.

Comments, suggestions and spin-offs are more than welcome.

# Blue/Green walkthrough:

## Prerequisites:

- Python 3.6
- Django 2.0
- Project is cloned locally.

## Step 1 - Setup Green App

1. `git checkout step-1`
2. `./manage.py migrate
3. `./manage.py runserver <port>`
4. go to: http://localhost:<port>/books/ - see green app serving initial data.

## Step 2 - Add Routing App.
1. `git checkout step-2`
2. Server restarts (Automatically). see green app still serving, through router app.

## Step 3 - Add Blue App (As copy of Green)
1. `git checkout step-3`
2. `./manage.py migrate blue --fake`
3. Server restarts. See green app still serving, through router app. 
Blue app is exact copy of green, waiting to be changed

## Step 4 - Change Blue App
1. `git checkout step-4` (server restarts)
2. `./manage.py migrate`
3. See project switches to Blue app immediately, by appliying the migration.

## Step 5 - Clean up
1. `./manage.py migrate green zero --fake`
2. `git checkout step-5`
3. See blue app serving, now project has one app, migration is complete.

## Step 6 - ?

## Step 7 - Profit
