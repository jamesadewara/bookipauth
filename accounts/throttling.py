from rest_framework.throttling import SimpleRateThrottle
import redis

class RedisThrottle(SimpleRateThrottle):
    # Define rate limit as 100 requests per 60 seconds
    rate = '100/hour'  # You can change this rate as needed

    def get_cache_key(self, request, view):
        # Use IP address to limit requests per IP
        return self.cache_format % {'ip': self.get_ident(request)}

    def allow_request(self, request, view):
        # Get the IP address of the requestor
        ip = self.get_ident(request)
        
        # Use Redis to count the requests for this IP
        redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
        current_count = redis_client.get(ip)

        if current_count is None:
            redis_client.set(ip, 1, ex=60)  # Set TTL of 60 seconds for each IP
        else:
            redis_client.incr(ip)

        if int(current_count or 0) < 100:
            return True  # Allow the request
        else:
            return False  # Throttle the request
