Python3 script to return all available bunldes on HumbleBundle.com and email the updated list given a sender and recipent.

Dockerfile to run the whole thing as a container.
Must have a data folder for file storage mounted to the container. 

Run on Docker with:  
docker build . -t python-humble-bundle  
docker run -v /path/to/data:/data python-humble-bundle

Alternatively with Python:  

pip3 install -r requirements.txt  
python3 get_bundles.py
