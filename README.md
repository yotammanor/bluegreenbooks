# Blue/Green Books - A Demo Blue/Green Deployment in Django
This is a demo implementation of an Application-based Blue/Green Deployment in Django.
If you don't know what Blue/Green Deployment is, [Martin Fowler](https://martinfowler.com/bliki/BlueGreenDeployment.html)
is always a great starting point.

App-based Blue/Green Deployment is similar to a regular Blue/Green, but all the blue/green
mechanisms are implemented inside a single app, talking with one database that supports only one
schema structure at a given moment. This greatly simplifies the complexity of maintaining data
consistency, without any degragation in the user experience (no need for read-only mode).

This is an experimental approach, and this project shows a complete working walkthrough of a
naively simple case. I'd love to hear if you tried it in a more complex setting, and whether you
succeeded or faced problems that failed the approach.

This project is the companion of [this talk](https://github.com/yotammanor/bluegreenbooks/blob/master/PyWebIL%20-%20App%20Based%20Blue%20Green%20Migrations%20With%20Django.pptx), originally given at [PyWeb-IL](https://www.meetup.com/PyWeb-IL/events/246639354/). Both the talk and the repo are
standalones, and each can (hopefully) be understood without the other.

Credits: This implementation heavily draws on https://github.com/jazzband/django-hosts, and on
[work done](https://github.com/masschallenge/standards/blob/master/blue_green_transitions.md)
by my team and I at [MassChallenge Inc.](http://masschallenge.org/join-our-team).

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
