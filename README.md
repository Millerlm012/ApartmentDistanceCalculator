# Apartment Distance Calculator

## About

For starters, the name of the program is still in progress. With that out of the way, the purpose of this program is to generate a csv of all apartments in a provided city, state, and order them from least to greatest distance from a specified location.

## Setup

If you're wanting to run this program locally on your own machine, please follow the following setup instrutions.

1. Ensure you have `python3` installed on your machine. You can install `python3` [here](https://www.python.org/downloads/).
2. Once you have `python3` installed, create a virtual environment for the project, activate the newly created virtual environment, and install the required packages with the following command:

```
# please ensure you execute this command from a terminal that is in the same directory as the requirements.txt
pip install -r requirements.txt
```

3. After setting up you're environment you will need to create an API KEY to utilize [Google's Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/overview). [Click here](https://developers.google.com/maps/documentation/distance-matrix/get-api-key#creating-api-keys) to find instructions on how to create your key.
4. Once your key has been created, please create a `.env` file in the `srv/` directory. In the `.env`, please add the following:

```
DISTANCE_MATRIX_KEY=your_newly_created_distance_api_key
```

5. Finally, you should be able to execute `srv/main.py`, follow the prompts, and receive a `result.csv`! 

If you run into any issues, please contact Landon Miller at millerlm012@gmail.com.


NOTE: If you need assistance with installing `python3` or creating a virtual environment, feel free to check out my [blog post](https://landon-miller.com/blog/posts/python-tutorials/getting-started) that covers these topics!
