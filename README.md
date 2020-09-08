# PyFile

PyFile is a python library for advance file handeling in the easiest possible way

## Installation

```bash
pip install pyfile
```

## Usage

Consider a file "sample.txt" with following content

```
This is first line of the file.
This is second line of the file.
This is third line of the file.
This is fourth line of the file.
This is fifth line of the file.
This is sixth line of the file.
.
.
.
.
This is n(th) line of the file.
```

### First import the library and initiate the file object
```python
import pyfile
myfile = pyfile.file("sample.txt")
```
### Then calling the functions will make the desired changes to the file, here's a berief explaination to each.

#### read()
This will return the content of the file, you don't need to close().

#### readline(line_num)
This will return the specified
```python
>>> content = myfile.readline(line_num = 3)
>>> print(content)
This is third line of the file.
```

#### readlines(from_line_num, to_line_num)
This will return line in range from_line_num to _to_line_num. This will include both ends.
```python
>>> contents = myfile.readlines(from_line_num = 2, to_line_num = 5))
>>> print(content)
This is second line of the file.
This is third line of the file.
This is fourth line of the file.
This is fifth line of the file.
```

#### append(data)
This will append data to the file, you don't need to close().
```python
>>> myfile.append(data = "This is appended line.")
```
This will be the final content of the sample.txt.
```
This is first line of the file.
This is second line of the file.
This is third line of the file.
This is fourth line of the file.
This is fifth line of the file.
This is sixth line of the file.
.
.
.
.
This is n(th) line of the file.
This is appended line.
```

#### append_line(line_num,data)
This will append data to that line
```python
>>> myfile.append_line(line_num = 5, data = " This is appended data to line.")
```
This will be the final content of the sample.txt.
```
This is first line of the file.
This is second line of the file.
This is third line of the file.
This is fourth line of the file.
This is fifth line of the file. This is appended data to line.
This is sixth line of the file.
.
.
.
.
This is n(th) line of the file.
```

#### write(data)
This will write to the file
```python
>>> myfile.write("This is some data.")
```
This will be the final content of the sample.txt.
```
This is some data.
```

#### write_line(line_num,data)
This will write that particular line of the file.
```python
>>> myfile.write_line(line_num = 2, data = "This is new content of the line.")
```
This will be the final content of the sample.txt.
```
This is first line of the file.
This is new content of the line.
This is third line of the file.
This is fourth line of the file.
This is fifth line of the file.
This is sixth line of the file.
.
.
.
.
This is n(th) line of the file.
```

#### replace_word(line_num, old_word, new_word, occurence=ALL, from_word_num=None, to_word_num=None)
This will replace that particular word from that particular line
```python
>>> myfile.replace_word(line_num = 1, old_word = "file", new_word = "some word")
```
This will be the final content of the sample.txt.
```
1. This is first line of the some word.
2. This is second line of the file.
3. This is third line of the file.
4. This is fourth line of the file.
5. This is fifth line of the file.
6. This is sixth line of the file.
.
.
.
.
n. This is n(th) line of the file.
```
#### numiphy()
This will add numbers at the begining of each line
```python
>>> myfile.numiphy()
```
This will be the final content of the sample.txt.
```
1. This is first line of the file.
2. This is second line of the file.
3. This is third line of the file.
4. This is fourth line of the file.
5. This is fifth line of the file.
6. This is sixth line of the file.
.
.
.
.
n. This is n(th) line of the file.
```

#### denumiphy()
This will revert the changes caused by numiphy()
```python
>>> myfile.numiphy()
```
This will be the final content of the sample.txt.
```
This is first line of the file.
This is second line of the file.
This is third line of the file.
This is fourth line of the file.
This is fifth line of the file.
This is sixth line of the file.
.
.
.
.
This is n(th) line of the file.
```

#### bulletiphy()
This will add bullets "•" at the begining of each line.
```python
>>> myfile.bulletiphy()
```
This will be the final content of the sample.txt.
```
• This is first line of the file.
• This is second line of the file.
• This is third line of the file.
• This is fourth line of the file.
• This is fifth line of the file.
• This is sixth line of the file.
.
.
.
.
• This is n(th) line of the file.
```

#### debulletiphy()
This will revert the changes caused by bulletiphy().
```python
>>> myfile.debulletiphy()
```
This will be the final content of the sample.txt.
```
This is first line of the file.
This is second line of the file.
This is third line of the file.
This is fourth line of the file.
This is fifth line of the file.
This is sixth line of the file.
.
.
.
.
This is n(th) line of the file.
```

#### asteriphy()
This is same as bulletiphy() but this will add "*" instead of bullet.
```python
>>> myfile.asteriphy()
```
This will be the final content of the sample.txt.
```
* This is first line of the file.
* This is second line of the file.
* This is third line of the file.
* This is fourth line of the file.
* This is fifth line of the file.
* This is sixth line of the file.
.
.
.
.
* This is n(th) line of the file.
```

#### deasteriphy()
This will revert the changes caused by asteriphy().
```python
>>> myfile.deasteriphy()
```
This will be the final content of the sample.txt.
```
This is first line of the file.
This is second line of the file.
This is third line of the file.
This is fourth line of the file.
This is fifth line of the file.
This is sixth line of the file.
.
.
.
.
This is n(th) line of the file.
```

#### phy(phy)
This is same as asteriphy() or bulletiphy() but add the custom phy instead.
```python
>>> myfile.phy(phy = "hmm")
```
This will be the final content of the sample.txt.
```
hmm This is first line of the file.
hmm This is second line of the file.
hmm This is third line of the file.
hmm This is fourth line of the file.
hmm This is fifth line of the file.
hmm This is sixth line of the file.
.
.
.
.
hmm This is n(th) line of the file.
```
#### deasteriphy()
This will revert the changes caused by phy(phy).
```python
>>> myfile.dephy(phy = "mum")
```
This will be the final content of the sample.txt.
```
This is first line of the file.
This is second line of the file.
This is third line of the file.
This is fourth line of the file.
This is fifth line of the file.
This is sixth line of the file.
.
.
.
.
This is n(th) line of the file.
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
