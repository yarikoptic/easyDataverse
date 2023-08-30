#!/bin/bash

# Set the builtin user key
curl -X PUT -d $BUILTIN_USERS_KEY $SERVER_URL/api/admin/settings/BuiltinUsers.KEY &&

# Create a user and receive the API Token
USER_DATA=$( \
    curl -d @.github/workflows/assets/user.json \
    -H "Content-type:application/json" \
    "$SERVER_URL/api/builtin-users?password=$NEWUSER_PASSWORD&key=$BUILTIN_USERS_KEY"
)

# Print the API Token
echo $(jq -r '.apiToken' <<< "$USER_DATA")