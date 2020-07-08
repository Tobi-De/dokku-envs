import os
import sys


def set_dokku_app_envs(env_dict, app_name):
    command = "dokku config:set {app_name} {env_name}={env_value}"
    if env_dict:
        for env_name, env_value in env_dict.items():
            os.system(
                command.format(
                    app_name=app_name, env_name=env_name, env_value=env_value
                )
            )
    # set random secret key and admin url, comment if not needed

    os.system(
        f'dokku config:set {app_name} DJANGO_SECRET_KEY="$(openssl rand -base64 64)"'
    )
    os.system(
        f'dokku config:set {app_name} DJANGO_ADMIN_URL="$(openssl rand -base64 4096 | tr -dc "A-HJ-NP-Za-km-z2-9" | head -c 32)/"'
    )


if __name__ == "__main__":
    env_dict = {}
    try:
        app_name = sys.argv[1]
    except IndexError:
        print("usage: python dokku_config.py <app_name>")
    else:
        with open(".env", "r") as f:
            for line in f:
                env_list = line.strip().split("=")
                env_dict[env_list[0]] = env_list[1]
        set_dokku_app_envs(env_dict, app_name)
