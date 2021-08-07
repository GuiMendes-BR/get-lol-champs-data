import queue
import threading

from bots.base_bot import BaseBot



class BotThread(threading.Thread):

    def __init__(self, bot:BaseBot, out_queue:queue, args):
        self.bot = bot()
        self.args = args
        self.out_queue= out_queue
        threading.Thread.__init__(self, args=args)

    def run(self):
        self.bot.run(self.args, out_queue=self.out_queue)
        return None
