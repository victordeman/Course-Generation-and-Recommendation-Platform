# Unit tests for recommendation engine
import unittest
from backend.python.recommendation_engine import generate_learning_path

class TestRecommendationEngine(unittest.TestCase):
    def test_generate_learning_path(self):
        result = generate_learning_path(80)
        self.assertIsInstance(result, dict)
        self.assertIn("learning_path", result)

if __name__ == '__main__':
    unittest.main()
