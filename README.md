# dokku-envs

A python script to easilty and quickly set environment variable on a [dokku](http://dokku.viewdocs.io/dokku/) app from local machine.

## Usage

- copy the file to the root of your project or where ever your env file is located.
- make sure you have the [dokku-toolbelt](http://dokku.viewdocs.io/dokku/community/clients/#nodejs-dokku-toolbelt) installed and you have added the dokku remote repository to your project with git

  ```sh
  git remote add dokku dokku@dokku_server:your_app_name
  ```

- then run the script from your local pc with :

  ```sh
  python dokku_config.py <env_path>
  ```

  If you are running the script from the remote server using the dokku cli, you need to specify the project name

  ```sh
  python dokku_config.py --app <appname> <env_path>
  ```

## Required

- python >= 3.7
- click == 7.1.2

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
