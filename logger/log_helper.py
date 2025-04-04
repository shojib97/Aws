import json
import logging
import os


class LoggerHelper:
    logLevel = os.environ.get("LOGGING_LEVEL", logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel(logLevel)
    # logger.addHandler(logging.StreamHandler())

    def log_info(self, event, status, **record):
        """
        Log format function to remove duplication
        logger.info

        Args:
            event: str: event name
            status: str: status of the event
            record: dict: additional information to log
        """
        self.logger.info(
            json.dumps(
                {
                    "event": event,
                    "status": status,
                    **record,
                },
                default=str,
            )
        )
        return True

    def log_error(self, event, status, **record):
        """
        Log format function to remove duplication
        logger.error

        Args:
            event: str: event name
            status: str: status of the event
            record: dict: additional information to log
        """
        self.logger.error(
            json.dumps(
                {
                    "event": event,
                    "status": status,
                    **record,
                },
                default=str,
            )
        )
        return True
