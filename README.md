# LA_03
# Recommendation systems with API

## This repository contains the submission for Recommendation Systems Lab Assignment 3.

## Team members
- Dhara Shah (202211008)
- Hinal Desai (202211035)
- Naiya Patel (202211075)
- Jay Joshi (202211079)


# API Documentation

## Base Url
This depends on the environment in which the api is run.
Eg. http://127.0.0.1:5000

## Authentication
None

## Endpoints

**GET /user/recommend**

Returns the recommendations for the specified user which is passed as query parameter.

**Parameters**
| Name | Type | Description |
|--- | --- | --- |
| user_id | string | The id of the user for whom item recommendations are requested |
| filter | string | The type of filtering to use - cb for content-based and cf for collaborative|
| type | string | Additional parameter to be passed in case of collaborative filtering - user for user-based or item for item-based| 
