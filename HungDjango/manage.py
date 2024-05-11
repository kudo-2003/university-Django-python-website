import os
import sys
import webbrowser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8000/shop")
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HungDjango.settings')
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
    open_browser()
    main()
