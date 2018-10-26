FROM selenium/standalone-chrome

USER root
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

COPY . /

RUN pip3 install -r requirements.txt

CMD [ "python3", "./get_bundles.py"]

