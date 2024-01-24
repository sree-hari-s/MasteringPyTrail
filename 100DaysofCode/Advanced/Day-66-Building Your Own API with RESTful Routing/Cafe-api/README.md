# Cafe Finder API

Welcome to the Cafe Finder API! This API allows you to explore and manage information about various cafes. You can retrieve random cafes, get a list of all cafes, search for cafes at specific locations, add new cafes, update cafe prices, and delete cafes.

## Installation

1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the Flask application:

    ```bash
    python main.py
    ```

   The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## API Documentation

Explore the API endpoints and functionalities using the [Cafe Finder API Documentation](https://documenter.getpostman.com/view/27931839/2s9YynnQFt).

## Endpoints

- **GET /random:** Retrieve information about a random cafe.
- **GET /all:** Get a list of all cafes.
- **GET /search?loc={location}:** Search for cafes at a specific location.
- **POST /add:** Add a new cafe to the database.
- **PATCH /update-price/{id}:** Update the coffee price of a cafe.
- **DELETE /report-closed/{id}?api_key={api_key}:** Delete a cafe from the database. (Requires a valid API key)

## Usage

1. **Retrieve a Random Cafe:**
   - Endpoint: `/random`
   - Method: `GET`
   - Retrieve information about a randomly selected cafe.

2. **Get a List of All Cafes:**
   - Endpoint: `/all`
   - Method: `GET`
   - Get a list of all cafes in the database.

3. **Search for Cafes at a Specific Location:**
   - Endpoint: `/search?loc={location}`
   - Method: `GET`
   - Search for cafes at a specified location.

4. **Add a New Cafe:**
   - Endpoint: `/add`
   - Method: `POST`
   - Add a new cafe to the database.

5. **Update Cafe Price:**
   - Endpoint: `/update-price/{id}`
   - Method: `PATCH`
   - Update the coffee price of a specific cafe.

6. **Delete a Cafe:**
   - Endpoint: `/report-closed/{id}?api_key={api_key}`
   - Method: `DELETE`
   - Delete a cafe from the database. (Requires a valid API key)

## Important Note

To perform certain actions (e.g., deleting a cafe), an API key is required. Use the key `TopSecretAPIKey` as the `api_key` parameter.

Feel free to explore and enjoy the Cafe Finder API! If you have any questions or feedback, refer to the API documentation or contact the project maintainers.# Cafe Finder API
