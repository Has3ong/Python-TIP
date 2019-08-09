# Library_Tool

* re.match

```
import re

m = re.match('a.c', 'abc')
print(m)
```

```
<_sre.SRE_Match object; span=(0, 3), match='abc'>
```

* re.search

```
import re

m = re.search('a.c', 'test abc test')
print(m)
```
```
<_sre.SRE_Match object; span=(5, 8), match='abc'>
```

* re.findall

```
m = re.findall('a.c', 'test abc test')
print(m)
```
```
['abc']
```

* re.finditer

```
m = re.finditer('a.c', 'test abc test')
print([w.group() for w in m])
```
```
['abc']
```