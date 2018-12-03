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
            status = []
            for w in m.list():
                status.append((w.key[9:], w.get_ttl(), w.get_status()))

            status = sorted(status, key=lambda x: (x[1], x[0]))
            for s in status:
                try:
                    stdscr.addstr(i, 0, "{}\t{}\t{}".format(*s))
                except:
                    break
                i += 1
            stdscr.refresh()
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        curses.endwin()


if __name__ == "__main__":
    monitor()
