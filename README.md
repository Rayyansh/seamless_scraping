# Seamless Scraper Project

Welcome to the Seamless Scraper project. This project uses Selenium to scrape data from the Seamless website. Follow these instructions to set up your local environment and get started.

## Prerequisites

- [Python 3.8 or higher](https://www.python.org/downloads/)
- Chrome browser and [ChromeDriver](https://chromedriver.chromium.org/) installed and available in your system's PATH

## Setting Up Your Local Environment

### Step 1: Get the project code

You have two options to get the project code:

- **Option 1: Clone the repository**

    First, clone the repository to your local machine and navigate into the project directory:

    ```shell
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

- **Option 2: Download the repository as a ZIP file**

    Download the ZIP file from the repository on GitHub, extract it to your local machine, and navigate into the project directory.

### Step 2: Set up a virtual environment

To create and activate a virtual environment:

- **On Windows**:

    1. Install `virtualenv`:

        ```shell
        pip install virtualenv
        ```

    2. Create a virtual environment:

        ```shell
        virtualenv venv
        ```

    3. Activate the virtual environment:

        ```shell
        venv\Scripts\activate
        ```

- **On macOS**:

    1. Install `virtualenv`:

        ```shell
        pip install virtualenv
        ```

    2. Create a virtual environment:

        ```shell
        virtualenv venv
        ```

    3. Activate the virtual environment:

        ```shell
        source venv/bin/activate
        ```

### Step 3: Install the required packages

With the virtual environment activated, install the packages listed in `requirements.txt`:

```shell
pip install -r requirements.txt```

### Running the Scraper
After setting up the environment and installing the required packages, you can run the scraper using the following command in the terminal:

```shell
python main.py
```
