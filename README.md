# dokku-envs

A python script to easilty and quickly set environment variable on a [dokku](http://dokku.viewdocs.io/dokku/) app from local machine.

## Usage

- copy the file to the root of your project or where ever your .env file is located
- make sure you have the dokku cli installed(see dokku docs) and you have added the dokku remote repository to your project with git

  ```sh
  git remote add dokku dokku@dokku_server:your_app_name
  ```

- then run the script from your local machine, make sure your env file is structure like this:

  ```txt
  SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXX
  ```

  **or**

  ```txt
  SECRET_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
  ```
