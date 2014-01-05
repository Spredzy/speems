speems
======

A serverspec metadata service

## What ?

Speems is a serverspec metadata service, meaning that given a specific hostname speems will return the appropriate serverspec file.

It is a web.py base application to run it simply clone the repository and run

    python code.py [PORT]

## How ?

How to query the metadata service ?

    curl -H 'x-hostname: myhostname.mydomain.com' 127.0.0.1:8080

**Note**: The x-hostname header is a requisite. This is how the metadata service determines which files to return

## Configuration

The ```speems.cfg``` is the configuration file for the application. It supports regular expression.
The basic pattern is

    role:
      - aregexp
      - anotherregexp

    role2:
      - aregexp
      - anotherregexp2

The role name needs to match a file in spec.d/*role*_spec.rb

## Dependencies

* web.py
* yaml
