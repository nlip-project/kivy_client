# NLIP CLient 

This is a simple implementation of a NLIP Client written using python kivy package. 

It is currently only supporting NLIP text messages exchange with a server. 



## Installation

To set up this python project, create a virtual environment for python using the following commands (You can use your own environment name instead of using the provided name of env_kivy: 

```
$ python -m venv env_kivy
$ source env_kivy/bin/activate
```

Next, install the required packages:
```
$ pip install -r requirements.txt
```

Now the python environment is setup and you can play with a few of the commands.

## Running the client

Invoke the following commands:
```
$ python simple.py 
```

The client GUI will appear. You can type the hostname and port of the NLIP server at the top and communicate with them. The client shows all exchanges with various servers in a single window. 