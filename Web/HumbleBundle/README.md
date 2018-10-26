Python3 script to return all available bunldes on HumbleBundle.com and email the updated list given a sender and recipent.

Dockerfile to run the whole thing as a container.
Must have a data folder for file storage mounted to the container. 

Run with:  docker run -it -v /path/to/data:/data python-humble-bundle
