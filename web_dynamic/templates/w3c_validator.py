#!/usr/bin/python3
"""
validataor
For HTML and CSS files.

Usage:
Simple file:
```
./w3c_validator.py index.html
```
Multiple files:
```
./w3c_validator.py index.html header.html styles/common.css
```

"""
import sys
import requests


def __print_stdout(msg):
    """display message

    """
    sys.stdout.write(msg)


def __print_stderr(msg):
    """display message
    """
    sys.stderr.write(msg)


def __analyse_html(file_path):
    """analyzing the html file in context
    """
    head = {'Content-Type': "text/html; charset=utf-8"}
    down = open(file_path, "rb").read()
    url = "https://validator.w3.org/nu/?out=json"
    reserve = requests.post(url, headers=head, data=down)
    result = []
    messages =  reserve.json().get('messages', [])
    for m in messages:
        result.append("[{}:{}] {}".format(file_path, m['lastLine'], m['message']))
    return result


def __analyse_css(file_path):
    """Start analyse of CSS file
    """
    data = {'output': "json"}
    file_c = {'file': (file_path, open(file_path, 'rb'), 'text/css')}
    url = "http://jigsaw.w3.org/css-validator/validator"
    r = requests.post(url, data=down, files=file_c)
    result = []
    errors = r.json().get('cssvalidation', {}).get('errors', [])
    for e in errors:
        res.append("[{}:{}] {}".format(file_path, e['line'], e['message']))
    return result


def __analyse(file_path):
    """check file
    """
    nb_errors = 0
    try:
        result = None
        if file_path.endswith('.css'):
            result = __analyse_css(file_path)
        else:
            result = __analyse_html(file_path)

        if len(result) > 0:
            for msg in result:
                __print_stderr("{}\n".format(msg))
                nb_errors += 1
        else:
            __print_stdout("{}: OK\n".format(file_path))

    except Exception as e:
        __print_stderr("[{}] {}\n".format(e.__class__.__name__, e))
    return nb_errors


def __files_loop():
    """iterates thru inputs
    """
    nb_errors = 0
    for file_path in sys.argv[1:]:
        nb_errors += __analyse(file_path)

    return nb_errors


if __name__ == "__main__":
    """Execute
    """
    if len(sys.argv) < 2:
        __print_stderr("usage: w3c_validator.py file1 file2 ...\n")
        exit(1)

    """if test passes display
    """
    sys.exit(__files_loop())

