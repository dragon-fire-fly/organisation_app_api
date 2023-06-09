# EventTrove

EventTrove is a one-stop location for all your event discovery, sharing and organisation needs!
This interactive platform includes the option to view, add, edit and delete events and posts to share all kinds of events, big and small! A built in calendar allows visual organisation of your events to make sure you never miss an event!

The project has been split into two parts - the back-end constructed with [Django REST Framework](https://www.django-rest-framework.org/) and the frontend supercharged with [React](https://react.dev/).

More information on the front-end of the site can be found in the [front-end repository](https://github.com/dragon-fire-fly/organisation_app_frontend).

Link to the live site - [EventTrove Live Site](https://organisation-app-frontend.herokuapp.com/)

Link to the live API - [EventTrove Live API](https://organisation-app-api.herokuapp.com/)

Link to the front-end repository - [EventTrove Front-End Repo](https://github.com/dragon-fire-fly/organisation_app_frontend)

## User Stories

All user stories can be found in the [User Story grid](https://docs.google.com/spreadsheets/d/1-8NA5gjndIE3oYSuDAwsheJqryA4tlZQ6CmLRp4fKt8/edit?usp=sharing)

In the grid, each user story has details of it's EPIC, the user story number, the title, user story, acceptance criteria and both the backend and frontend tasks (with link to backend and frontend issues).

More details about Agile and use stories may be found in the [frontend repository](https://github.com/dragon-fire-fly/organisation_app_frontend) for this project.

User story testing may be found in the [Testing](TESTING.md) documentation.

## Database Design

### API Entity Relationship Diagram

The following diagram (created from actual django models) was created in [DBeaver](https://dbeaver.io/) and shows the relationship between all the entities in the database. Each table relates to a specific model created in Django Rest Framework. There are a total of 11 tables - one for each of the 9 models, plus the auth_user (default User model from Django) and the many-to-many intermediate table (between event and calendar).

![API ERD](documentation/api-erd.png)

### Models

There are a total of 9 models present in this project.

The following 5 models are taken from the Code Institute Moments walkthrough tutorial:

- Post
- Comment
- Like
- Follower
- Profile

The folowing 4 models are custom:

- Event  
  This model is based on the `Post` model, but has many additional fields, including the following:

  - ManyToMany field (to calendars)
  - DateTime field (event start and end)
  - URL field (for links)
  - Boolean fields (for all_day, past and notification fields)
  - Choice fields (for event_type, privacy and time_zone fields)

- Watch  
  This model is very similar to the "like" model, but for events

- Memory  
  This model is based on the "comment" model, but has the following additional fields:

  - ImageField (for attaching an image to the memory)
  - Boolean field (for determining whether a memory is a "plan" or not)

- Calendar  
  This model has a one-to-one relationship with user so that each user has exactly one calendar. The calendar is created and assigned during user creation such that each calendar has the same pk as the user. This is achieved with the create_calendar function and the post_save method to associate the user.

  The calendar model also has a timezone field. This field retrieves the user's timezone from their IP address using the [timezoneapi.io](https://timezoneapi.io) API with a token stored in the application's hidden variables. If the user's ip address cannot be determined in this way, the default value of "UTC" is used.

  This is part of a future feature concerned with connecting the application to the Google Calendar API. When creating events, it is crucial that the correct timezone is used, otherwise the event time will inaccurate and any reminders set up will display at the wrong point. This feature is not yet implemented in the frontend of the application, but is planned for the near future.

## Features

Below are all of the valid endpoints for the API, seperated into their respective apps. There are 9 apps in total that each have a set of API endpoints which can be accessed at the URIs listed below.

### Root route

<details> 
<summary>More details about the root route</summary>

![root route](documentation/features/root_route.png)

</details>

### Profiles

<details> 
<summary>More details about Profiles</summary>

| HTTP | URI            | CRUD Operation              | View name |
| ---- | -------------- | --------------------------- | --------- |
| GET  | /profiles/     | list all profiles           | LIST      |
| GET  | /profile/{id}/ | retrieve a specific profile | DETAIL    |
| PUT  | /profile/{id}/ | update a specific profile   | DETAIL    |

![profiles list route](documentation/features/profiles.png)
![profile detail route](documentation/features/profile_detail.png)

</details>

### Events

<details> 
<summary>More details about Events</summary>

| HTTP   | URI                             | CRUD Operation                                                                                                             | View name |
| ------ | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------- |
| GET    | /events/                        | list all events                                                                                                            | LIST      |
| POST   | /events/                        | create an event entry                                                                                                      | LIST      |
| GET    | /event/{id}/                    | retrieve a specific event entry                                                                                            | DETAIL    |
| PUT    | /event/{id}/                    | update a specific event entry                                                                                              | DETAIL    |
| DELETE | /event/{id}/                    | delete a specific event entry                                                                                              | DETAIL    |
| GET    | /events/calendars/{id}/         | list all events in a specific calendar                                                                                     | LIST      |
| GET    | /events/calendars/{id}/addevent | route to specifically allow edit of the event resource by any user (for the purpose of adding the event to their calendar) | DETAIL    |

Event list route. Authenticated users can also create new events on this route
![event list route](documentation/features/events.png)
Event detail route. Event owners can also edit and delete events on this page
![event detail route](documentation/features/event_detail.png)
Calendar event route. This route is used by the calendar to retrieve all events from a specific calendar
![calendar events list route](documentation/features/calendar_events.png)
If the route for a non existant event is entered, a 404 error is returned
![event detail route](documentation/features/event_not_found.png)

</details>

### Posts

<details> 
<summary>More details about Posts</summary>

| HTTP   | URI               | CRUD Operation           | View name |
| ------ | ----------------- | ------------------------ | --------- |
| GET    | /posts/           | list all posts           | LIST      |
| POST   | /posts/create/    | create a post            | LIST      |
| GET    | /posts/{id}/      | retrieve a specific post | DETAIL    |
| PUT    | /posts/{id}/edit/ | update a specific post   | DETAIL    |
| DELETE | /posts/{id}/edit/ | delete a specific post   | DETAIL    |

Post list route. This route does not contain the event serializer on the event field. Authenticated users can also create new posts on this route
![post list route](documentation/features/posts.png)
Event detail route. This route does contains the event serializer on the event field
![post detail route](documentation/features/post_detail.png)
Post edit and delete route. This route does not contain the event serializer on the event field
![post edit and delete route](documentation/features/post_edit_delete.png)
If the route for a non existant post is entered, a 404 error is returned
![post not found](documentation/features/post_not_found.png)

</details>

### Comments

<details> 
<summary>More details about Comments</summary>

| HTTP   | URI             | CRUD Operation              | View name |
| ------ | --------------- | --------------------------- | --------- |
| GET    | /comments/      | list all comments           | LIST      |
| POST   | /comments/      | create a comment            | LIST      |
| GET    | /comments/{id}/ | retrieve a specific comment | DETAIL    |
| PUT    | /comments/{id}/ | update a specific comment   | DETAIL    |
| DELETE | /comments/{id}/ | delete a specific comment   | DETAIL    |

![comments list route](documentation/features/comments.png)
![comment detail route](documentation/features/comment_detail.png)

</details>

### Likes

<details> 
<summary>More details about Likes</summary>

| HTTP   | URI          | CRUD Operation           | View name |
| ------ | ------------ | ------------------------ | --------- |
| GET    | /likes/      | list all likes           | LIST      |
| POST   | /likes/      | create a like            | LIST      |
| GET    | /likes/{id}/ | retrieve a specific like | DETAIL    |
| DELETE | /likes/{id}/ | delete a specific like   | DETAIL    |

![likes list route](documentation/features/likes.png)
![like detail route](documentation/features/like_detail.png)

</details>

### Watches

<details> 
<summary>More details about Watches</summary>

| HTTP   | URI            | CRUD Operation            | View name |
| ------ | -------------- | ------------------------- | --------- |
| GET    | /watches/      | list all watches          | LIST      |
| POST   | /watches/      | create a watch            | LIST      |
| GET    | /watches/{id}/ | retrieve a specific watch | DETAIL    |
| DELETE | /watches/{id}/ | delete a specific watch   | DETAIL    |

![watches list route](documentation/features/watches.png)
![watch detail route](documentation/features/watch_detail.png)

</details>

### Memories

<details> 
<summary>More details about Memories</summary>

| HTTP   | URI             | CRUD Operation             | View name |
| ------ | --------------- | -------------------------- | --------- |
| GET    | /memories/      | list all memories          | LIST      |
| POST   | /memories/      | create a memory            | LIST      |
| GET    | /memories/{id}/ | retrieve a specific memory | DETAIL    |
| PUT    | /memories/{id}/ | update a specific memory   | DETAIL    |
| DELETE | /memories/{id}/ | delete a specific memory   | DETAIL    |

![memories list route](documentation/features/memories.png)
![memory detail route](documentation/features/memory_detail.png)

</details>

### Followers

<details> 
<summary>More details about Followers</summary>

| HTTP   | URI              | CRUD Operation               | View name |
| ------ | ---------------- | ---------------------------- | --------- |
| GET    | /followers/      | list all followers           | LIST      |
| POST   | /followers/      | create a follower            | LIST      |
| GET    | /followers/{id}/ | retrieve a specific follower | DETAIL    |
| DELETE | /followers/{id}/ | delete a specific follower   | DETAIL    |

![followers list route](documentation/features/followers.png)
![follower detail route](documentation/features/follower_detail.png)

</details>

### Calendars

<details> 
<summary>More details about Calendars</summary>

| HTTP | URI              | CRUD Operation               | View name |
| ---- | ---------------- | ---------------------------- | --------- |
| GET  | /calendars/      | list all calendars           | LIST      |
| GET  | /calendars/{id}/ | retrieve a specific calendar | DETAIL    |
| PUT  | /calendars/{id}/ | update a specific calendar   | DETAIL    |

![calendars list route](documentation/features/calendars.png)
![calendar detail route](documentation/features/calendar_detail.png)

</details>

### Future Features

- Connect to the Google Calendar API
- Integration of google maps to determin precise location
- Email notifications (when user agrees) to remind users about events and send a weekly/monthly digest of upcoming/recently passed events
- Inclusion of a weather API to diplay the weather forecast for each event (according to their location)

## Testing

[Testing documentation can be found in the TESTING.md file](TESTING.md)

## Deployment

The live deployed application can be found deployed on [Heroku](https://organisation-app-frontend.herokuapp.com/).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: developer_matcher).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For _Primary interest_, you can choose _Programmable Media for image and video API_.
- Optional: _edit your assigned cloud name to something more memorable_.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key                     | Value                                                                |
| ----------------------- | -------------------------------------------------------------------- |
| `ALLOWED_HOST`          | user's deployed API URL                                              |
| `CLIENT_ORIGIN`         | user's deployed frontend URL                                         |
| `CLOUDINARY_URL`        | user's own value                                                     |
| `DATABASE_URL`          | user's own value                                                     |
| `DISABLE_COLLECTSTATIC` | 1 (_this is temporary, and can be removed for the final deployment_) |
| `SECRET_KEY`            | user's own value                                                     |
| `TIME_ZONE_TOKEN`       | (optional) user's own value if the time zone API is used             |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- _replace **app_name** with the name of your primary Django app name; the folder where settings.py is located_

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace _app_name_ with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  - `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the _requirements.txt_ file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/dragon-fire-fly/organisation_app_api/)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
   - `git clone https://github.com/dragon-fire-fly/organisation_app_api/.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/dragon-fire-fly/organisation_app_api/)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/dragon-fire-fly/organisation_app_api/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Technologies and Tools

- [Python](https://www.python.org) used as the back-end programming language.
- [Django Rest Framework](https://www.django-rest-framework.org/) - A python based framework for building APIs.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [Visual Studio Code](https://code.visualstudio.com/) used as a local IDE for development.
- [Black](https://pypi.org/project/black/) used as a PEP8 compliant Python code formatter.
- [DBeaver](https://dbeaver.io/) used to produce ERDs and help plan the database models.
- [Postman](https://www.postman.com/) used to test API routes.

## Credits

### References

- Code Institute's "Moments" walkthrough project
- Obtaining user's timezone: https://www.youtube.com/watch?v=lUe_-WnrPUE
- Creating events in google calendar: https://developers.google.com/calendar/api/guides/create-events

### Acknowledgements

- I would like to thank my Code Institute mentor, Martina Terlevic for her support throughout the development of this project.
- I would like to thank my previous Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN). Although he isn't my mentor anymore, his previous support and guidance still helps me every day.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com), particularly the class of May 2022, for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my husband (Christian Schmidt), for believing in me, and allowing me to make this transition into software development.
