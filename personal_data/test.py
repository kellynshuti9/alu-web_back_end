import logging
from filtered_logger import RedactingFormatter

message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=1234;"
record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)

formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(record))
