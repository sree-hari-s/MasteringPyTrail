## Anaemia Detection

Anaemia is a condition in which the number of red blood cells or the haemoglobin concentration within them is lower than normal. Haemoglobin is needed to carry oxygen and if you have too few or abnormal red blood cells, or not enough haemoglobin, there will be a decreased capacity of the blood to carry oxygen to the body’s tissues. This results in symptoms such as fatigue, weakness, dizziness and shortness of breath, among others. 

Anaemia may be caused by several factors: nutrient deficiencies through inadequate diets or inadequate absorption of nutrients, infections (e.g. malaria, parasitic infections, tuberculosis, HIV), inflammation, chronic diseases, gynaecological and obstetric conditions, and inherited red blood cell disorders. The most common nutritional cause of anaemia is iron deficiency, although deficiencies in folate, vitamins B12 and A are also important causes. 


**Dataset**

You can access the anaemia dataset here in [Kaggle](https://www.kaggle.com/datasets/biswaranjanrao/anemia-dataset)

**Goal**

The goal of this problem statement is to create a prediction model which will predict the chances of having Anaemia in a person.

**Working!**
It firstly takes in 5 inputs which are Gender, Hemoglobin, MCH, MCHC, and MCV and predict if you have Anaemia or not.

Gender: 0 - male, 1 - female

Hemoglobin: Hemoglobin is a protein in your red blood cells that carries oxygen to your body's organs and tissues and transports carbon dioxide from your organs and tissues back to your lungs

MCH: MCH is short for "mean corpuscular hemoglobin." It's the average amount in each of your red blood cells of a protein called hemoglobin, which carries oxygen around your body.

MCHC: MCHC stands for mean corpuscular hemoglobin concentration. It's a measure of the average concentration of hemoglobin inside a single red blood cell.

MCV: MCV stands for mean corpuscular volume. An MCV blood test measures the average size of your red blood cells.

**What Have I Done**

1. Imported all the required libraries
2. Processed Data Cleaning and demonstrated Data Visualization with insights
3. Finally implemented Prediction Modelling :

    - Tensorflow Sequential Model
    - Logistic Regression
    - Decision Tree Classifier
      
4. Atlast, compared the results for better conclusion

**Model Results**

I had applied different algorithms to check the accuracy score of the models. Keeping a glance, all the models reverted with a score with one model as 92 and Logistic Regression of 98. We can apply any of the models / algorithms to deploy the final model. I suggest to go with logstic regression sufficiently.