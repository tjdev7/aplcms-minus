
# APLCMS-Minus Project Setup

Welcome to the APLCMS-Minus project! This guide will help you set up your development environment, clone the repository, and start the project with DDEV, including the option of using GitHub Codespaces. We're here to assist you through the process.

## Prerequisites

Ensure you have the following installed or accessible:

- **GitHub Codespaces or Local Development Tools**: Have a GitHub account with Codespaces enabled for cloud-based development, or Docker/Colima for local development.
    - [Colima Installation Guide](https://github.com/abiosoft/colima)
    - [Docker Get Started Guide](https://www.docker.com/get-started)

- **DDEV**: Simplifies PHP applications setup with Docker.
    - [DDEV Documentation](https://ddev.readthedocs.io/en/stable/)

- **Git LFS**: For handling large files such as `aplcms-minus.sql.gz`.
    - [Git LFS Documentation](https://git-lfs.github.com/)

## Getting Started

### Option 1: Local Setup with DDEV

1. Clone the repository: `git clone git@github.com:APL-Innovation-Lab/aplcms-minus.git`
2. Enter the project directory: `cd aplcms-minus`
3. Initialize Git LFS: `git lfs install` followed by `git lfs pull`
4. Start DDEV: `ddev start`

### Option 2: GitHub Codespaces Setup

GitHub Codespaces offers a powerful, cloud-based environment. You can start with a pre-configured environment or set up a new Codespace:

- **Pre-configured Environment**: Select a pre-configured environment like "urban goldfish" from the Codespaces tab. These are ready for use, and you can check the status or launch the project using `ddev` commands. Open in VS Code for an enhanced experience or directly in a browser.

- **New Codespace Setup**: Create a new Codespace and run `time bash import.sh` in the Terminal to set up your environment and import the database, taking about 20-25 minutes. Manage your project with `ddev` commands. Opt to open in VS Code or a browser for convenience.

### Import Project Dependencies and Database

Regardless of your setup choice, run `bash import.sh` to import project dependencies and the database, ensuring your environment is up to date.

## Missing Images Handler

To address missing images during development, run the provided script to identify and download them, preserving the directory structure.

**Need Help?** Reach out for assistance with your development environment or any project-related questions. We aim to create a supportive environment for all contributors.

Thank you for contributing to the APLCMS-Minus project!