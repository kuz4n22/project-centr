import os
import sys
##sys.path.insert(0, '/home/g/genrikh/venv/project-##centr/lib/python3.11/site-packages/django')
##sys.path.insert(0, '/home/g/genrikh/public_html/apartment_planning/')
print('hello manage')

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apartment_planning.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()