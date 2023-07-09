
# Cervical cancer risk classification

This project use to classify if someone on cervical cancer or not `in API format`, you can detect if someone had cancer or not by assign some variable to flask webapp, this project is usefull for detecting cancer 

## Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [seaborn](http://seaborn.org/)
- [imblearn](https://imbalanced-learn.org/stable/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [fastapi](https://flask.palletsprojects.com/)

## Usage

first, you can clone this git repository

```
git clone https://github.com/HillalXD/Cancer-Risk-Classification.git
```

then navigate your command to this directory

```
cd Cancer-Risk-Classification
```

after that run `app.py` to use fast api

```
uvicorn app:app --reload
```

then on fastapi app browser url add `/docs`like this:
```
http://127.0.0.1:8000/docs
```


## Code 
- Template code is provided in the `classifier.ipynb` notebook file.
- `cervical.csv` in provide data source for training model
- `app.py` is fastapi web application to user input features for model predicting and return predicted price as output

## Dataset features

for doing prediction you need to input this features:

| features  | explanation  | 
| :-------- | :------- | 
| Schiller | is user on schiller or not |
| Hinselmann  | is user have Hinselmann or not |
| Citology  | is user have Citology or not |
| STDs   | is user have infections that are passed from one person to another through sexual contact |
| hormonal_contraceptives_years  | how long user have hormon contraceptive (0 if dont) |
| Smoke_years | how long user have smoke or not (0 if dont)|
| iud  | is user on iud or not |
| age  | user age |
| hormonal_contraceptives | is user have hormon contraceptive or not |
| iud_years  | how long user is on iud |




