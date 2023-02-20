import sys
from logging import getLogger, StreamHandler, Formatter

from requests import Request, Response, PreparedRequest

# Настройки логгера
logger = getLogger()
logger.setLevel("INFO")

# Настройки
handler = StreamHandler(sys.stdout)
handler.setFormatter(Formatter('%(asctime)s | %(levelname)s | %(message)s', '%H:%M:%S'))
logger.addHandler(handler)


def log_request(request: PreparedRequest or Request):
    """Залогировать запрос

    Args:
        request: запрос
    """
    msg = f"HTTP-method:  {request.method}\n" \
          f"\t\t\t\t  URL:\t\t\t{request.url}\n" \
          f"\t\t\t\t  Headers:\t\t{request.headers}\n"
    msg += f"\t\t\t\t  Body: \t\t{request.body}" if getattr(request, 'body') else ''
    logger.log(msg=msg, level=20)


def log_response(response: Response):
    """Залогировать ответ

    Args:
        response: ответ
    """
    logger.log(
        msg=f"Code:    {response.status_code}\n"
            f"\t\t\t\t  Headers: {response.headers}\n"
            f"\t\t\t\t  Body:    {response.json()}",
        level=20
    )
