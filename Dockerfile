FROM ubuntu:20.04
RUN apt-get update
# install tzdata to avoid interruption
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN apt-get install -y python3 libreoffice imagemagick
# allow imagemagick to generate PDFs
RUN sed -i "/PDF/d" /etc/ImageMagick-6/policy.xml