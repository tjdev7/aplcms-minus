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

GitHub Codespaces provides a powerful, cloud-based development environment. For the APLCMS-Minus project, start with setting up a new Codespace:

- **New Codespace Setup**: Create a new Codespace from the Codespaces tab in the GitHub repository. The first step is to run `time bash import.sh` in the Terminal, which sets up your environment and imports the database, taking about 20-25 minutes. Afterwards, you can manage your project with `ddev` commands. For an enhanced development experience, it's recommended to open the Codespace in VS Code, but you can also work directly in a browser for convenience.

### Import Project Dependencies and Database

Regardless of your setup choice, run `bash import.sh` to import project dependencies and the database, ensuring your environment is up to date.

## Missing Images Handler

If you encounter missing images during development, run the provided script to identify and download them, preserving the directory structure.

```python3
python3 missing.py
```

**Need Help?** If you need assistance with your development environment or have questions about the project, don't hesitate to reach out. Our aim is to create a supportive environment for all contributors.

Thank you for contributing to the APLCMS-Minus project!
