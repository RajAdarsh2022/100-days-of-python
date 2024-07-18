# Cafe API

A Flask-based API to manage a database of cafes. The API allows you to retrieve, add, update, and delete cafe information.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cafe-api.git
    cd cafe-api
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the project root.
    - Add your API key:
        ```
        API_KEY=your_secret_api_key
        ```

5. Run the application:
    ```bash
    python main.py
    ```

## Routes

### Home

- **Endpoint**: `/`
- **Method**: GET
- **Description**: Renders the home page.
- **Response**: HTML content.

### Get All Cafes

- **Endpoint**: `/all`
- **Method**: GET
- **Description**: Retrieves all cafes from the database.
- **Response**: 
    ```json
    {
        "cafes": [
            {
                "id": 1,
                "name": "Cafe Name",
                "map_url": "https://...",
                "img_url": "https://...",
                "location": "Location",
                "seats": 50,
                "has_toilet": true,
                "has_wifi": true,
                "has_sockets": false,
                "can_take_calls": true,
                "coffee_price": "$4.50"
            },
            ...
        ]
    }
    ```

### Get Random Cafe

- **Endpoint**: `/random`
- **Method**: GET
- **Description**: Retrieves a random cafe from the database.
- **Response**: 
    ```json
    {
        "id": 1,
        "name": "Cafe Name",
        "map_url": "https://...",
        "img_url": "https://...",
        "location": "Location",
        "seats": 50,
        "has_toilet": true,
        "has_wifi": true,
        "has_sockets": false,
        "can_take_calls": true,
        "coffee_price": "$4.50"
    }
    ```

### Search Cafes by Location

- **Endpoint**: `/search`
- **Method**: GET
- **Description**: Retrieves cafes based on a specific location.
- **Query Parameters**: 
    - `loc` (string): The location to search for cafes.
- **Response**: 
    ```json
    {
        "cafes": [
            {
                "id": 1,
                "name": "Cafe Name",
                "map_url": "https://...",
                "img_url": "https://...",
                "location": "Location",
                "seats": 50,
                "has_toilet": true,
                "has_wifi": true,
                "has_sockets": false,
                "can_take_calls": true,
                "coffee_price": "$4.50"
            },
            ...
        ]
    }
    ```
    If no cafes are found:
    ```json
    {
        "msg": "No cafes as per ur location!"
    }
    ```

### Add New Cafe

- **Endpoint**: `/add`
- **Method**: POST
- **Description**: Adds a new cafe to the database.
- **Form Data**: 
    - `name` (string): Cafe name.
    - `map_url` (string): URL to the cafe's map location.
    - `img_url` (string): URL to the cafe's image.
    - `location` (string): Cafe location.
    - `seats` (int): Number of seats.
    - `has_toilet` (bool): Whether the cafe has a toilet.
    - `has_wifi` (bool): Whether the cafe has Wi-Fi.
    - `has_sockets` (bool): Whether the cafe has power sockets.
    - `can_take_calls` (bool): Whether calls can be taken in the cafe.
    - `coffee_price` (string, optional): Price of the coffee.
- **Response**: 
    ```json
    {
        "mssg": "successfully added"
    }
    ```

### Update Coffee Price

- **Endpoint**: `/update-price/<int:cafe_id>`
- **Method**: PATCH
- **Description**: Updates the coffee price of a specific cafe.
- **URL Parameters**: 
    - `cafe_id` (int): The ID of the cafe to update.
- **Query Parameters**: 
    - `new_price` (string): The new coffee price.
- **Response**: 
    ```json
    {
        "mssg": "Data updated successfully"
    }
    ```
    If no new price is provided:
    ```json
    {
        "mssg": "New price must be passed as a parameter"
    }
    ```
    If cafe is not found:
    ```json
    {
        "mssg": "Sorry a cafe with that id was not found in the database."
    }
    ```

### Delete Cafe

- **Endpoint**: `/report-closed/<int:cafe_id>`
- **Method**: DELETE
- **Description**: Deletes a cafe from the database.
- **URL Parameters**: 
    - `cafe_id` (int): The ID of the cafe to delete.
- **Query Parameters**: 
    - `api-key` (string): The API key for authorization.
- **Response**: 
    ```json
    {
        "mssg": "Cafe deleted successfully"
    }
    ```
    If the cafe is not found:
    ```json
    {
        "mssg": "The cafe that u r looking for doesn't exist"
    }
    ```
    If the API key is incorrect:
    ```json
    {
        "mssg": "Sorry, that's not allowed. Make sure you have the correct api-key"
    }
    ```

## Models

### Cafe

- `id` (int): Primary key.
- `name` (string): Cafe name.
- `map_url` (string): URL to the cafe's map location.
- `img_url` (string): URL to the cafe's image.
- `location` (string): Cafe location.
- `seats` (int): Number of seats.
- `has_toilet` (bool): Whether the cafe has a toilet.
- `has_wifi` (bool): Whether the cafe has Wi-Fi.
- `has_sockets` (bool): Whether the cafe has power sockets.
- `can_take_calls` (bool): Whether calls can be taken in the cafe.
- `coffee_price` (string): Price of the coffee.
