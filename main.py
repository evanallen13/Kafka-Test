import redis

def redis_set(key, value, host='localhost', port=6379, db=0, expiration=None):
    """
    Store data in Redis (equivalent to a POST operation).
    
    Args:
        key (str): The key under which to store the data
        value (str/int/dict/list): The value to store
        host (str): Redis server hostname
        port (int): Redis server port
        db (int): Redis database number
        expiration (int, optional): Time in seconds after which the key will expire
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Connect to Redis
        r = redis.Redis(host=host, port=port, db=db, decode_responses=True)
        
        # Check connection
        r.ping()
        
        # Set the value
        if expiration:
            return r.setex(key, expiration, value)
        else:
            return r.set(key, value)
    except redis.ConnectionError as e:
        print(f"Connection Error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def redis_get(key, host='localhost', port=6379, db=0):
    """
    Retrieve data from Redis (equivalent to a GET operation).
    
    Args:
        key (str): The key to retrieve
        host (str): Redis server hostname
        port (int): Redis server port
        db (int): Redis database number
        
    Returns:
        The value associated with the key, or None if the key does not exist
    """
    try:
        # Connect to Redis
        r = redis.Redis(host=host, port=port, db=db, decode_responses=True)
        
        # Check connection
        r.ping()
        
        # Get the value
        return r.get(key)
    except redis.ConnectionError as e:
        print(f"Connection Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Set a value in Redis
    success = redis_set("example_key", "example_value", expiration=3600)  # expires in 1 hour
    if success:
        print("Value successfully stored in Redis")
    
    # Get a value from Redis
    value = redis_get("example_key")
    if value:
        print(f"Retrieved value: {value}")
    else:
        print("Key not found or error occurred")