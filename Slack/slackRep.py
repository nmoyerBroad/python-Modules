#!/usr/bin/env python

import logging
from slacker_log_handler import SlackerLogHandler, NoStacktraceFormatter

def reporting(msg,channel,bot):
    """
    this sends errors to a slack channel so that
    msg{str} --> error message
    """
    # Create slack handler
    slack_handler = SlackerLogHandler(channel, bot,stack_trace=True)

    # Create logger
    logger = logging.getLogger('Send Conf.')
    logger.addHandler(slack_handler)

    # Format
    formatter = NoStacktraceFormatter('%(asctime)s --> ERROR - %(message)s')
    slack_handler.setFormatter(formatter)
    slack_handler.setLevel(logging.DEBUG)

    # Message to send
    logger.error(msg)


def main():
    msg = 'msg'
    channel = 'chat key'
    bot = 'name'

    reporting(msg,channel,bot)

if __name__ == "__main__":
    main()
