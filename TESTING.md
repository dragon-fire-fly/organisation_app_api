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

### Sign up

| HTTP | URI                          | Testing                      | Response | Screenshot                                                                         |
| ---- | ---------------------------- | ---------------------------- | -------- | ---------------------------------------------------------------------------------- |
| GET  | "dj-rest-auth/registration/" | not allowed                  | 405      | ![get route not allowed](documentation/testing/postman/signup-get-not-allowed.png) |
| POST | "dj-rest-auth/registration/" | blank username & password    | 400      | ![blank username and password](documentation/testing/postman/signup-blank.png)     |
| POST | "dj-rest-auth/registration/" | password too short           | 400      | ![password too short](documentation/testing/postman/signup-pw-too-short.png)       |
| POST | "dj-rest-auth/registration/" | non matching password        | 400      | ![non matching password](documentation/testing/postman/signup-pw-nomatch.png)      |
| POST | "dj-rest-auth/registration/" | password similar to username | 400      | ![password too similar](documentation/testing/postman/signup-pw-too-similar.png)   |
| POST | "dj-rest-auth/registration/" | password too common          | 400      | ![password too common](documentation/testing/postman/signup-pw-too-common.png)     |
| POST | "dj-rest-auth/registration/" | valid username & password    | 200      | ![successful signup](documentation/testing/postman/signup-success.png)             |

### Sign in

| HTTP | URI                   | Testing                   | Response | Screenshot                                                                         |
| ---- | --------------------- | ------------------------- | -------- | ---------------------------------------------------------------------------------- |
| GET  | "dj-rest-auth/login/" | not allowed               | 405      | ![get route not allowed](documentation/testing/postman/signin-get-not-allowed.png) |
| POST | "dj-rest-auth/login/" | blank username & password | 400      | ![blank username and password](documentation/testing/postman/signin-blank.png)     |
| POST | "dj-rest-auth/login/" | valid username & password | 200      | ![successful login](documentation/testing/postman/signin-success.png)              |

To access restricted content using Postman, the JWT token must be supplied as an Authorization header with the prefix "Bearer". On successful signup/sign in, the user's JWT token is displayed. This can be copied into the Authorization header to access content appropriate for the user's permission state. :
![authorisation details supplied](documentation/testing/postman/authorisation-heading.png)

### Profiles

### Posts

### Events

### Calendars

### Comments

### Likes

### Memories

### Watches

### Followers
