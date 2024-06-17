# Install dependencies on virtual environment
- Run the command ". venv.sh" in bash to initialize and activate the virtual environment and install the dependencies contained in requirements.txt.
- To exit the virtual environment, run the command "deactivate".
- To activate the virtual environment, run the command ". activate.sh".

# Double check the interpreter
- Make sure the interpreter is set to the python version of your virtual environment. In VSCode the interpreter can be found in the bottom right corner of the window.

# Add environment file
- Don't forget to manually add the file .env which contains:

OPENAI_KEY="YOUR_API_KEY"
CONNECTION_STRING="postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]"

# Adding dependencies to the automated installation process
- To add new dependencies to the automated process, install the dependencies and write them to requirements.txt afterwards by running the following command: pip freeze requirements.txt

# Starting the application
- To start the application, run the command "python main.py" or simply "flask run".

# Database
- Using pgAdmin create a postgres database, you can name this anything, make sure to use that name in the .env connection_string

# Testing database connection
- To test whether the database connection is standing and stable, send a GET request to the endpoint ".../testdb/{database_name}"
- Replace {database_name} by one of the following, dependent on which context you are using:
    postgresql

# Stopping the application
- To stop the application, hit ctrl + C