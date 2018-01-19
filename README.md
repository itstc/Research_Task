# Research Task
Retrieves all commits of a repository using Github REST api v3 and filters out commits with keywords specified

#### Installation

Requirements: Python3.6, pip

To install virtualenv on your machine run in your terminal
```pip install virtualenv```

##### 1. Once virtualenv has been installed

Goto the directory you want to store your virtualenv
```
virtualenv ENV_NAME

cd ENV_NAME
```

##### 2. Activate your environment

###### For OSX

```
source bin/activate
```

###### For Windows

```
.\Scripts\activate
```

##### 3. Clone repository to virtual environment and import dependencies
```
git clone https://github.com/ThomasChuDesigns/Research_Task.git
cd Research_Task
pip install -r requirements.txt
```

##### 4. Run Task Script
In your terminal, change to this repository folder and run this command:
```
python task.py
```

#### Authentication Note:
Github REST api only allows 60 requests/hour for unauthenticated users. If  you do decide to leave the username input blank your results may not be complete.
###### *Authenticating the script will increase the request quota to 5000/hour

#### Tested Inputs
I have ran the script with the following inputs and the .csv files are in the results folder included in this repository:

```
// For django/django repository
Enter Github Username (optional): USERNAME
Enter Github Password or Access Key: PASSWORD
Enter repository to mine (:owner/:name): django/django
Enter where to output file: results/django.csv

// For tensorflow/tensorflow repository
Enter Github Username (optional): USERNAME
Enter Github Password or Access Key: PASSWORD
Enter repository to mine (:owner/:name): tensorflow/tensorflow
Enter where to output file: results/tensorflow.csv

// For ThomasChuDesigns/pyRPG repository
Enter repository to mine (:owner/:name): ThomasChuDesigns/pyRPG
Enter where to output file: results/test.csv
```





