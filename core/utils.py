import csv

def export_to_csv(path, data):
    # creates a csv file with results
    # format: Commit SHA | Commit Message
    #         result sha | result message

    # no path defined, print to terminal
    if not path: 
        print(data)
        return 0

    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, ['Commit SHA', 'Commit message'])
        writer.writeheader()
        writer.writerows(data)

    print("{} has been created!".format(path))
    f.close()

def append_to_csv(path, data, headers):
    # param path: string
    # param data: list({'header_name': data})
    # headers: list('header_name', ...)
    # appends data to csv file according to headers given
    with open(path, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, headers)
        writer.writerows(data)
    
    f.close()
