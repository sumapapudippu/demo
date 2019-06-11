def evaluate_it():
    """
    this function evaluates a dictionary of rules  and returns a list 
    of enabled rules to execute in order of priority
    param: x: 
    """
    rules = {
        'move':
            {
            'description': 'move the file',
            'fname': 'move_file',
            'completion_value': 20,
             'priority': 1,
             'enabled': 1
            },
        'delete':
            {
             'description': 'delete the file',
             'fname':'delete_file',
             'completion_value': 50,
             'priority': 2,
             'enabled': 0
             },
        'write':
            {
             'description': 'write to the file',
             'fname':'write_to_file',
             'completion_value': 10,
             'priority': 4,
             'enabled': 1
             },
        'exit':
            {
             'description': 'exit rule evaluation - do not execute any rules after this one.',
             'fname': None,
             'completion_value': 0,
             'priority': 3,
             'enabled': 1
             }
    }
    for r_type,r_info in rules.items():
        print('\n Rule type',r_type)
        for key,value in r_info:
            if(key == 'enabled'):
                if(value == 1):
                    output=[r_type for i in range(1,3) if r.info['priority']==i]
        print(output)

evaluate_it()            
   
    
    
    
