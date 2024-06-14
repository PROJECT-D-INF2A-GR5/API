import re

def convert_connection_string(sqlalchemy_connection_string):
    # Regular expression to match the different parts of the connection string
    pattern = re.compile(
        r'postgresql\+psycopg2://(?P<user>[^:]+):(?P<password>[^@]+)@(?P<host>[^:]+):(?P<port>\d+)/(?P<dbname>.+)'
    )

    # Match the pattern with the provided connection string
    match = pattern.match(sqlalchemy_connection_string)
    
    if not match:
        raise ValueError("Invalid SQLAlchemy connection string format")
    
    # Extract the matched components
    components = match.groupdict()

    # Format the components into the psycopg2 connection string
    psycopg2_connection_string = (
        f"dbname='{components['dbname']}' "
        f"user='{components['user']}' "
        f"password='{components['password']}' "
        f"host='{components['host']}' "
        f"port='{components['port']}'"
    )

    return psycopg2_connection_string