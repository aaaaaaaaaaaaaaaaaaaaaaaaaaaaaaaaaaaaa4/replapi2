# replapi v2

#### by ch1ck3n

## Introduction

All replit users have trouble getting profile information for this web app, not anymore! ch1ck3n made a replit api that is super easy to use. Just read on!

## using it

assuming you've installed this package, let's make a basic python file.

```
main.py
_______

import replapi2
```

you've imported replapi2. now let's get say... the amount of cycles the user has?

```
main.py
_______

import replapi2

ch1ck3n = replapi2.UserInfo("ch1ck3n") # you can change "ch1ck3n" to any username you want!

print(ch1ck3n.replit_cycles)

```

Congrats! you can now view the replit cycles for every user.

Here are all of the other methods:

`user_pic()`

Gets the url for the user's picture

`full_name()`

gets the user's full name.

`repls()`

returns the user's most recent repls.

`email()`

returns the has of the user's email.

`bio()`

returns the user's bio.

`top_languages()`

returns the user's top languages.

`hacker()`

return if the user is a hacker or not.

`organization()`

returns the name of the user's organization.

`replit_cycles()`

returns the user's replit cycles.

`comments()`

returns the user's replit comments.

