# docker-test
Simple program that takes user input and runs the correspoding program inside a docker container. 
Then displays the terminal output(success and errors). 
Runs on your LocalMachine



Usage:


-Set up a python virtual environment to import dependencies.

-Build a Docker image with python3 imported. (If you are using MacOS or windows, you need to set up a linux vm to run docker)

-Put the python test script inside the same folder as your Dockerfile

-Make sure the docker container has group permissions set to your user(enable the image to run without "sudo")

-Activate virtualenv: "source virtualenv/bin/activate"

-Run Flask web app: "python phase1.py"(or run using wsgi)

-Go to the address where the app is running on your browser (eg. https://0.0.0.0:5000/)

