import sys
import socket
import getopt
import threading
import subprocess

#define global variables
listen             = false
command            = false
upload             = false
execure            = ""
target             = ""
upload_destination = ""
port               = 0