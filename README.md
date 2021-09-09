# Working with Files (File I/O)

#Technology: pandas library

# user story
The company you work with needs some modules in a bigger project for doing the following

- Performing IO operations on specifically 3 different files namely, Text, CSV and TSV files
- Reading rows from both CSV and TSV files

The relationship between these  files can be seen in the following ways

- Text, CSV and TSV files are types of files  
- CSV and TSV files are types of spreadsheets

In the bigger project, there exist two modules **ReadBytesFromFile** and **ProcessSpreadSheet** of which we do not know the actual implementation details of these modules, except for the signature and operations these modules expects to be performable on their respective argument.

**ReadBytesFromFile()**: This is a module that takes a file (either Text, CSV or TSV file) and can perform the following operations

- Treat the file object as a context manager, where on enter, the file is opened and then closed on exit.
- Treat the file object as an iterator which we can use to looping through lines in the file
- Read the complete content of the file at once.
- Read the first two lines of the file only.
- Read the last two lines only.

**ProcessSpreadsheet()**: This is a module that expects a spreadsheet, (either a CSV or TSV spreadsheet) as an argument and can perform the following operations

- Treat the spreadsheet object as an iterator for looping through the rows
- Iterate through the rows of the spreadsheet
- Read the complete content of the file
- Fetch only the first two rows of the spreadsheet
- Fetch only the last two rows of the spreadsheet

## Hints

- Treat a list of expected behavior above as contracts that the different files and spreadsheet respectively must comply to.
- The spreadsheet cannot be a type of file and vice versa because Text files cannot be treated as a spreadsheet.

### Important Notes

- The **ReadBytesFromFile** is not expected to know the kind of file it is taking in, it should just be able to perform all the expected operations on any file that comes in, same for ProcessSpreadsheet, it should not have an idea of whether the spreadsheet passed in is TSV or CSV.
- Opening files should manage its own context, that is opening the file and closing it afterwards. We do not want any close method in any of the modules.
- Handling CSV and TSV files should be done using Pandas DataFrame.
- Create a PR template of your choice into the .github folder to be used for PRs you will raise later
- Ensure to write unittest that covers at least 90% of your implementation
- When done and all tests are passing, raise a PR with a good title and body structure based on the content of the PR template you created at the beginning.

### Approach

- Understanding specification and asking timely questions where necessary.
- Broke down large tasks into the smallest chunk of work
- Splitting a large module into components based on specification and understanding how to assemble these components to make up the whole usable module.
- Created a good folder structure for module components.
- Strictly writing codes that comply with the SOLID principles.
- Understanding and using a third party library such as Pandas.
- Inheritance and Interface Polymorphisms.
- Iterators and generators
- Constructing a good inheritance hierarchy.
- Interfaces using abstract base classes.
- Unittest implementations

## how to use this app
-clone this repository
-insert files you want to read inside files folder
-create virtual environment ' python -m venv'
-activate virtual environment 'source activate/bin/activate'
-install requirements.txt 'pip install -r requirements.txt'
-open main.py and uncomment the method you want to run by removing the #
-run python main.py name_of_file_to_read on your terminal or command line

## screen shots : read all
![Screen Shot 2021-09-09 at 9 28 46 AM](https://user-images.githubusercontent.com/81101034/132652021-7f5d6da1-7233-48df-995e-4ac299817cd9.png)


## screen shots : read first two lines
![Screen Shot 2021-09-09 at 9 28 58 AM](https://user-images.githubusercontent.com/81101034/132652082-fea700d1-634c-4493-8967-7519532db3d1.png)


## screen shots : read last two lines
![Screen Shot 2021-09-09 at 9 35 20 AM](https://user-images.githubusercontent.com/81101034/132652251-6c374640-c3a0-4b49-b44e-8154657e794c.png)

