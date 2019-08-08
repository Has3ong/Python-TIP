## Config1

* configparser

```
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {
    'debug' : True
}
config['web_server'] = {
    'host':'127.0.0.1',
    'port': 80
}
config['db_server'] = {
    'host': '127.0.0.1',
    'port': 3306
}

with open('config.ini', 'w') as config_file:
    config.write(config_file)
```

config.ini
```
[DEFAULT]
debug = True

[web_server]
host = 127.0.0.1
port = 80

[db_server]
host = 127.0.0.1
port = 3306
```

```
config = configparser.ConfigParser()
config.read('config.ini')
```

* yaml
```
import yaml

with open('config.yml', 'w') as yaml_file:
    yaml.dump({
        'web_server':{
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host' : '127.0.0.1',
            'port': 3306
        }
    }, yaml_file, default_flow_style=False)
```

config.yml
```
db_server:
  host: 127.0.0.1
  port: 3306
web_server:
  host: 127.0.0.1
  port: 80
```

```
with open('config.yml', 'r') as yaml_file:
    data = yaml.load(yaml_file)
```

