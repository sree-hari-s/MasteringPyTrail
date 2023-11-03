# Rain Alert Application 

Rain alert application utilizing [openweathermap](https://openweathermap.org) and [twilio](https://www.twilio.com). Checks the weather data of the next 12 hours of the day and send a message as an SMS if the weather is rainy.

## Installation

- Create a virtual environment and install the required packages.

    ```bash
        virtualenv env

        env\Scripts\activate

        pip install - r requirements.txt
    ```

- Create an account in [openweathermap](https://openweathermap.org) and [twilio](https://www.twilio.com) for getting API keys for the environment variables.
- Update the values in the `.env` file matching the `.env_sample` file
- Run the application updating your Latitude and Longitude.
  - Note: Find your latitude and longitude using this [link](https://www.latlong.net/)

    ```bash
        python main.py
    ```
