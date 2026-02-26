import unittest

def test_empty_grid(self): 
  grid = []
  dictionary = ["HELLO", "WORLD"]
  mygame = Boggle(grid, dictionary)
  self.assertEqual(mygame.getSolution(), [])

def test_number(self):
  grid = [["A", "B"], ["C", "D"]]
  dictionary = ["A1B", "C2D"] 
  mygame = Boggle(grid, dictionary)     
  self.assertEqual(mygame.getSolution(), [])

def test_special_tile(self):
  grid = [["Qu", "A"], ["R", "T"]]
  dictionary = ["QUART"] 
  mygame = Boggle(grid, dictionary)
  solution = mygame.getSolution()
  self.assertIn("QUART", solution)

def test_no_words_found(self):
  grid = [["X", "Y"], ["Z", "W"]]
  dictionary = ["APPLE", "BANANA"]
  mygame = Boggle(grid, dictionary)
  self.assertEqual(mygame.getSolution(), [])

def test_word_length(self):
  grid = [["A", "B", "C"]]
  dictionary = ["AB", "BC", "ABC"]
  mygame = Boggle(grid, dictionary)
  solution = mygame.getSolution()
  self.assertNotIn("AB", solution)
  self.assertIn("ABC", solution)

def test_tile_reuse(self):
  grid = [["A", "B"]]
  dictionary = ["ABA"] 
  mygame = Boggle(grid, dictionary)
  self.assertNotIn("ABA", mygame.getSolution())
def test_even_grid(self):
         
  grid = [
          ["A", "B", "C"],
          ["D", "E", "F"],
          ["G", "H", "I"]
          ]
          
  dictionary = ["ADG", "AEI", "ABC"]
          
          
  mygame = Boggle(grid, dictionary)
  solution = mygame.getSolution()
          
          
  self.assertIn("ADG", solution)
  self.assertIn("AEI", solution)
  self.assertIn("ABC", solution)    



def test_upper_case(self):
   grid = [["a","b"],["c","d",]]
   dictionary =["abcd"]
   mygame = Boggle(grid, dictionary)
   solution = mygame.getSolution()

   mygame = Boggle(grid, dictionary)
   solution = mygame.getSolution()

   self.assertIn("ABCD", solution)

def test_raw_i(self):
  grid = [["A","B"],["C","I"]]
  dictionary =["I","ABC"]
  mygame = Boggle(grid, dictionary)
  solution = mygame.getSolution()
  self.assertNotIn("I",solutions)

def test_invalid_word(self):
  grid = [["A","B"]["C","D"]]
  dictionary = ["ZEBRA"]
  mygame = Boggle(grid, dictionary)
  solution = mygame.getSolution()
  self.assertNotIn("ZEBRA",solution)

if __name__ == '__main__':
    unittest.main()