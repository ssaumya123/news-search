# Part 1 - News Search
This is a README file that provides information about the execution of news_search script and how to run/execute the unit tests.

## Steps to run/execute news_search.py
The following steps are required to run the news_search.py.

### For Windows/Ubuntu:
1. The hscic-news and news_search.py must be placed in the same folder.
2. Open the Command Prompt for windows and Terminal for Ubuntu.
3. Change the directory path to the folder containing news_search.py, by executing command as:
```
    cd <folder_path>/news_search_cmd
```
4. Execute the following command to run news_search.py, and it will print the expected document reference as:
```
    python news_search.py --search-type 'OR' --query 'Care,Quality,Commission'
    Expected outcome: 0,1,2,3,4,5,6
```
5. Execute the following command to run unit tests on news_search.py:
```
    python test_news_search.py
    It will ran 5 tests.
```
