import csv

def export_to_csv(results, path):
    # creates a csv file with results
    # format: Commit SHA | Commit Message
    #         result sha | result message

    with open("{}.csv".format(path), 'w', newline='') as f:
        writer = csv.DictWriter(f, ['Commit SHA', 'Commit message'])
        writer.writeheader()
        writer.writerows(results)

    f.close()