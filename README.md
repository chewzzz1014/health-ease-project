- Course project for **CSC4602 Machine Learning** during sem 5 of my degree. A machine learning application that evaluates the depression level (not depressed, moderately depressed, severely depressed). 

- Train models on Kaggle notebook. Built the backend using FastAPI and frontend using Gradio.

- Used: Pandas, Tensorflow, Sklearn, Uvicorn, Gradio

- For more information:
  - About the project (Final Report Soon...)
  - [Kaggle Notebook](https://www.kaggle.com/code/chewziqing/health-ease-depression-prediction)
 
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




