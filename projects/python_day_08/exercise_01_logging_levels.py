"""Week 3 - Tuesday - Exercise 1: the five logging levels."""

import logging

# Configure logging: show the time, the level name, and the message.
logging.basicConfig(
    level=logging.WARNING,  # the threshold: show DEBUG and everything above
    format="%(asctime)s | %(levelname)-8s | %(message)s",
)

logging.debug("Opening CAN log file")
logging.info("Parsed 5000 frames successfully")
logging.warning("Skipped 1 malformed line")
logging.error("Could not open file: can_log.csv")
logging.critical("Parser cannot continue")