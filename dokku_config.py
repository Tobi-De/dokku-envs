import os
import sys
from pathlib import Path
import click

# TODO use click package
# TODO instead of dokku, the dt command could be use
# TODO the app name is not needed with the dokku-toolbet
# TODO refactor this code, maybe with an oop approach


def run_commands(command, appname, env_dict):
    #  app_name=app_name, env_name=env_name, env_value=env_value
    for env_name, env_value in env_dict.items():
        os.system(
            command.format(app_name=app_name, env_name=env_name, env_value=env_value)
        )


def read_env_file(file_path):
    env_dict = {}
    with open(file_path, "r") as f:
        for line in f:
            env_list = line.strip().split("=")
            env_dict[env_list[0]] = env_list[1]
    return env_dict


@click.command()
@click.option(
    "--env",
    default="prodconfig",
    help="The file where the env variables should be read from.",
)
@click.option(
    "--appname",
    default="",
    help="The name of your app, this is neccessary when your are\
     using the dokku cli directly instead of the dokku-toolbet wrapper",
)
def set_dokku_app_envs(env, appname):
    """Simple program that set environment variable for app deploy with dokku"""

    command = (
        "dokku config:set {app_name} {env_name}={env_value}"
        if appname
        else "dt config:set {env_name}={env_value}"
    )

    env_dict = read_env_file(file_path=env)

    if not env_dict:
        return

    run_commands(command, env_dict)

    # set random secret key and admin url, comment if not needed
    defaults = {
        "DJANGO_SECRET_KEY": "$(openssl rand -base64 64",
        "DJANGO_ADMIN_URL": "$(openssl rand -base64 4096 | tr -dc 'A-HJ-NP-Za-km-z2-9' | head -c 32)/",
        "WEB_CONCURRENCY": "4",
        "PYTHONHASHSEED": "random",
    }

    run_commands(command, defaults)


if __name__ == "__main__":
    try:
        env_file = sys.argv[2]
    except IndexError:
        env_file = ".env"
    try:
        app_name = sys.argv[1]
    except IndexError:
        print("usage: python dokku_config.py <app_name>")
    else:
        env_dict = read_env_file(env_file)
        set_dokku_app_envs(env_dict, app_name)
