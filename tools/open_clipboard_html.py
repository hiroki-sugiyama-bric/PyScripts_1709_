import os
import pyperclip
import subprocess
from tempfile import NamedTemporaryFile

def open_clipboard_html():
    html = pyperclip.paste()
    ntf = NamedTemporaryFile(delete=False)
    ntf.write(html.encode())

    print(html)
    os.rename(ntf.name, ntf.name + '.html')
    ntf.name += '.html'

    rc = subprocess.run(['open', ntf.name]).returncode

    # os.remove(ntf.name)

if __name__ == '__main__':
    open_clipboard_html()
