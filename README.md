# Iris EDA Project

This project is focused on exploratory data analysis (EDA) of the Iris dataset. The Iris dataset is a well-known dataset in the field of machine learning and statistics, containing measurements of iris flowers from three different species.

## Project Structure

```
iris-eda-project
├── data
│   └── iris.csv          # Contains the Iris dataset
├── notebooks
│   └── eda.ipynb        # Jupyter notebook for EDA
├── src
│   ├── data_loader.py    # Functions to load the dataset
│   ├── eda.py            # Functions for EDA
│   └── utils.py          # Utility functions for data processing
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Installation

To set up the project, you need to install the required Python packages. You can do this by running:

```
pip install -r requirements.txt
```

## Usage

1. Load the dataset using the `load_data()` function from `src/data_loader.py`.
2. Perform exploratory data analysis using functions from `src/eda.py`.
3. Visualize the data and insights in the Jupyter notebook located in the `notebooks` directory.

## License

This project is licensed under the MIT License.