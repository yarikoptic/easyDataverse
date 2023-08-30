import argparse
import json
import os
from typing import Dict

import requests


def main(server_url: str, user_json: Dict) -> None:
    """Creates a builtin user on the server and adds the API Token to the environment variables."""

    BUILTIN_USERS_KEY = os.environ["BUILTIN_USERS_KEY"]
    NEWUSER_PASSWORD = 'SDm!>,"-ek/OKeA9'

    url = f"{server_url}/api/builtin-users?password={NEWUSER_PASSWORD}&key={BUILTIN_USERS_KEY}"
    response = requests.get(
        url,
        json=user_json,
        headers={"Content-Type": "application/json"},
    )

    if response.status_code != 200:
        raise Exception(f"Failed to create builtin user: {response.text}")


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
