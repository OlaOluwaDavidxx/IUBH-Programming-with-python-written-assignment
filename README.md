# International University of Applied Sciences

## Getting Started

### Task
```Python program that uses training data to choose the four ideal functions which are the best fits from the fifty provided functions. And the four functions will be used to test the test datasets ```

### Installation
- Clone the repository
- Get python IDLE installed
- Upgrade pip with ```python -m pip install --upgrade pip```
- Activate virtual environment to manage the packages
- Run ```pip install -r requirements.txt```
- Run main.py ```python main.py```

### Project Structure
```
├── requirements.txt                # The list of packages
├── main.py                         # The startup script
├── configure_working_env.py        # Configure the working environment
├── utils
│   ├── visualization
│   │   ├── data_visualization.py   # Functions to handle data visualization
│   │   ├── figure.py               # Function to handle save figure
│   │   └── plot.py                 # Funct5ions to create plots in bokeh
│   │  
│   ├── CONSTANT.py                 # Save constants
│   └── utils.py                    # Contains utility functions used in processing
│
├── test
│   ├── test_error.py               # test files for functions
│   └── test_working_env.py         # test file for working environment 
│
├── reports 
│   ├── test_report                 # folder contains html files of figure generated during testing
│   └── figure                      # Path to save figures
│
├── model
│   └── modelling.py                # models to test the test dataset with the ideal four functions generated
│
├── middleware
│   ├── errorhandlers.py           # user's errors declaration
│   └── evaluate_score.py          # squared error function
│
├── dataset                        # Path to store the datasets
├── database
│   └── to_db.py                   # Handles data migration to the database
│
└── controllers
    ├── data.py                    # Handles data conversion
    ├── data_perpresentation.py    # Handles data initialization
    ├── final_data_format.py       # Handles final data format
    └── load_data_controller.py    # Handles preprocessing and loading
```

### Additional Task
- fork repo for "develop"
- ```git clone repo(forked) link```
- ```git checkout -b (new branch)``` 
- ```git remote add upstream (forked repo link)```
- upon making changes to code, execute the next step.
- ```git add -A```
- ```git commit -m "Add message"```
- ```git push -u origin develop```
- return to github and make a compare and pull request
- create a pull request and wait for the main branch owner to merge


### Miscellaneous
- ```__init__.py``` convert the folder to python package
- The figures generated are in html format. It opens automatically in the browser. They can as well be opened manually
