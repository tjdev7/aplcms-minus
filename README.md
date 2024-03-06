
# APLCMS-Minus Project Setup

Welcome to the APLCMS-Minus project! This guide will walk you through setting up your development environment, cloning the repository, and starting the project with DDEV, including the option of using GitHub Codespaces. If you're new to any of these tools or encounter any bumps along the way, don't hesitate to reach out. We're here to make your setup process as smooth as possible.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your machine or accessible in your development environment:

- **GitHub Codespaces or Local Development Tools**:
    - For GitHub Codespaces, ensure you have a GitHub account with Codespaces enabled.
    - For local development, you will need Docker or Colima to containerize applications, ensuring consistency across environments.
        - Colima installation guide: [Colima GitHub](https://github.com/abiosoft/colima)
        - Docker installation guide: [Docker Get Started](https://www.docker.com/get-started)

- **DDEV**: An open-source tool that simplifies the setup and management of PHP applications with Docker.
    - DDEV installation guide: [DDEV Documentation](https://ddev.readthedocs.io/en/stable/)

## Getting Started

You have the option to set up your environment locally using DDEV or using GitHub Codespaces for a cloud-based development environment.

### Option 1: Local Setup with DDEV

Follow these steps to clone the repository and start your project with DDEV locally:

1. **Clone the Repository**

    ```bash
    git clone git@github.com:APL-Innovation-Lab/aplcms-minus.git
    ```

2. **Enter the Project Directory**

    Navigate to the project directory:

    ```bash
    cd aplcms-minus
    ```

3. **Start DDEV**

    Initialize the DDEV environment:

    ```bash
    ddev start
    ```

### Option 2: GitHub Codespaces Setup

1. **Open the Repository in GitHub Codespaces**

    Navigate to the GitHub repository and use the Codespaces tab to create a new codespace.

2. **Codespaces will automatically prepare your development environment.**

### Import Project Dependencies and Database

Regardless of the chosen method, you should import project dependencies and the database:

- **Run the import script to update dependencies and install a recent backup of the production database:**

    ```bash
    time bash import.sh
    ```

    **Note:** The `import.sh` script updates dependencies and installs a recent backup from `aplcms-minus.sql.gz`. This process may take up to 20 minutes due to the size of the database but is necessary only occasionally to refresh your environment with the latest data.

The installed backup is a recent snapshot from our production website at [library.austintexas.gov](https://library.austintexas.gov), with all personally identifiable information removed for privacy.

## Missing Images Handler

If you encounter missing images during development, we've prepared a script to help you identify and download these images from the production site, ensuring your environment mirrors the live site as closely as possible.

### Script Usage

- Ensure you have `wget` installed on your system for downloading missing images.
- Run the provided script to identify missing images and download them while preserving the directory structure. 

**We're here to help!** If you need assistance setting up your development environment or have questions about the project, don't hesitate to reach out. Our goal is to ensure a welcoming and supportive environment for all contributors.

Thank you for contributing to the APLCMS-Minus project!
