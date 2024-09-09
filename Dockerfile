# Use Ubuntu as the base image
FROM ubuntu:20.04

# Set the environment variable for non-interactive apt install
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages including Ansible, Python, and dependencies
RUN apt-get update && \
    apt-get install -y software-properties-common curl && \
    apt-add-repository --yes --update ppa:ansible/ansible && \
    apt-get install -y ansible python3-pip python3-apt sshpass && \
    apt-get clean

# Set the working directory
WORKDIR /ansible

# Copy your playbooks and roles into the Docker container (optional, if you want your local files inside the container)
COPY . /ansible

# Set the default entry point to bash so you can run commands manually
ENTRYPOINT ["/bin/bash"]
