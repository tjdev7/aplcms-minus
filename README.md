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

- **Git LFS**: To handle large files such as `aplcms-minus.sql.gz` which is managed with Git Large File Storage.
    - Git LFS installation guide: [Git LFS Documentation](https://git-lfs.github.com/)

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

3. **Ensure Git LFS is Initialized**

    Before pulling the large files, ensure Git LFS is initialized:

    ```bash
    git lfs install
    ```

4. **Pull LFS Files**

    Make sure all LFS-tracked files are correctly downloaded:

    ```bash
    git lfs pull
    ```

5. **Start DDEV**

    Initialize the DDEV environment:

    ```bash
    ddev start
    ```

### Option 2: GitHub Codespaces Setup

GitHub Codespaces provides a powerful, customizable, and scalable cloud-based development environment. Here's how to access and use a Codespace for the APLCMS-Minus project:

1. **Accessing a Codespace**

    GitHub Codespaces provides a flexible and powerful development environment, allowing you to choose between accessing a pre-configured environment or setting up a new one. Here are your options:

1. **Accessing a Codespace**

    GitHub Codespaces offers a seamless and flexible development experience, allowing you to choose between jumping into a pre-configured environment or starting fresh with a new setup. Below are your options, along with the added flexibility of using VS Code or a browser:

    - **Access a Pre-configured Environment**: Navigate to the GitHub repository and use the Codespaces tab to select an environment that already has the development environment configured and the database imported. Look for environments like "urban goldfish" or other similarly named temporary environments. These environments are ready to use, and you can immediately check the status in the Terminal with `ddev status` or launch the project using `ddev launch`. For an enhanced development experience, it's recommended to open the Codespace with VS Code. However, you also have the convenience of working directly in a browser, offering quick access without the need for local installations.

    - **Set Up a New Codespace**: If you choose to set up a new Codespace, create one from the Codespaces tab in the GitHub repository. The first step for a new Codespace is to run the `import.sh` script, which takes about 20-25 minutes to complete. This script will set up your environment and import the database. To begin, open the Terminal within the IDE and execute:

        ```bash
        time bash import.sh
        ```

    After the import process completes, you can manage the project using DDEV commands such as `ddev status` to check the environment status or `ddev launch` to start the project. Similar to accessing a pre-configured environment, you can choose to open the new Codespace in VS Code for a comprehensive development experience or directly in a browser for convenience.


    - **Set Up a New Codespace**: If you prefer to set up a new Codespace, create one from the Codespaces tab in the GitHub repository. The first step in a new Codespace is to run the `import.sh` script. This script takes about 20-25 minutes to complete and will set up your environment and import the database. To start, open the Terminal within the IDE and execute:

        ```bash
        time bash import.sh
        ```

    After the import process completes, you can manage the project using DDEV commands such as `ddev status` to check the environment status or `ddev launch` to start the project.


2. **Opening the Codespace**

    - Once your codespace is ready, you can open it directly in your browser or in VS Code for a more integrated development experience.

3. **Starting the DDEV Project**

    - Upon starting your codespace, open the Terminal within the IDE and execute the following command to start and launch the DDEV project:

        ```bash
        ddev launch
        ```

    This command initializes your development environment and launches the project, making it accessible for further development and testing.

### Import Project Dependencies and Database

Regardless of the chosen method, you should import project dependencies and the database:

- **Run the import script to update dependencies and install a recent backup of the production database:**

    ```bash
    bash import.sh
    ```

    **Note:** The `import.sh` script updates dependencies and installs a recent backup from `aplcms-minus.sql.gz`. This process may take up to 20 minutes due to the size of the database but is necessary only occasionally to refresh your environment with the latest data.

The installed backup is a recent snapshot from our production website at [library.austintexas.gov](https://library.austintexas.gov), with all personally identifiable information removed for privacy.

## Missing Images Handler

If you encounter missing images during development, we've prepared a script to help you identify and download these images from the production site, ensuring your environment mirrors the live site as closely as possible.

### Script Usage

- Run the provided script to identify missing images and download them while preserving the directory structure:

    ```python3
    python3 missing.py
    ```

**We're here to help!** If you need assistance setting up your development environment or have questions about the project, don't hesitate to reach out. Our goal is to ensure a welcoming and supportive environment for all contributors.

Thank you for contributing to the APLCMS-Minus project!
