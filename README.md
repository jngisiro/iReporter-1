# iRporter

| [![Build Status](https://travis-ci.com/Paphra/iReporter.svg?branch=api)](https://travis-ci.com/Paphra/iReporter) | [![Coverage Status](https://coveralls.io/repos/github/Paphra/iReporter/badge.svg?branch=api)](https://coveralls.io/github/Paphra/iReporter) | [![Maintainability](https://api.codeclimate.com/v1/badges/98b3fa2007fd1192b882/maintainability)](https://codeclimate.com/github/Paphra/iReporter/maintainability)|

Corruption is a huge bane to Africaâ€™s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

## Project On Pivatal Tracker

The url is https://www.pivotaltracker.com/n/projects/2227847

## GitHub Pages

The site is hosted on git hub pages under the url
https://paphra.github.io/iReporter

## Access

The inner site is not accessible to the outside world because the code for the authentication is not yet made.
| Page | Link |
|----|----|
|**Signup**| https://paphra.github.io/iReporter/UI/signup.html |
|**Signin**| https://paphra.github.io/iReporter/UI/signin.html |
|**About**| https://paphra.github.io/iReporter/UI/about.html |
|**Profile**| https://paphra.github.io/iReporter/profile.html |
|**Admin**| https://paphra.github.io/iReporter/admin.html |

Others like the create, details, edit, change status, and view all are then accessed using different buttons

## Next Steps

The next thing would be to design the code to enable sigin and signup process.
I have made it in a way that the js framework shall be used for form validation/authentication and loading of data.

## The API

The API is already developed and hosted on https://paphra-ireporter.herokuapps.com
For accessing diffent features within the API, the following are used.

|METHOD|END POINT|Format JSON in request|Format of JSON in response|Description|
|---|---|----|---|--|
|POST|/api/v1/users|
'''python
    {
        "id" : Integer,
        "firstname" : String,
        "lastname" : String,
        "othernames" : String,
        "email" : String,
        "phoneNumber" : String,
        "username" : String,
        "registered" : Date,
        "isAdmin" : Boolean,
        "password": String,
        "gender": String,
        "address": String,
        "occupation": String
    }
    '''
| '''python
    {
        "status": 201,
        "data": [{
            "id": Integer,
            "message": "New User Added!"}]
    }
    '''
|If user is added successfully. Else, an error message of code 200, meaning successful request but user already exists|
|POST|/api/v1/red-flags|
'''python
    {
        "id" : Integer,
        "createdOn" : Date,
        "createdBy" : Integer, # represents the user who created this record
        "type" : String, # [red-flag, intervention]
        "location" : String, # Lat Long coordinates
        "status" : String , # [draft, under investigation, resolved, rejected]
        "Images" : [Image, Image],
        "Videos" : [Image, Image],
        "title": String,
        "otherFiles": [File, File]
        "comment" : String
    }
    ''''
|'''python
    {
        "status" : Integer,
        "data" : [ {
        "id" : Integer, # red flag record primary key
        "message" : �Created red-flag record" } ]
    }
    '''
| For if the flag is created successfully. On error, 400 is returned for bad request|