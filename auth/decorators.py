from django.conf import settings
from django.http import JsonResponse
from functools import wraps
from jose import jwt

def jwt_required(f):
    @wraps(f)
    def decorator(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return JsonResponse({'message': 'Authorization header is missing'}, status=401)
        
        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            request.user = payload['user']
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'Token has expired'}, status=401)
        except jwt.JWTError:
            return JsonResponse({'message': 'Invalid token'}, status=401)
        
        return f(request, *args, **kwargs)
    
    return decorator
