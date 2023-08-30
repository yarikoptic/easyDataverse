#!/bin/bash

curl -X PUT -d $BUILTIN_USERS_KEY $SERVER_URL/api/admin/settings/BuiltinUsers.KEY \
USER_DATA = $( \
    curl -d @.github/workflows/assets/user.json \
    -H "Content-type:application/json" \
    "$SERVER_URL/api/builtin-users?password=$NEWUSER_PASSWORD&key=$BUILTIN_USERS_KEY" \
)

echo $USER_DATA | grep -o '"apiToken":"[^"]*' | grep -o '[^"]*$'