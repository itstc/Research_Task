import csv

def export_to_csv(results, path):
    # creates a csv file with results
    # format: Commit SHA | Commit Message
    #         result sha | result message

    # no path defined, print to terminal
    if not path: 
        print(results)
        return 0

    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, ['Commit SHA', 'Commit message'])
        writer.writeheader()
        writer.writerows(results)

    print("{} has been created!".format(path))
    f.close()
