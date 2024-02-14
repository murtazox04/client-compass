# Client Compass

Client Compass is a Django-based web application designed to help businesses manage their clients, employees, and product orders effectively. It provides features such as client and employee statistics, order tracking, and product management.

## Project Goals

The main goals of the Client Compass project are:

- Provide a user-friendly interface for managing clients, employees, products, and orders.
- Generate insightful statistics and reports to help businesses make informed decisions.
- Ensure data integrity and security through robust database management and user authentication mechanisms.

## Manual Project Launch

To manually launch the Client Compass project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/murtazox04/client-compass.git
   ```

2. Navigate to the project directory:

   ```bash
   cd client-compass
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser account (for admin access):

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application in your web browser at [http://localhost:8000](http://localhost:8000).

## Docker Launch

To launch the Client Compass project using Docker, ensure you have Docker installed on your system. Then, follow these steps:

1. Create a `.env` file in the project root directory and define the following environment variables:

   ```plaintext
   ENV_TYPE=your_env_type
   DEBUG=true_or_false
   DB_NAME=client_compass_db
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   DB_PORT=your_db_port
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

3. Access the application in your web browser at [http://localhost:8000](http://localhost:8000).

## Project Testing

To run tests for the Client Compass project, execute the following command:

```bash
python manage.py test api
```

This command will run all tests located in the `api` app.

## Contributing

Contributions to the Client Compass project are welcome! If you have ideas for new features, find bugs, or want to improve documentation, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
