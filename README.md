# TechDB
## The project implemented a Demo Database System, which include the following several modules:
- Data type abstraction: Simplify database fields only have String, Integer and Float data type;
- Tuple Abstraction: Each tuple contains a fixed number of Fields with different data type;
- Storage Abstraction: Storage Manager is used to write pages from memory to disk;
- Buffer Manager Abstraction: Buffer manager is used to make hot page switch strategy;
- Index Abstraction: Index is build for faster query; 

## How to use it
- genData.py: script to generate original dataset with key and value, generate 10000 items in default;
  command: ```python genData.py```
- Compile Database: ```g++ -g techdb.cpp -o techdb```
- Run Databse: ```./techdb```, it shows query time by index and query time by scanning the database table;
