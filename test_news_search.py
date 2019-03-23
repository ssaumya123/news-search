"""
This test script is used to do unit testing on the news_search.py file.
"""

import unittest
from news_search import main

class TestNewsSearch(unittest.TestCase):

    # To Test the Acceptance Criteria having query as 'Care Quality Commission' and search type as 'OR' with
    # expected document reference as '0,1,2,3,4,5,6'.
    def test_OR_query1(self):
        arguments = ['--query','Care,Quality,Commission','--search-type','OR']
        cached_docs_ref = main(arguments)
        self.assertEqual('0,1,2,3,4,5,6', cached_docs_ref)

    # To Test the Acceptance Criteria having query as 'September 2004' and search type as 'OR' with
    # expected document reference as '9'.
    def test_OR_query2(self):
        arguments = ['--query','September,2004','--search-type','OR']
        cached_docs_ref = main(arguments)
        self.assertEqual('9', cached_docs_ref)

    # To Test the Acceptance Criteria having query as 'general population generally and search type as 'OR' with
    # expected document reference as '6,8'.
    def test_OR_query3(self):
        arguments = ['--query','general,population,generally','--search-type','OR']
        cached_docs_ref = main(arguments)
        self.assertEqual('6,8', cached_docs_ref)

    # To Test the Acceptance Criteria having query as 'Care Quality Commission admission and search type as 'AND' with
    # expected document reference as '1'.
    def test_AND_query1(self):
        arguments = ['--query','Care,Quality,Commission,admission','--search-type','AND']
        cached_docs_ref = main(arguments)
        self.assertEqual('1', cached_docs_ref)

    # To Test the Acceptance Criteria having query as 'general population Alzheimer' and search type as 'AND' with
    # expected document reference as '6'.
    def test_AND_query2(self):
        arguments = ['--query','general,population,Alzheimer','--search-type','AND']
        cached_docs_ref = main(arguments)
        self.assertEqual('6', cached_docs_ref)

if __name__ == '__main__':
    unittest.main()
