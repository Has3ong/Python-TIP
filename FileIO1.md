## File I/O 1

* Templates

```
import string

with open('test.txt') as f:
    t = string.Template(f.read())
contents = t.substitute(name='Has3ong', contents= 'Github')
print(contents)
```
test.txt
```
Hi $name.

$contents

Hello Python Language
```
```
Hi Has3ong.

Github

Hello Python Language
```

* tarfile

```
import tarfile

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir)

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    with tr.extractfile('test_dir/sub/sub.txt') as f:
        print(f.read())
```

* zipfile

```
import glob
import zipfile

with zipfile.Zipfile('test.zip', 'w') as z:
    for f i nglob.glob('test_dir/**', recursive=True):
        z.write(f)

with zipfile.Zipfile('test.zip', 'r') as z:
    z.extractall('123123123')

* tempfile

```
import tempfile

with tempfile.TemporaryFie(mode='w+') as t:
    t.write('Hello Python')
    t.seek(0)
    print(t.read())

with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())
```
* subprocess
```
import subprocess
subprocess.run('ls -al', shell=True)
```