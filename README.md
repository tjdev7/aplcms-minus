# APLCMS-Minus Project Setup

Welcome to the APLCMS-Minus project! This guide will walk you through setting up your development environment, cloning the repository, and starting the project with DDEV. If you're new to any of these tools or encounter any bumps along the way, don't hesitate to reach out. We're here to make your setup process as smooth as possible.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your machine:

- **Colima or Docker**: These tools allow you to containerize applications, ensuring consistency across development and production environments.
    - Colima installation guide: [Colima GitHub](https://github.com/abiosoft/colima)
    - Docker installation guide: [Docker Get Started](https://www.docker.com/get-started)

- **DDEV**: An open-source tool that simplifies the setup and management of PHP applications with Docker.
    - DDEV installation guide: [DDEV Documentation](https://ddev.readthedocs.io/en/stable/)

## Getting Started

Follow these steps to clone the repository and start your project with DDEV:

### 1. Clone the Repository

```bash
git clone git@github.com:APL-Innovation-Lab/aplcms-minus.git
```

### 2. Enter the Project Directory

Navigate to the project directory:

```bash
cd aplcms-minus
```

### 3. Start DDEV

Initialize the DDEV environment:

```bash
ddev start
```

### 4. Import Project Dependencies and Database

Run the import script to update dependencies and install a recent backup of the production database:

```bash
time bash import.sh
```

**Note:** The `import.sh` script updates the dependencies listed in `composer.json` and then installs the recent backup from `aplcms-minus.sql.gz`. The import process may take a few minutes and performs better on machines with a minimum of 8GB memory.

The installed backup is a recent snapshot from our production website at [library.austintexas.gov](https://library.austintexas.gov), with all personally identifiable information, such as email addresses, removed for privacy.

## Missing Images Handler

If you encounter missing images during development, we've prepared a script to help you identify and download these images from the production site. This ensures your local environment mirrors the live site as closely as possible.

### Script Usage

- Ensure you have `wget` installed on your system to download missing images.
- Run the provided script to identify missing images and download them while preserving the directory structure. 

**We're here to help!** If you need assistance setting up your development environment or have questions about the project, don't hesitate to reach out. Our goal is to ensure a welcoming and supportive environment for all contributors.

Thank you for contributing to the APLCMS-Minus project!
