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

* Logging Filter

```
import logging

logging.basicConfig(level=logging.INFO)

class MyFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message

logger = logging.getLogger(__name__)
logger.addFilter(MyFilter())
logger.info('main')
logger.info('main password = "test"')
```
```
INFO:__main__:main
```

* Email
```
from email import message
import smtplib

smtp_host = 'smtp.naver.com'
smtp_port = 587

from_email = ''
to_email = ''
username = ''
password = ''

msg = message.EmailMessage()
msg.set_content('Test email')
msg['Subject'] = 'Test Email Sub'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
```