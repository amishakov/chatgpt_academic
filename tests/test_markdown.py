md = """
You can use the following Python script to rename files matching the pattern '* - 副本.tex' to '* - wushiguang.tex' in a directory:

```python
import os

# Directory containing the files
directory = 'Tex/'

for filename in os.listdir(directory):
    if filename.endswith(' - 副本.tex'):
        new_filename = filename.replace(' - 副本.tex', ' - wushiguang.tex')
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
```

Replace 'Tex/' with the actual directory path where your files are located before running the script.
"""


md = """
Following code including wrapper

```mermaid
graph TD
    A[Enter Chart Definition] --> B(Preview)
    B --> C{decide}
    C --> D[Keep]
    C --> E[Edit Definition]
    E --> B
    D --> F[Save Image and Code]
    F --> B



```

<details>
<summary><b>My section header in bold</b></summary>

Any folded content here. It requires an empty line just above it.

</details>

"""
def validate_path():
    import os, sys

    os.path.dirname(__file__)
    root_dir_assume = os.path.abspath(os.path.dirname(__file__) + "/..")
    os.chdir(root_dir_assume)
    sys.path.append(root_dir_assume)


validate_path()  # validate path so you can run from base directory
from toolbox import markdown_convertion
from shared_utils.advanced_markdown_format import markdown_convertion_for_file
# with open("gpt_log/default_user/shared/2024-04-22-01-27-43.zip.extract/translated_markdown.md", "r", encoding="utf-8") as f:
    # md = f.read()
html = markdown_convertion_for_file(md)
# print(html)
with open("test.html", "w", encoding="utf-8") as f:
    f.write(html)


# TODO: 列出10个经典名著