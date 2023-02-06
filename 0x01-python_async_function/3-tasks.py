#!/usr/bin/env python3
'''task 3'''

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ A function that returns an asyncio.Task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task