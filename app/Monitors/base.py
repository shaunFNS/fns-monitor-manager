from abc import ABC, abstractmethod


class BaseMonitor(ABC):

    def __init__(self, client):
        self.client = client
        self.ui = client.ui

    @abstractmethod
    def create(self):
        pass