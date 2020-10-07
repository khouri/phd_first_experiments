# PhD first experiments
These repo contains the source code of the paper: "Aplicação de técnica para 
interpretar modelos caixa-preta, uma abordagem local e independente 
de modelo" presented in SBSI conference 2021.

The paper shows a literature review about black box statistical model 
interpretation using local, agnostic approachs. Besides that, the authors 
apply LIME technique over 3 datasets and 10 classifiers to explain 
their results and teaching how to use the tecnique.


## Project structure:
1. **data**: Folder with the datasets used to train the model

2. **ml_helper**: Sci-kit learn source code used

3. **serialized_model**: Serialized models

4. **pictures**:  Pictures folder

5. **EDA.ipynb**: Exploratory data analisys over the datasets

6. **data_cleaning.ipynb**: Cleaning techniques to standardize the data

7. **model_trainning.ipynb**: Sci-kit learn source code used to get the data and train it

8. **model_interpretation.ipynb**: Source code
