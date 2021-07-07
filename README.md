# Texas Connect

A community-based mesage site built entirely in Django.

This site is a message board for local comunities anywhere, but built with my local community mine in Texas. It features a article posting system where a user can create a post, with options for editing or deleteing it.

## How to Install

Follow GitHub practices to fork and clone the repository to your local environment. From there use `pip3 install` to load the dependencies required for this project. In your terminal run `python3 manage.py runserver` to launch the project inside your browser, defaulting port 8000.

## How to use Texas Connect

First things first, signup and create an account. This will be your login credentials. To view any posts in the community, click View all Articles and browse through a series of posts from other community members. There's no need to be signed in to view posts. This principle goes with viewing the weather as well. A user can enter a city, or a zip code, and get the local forecast.

Once signed in, a new article can be created using the link in the navigation bar, or the plus button located at the lower right of the screen. The user is taken to the create an article page. On saving, they can view their post and return to all articles to view their submission at the bottom of the list. The list is sorted older to newer.

When the user's name is clicked in the upper right corner, a password change page can help reset a comprimised password, and the guidelines page will explain any considerations for submitting articles to the community. The user will be able to log out here as well.

## About the project

The idea for Texas Connect came about organically. What started out as a simple idea while following the infamous polls tutorial on the Django webiste soon realized into a workng message board app. I kept reading passing comments that Django was built to provide a digital space for the Lawrence Journal-World, and decided that to properly understand this web framework, and the model-template-view architecture it uses. For writng articles, editing and posting to a site this method seemed logical. Getting a chance to learn python is an added bonus. Experimenting with multiple apps inside one project was paramount for this endeavour.

In practicing with a new framework, I tried to keep models and views as simple as possible for this project. Using generic, built in Django classes, I was able to construct an easily readable structure that complies with CRUD functionality for writing and posting articles.









