from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
'''
create_engine() is a SQLAlchemy function that creates a database engine - the starting point for any SQLAlchemy application. It establishes a connection pool to your database.

Parameters in your code:
SQLALCHEMY_DATABASE_URL ("sqlite:///./todosapp.db")

The database connection string
sqlite:/// indicates SQLite database
./todosapp.db is the database file location (current directory)
connect_args={"check_same_thread": False}

SQLite-specific configuration dictionary
check_same_thread: False allows SQLite to be used with multiple threads
Important: SQLite by default only allows access from the same thread that created the connection. FastAPI runs async/multi-threaded, so this parameter is necessary.
Common parameters:
echo=True/False: Logs all SQL statements (useful for debugging)
pool_size: Number of connections to maintain in the pool
max_overflow: Maximum overflow connections beyond pool_size
pool_pre_ping: Verifies connections before using them
The engine object is used to create sessions that interact with the database.
'''

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

'''
sessionmaker()
A factory function that creates a configured Session class. Sessions are used to interact with the database (query, insert, update, delete).

Parameters in your code:
autocommit=False

Transactions must be explicitly committed using session.commit()
Provides transaction safety - changes aren't saved until you commit
autoflush=False

Prevents automatic flushing of pending changes to the database
Gives you more control over when database operations happen
bind=engine

Binds the session to your database engine
Tells the session which database to connect to
Usage:
declarative_base()
Creates a base class for your ORM models. All your database table models will inherit from this base class.

Purpose:
Maps Python classes to database tables
Provides SQLAlchemy functionality to your models
Maintains a registry of all mapped classes (metadata)
Usage:
The Base.metadata.create_all(bind=engine) creates all tables defined by models inheriting from Base.'''
