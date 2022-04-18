
import logging
from server_echo import HTTPServer


logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    logger = logging.getLogger("Server")
    try:
        print("Enter \\c to stop")
        HTTPServer(('localhost', 5000)).run()
    except KeyboardInterrupt:
        logger.info("Stop")
