import sys

clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
           'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
           'elon@paypal.com', 'jessica@gmail.com']

participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']

recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']


def to_set_clients():
    return set(clients)


def to_set_participants():
    return set(participants)


def to_set_recipients():
    return set(recipients)


def call_center_task():
    #Clients minus recipients
    clients_set = to_set_clients()
    recipients_set = to_set_recipients()
    
    return sorted(list(clients_set - recipients_set))


def potential_clients_task():
    #Participants minus clients
    participants_set = to_set_participants()
    clients_set = to_set_clients()
    
    return sorted(list(participants_set - clients_set))


def loyalty_program_task():
    #Clients minus participants
    clients_set = to_set_clients()
    participants_set = to_set_participants()
    
    return sorted(list(clients_set - participants_set))


def main():
    if len(sys.argv) != 2:
        return
    
    task_name = sys.argv[1]
    
    tasks = {
        'call_center': call_center_task,
        'potential_clients': potential_clients_task,
        'loyalty_program': loyalty_program_task
    }
    
    if task_name not in tasks:
        raise ValueError(f"Invalid task name: {task_name}")
    
    result = tasks[task_name]()
    print(result)


if __name__ == "__main__":
    main()