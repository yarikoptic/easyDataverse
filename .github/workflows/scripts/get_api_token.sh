#!/bin/bash

# Set the builtin user key
curl -X PUT -d $BUILTIN_USERS_KEY $SERVER_URL/api/admin/settings/BuiltinUsers.KEY && echo "Added BuiltinUsers.KEY"

# Create a user and receive the API Token
curl -d @.github/workflows/assets/user.json \
    -H "Content-type:application/json" \
    -o ./user_data.json \
    "$SERVER_URL/api/builtin-users?password=$NEWUSER_PASSWORD&key=$BUILTIN_USERS_KEY" \
    && echo "Created user"

# Retrieve the API Token and put into env variable
USER_DATA=$(cat ./user_data.json)
echo "API_TOKEN=$(echo $USER_DATA | jq -r '.data.apiToken')" >> $GITHUB_ENV