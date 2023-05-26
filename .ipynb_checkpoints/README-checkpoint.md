# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
My goals for this project are to complete the following steps:

- Data Preparation
- Feature Engineering
- Supervised Learning
- Pipelines
- Model Persistance
- Flask - building an API
- Deployment to Cloud (AWS)

## Hypothesis
(fill in your hypothesis about which subset of applicants will be most likely to have their loan approved, and why. Give some examples of how you will test this hypothesis)

## EDA 
- The dataset contains 13 columns with 614 rows.
- There are null values in the data that we must clean
- 77.3% of dataset have credit history 
- ApplicantIncome - Mean: 5403.459283387622  Median: 3812.5
- CoapplicantIncome - Mean: 1621.2457980271008  Median: 1188.5
- Therefore the income can be considered skewed to the right since the median is less than the mean
- The 75th percentile of applicant income is at $5700, therefore majority of applicants have low income
- Income above $10,000 can be considered outliers.
- Majority of applicants are graduates 478.
- Distribution of income by education shows that maximum income of non-graduates is around $20,000 whereas it is $80,000 for graduates
- No credit history is a high indicator of not getting approved
- Semi-urban property area have the highest approval rates and rural have the lowest relatively speaking. (not much difference between all)
- No other categorical variables show significant indicators of approval
- 
## Process

### Step 1: Explore and understand the dataset
- Conducted exploratory data analysis to gain insights into the dataset's structure, variables, and distributions.

### Step 2: Data cleaning & feature engineering
- Handled null values by filling them based on specific criteria:
- Mode: Gender, Self-Employed, Dependents, Credit History.
- Mean: Loan amount (grouped by loan amount term).
- Married column filled based on whether CoApplicant Income was filled or not.
- Median: Loan amount term (grouped by loan amounts).
- Created new features to enhance the predictive power of the model, such as taking the log of income to reduce extreme values and combining applicant and coapplicant income into a total income column.

### Step 3: Build predictive model
- Trained a Logistic Regression model and a Random Forest Classifier on the preprocessed data.
- Evaluated the models using various metrics:
- Logistic Regression:
Accuracy: 78.38%
Precision: 83.15%
Recall: 70.29%
F1 score: 71.87%
- Random Forest Classifier:
Accuracy: 77.84%
Precision: 79.92%
Recall: 70.58%
F1 score: 72.08%

### Step 4: Hyperparameter tuning
- Utilized grid search to optimize the hyperparameters of the Logistic Regression model.
- Identified the best parameters: {'C': 1, 'penalty': 'l2'}.
- Achieved a slightly improved accuracy by fine-tuning the model.
- Best Score: 0.8157865937072504

### Step 5: Create a pipeline of the whole process
- Developed a pipeline to streamline the data cleaning, feature engineering, and model training steps into a single line of code.
- Ensured consistency and reproducibility in the process.

### Step 6: Save the model with pickle
- Saved the trained model as a file (loan_prediction.pkl) using the pickle library.
- This allows for easy loading and reuse of the model in the future.

### Step 7: Create API and deploy model to AWS
- Deployed the model on an AWS instance using Flask to create an API.
- Tested the API to ensure it returns predictions accurately.



## Results/Demo
- Best Score: 0.8157865937072504

## Challanges 
Connecting to the AWS instance after disconnecting had a lot of troubleshooting.

## Future Goals
