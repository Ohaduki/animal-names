from data_processing.data_processing import get_adjectives

class TestGetAdjectives:

    def setup_class(self):
        self.adjectives = get_adjectives()
    
    def test_function_works(self):
        assert self.adjectives
    
    def test_returns_dict(self):
        assert type(self.adjectives) == dict
    
    def test_simian_in_result(self):
        assert 'simian' in self.adjectives.keys()
    
    def test_ape_in_simian(self):
        assert ('Ape', 'JPG') in self.adjectives['simian']
    