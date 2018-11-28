#!/usr/bin/env python

import time
import curses
from reworker import Worker


def monitor():
    m = Worker()
    stdscr = curses.initscr()
    try:
        while 1:
            i = 0
            stdscr.clear()
            for w in m.list():
                stdscr.addstr(i, 0, "\r{} {} {}".format(w.key, w.get_ttl(), w.get_status()))
                i += 1
            stdscr.refresh()
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        curses.endwin()


if __name__ == "__main__":
    monitor()
