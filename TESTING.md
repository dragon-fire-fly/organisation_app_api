# Testing

## Ci Workflow

A Continuous Integration (CI) workflow was set up on Github actions to monitor the API and run all unittests after each commit.
This enabled early detection of test failures and therefore faster fixture of bugs.

The [workflow file](https://github.com/dragon-fire-fly/organisation_app_api/blob/main/.github/workflows/ci.yml) can be found in the github repository for the project.

## PEP8

All files in the project have been run through the internal pycodestyle linter in VSCode during development.
In addition, the [Black](https://pypi.org/project/black/) pep8 validation tool was used on all files, installed into my VSCode environment throughout the development of the project. The line-length setting for Black was amended to 79 instead of the default 108 to comply with best practices.

To install and run pycode style:

- Run the command 'pip3 install -r requirements.txt'
- Press Ctrl+Shift+P
- Type 'linter' into the search field
- Select 'Python: Select Linter
- Select 'pycodestyle' from the list
- Select the 'Problems' tab in the terminal area at the bottom of the screen
- PEP8 errors are now displayed in the "problems"tab as well as being underlined in red in files themselves

![pycodestyle no errors](documentation/testing/no_problems_pycodestyle.png)
![Black PEP8 check](documentation/testing/black-pep8-linting.png)

## Manual Testing

Manual testing was performed for the API using Postman.
Postman is...

### Root

![root route](documentation/testing/postman/root.png)

### Sign up

| HTTP | URI                        | Testing                      | Response | Screenshot                                                                         |
| ---- | -------------------------- | ---------------------------- | -------- | ---------------------------------------------------------------------------------- |
| GET  | dj-rest-auth/registration/ | not allowed                  | 405      | ![get route not allowed](documentation/testing/postman/signup-get-not-allowed.png) |
| POST | dj-rest-auth/registration/ | blank username & password    | 400      | ![blank username and password](documentation/testing/postman/signup-blank.png)     |
| POST | dj-rest-auth/registration/ | password too short           | 400      | ![password too short](documentation/testing/postman/signup-pw-too-short.png)       |
| POST | dj-rest-auth/registration/ | non matching password        | 400      | ![non matching password](documentation/testing/postman/signup-pw-nomatch.png)      |
| POST | dj-rest-auth/registration/ | password similar to username | 400      | ![password too similar](documentation/testing/postman/signup-pw-too-similar.png)   |
| POST | dj-rest-auth/registration/ | password too common          | 400      | ![password too common](documentation/testing/postman/signup-pw-too-common.png)     |
| POST | dj-rest-auth/registration/ | valid username & password    | 200      | ![successful signup](documentation/testing/postman/signup-success.png)             |

### Sign in

| HTTP | URI                 | Testing                   | Response | Screenshot                                                                         |
| ---- | ------------------- | ------------------------- | -------- | ---------------------------------------------------------------------------------- |
| GET  | dj-rest-auth/login/ | not allowed               | 405      | ![get route not allowed](documentation/testing/postman/signin-get-not-allowed.png) |
| POST | dj-rest-auth/login/ | blank username & password | 400      | ![blank username and password](documentation/testing/postman/signin-blank.png)     |
| POST | dj-rest-auth/login/ | valid username & password | 200      | ![successful login](documentation/testing/postman/signin-success.png)              |

To access restricted content using Postman, the JWT token must be supplied in the Authorization tabas a "Bearer Token". On successful signup/sign in, the user's JWT token is displayed. This can be copied into the Authorization tab to access content appropriate for the user's permission state. :
![authorisation details supplied](documentation/testing/postman/authorisation-heading.png)

### Profiles

| HTTP | URI             | Testing                       | Response | Screenshot                                                                            |
| ---- | --------------- | ----------------------------- | -------- | ------------------------------------------------------------------------------------- |
| GET  | /profiles/      | list view                     | 200      | ![profiles list](documentation/testing/postman/profiles.png)                          |
| POST | /profiles/      | method not allowed            | 405      | ![post not allowed](documentation/testing/postman/profiles-post-not-allowed.png)      |
| GET  | /profiles/{id}/ | detail view                   |          | ![profile detail view](documentation/testing/postman/profile.png)                     |
| PUT  | /profiles/{id}/ | put with unauthenticated user |          | ![unauthenticated put](documentation/testing/postman/profile-put-unauthenticated.png) |
| PUT  | /profiles/{id}/ | put with validated user       |          | ![authenticated put](documentation/testing/postman)                                   |

### Posts

| HTTP   | URI               | Testing                                 | Response | Screenshot                                                                             |
| ------ | ----------------- | --------------------------------------- | -------- | -------------------------------------------------------------------------------------- |
| GET    | /posts/           | list view                               | 200      | ![get list view](documentation/testing/postman/posts-get-success.png)                  |
| POST   | /posts/           | method not allowed                      | 405      | ![post not allowed](documentation/testing/postman/posts-post-not-allowed.png)          |
| POST   | /posts/create/    | unauthenticated user not able to post   | 401      | ![unauthenticated post](documentation/testing/postman/create-post-unauthenticated.png) |
| POST   | /posts/create/    | authenticated user able to post         | 201      | ![authenticated post](documentation/testing/postman/create-post-success.png)           |
| GET    | /posts/{id}/      | detail view                             | 200      | ![get detail view](documentation/testing/postman/post-detail-get.png)                  |
| PUT    | /posts/{id}/edit/ | put with unauthenticated user           | 401      | ![unauthenticated put](documentation/testing/postman/post-put-unauthenticated.png)     |
| PUT    | /posts/{id}/edit/ | put with valid user (not post owner)    | 403      | ![no permission put](documentation/testing/postman/post-put-no-permission.png)         |
| PUT    | /posts/{id}/edit/ | put with valid user (post owner)        | 200      | ![authenticated put](documentation/testing/postman/post-put-success.png)               |
| DELETE | /posts/{id}/edit/ | delete with unauthenticated user        | 401      | ![unauthenticated delete](documentation/testing/postman/post-delete-unauthorised.png)  |
| DELETE | /posts/{id}/edit/ | delete with valid user (not post owner) | 403      | ![authenticated delete](documentation/testing/postman/post-delete-no-permission.png)   |
| DELETE | /posts/{id}/edit/ | delete with valid user ([post owner])   | 204      | ![authenticated delete](documentation/testing/postman/post-delete-success.png)         |

### Events

| HTTP   | URI           | Testing                                       | Response | Screenshot                                                                             |
| ------ | ------------- | --------------------------------------------- | -------- | -------------------------------------------------------------------------------------- |
| GET    | /events/      | list view                                     | 200      | ![get list view](documentation/testing/postman/events-get-success.png)                 |
| POST   | /events/      | post with unauthenticated user                | 401      | ![unauthenticated post](documentation/testing/postman/event-post-unauthorised.png)     |
| POST   | /events/      | post with authenticated user                  | 201      | ![authenticated post](documentation/testing/postman/event-post-success.png)            |
| GET    | /events/{id}/ | detail view                                   | 200      | ![get detail view](documentation/testing/postman/event-get-success.png)                |
| PUT    | /events/{id}/ | put with unauthenticated user                 | 401      | ![unauthenticated put](documentation/testing/postman/event-put-unauthorised.png)       |
| PUT    | /events/{id}/ | put with valid user (not event owner)         | 403      | ![no permission put](documentation/testing/postman/event-put-no-permission.png)        |
| PUT    | /events/{id}/ | put with valid user (event owner)             | 200      | ![authenticated put](documentation/testing/postman/event-put-success.png)              |
| DELETE | /posts/{id}/  | delete with unauthenticated user              | 401      | ![unauthenticated delete](documentation/testing/postman/event-delete-unauthorised.png) |
| DELETE | /posts/{id}/  | delete with valid user (not event owner) \*\* | 403      | ![no permission delete](documentation/testing/postman)                                 |
| DELETE | /posts/{id}/  | delete with valid user (event owner)          | 204      | ![authenticated delete](documentation/testing/postman/event-delete-success.png)        |

### Calendars

| HTTP   | URI              | Testing            | Response | Screenshot                                                                        |
| ------ | ---------------- | ------------------ | -------- | --------------------------------------------------------------------------------- |
| GET    | /calendars/      | list view          | 200      | ![get list view](documentation/testing/postman/calendars-get-success.png)         |
| GET    | /calendars/{id}/ | detail view        | 200      | ![get detail view](documentation/testing/postman/calendar-get-success.png)        |
| DE:ETE | /calendars/{id}/ | delete not allowed | 405      | ![get detail view](documentation/testing/postman/calendar-delete-not-allowed.png) |

### Comments

| HTTP   | URI             | Testing                                    | Response | Screenshot                                                                               |
| ------ | --------------- | ------------------------------------------ | -------- | ---------------------------------------------------------------------------------------- |
| GET    | /comments/      | list view                                  | 200      | ![get list view](documentation/testing/postman/comments-get-success.png)                 |
| POST   | /comments/      | post with unauthenticated                  | 401      | ![unauthenticated post](documentation/testing/postman/comment-post-unauthenticated.png)  |
| POST   | /comments/      | post with authenticated user               | 201      | ![authenticated post](documentation/testing/postman/comment-post-success.png)            |
| GET    | /comments/{id}/ | detail view                                | 200      | ![get detail view](documentation/testing/postman/comment-get-success.png)                |
| PUT    | /comments/{id}/ | put with unauthenticated user              | 401      | ![unauthenticated put](documentation/testing/postman/comment-put-unauthenticated.png)    |
| PUT    | /comments/{id}/ | put with valid user (not comment owner)    | 403      | ![no permission put](documentation/testing/postman/comment-put-no-permission.png)        |
| PUT    | /comments/{id}/ | put with valid user (comment owner)        | 200      | ![authenticated put](documentation/testing/postman/comment-put-success.png)              |
| DELETE | /comments/{id}/ | delete with unauthenticated user           | 401      | ![unauthenticated delete](documentation/testing/postman/comment-delete-unauthorised.png) |
| DELETE | /comments/{id}/ | delete with valid user (not comment owner) | 403      | ![no permission delete](documentation/testing/postman/comment-delete-no-permission.png)  |
| DELETE | /comments/{id}/ | delete with valid user (comment owner)     | 204      | ![authenticated delete](documentation/testing/postman/comment-delete-success.png)        |

### Likes

| HTTP   | URI          | Testing                                 | Response | Screenshot                                                                            |
| ------ | ------------ | --------------------------------------- | -------- | ------------------------------------------------------------------------------------- |
| GET    | /likes/      | list view                               | 200      | ![get list view](documentation/testing/postman/likes-get-success.png)                 |
| POST   | /likes/      | post with unauthenticated               | 401      | ![unauthenticated post](documentation/testing/postman/likes-post-unauthenticated.png) |
| POST   | /likes/      | post with authenticated user            | 201      | ![authenticated post](documentation/testing/postman/like-post-success.png)            |
| GET    | /likes/{id}/ | detail view                             | 200      | ![get detail view](documentation/testing/postman/like-get-success.png)                |
| DELETE | /likes/{id}/ | delete with unauthenticated user        | 401      | ![unauthenticated delete](documentation/testing/postman/like-delete-unauthorised.png) |
| DELETE | /likes/{id}/ | delete with valid user (not like owner) | 403      | ![authenticated delete](documentation/testing/postman/like-delete-no-permission.png)  |
| DELETE | /likes/{id}/ | delete with valid user (like owner)     | 204      | ![authenticated delete](documentation/testing/postman/like-delete-success.png)        |

### Memories

| HTTP   | URI             | Testing                                   | Response | Screenshot                                                                               |
| ------ | --------------- | ----------------------------------------- | -------- | ---------------------------------------------------------------------------------------- |
| GET    | /memories/      | list view                                 | 200      | ![get list view](documentation/testing/postman/memories-get-success.png)                 |
| POST   | /memories/      | post with unauthenticated                 | 401      | ![unauthenticated post](documentation/testing/postman/memories-post-unauthenticated.png) |
| POST   | /memories/      | post with authenticated user              | 201      | ![authenticated post](documentation/testing/postman/memories-post-success.png)           |
| GET    | /memories/{id}/ | detail view                               | 200      | ![get detail view](documentation/testing/postman/memory-get-success.png)                 |
| PUT    | /memories/{id}/ | put with unauthenticated user             | 401      | ![unauthenticated put](documentation/testing/postman/memories-post-unauthenticated.png)  |
| PUT    | /memories/{id}/ | put with valid user (not memory owner)    | 403      | ![no permission put](documentation/testing/postman/memories-put-unauthorised.png)        |
| PUT    | /memories/{id}/ | put with valid user (memory owner)        | 200      | ![authenticated put](documentation/testing/postman/memory-put-success.png)               |
| DELETE | /memories/{id}/ | delete with unauthenticated user          | 401      | ![unauthenticated delete](documentation/testing/postman/memory-delete-unauthorised.png)  |
| DELETE | /memories/{id}/ | delete with valid user (not memory owner) | 403      | ![no permiossion delete](documentation/testing/postman/memory-delete-no-permission.png)  |
| DELETE | /memories/{id}/ | delete with valid user (memory owner)     | 204      | ![authenticated delete](documentation/testing/postman/memory-delete-success.png)         |

### Watches

| HTTP   | URI            | Testing                                  | Response | Screenshot                                                                                |
| ------ | -------------- | ---------------------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| GET    | /watches/      | list view                                | 200      | ![get list view](documentation/testing/postman/watches-get-success.png)                   |
| POST   | /watches/      | post with unauthenticated                | 401      | ![unauthenticated post](documentation/testing/postman/watches-post-unauthenticated.png)   |
| POST   | /watches/      | post with authenticated user             | 201      | ![authenticated post](documentation/testing/postman/watch-post-success.png)               |
| GET    | /watches/{id}/ | detail view                              | 200      | ![get detail view](documentation/testing/postman/watch-get-success.png)                   |
| DELETE | /watches/{id}/ | delete with unauthenticated user         | 401      | ![unauthenticated delete](documentation/testing/postman/watch-delete-unauthenticated.png) |
| DELETE | /watches/{id}/ | delete with valid user (not watch owner) | 403      | ![no permission delete](documentation/testing/postman/watch-delete-no-permission.png)     |
| DELETE | /watches/{id}/ | delete with valid user (watch owner)     | 204      | ![authenticated delete](documentation/testing/postman/watch-delete-success.png)           |

### Followers

| HTTP   | URI              | Testing                            | Response | Screenshot                                                                                   |
| ------ | ---------------- | ---------------------------------- | -------- | -------------------------------------------------------------------------------------------- |
| GET    | /followers/      | list view                          | 200      | ![get list view](documentation/testing/postman/followers-get-success.png)                    |
| POST   | /followers/      | post with unauthenticated          | 401      | ![unauthenticated post](documentation/testing/postman/follower-post-unauthenticated.png)     |
| POST   | /followers/      | post with authenticated user       | 201      | ![authenticated post](documentation/testing/postman/follower-post-success.png)               |
| GET    | /followers/{id}/ | detail view                        | 200      | ![get detail view](documentation/testing/postman/follower-get-success.png)                   |
| DELETE | /followers/{id}/ | delete with unauthenticated user   | 401      | ![unauthenticated delete](documentation/testing/postman/follower-delete-unauthenticated.png) |
| DELETE | /followers/{id}/ | delete with valid user (not owner) | 403      | ![no permission delete](documentation/testing/postman/follower-delete-no-permission.png)     |
| DELETE | /followers/{id}/ | delete with valid user (owner)     | 204      | ![authenticated delete](documentation/testing/postman/follower-delete-success.png)           |
