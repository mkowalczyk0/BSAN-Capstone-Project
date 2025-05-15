# Scope:

**Business Context**: Changed is an app that pays off user debt sooner by rounding up everyday purchases. We want to understand our users debt on a deeper level and conduct an analysis to lead to actionable insights.

## Data Schema:

- UID: user_id 
- Is_Linked: linked the loans to the app and can see them. can be enabled. 
- Is_Enabled: enabled the loan for pay off, the user can begin to pay off the debt
- Interest_Rate: interest rate on the loan
- Minimum_Payment: minimum payment for the loan
- Current_Loan_Balance: the loans current balance
- Original_Loan_Balance: the loans original balance at issuance 
- Loan_Provider: provider of the loan 
- Date_Issued: date the loan was issued
- Loan_Term: term of the loan, credit cards have 999 since they are revolving
- Date_Linked: date the loan was linked 
- Loan_Last_Payment: date the user last sent a payment to their loan
- Is_Primary_Loan: primary loan of the user
- Loan_Type: type of loan
- Unique_Saved_In_Interest: amount the user has saved on the loan using the app



## ETL Pipeline *I can move this into the cloud*
1. Handling ingestion as an overwrite, we can surmise an SCD-Type 1 (latest data)
2. Performing transforms in clean.py
3. Loading into offline csv




## Further Preliminary Analysis

### Descriptive & Statistical Summaries
- **Correlation Analysis**: Explore relationships between key numerical features such as interest rate, loan balances, minimum payments, and unique saved interest.
- **Group Comparisons**: Compare statistics between subgroups (e.g., linked vs. not linked loans, enabled vs. non-enabled loans, or different loan types) to identify behavioral patterns.

### Data Segmentation & Clustering
- **User Segmentation**: Use clustering techniques to segment users based on loan characteristics (balance, interest rate, payment history).
- **Loan Provider Analysis**: Investigate differences among loan providers in terms of user debt, interest rate profiles, and engagement levels.

### Outlier & Anomaly Detection
- **High-Value Loans**: Identify outliers with extremely high balances and determine if they belong to specific loan types or indicate data issues.
- **Missing Data Impact**: Examine missing `Loan_Last_Payment` values to understand whether they indicate inactive users or new loans.

### Predictive Modeling (Conceptual)
- **Regression or Classification Models**: Predict potential interest savings (`Unique_Saved_In_Interest`) based on loan balance, interest rate, and minimum payment.
- **Conversion Prediction**: Build a model to predict whether a linked loan will become enabled.


---


## Analysis Directions

### Decision Science / Business Statistics
- Conduct hypothesis testing (e.g., t-tests, chi-squared tests) to determine if engagement differences (linked vs. non-linked, enabled vs. non-enabled) are significant.
- Use confidence intervals to assess uncertainty around key metrics like average savings or balance amounts.

### Business Analytics & Intelligence
- Develop **BI dashboards** (Tableau, Power BI, Plotly/Dash) to track key KPIs such as outstanding debt, engagement rates, and savings.
- Generate reports translating findings into **actionable insights** for business decision-makers.

### Data Mining & Machine Learning
- Apply clustering (e.g., **K-Means, hierarchical clustering**) to uncover user segments.
- Use predictive models (**regression, classification**) to forecast which users would benefit most from app intervention.

### Data Visualization
- Create **interactive visualizations** for stakeholders to explore different segments (by loan type, provider, user demographics if available).
- Visualize **temporal trends, correlations, and distributions** with clear annotations.

### Database & Data Warehousing Considerations
- Consider **structuring data into a relational database** for easier querying.
- Plan for a **data warehouse** to consolidate multiple data streams for real-time analytics.

### Business Process Automation & Web Analytics
- Identify **repetitive analysis or reporting tasks** that can be automated.
- If web/app usage data is available, integrate it with loan data to analyze user behavior comprehensively.

### Electives / Further Analysis
- Explore **customer segmentation based on demographics** or behavioral data (if available).
- Investigate **external factors (e.g., economic indicators)** affecting debt and payment behavior.

