import redis

# Create a connection pool to the Redis database
try:
    pool = redis.ConnectionPool(
        host='localhost',
        port=6379,
        password='123456',
        db=2,
        max_connections=20
    )
    print("Connection pool created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

