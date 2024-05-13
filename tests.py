from tic_tac_toe import DataLoader, TicTacToe
import unittest
from unittest.mock import MagicMock, patch, mock_open


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.window = MagicMock()
        self.data_loader = DataLoader()
        self.game = TicTacToe(self.window, self.data_loader)

    def test_next_turn(self):
        # Simulate player X's turn
        self.game.next_turn(0, 0)
        self.assertEqual(self.game.player, "O")  # Check if the player switched to O
        # Simulate player O's turn
        self.game.next_turn(1, 1)
        self.assertEqual(self.game.player, "X")  # Check if the player switched back to X
        # Simulate clicking on an already marked cell
        self.game.next_turn(0, 0)
        self.assertEqual(self.game.player, "X")  # Check if the player remains the same
        # Simulate game ending with a win
        self.game.next_turn(0, 1)
        self.game.next_turn(1, 0)
        self.game.next_turn(0, 2)
        self.assertEqual(self.game.label.cget("text"), "X wins!")  # Check if X wins

    def test_check_winner(self):
        # Simulate horizontal win
        self.game.buttons[0][0]["text"] = "X"
        self.game.buttons[0][1]["text"] = "X"
        self.game.buttons[0][2]["text"] = "X"
        self.assertTrue(self.game.check_winner())  # Check if X wins
        # Simulate vertical win
        self.game.buttons[0][0]["text"] = ""
        self.game.buttons[1][0]["text"] = "O"
        self.game.buttons[2][0]["text"] = "O"
        self.assertTrue(self.game.check_winner())  # Check if O wins
        # Simulate diagonal win
        self.game.buttons[1][1]["text"] = "X"
        self.game.buttons[2][2]["text"] = "X"
        self.assertTrue(self.game.check_winner())  # Check if X wins diagonally

    def test_empty_spaces(self):
        # Test when the board is empty
        self.assertTrue(self.game.empty_spaces())
        # Test when the board is partially filled
        self.game.buttons[0][0]["text"] = "X"
        self.assertTrue(self.game.empty_spaces())
        # Test when the board is completely filled
        for row in range(3):
            for column in range(3):
                self.game.buttons[row][column]["text"] = "O"
        self.assertFalse(self.game.empty_spaces())


    def test_new_game(self):
        # Simulate a game in progress
        self.game.buttons[0][0]["text"] = "X"
        self.game.player = "O"
        self.game.new_game()  # Reset the game
        # Check if all buttons are cleared
        for row in range(3):
            for column in range(3):
                self.assertEqual(self.game.buttons[row][column]["text"], "")
        # Check if the player is randomized
        self.assertIn(self.game.player, ["X", "O"])
        # Check if the turn indicator is set correctly
        self.assertEqual(self.game.label.cget("text"), f"{self.game.player} it is your turn")
        
    def test_data_loading(self):
        # Create a mock file with some predefined data
        with patch("builtins.open", mock_open(read_data="Mocked Data")) as mock_file:
            # Call the method under test
            data = self.data_loader.load_data()

            # Assert that the file is opened with the correct filename
            mock_file.assert_called_once_with("game_settings.txt", "r")
            
            # Assert that the data returned by load_data is correct
            self.assertEqual(data, "Mocked Data")

    def test_data_loading_file_not_found(self):
        # Test case for when the file is not found
        with patch("builtins.open", side_effect=FileNotFoundError):
            data = self.data_loader.load_data()
            self.assertIsNone(data)

    def test_data_loading_error(self):
        # Test case for when an error occurs during data loading
        with patch("builtins.open", side_effect=Exception("Error")):
            data = self.data_loader.load_data()
            self.assertIsNone(data)


    def test_data_loading_stub(self):
        # Stub the load_data method to return predefined data
        expected_data = "Predefined Data"
        self.data_loader.load_data = MagicMock(return_value=expected_data)

        # Call the method under test
        actual_data = self.data_loader.load_data()

        # Assert that the method returns the expected data
        self.assertEqual(actual_data, expected_data)

    def test_data_loading_mock(self):
        # Mock the load_data method to verify it's called once
        with patch.object(self.data_loader, 'load_data') as mock_load_data:
            # Call the method under test
            self.game.new_game()

            # Assert that the load_data method is called once
            mock_load_data.assert_called_once()


    def test_data_loading_fake(self):
        # Fake the load_data method to simulate different behavior
        def fake_load_data():
            # Simulate raising an exception during data loading
            raise Exception("Failed to load data")

        # Replace the load_data method with the fake implementation
        self.data_loader.load_data = fake_load_data

        # Call the method under test that uses the DataLoader
        # For example, you can test if an exception is properly handled
        with self.assertRaises(Exception):
            self.game.new_game()
