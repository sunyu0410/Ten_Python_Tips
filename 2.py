# Mutable objects and default arguments

def collectNames(*names, curList=[]):
    for name in names:
        curList.append(name)
    return curList


collectNames('David', 'Mary')
collectNames('David', 'Mary', curList=['Daisy'])

collectNames('David', 'Mary')
collectNames('David', 'Mary', curList=['Daisy'])

# This is because the default argument will only be
#  initiated once
# Solution - avoid using mutable objects as default 
#  arguments
def collectNames(*names, curList=None):
    if not curList:
        curList = []
    for name in names:
        curList.append(name)
    return curList


collectNames('David', 'Mary')
collectNames('David', 'Mary', curList=['Daisy'])

collectNames('David', 'Mary')
collectNames('David', 'Mary', curList=['Daisy'])
