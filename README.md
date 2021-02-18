# locust-woocomerce
Locust tests for a woocomerce website

# Prerequisites

This requires an instance of a woocomerce website up and running. This can be done from https://github.com/antonyfuentes/testing-playground.
This could either be locally or in a server.

Install https://locust.io/ : `pip install locust`

# How to run

This can be run from the terminal to see the UI and with the .sh file to run in silent mode

## Run from web UI

Run the command:
locust -f locust-lab.py --host **URL**  --users **NumberOfUsers** --spawn-rate **TimeBetweenUsers**

This can be run only with:
locust -f locust-lab.py
and the variables when the UI launches.

## Run in silent mode

Add the URL, number of users, time between users and total execution time to the script.
Execute the file **loadtest.sh**
