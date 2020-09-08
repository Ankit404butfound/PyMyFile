ALL = "all"


class LineException(Exception):
  """Class to raise LineException"""
  pass


class PhyException(Exception):
  """Class to raise PhyException"""
  pass


class file:
  """The file class of pyfile for dealing with advance file handeling"""
  def __init__(self,filepath):
    self.filepath = filepath


  def numiphy(self):
    """Will add numbers at the begining of each line\n1. Some data...\n2. Some date...\netc"""
    newdata = ""
    data = open(self.filepath).read()
    filelst = data.split("\n")
    total_lines = len(filelst)+1

    if len(filelst) < 1:
      raise LineException("Trying to numiphy file having only one line")
    
    else:                      
      for i in range(1,total_lines):
        newdata = f"{newdata}\n{str(i)}. {filelst[i-1]}"
      newdata = newdata.replace("\n","",1)
      file = open(self.filepath,"w")
      file.write(newdata)
      file.close()
      

  def denumiphy(self):
    """Opposite of numiphy()\nWill remove the changes done by numiphy() function"""
    newdata = ""
    data = open(self.filepath).read()
    filelst = data.split("\n")
    
    if "\n2. " in data:
      for i in range(1,len(filelst)+1):
        newdata = f"""{newdata}\n{filelst[i-1].replace("%s. "%i,"",1)}"""
      newdata = newdata.replace("\n","",1)
      file = open(self.filepath,"w")
      file.write(newdata)
      file.close()

    else:
      raise PhyException("Attempt to denumiphy file which hasn't been numiphied")

    
  def read(self):
    """This will return the content of the file"""
    return open(self.filepath).read()
  

  def readline(self,line_num):
    """This will return that line of the file only"""
    data = open(self.filepath).read()
    filelst = data.split("\n")
    
    if line_num-1 > len(filelst):
      raise LineException("line_num can not be greater than total number of lines in the file")
    
    else:
      return filelst[line_num-1]
    

  def readlines(self,from_line_num,to_line_num):
    """This will return the lines of file in that range including both ends"""
    newdata = ""
    data = open(self.filepath).read()
    filelst = data.split("\n")
    total_lines = len(filelst)+1
    newdata = filelst[from_line_num-1]
    
    for i in range(to_line_num):
      if i > from_line_num-1:
        newdata = f"{newdata}\n{filelst[i]}"
        
    return newdata


  def append(self,data):
    """This will append data to the file"""
    try:
      self.denumiphy()
      numiphied = True

    except:
      numiphied = False
      
    file = open(self.filepath,"a")
    file.write(data)
    file.close()
    if numiphied:
      self.numiphy()


  def append_line(self,line_num,data):
    """This will append that line to the file, see source od docs for more information"""
    try:
      self.denumiphy()
      numiphied = True

    except:
      numiphied = False
      
    filedata = open(self.filepath).read()
    filelst = filedata.split("\n")
    line_cont_new = filelst[line_num-1]+data
    del filelst[line_num-1]
    filelst.insert(line_num-1,line_cont_new)
    newdata = '\n'.join([str(elem) for elem in filelst])
    file = open(self.filepath,"w")
    file.write(newdata)
    file.close()
    if numiphied:
      self.numiphy()
  

  def replace_word(self,line_num, old_word, new_word, occurence=ALL, from_word_num=None, to_word_num=None):
    """This will replace that particular word from that particular line, see source od docs for more information"""
    data = open(self.filepath).read()
    filelst = data.split("\n")
    
    if line_num > len(filelst)+1:
      raise LineException("Line number passed is greater than total number of lines in the file")

    else:
      line = str(filelst[line_num-1])
      
      if from_word_num and to_word_num:
        temp_line = line.replace(old_word,new_word,to_word_num)
        newline = temp_line.replace(new_word,old_word,from_word_num-1)

      elif occurence != ALL:
        print("here")
        newline = line.replace(old_word,new_word,occurence)

      else:
        newline = line.replace(old_word,new_word)

      filelst.remove(line)
      filelst.insert(line_num-1,newline)
      newdata = '\n'.join([str(elem) for elem in filelst])
     # print(newdata)
      file = open(self.filepath,"w")
      file.write(newdata)
      file.close()


