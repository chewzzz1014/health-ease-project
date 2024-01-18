Course project for **CSC4602 Machine Learning** during sem 5 of my degree. A machine learning application that evaluates a message's depression level (not depressed, moderately depressed, severely depressed). 

Kaggle Notebook: https://www.kaggle.com/code/chewziqing/health-ease-depression-prediction

## About the Project
The primary objective is to predict the depression level based on the user message. There are 3 depression levels, **Not depressed**, **Moderately depressed** and **Severely depressed** represented by label 2, 1, and 0 respectively. 

HealthEase employs a machine learning model, BiGRU, to assess the severity of depression by categorizing user messages into any of these three depression levels. Upon determining the depression level, HealthEase provides tailored advice and information to users. This involves suggesting appropriate actions and resources based on the severity of depression detected. Moreover, the application identifies relevant keywords in user messages to offer a list of counseling, therapy, and helpline services available in Malaysia.

The advice and information module in the HealthEase’s output is not based on machine learning but relies on a predefined set of responses and resources. It is designed to be adaptive and responsive to the user's expressed needs. The relevance of the suggested resources is enhanced by detecting specific keywords related to mental health concerns in the user's messages.

## Dataset
The dataset for predicting user’s depression level is obtained from the dataset of the winning solution for the Shared Task on Detecting Signs of Depression from Social Media Text at LT-EDI-ACL2022. In this project, Rafal et al. (2022) collected and preprocessed reddits posts that are related to depression, then annotated each of them with any depression level label. Refer to their [github repository](https://github.com/rafalposwiata/depression-detection-lt-edi-2022) for more details and to view the dataset (located in the /data folder). 

This [journal](https://arxiv.org/abs/2202.03047) explained in detail how the depression level is categorized using the dataset that Rafal et al. were working on. Based on this paper, there are guidelines to follow when annotating the depression level of a text during the data preparation. 

The text will be annotated as “Not depressed", if the text has one of the following scenarios:
 - Has only one or two lines about irrelevant topics.
 - Reflects momentary feelings of the present situation.
 - Is about asking questions about information or medication
 - Is about asking/seeking help for a friend's difficulties.

The text will be annotated as “Moderately depressed", if the text has one of the following scenarios:
- Reflect change in feelings (feeling low for some time and feeling better for some time).
- Shows that they aren’t feeling completely immersed in any situations
- Show that they have hope for life.

The text will be annotated as “Severely depressed", if the text has one of the following scenarios:
- Express more than one disorder condition.
- Explain about history of suicide attempts.

The dataset comprises 10,251 rows and consists of three columns: pid, text, and labels.

## How it Works
Below are the list of tools and libraries used in this machine learning application:
 - Pandas: Working with dataset in csv format.
 - Scikit-learn: Implement the Decision Tree Classifier.
 - Matplotlib: Plot graphs of depression level distribution during EDA, the accuracy and loss of BiLSTM and GRU during training and validation.
 - Keras: Implement the BiLSTM and BiGRU.
 - FastAPI: Implement the backend of the application.
 - Gradio: Implement the frontend of the application
 - Uvicorn: Serve as web server for the application to be running locally
 - Kaggle: Run the model setups and trainings
- VSCode: IDE of the backend and frontend of the application.

We trained 3 machine learning models using Decision Tree Classifier, BiLSTM, and BiGRU. The BiGRU had the best performance amongst all, with 62% accuracy.  The implementation of all algorithms are available in our Kaggle Notebook accessible via https://www.kaggle.com/code/chewziqing/health-ease-depression-prediction  

The tokenizer and trained BiGRU are exported and then imported in the application for prediction. To make depression level prediction, the user’s message is transformed into a format acceptable by the model using the tokenizer and padded using _pad_sequence_ function from scikit-learn. The prediction result is in the form of an array of possibilities that the depression level belongs to label 0, 1 or 2. Choose the label with the highest value as the predicted depression level.

 
## How to Run
1. Make sure that Git, Python, pip and virtualenv are installed on the machine.
2. Clone the application from its github repository by running the following on Git bash/ command prompt (Windows)/terminal (Mac OS).
```
git clone https://github.com/chewzzz1014/health-ease-project.git
```
3. If it’s your first time running this application, navigate into the folder you just cloned and setup the virtual environment by running the following
```
python -m venv <your-virtual-environment-name>
```
4. Activate the virtual environment by running the following based on your machine operating system

```
.\\<your-virtual-environment-name>\Scripts\activate
Or
source <your-virtual-environment-name>/Scripts/activate
```

5. If it’s your first time running this application, download all the packages needed by the application by running the following
```
pip install -r requirements.txt
```

6. Start the application by running the following
```
uvicorn server:app
```
7. Visit http://localhost:8000/chat on your browser




