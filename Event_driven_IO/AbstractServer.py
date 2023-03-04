from abc import ABC, abstractmethod


class EventHandler:
    @abstractmethod
    def fileno(self):
        """Return associated file descriptor"""
        raise NotImplementedError

    def wants_to_receive(self):
        """Return true if is allow"""
        return False

    def handle_receive(self):
        pass

    def wants_to_send(self):
        return False

    def handle_send(self):
        pass
