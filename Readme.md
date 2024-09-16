# Bengaluru Home Price Prediction

This project is a web application built using Django that predicts home prices in Bengaluru based on various features such as area, number of bedrooms, number of bathrooms, and location. The prediction model is built using machine learning techniques.

## Features

- Predict home prices based on user input
- User-friendly interface with forms for input
- Responsive design

## Technologies Used

- Django
- HTML/CSS
- JavaScript (jQuery)
- Bootstrap
- Machine Learning (scikit-learn, pandas, numpy)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Soumen3/Bengaluru_Home_Price_Prediction.git
    cd Bengaluru_Home_Price_Prediction
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r req.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

6. Open your browser and go to `http://127.0.0.1:8000/`

## Usage

1. Enter the area in square feet.
2. Select the number of bedrooms (BHK).
3. Select the number of bathrooms.
4. Choose the location from the dropdown.
5. Click on the "Predict" button to get the predicted home price.

## Project Structure

- `bengaluru_home_price_prediction/`: Main Django project directory
- `prediction/`: Django app for home price prediction
- `static/`: Static files (CSS, JavaScript)
- `templates/`: HTML templates
- `req.txt`: List of required Python packages

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [scikit-learn](https://scikit-learn.org/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
