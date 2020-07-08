# dokku-envs

A python script to easilty and quickly set environment variable on a [dokku](http://dokku.viewdocs.io/dokku/) app from local machine.

## Usage

- copy the file to the root of your project or where ever your .env file is located
- make sure you have the dokku cli installed(see dokku docs) and you have added the dokku remote repository to your project with git

  ```sh
  git remote add dokku dokku@dokku_server:your_app_name
  ```

- then run the script with :

  ```sh
  python dokku_config.py <app_name>
  ```

  you can also specify the file path you want to use but the file should alway be formatted like describe below in the required section

  ```sh
  python dokku_config.py <app_name> <file_path>
  ```

## Required

- python 3.X

- make sure your env file is structure like this:

  ```txt
  SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXX
  DEBUG=False
  ```

  **or**

  ```txt
  SECRET_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
  DEBUG="False"
  ```

  Each env value on a line.

### Sidenote

You can also use this script for [heroku](https://heroku.com) app, just replace **dokku** by **heroku** everywhere.
