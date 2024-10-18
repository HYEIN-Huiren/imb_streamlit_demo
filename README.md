# [Kaggle](https://www.kaggle.com/competitions/playground-series-s4e10/overview) Loan Approval Prediction Dataset Analysis

- Period: 2024/10/18 (1Day)
- Goal: Develop an interactive dashboard (with streamlit) for statistical analysis of a finance dataset from Kaggle.
    - Statistical Analysis Learning
- App: [Streamlit-Demo](https://imb-demo.streamlit.app/)

### Features
- `person_age`: Applicant’s age in years.
- `person_income`: Annual income of the applicant in USD.
- `person_home_ownership`: Status of homeownership (Categorical).
- `person_emp_length`: Length of employment in years.
- `loan_intent`: Purpose of the loan (Categorical).
- `loan_grade`: Risk grade assigned to the loan, assessing the applicant’s creditworthiness.
- `loan_amnt`: Total loan amount **requested** by the applicant.
- `loan_int_rate`: Interest rate associated with the loan.
- `loan_status`: The **approval status** of the loan.
- `loan_percent_income`: Percentage of the applicant’s income allocated towards loan repayment.
- `cb_person_default_on_file`: Indicates if the applicant has a history of default.
- `cb_person_cred_hist_length`: Length of the applicant’s credit history in  years.

### Hypothesis
**Needs to be organized**
> 1. Purpose of the loan does **NOT** influence the loan status.
> 2. Easily available for loans at the applicant's **MOST employable age** group.
> 3. Loan grade **MAY** the characteristic Feature that has the greatest impact on the loan status.
> 4. Loan grade 연관 있는 Feature들 (`cb_person_default_on_file`, `cb_person_cred_hist_length`, `loan_percent_income`, `loan_amnt`,`...` what else?)
> 5. 이자율과 다른 Feature과의 관계? (~Loan grade?)
> 6. 

### Analysis Plan
**Needs to be organized**
- `loan_status` ~ `person_age`+`person_income`+`person_emp_length`
- `loan_int_rate` ~ `loan_grade` (+`loan_amnt`?)
- `loan_status`~`loan_amnt`
- `loan_status`~`person_income` + `loan_int_rate`