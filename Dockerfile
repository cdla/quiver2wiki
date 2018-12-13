From python:3.6-alpine

# docker build -t cdla/docker2wiki .
# docker run cdla/docker2wiki


RUN mkdir /app
ADD . /app
RUN python /app/setup.py install

ENTRYPOINT ["quiver2wiki"]