##  def replace_line(self,line_num,new_line_content):
##    try:
##      self.denumiphy()
##      numiphied = True
##
##    except:
##      numiphied = False
##      
##    filedata = open(self.filepath).read()
##    filelst = filedata.split("\n")
##    del filelst[line_num-1]
##    filelst.insert(line_num-1,new_line_content)
##    newdata = '\n'.join([str(elem) for elem in filelst])
##    file = open(self.filepath,"w")
##    file.write(newdata)
##    file.close()
##    
##    if numiphied:
##      self.numiphy()
      

  def write(self,data):
    """This will write to the file"""
    try:
      self.denumiphy()
      numiphied = True

    except:
      numiphied = False
      
    file = open(self.filepath,"w")
    file.write(data)
    file.close()

    if numiphied:
      self.numiphy()


  def write_line(self,line_num,data):
    """This will attempt to write that particular line of the file"""
    try:
      self.denumiphy()
      numiphied = True

    except:
      numiphied = False
      
    filedata = open(self.filepath).read()
    filelst = filedata.split("\n")
    del filelst[line_num-1]
    filelst.insert(line_num-1,data)
    newdata = '\n'.join([str(elem) for elem in filelst])
    file = open(self.filepath,"w")
    file.write(newdata)
    file.close()

    if numiphied:
      self.numiphy()


  def bulletiphy(self):
    """This will add bullets (•) at the begining of each line"""
    newdata = ""
    data = open(self.filepath).read()
    filelst = data.split("\n")
    total_lines = len(filelst)+1

    if len(filelst) < 1:
      raise LineException("Trying to bulletiphy file having only one line")
    
    else:                      
      for i in range(1,total_lines):
        newdata = f"{newdata}\n• {filelst[i-1]}"
      newdata = newdata.replace("\n","",1)
      file = open(self.filepath,"w")
      file.write(newdata)
      file.close()


  def debulletiphy(self):
    """This will revert the effect of bulletiphy()"""
    newdata = ""
    data = open(self.filepath).read()
    filelst = data.split("\n")
    
    if "\n• " in data:
      for i in range(1,len(filelst)+1):
        newdata = f"""{newdata}\n{filelst[i-1].replace("• ","",1)}"""
      newdata = newdata.replace("\n","",1)
      file = open(self.filepath,"w")
      file.write(newdata)
      file.close()

    else:
      raise PhyException("Attempt to debulletiphy file which hasn't been bulletiphied")


  def asteriphy(self):
    """This will add bullets (*) at the begining of each line"""
    newdata = ""
    data = open(self.filepath).read()
    filelst = data.split("\n")
    total_lines = len(filelst)+1

    if len(filelst) < 1:
      raise LineException("Trying to asteriphy file having only one line")
    
    else:                      
      for i in range(1,total_lines):
        newdata = f"{newdata}\n* {filelst[i-1]}"
      newdata = newdata.replace("\n","",1)
      file = open(self.filepath,"w")
      file.write(newdata)
      file.close()


  def deasteriphy(self):
    """This will revert the effect of asteriphy()"""
    newdata = ""
    data = open(self.filepath).read()
    filelst = data.split("\n")
    
    if "\n* " in data:
      for i in range(1,len(filelst)+1):
        newdata = f"""{newdata}\n{filelst[i-1].replace("* ","",1)}"""
      newdata = newdata.replace("\n","",1)
      file = open(self.filepath,"w")
      file.write(newdata)
      file.close()

    else:
      raise PhyException("Attempt to deasteriphy file which hasn't been asteriphied")


  def phy(self,phy):
    """This will let you add custom "phy" at the begining of each line"""
    newdata = ""
    data = open(self.filepath).read()
    filelst = data.split("\n")
    total_lines = len(filelst)+1

    if len(filelst) < 1:
      raise LineException("Trying to phy file having only one line")
    
    else:                      
      for i in range(1,total_lines):
        newdata = f"{newdata}\n{phy} {filelst[i-1]}"
      newdata = newdata.replace("\n","",1)
      file = open(self.filepath,"w")
      file.write(newdata)
      file.close()


  def dephy(self,phy):
    """This will revert the effect of phy()"""
    newdata = ""
    data = open(self.filepath).read()
    filelst = data.split("\n")
    
    if f"\n{phy} " in data:
      for i in range(1,len(filelst)+1):
        newdata = f"""{newdata}\n{filelst[i-1].replace("%s "%phy,"",1)}"""
      newdata = newdata.replace("\n","",1)
      file = open(self.filepath,"w")
      file.write(newdata)
      file.close()

    else:
      raise PhyException(f"Attempt to dephy file which hasn't been phied with {phy}")
    
