## Logging1


* logging
```
import logging

logging.basicConfig(level=logging.DEBUG)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')
```
```
CRITICAL:root:critical
ERROR:root:error
WARNING:root:warning
INFO:root:info
DEBUG:root:debug
```