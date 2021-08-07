from os import name
import ast
from threads.bot_thread import BotThread

import time
import threading
import queue

class MultiThreadBot:
    
    def __init__(self, max_threads=None,
                 bot=None,
                 items_to_process=None):
        self.max_threads = max_threads
        self.bot = bot
        self.items_to_process = items_to_process
        self.queue = queue.Queue()

    def print_active_threads(self):
        print("  Active threads:")
        for thread in threading.enumerate(): 
            if thread.name in [str(item) for item in self.items_to_process]:
                print("-> "+ thread.name)
        print("")
        print(f"{self.queue.qsize()} items have been processed")


    def run(self):

        scraping_threads = []

        max_active_thread = threading.active_count() + self.max_threads - 1
        for item_count, item in enumerate(self.items_to_process):
            # If we've reached the limit of active threads, we should wait for a thread to finish
            while threading.active_count() > max_active_thread:
                time.sleep(0)

            # Here we create a new bot thread
            # The out_queue argument will be populated by the bot with it's result
            # The args are the input parameters that will be used by the bot
            thread = BotThread(bot=self.bot, out_queue=self.queue, args=item)
            thread.name = str(item)
            thread.start()
            scraping_threads.append(thread)

            self.print_active_threads()

        for thread in scraping_threads:
            try:
                thread.join()
            except:
                continue

        # During the execution of a BotThread object, it populates a queue and we return the populated queue as a list.
        # The programmer should be mindful that this list won't be in the same order of 
        # self.items_to_process since the queue is populated in parallel.
        return list(self.queue.queue)