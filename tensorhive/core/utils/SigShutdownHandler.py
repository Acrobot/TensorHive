import signal
import logging
log = logging.getLogger(__name__)


class SigShutdownHandler():
    '''Implements the behaviour for unexpected termination requests, like: Ctrl+C etc.'''
    _kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.shutdown_gracefully)
        signal.signal(signal.SIGTERM, self.shutdown_gracefully)

    def shutdown_gracefully(self, signum, frame):
        self._kill_now = True
        log.info('[✔] All stopped')
        exit(0)
