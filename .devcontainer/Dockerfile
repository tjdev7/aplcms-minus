# Use a base image that supports Docker, as DDEV requires Docker to run
FROM docker:20.10.7

# Install dependencies
RUN apk add --no-cache bash curl git

# Install DDEV using the official installation script
RUN curl -L https://raw.githubusercontent.com/drud/ddev/master/scripts/install_ddev.sh | bash

# Consider adding any PHP 8.1 extensions or other tools specific to your project
