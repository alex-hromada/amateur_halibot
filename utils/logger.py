import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup as many loggers as you want"""

    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    
    handler = RotatingFileHandler(f'logs/{log_file}', maxBytes=2000000, backupCount=5)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    # If you want to log to console as well:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

# Create loggers
discord_logger = setup_logger('discord', 'discord.log')
twitch_logger = setup_logger('twitch', 'twitch.log')
main_logger = setup_logger('main', 'main.log')