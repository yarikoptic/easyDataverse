import argparse
import json
import os
from typing import Dict

import requests


def _set_builtin_users_key(server_url: str, builtin_users_key: str) -> None:
    """Sets the builtin users key on the server.

    Args:
        server_url (str): Dataverse server url
        builtin_users_key (str): The builtin users key
    """

    url = f"{server_url}/api/admin/settings/BuiltinUsers.KEY"
    response = requests.put(
        url,
        data=builtin_users_key,
        headers={"Content-Type": "text/plain"},
    )

    if response.status_code != 200:
        raise Exception(f"Failed to set builtin users key: {response.text}")


def _create_builtin_user(server_url: str, user_json: Dict, password: str) -> Dict:
    """Creates a builtin user on the server.

    Args:
        server_url (str): Dataverse server url
        user_json (Dict): Payload for creating a builtin user
        password (str): Password for the new user

    Returns:
        Dict: Payload containing the new user's API Token
    """

    url = f"{server_url}/api/builtin-users?password={password}"
    response = requests.get(
        url,
        json=user_json,
        headers={"Content-Type": "application/json"},
    )

    if response.status_code != 200:
        raise Exception(f"Failed to create builtin user: {response.text}")

    return response.json()


def main(server_url: str, user_json: Dict) -> None:
    """Creates a builtin user on the server and adds the API Token to the environment variables.

    Args:
        server_url (str): DataVerse server url
        user_json (Dict): Payload for creating a builtin user
    """

    BUILTIN_USERS_KEY = os.environ["BUILTIN_USERS_KEY"]
    NEWUSER_PASSWORD = "ThisIsATest2023!"

    _set_builtin_users_key(
        server_url=server_url,
        builtin_users_key=BUILTIN_USERS_KEY,
    )

    user_data = _create_builtin_user(
        server_url=server_url,
        user_json=user_json,
        password=NEWUSER_PASSWORD,
    )

    print(user_data.keys())


if __name__ == "__main__":
    # Get the server url from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--server-url")
    parser.add_argument("--json-path")
    args = parser.parse_args()

    # Check if any argument is none
    if any(arg is None for arg in vars(args).values()):
        raise Exception(
            f"Missing arguments: {[arg for arg in vars(args).keys() if vars(args)[arg] is None]}"
        )

    # Set the arguments
    server_url = args.server_url
    user_json = json.load(open(args.json_path))

    main(server_url=server_url, user_json=user_json)
