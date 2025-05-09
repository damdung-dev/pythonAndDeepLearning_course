class Student:
  # Attributes: ID, name, semester, course
  count = 0
  # Constructor:
  def __init__(self, name, semester, course):
    self.__name     = name
    self.__semester = semester
    self.__course   = course
    Student.count+= 1
    self.__ID       = Student.count
  # Getters/ setters
  @property
  def ID(self):
    return self.__ID
  @ID.setter
  def ID(self, ID):
    self.__ID = ID
  @property
  def name(self):
    return self.__name
  @name.setter
  def name(self, name):
    self.__name = name
  @property
  def semester(self):
    return self.__semester
  @semester.setter
  def semester(self, semester):
    self.__semester = semester
  @property
  def course(self):
    return self.__course
  @course.setter
  def course(self, course):
    self.__course = course
  # Methods:
  def __str__(self):
    st=""
    st+=f"-"*40
    st+=f"\n{self.__ID:10}|{self.__name:10}|{self.__semester:10}|{self.__course}"
    return st