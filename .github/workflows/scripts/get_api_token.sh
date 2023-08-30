#!/bin/bash

curl -X PUT -d $BUILTIN_USERS_KEY $SERVER_URL/api/admin/settings/BuiltinUsers.KEY \
&& \
curl -d @.github/workflows/assets/user.json \
    -H "Content-type:application/json" \
    -out ./user_payload.json \
    "$SERVER_URL/api/builtin-users?password=$NEWUSER_PASSWORD&key=$BUILTIN_USERS_KEY" \
&& \
echo $(grep -oP '(?<="apiToken": ")[^"]*' ./user_payload.json)