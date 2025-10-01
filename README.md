<h1 align="center">Django - News Digester</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Author](#author)

## About <a name = "about"></a>

Short local Django project, about collecting articles from differents RSS feeds and managing digests. Everything is done only on admin site.

This project has been developed for testing purpose on local computer.

## Features <a name = "features"></a>

<ul>
    <li>Django 5.2.6</li>
    <li>Python 3.13.7</li>
    <li>Docker 28.3 </li>
    <li>Redis 7</li>
    <li>PostgreSQL 17</li>
    <li>Celery 5.2</li>
    <li>FeedParser 6</li>
</ul>
This project:
<ul>
    <li>Collects articles from Active RSS Feeds/Sources, every 2 minutes (can be changed in the code '/newsdigester/celery.py'),</li>
    <li>Allows to collect articles from Active RSS feeds/Sources, on demand (using commandline),</li>
    <li>Allows you to create, delete, update Digests,</li>
    <li>Allows you to create, delete, update what Articles should be in your digest,</li>
    <li>Allows you to manage collected Articles from Active RSS Sources/feeds,</li>
    <li>Allows you to manage RSS Sources/Feeds.</li>
</ul>

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

In order to run this project, you need to have [Docker](https://www.docker.com/) and/or [Docker Desktop](https://www.docker.com/) installed on your local machine.

### Installing

<ul>
    <li>Get a copy of this project on your local computer</li>
    <li>Open a terminal and build the docker stack, typing:</li>
</ul>

```
docker-compose build
```

<ul>
    <li>Run your docker stack, typing:</li>
</ul>

```
docker compose up -d
```

<ul>
    <li>Once docker stack is running, you need to get the Container ID of the web container.<p>On Docker Desktop, just click on the icon beside your web container.</p><p>You can also get the container IDo usin a terminal/console, typing:</p></li>
</ul>

```
docker ps -a
```

<ul>
    <li>Once you have the web container ID, you need to create an admin user account in django, typing:</li>
</ul>

```
docker exec -it 'your web container ID' python manage.py createsuperuser
```

<ul>
    <li>Enter requested data by Django (username, email, password, password confirmation)</li>
</ul>

Once super user (admin user) is created, you can proceed to use this Django project.

## Usage <a name="usage"></a>

<ul>
    <li>Open your favorite web browser and type:</li>
</ul>

```
http://localhost:8000/admin
```

<ul>
    <li>Use 'username' and 'password', you typed to create the admin/super user.</li>
</ul>

To use this project, you have to:

<ol>
    <li>Add RSS Sources, using the model "NewSources" and mark as 'Active' the RSS Sources, from which you want to collect Articles,</li>
    <li>Add Digests to which Articles will be linked (behing the scene, Django will collect Articles),</li>
    <li>Attach Articles to desired Digest.</li>
</ol>

Every 2 minutes, the project will check each ACTIVE RSS Source and store into database, all articles relative to active RSS feeds.
If you want to manually collect and store to database, articles relative to ACTIVE RSS Sources, you can use the following commandline in terminal/console:
```
docker exec -it ID_OF_WEB_CONTAINER python manage.py fetchfeeds
```

## Built Using <a name = "built_using"></a>

- [Docker](https://www.docker.com/) - Docker environment
- [Django](https://www.djangoproject.com/) - Python Server Framework
- [PostgreSQL](https://www.postgresql.org/) - SQL Database
- [Redis](https://redis.io/) - Real Time-Data Environment
- [Celery](https://docs.celeryq.dev/en/main/index.html) - Asynchronous task or job queue

## Author <a name = "author"></a>

- [Alain Roger](https://github.com/alainroger91100)
