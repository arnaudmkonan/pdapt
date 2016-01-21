import unittest
import pdapt_lib.machine_learning.nlp as nlp

class TestNLP(unittest.TestCase):

    def compare_dicts(self, a, b):
        """ make sure each item is in both dicts,
        irrespective of order
        """
        if len(a) != len(b):
            return False
        else:
            for k, v in a.items():
                if b[k] != v:
                    return False
        return True

    def test_tokenize(self):
        a_tokens = nlp.tokenize("A simple version of a tokenizer", 1, False)
        b = {'a': 2, 'simple': 1, 'version': 1, 'tokenizer': 1, 'of': 1}
        result = self.compare_dicts(a_tokens, b)
        self.assertEqual(result, True)

    def test_tokenize2(self):
        a_tokens = nlp.tokenize("A simple version1 of a tokenizer", 1, False)
        b = {'tokenizer': 1, 'a': 2, 'of': 1, 'VERSION1': 1, 'simple': 1}
        result = self.compare_dicts(a_tokens, b)
        self.assertEqual(result, True)

    def test_tokenize3(self):
        a_tokens = nlp.tokenize("A simple version-2 of a tokenizer", 1, False)
        b = {'tokenizer': 1, 'a': 2, 'VERSION2': 1, 'of': 1, 'simple': 1}
        result = self.compare_dicts(a_tokens, b)
        self.assertEqual(result, True)

    def test_tokenize4(self):
        a_tokens = nlp.tokenize("the rain in Spain falls mainly in Spain", 2, False)
        b = {'the rain': 1, 'in spain': 2, 'rain in': 1, 'spain falls': 1, 'falls mainly': 1, 'mainly in': 1}
        result = self.compare_dicts(a_tokens, b)
        self.assertEqual(result, True)


