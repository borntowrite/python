#############################################################
# List with Class Object and Sort 
#############################################################
class Employee:
   def __init__(self, name, age, salary):
       self.name = name
       self.age = age
       self.salary = salary
   def __repr__(self):
       return "{}.{}.{}".format(self.name, self.age, self.salary)

emp1 = Employee('Fred', 30, 10000)
emp2 = Employee('Mark', 31, 5000)
emp3 = Employee('Jacob', 40, 10)

employees = [emp1, emp2, emp3]
def e_sort(emp):
   return emp.name
   # return emp.age
   # return emp.salary

s_employees = sorted(employees, key=e_sort, reverse=True)
# s_employees = sorted(employees, key=e_sort, reverse=False)
# s_employees = sorted(employees, key=lambda e: e.name)
# s_employees = sorted(employees, key=lambda e: e.age)
# s_employees = sorted(employees, key=lambda e: e.salary)
# s_employees = sorted(employees, key=attrgetter('age'))
print(s_employees)

##########################################################
# Sorting Class object
##########################################################
class Custom(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number
    # def __cmp__(self, other):
    #     if hasattr(other, 'number'):
    #         return self.number.__cmp__(other.number)
    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__, self.name, self.number)

customlist = [Custom('object', 99), Custom('michael', 1), Custom('theodore the great', 59),Custom('life', 42)]

def getKey1(custom):
    return custom.name
def getKey2(custom):
    return custom.number
def cmp_two_obj2(a, b):
    return cmp(a.number, b.number)
print(sorted(customlist, key=getKey1))
print(sorted(customlist, key=getKey2))
print(sorted(customlist, cmp=cmp_two_obj2)) # same result
# TypeError: '<' not supported between instances of 'Custom' and 'Custom'
#print(sorted(customlist)) 

##########################################################
# Sorting Class object
##########################################################

class Person(object):
    def __init__(self, firstname, lastname):
         self.first = firstname
         self.last = lastname
    # def __cmp__(self, other):
    #     return cmp((self.last, self.first), (other.last, other.first))
    def __repr__(self):
        return "%s %s" % (self.first, self.last)

actors = [Person('Eric', 'Idle'), Person('John', 'Cleese'), Person('Michael', 'Palin'),
Person('Terry', 'Gilliam'), Person('Terry', 'Jones')]

def cmp_last_name(a, b):
    """ Compare names by last name"""
    return cmp(a.last, b.last)
def get_last_name(a):
    """ Compare names by last name"""
    return a.last

print(sorted(actors, cmp=cmp_last_name))
print(sorted(actors, key=get_last_name))

"""
####################################################################
# C++
####################################################################
struct {
    bool operator()(pair<string,int> elem1, pair<string,int> elem2) 
    {   
        return elem1.second > elem2.second; // DESC
        //return elem1.second < elem2.second; // ASC
    }   
} dosort;

sort(vec.begin(), vec.end(),dosort);

####################################################################
# C
####################################################################
typedef struct { 
    char *str; 
    unsigned int count; 
} word_t; 
word_t* words = NULL; 
qsort(words, strlen(words), sizeof(*words), cmpfunc); 
int cmpfunc(const void* a, const void* b) { 
    return strcmp(((word_t*)a)->word, ((word_t*)b)->word); 
}

####################################################################
# Java
####################################################################
Collection.sort(list, new Comparator() 
    {
        public int compare(Object o1, Object o2){
            Integer v1 = (Integer) ((Map.Entry) o1).getValue();
            Integer v2 = (Integer) ((Map.Entry) o2).getValue();
            return v1.compareTo(v2);
        }
    }
);

or

class Comparator<Object>{
    public String sortChars(String s){
        char[] content = s.toCharArrary();
        Arrays.sort(content)
        return new String(content)
    }
    public int compare(Object o1, Object o2){
        return sortChars(o1.getValue()).compareTo(sortChars(o2.getValue()))
    }
}

Arrays.sort(array, new Comparator())

"""