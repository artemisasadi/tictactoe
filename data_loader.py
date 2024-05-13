# Define DataLoader interface or base class
class DataLoaderInterface:
    def load_data(self):
        raise NotImplementedError()

# Implement stub for DataLoader
class StubDataLoader(DataLoaderInterface):
    def load_data(self):
        # Return predefined data for testing
        return "Stubbed data"

# Implement fake for DataLoader
class FakeDataLoader(DataLoaderInterface):
    def load_data(self):
        # Return hardcoded data for testing
        return "Fake data"

# Modify TicTacToe class to accept DataLoaderInterface instance
class TicTacToe:
    def __init__(self, window, data_loader: DataLoaderInterface):
        self.window = window
        self.data_loader = data_loader

# Modify TicTacToe class to accept DataLoaderInterface instance
class TicTacToe:
    def __init__(self, window, data_loader: DataLoaderInterface):
        self.window = window
        self.data_loader = data_loader

