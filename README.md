**Customer complaint prediction**
A customer complaint is a formal or informal expression of dissatisfaction or displeasure from a customer about a product, service, or experience provided by a company. Customer complaints can be communicated through various channels, such as in-person interactions, phone calls, emails, social media, online reviews, or dedicated customer feedback forms. These complaints highlight areas where customers feel the company has failed to meet their expectations or fulfill its promises.
Customer complaints are essential for companies for several reasons.

**Problem statement**
The consumer Financial Bureau (CFPB) is a federal U.S. agency that act as a mediator when disputes aries betweeen financial institutions and consumers. Via a web form, consumers can send the agency a narrative of their dispute.

They use Natural Language Processing(NLP) with machine learning models to process the issues text written in the complaint and other feature to predict either customer will dispute or not.

**Application scope**
Companies may use this application  to prioritize to their work and concentrate more on the issues which have high chance of having disputes.
For example CIVICA (UK based)

**Approaches available**
    • Spacy for text processing, classify based on companies and department.
    • Provide an expected response to customer about the complaint based on time and response.
    • NLP and ANN for both results and accuracy.

**Proposed Solutions**
    • Extract the data from CFPB api within time interval.
    • Using pyspark as a tool preprocessing the data and feature extraction.
    • Train the different machine learning models and select one with higher accuracy for classification.
    • Load and run the pipeline using Airflow.

**Pipeline components**
    • Data Ingestion
    • Data Validation
    • Data Transformation
    • Model Trainer
    • Model Evaluation










**Data Ingestion**
Downloading the data into the system using API of CFPB  from start date to end date where end date is current date. But if start date is not provided or less then constant start date then start date will be assigned as start date. The file are downloaded in chunk since the it could be of huge size so once the files are downloaded the complete file is merged into parquet and store in feature store. 




**Data validation**
The artifact of data ingestion is read in data validation stage performing required column check and dropping unwanted columns, all this necessary task are conclusion from research of jupyter file.
























**Data transformation**
Validated data from accepted dir are obtained from data validation artifact and splitted into train and test. The datas are converted into parquet file. The data transformed object are saved as a pipeline.











































**Model training**
During Model training stage the best model from jupyter file is choosen and pipeline function is written and metrics are calculated.
 




**Model Evaluation**
This is the final stage of pipeline where we check if trained model is available , if present then test the accuracy with previous model. If newly trained model has high accuracy then replaced to old model else old model will be used, finally the score are pushed into MongoDB.

















































**Batch Prediction**
Every time batch prediction is run, read input file from , preprocess it and generate prediction and store  data as a back up in Archive folder. The input are store in inbox folder and output is generated in outbox folder as predicted file.








**steps to run the project**

1) Download the anaconda and activate the environment.
2) Clone the project.
3) Create the conda environment with python requirements greater then 3.6.
4) Run the train.py for training and test.py for testing.
</br>
</br>
<h1>Output file</h1>
<img src="https://github.com/k17hawk/finance_complaint/blob/main/screenshots/Predict.png"/>
</br>
</br>
<h1>MongoDB Model evaluation stage</h1>
<img src="https://github.com/k17hawk/finance_complaint/blob/main/screenshots/mongo_db.png"/>
</br>
</br>

<h1>Airflow 2.8.1</h1>
<img src="https://github.com/k17hawk/finance_complaint/blob/main/screenshots/airflow.png"/>




