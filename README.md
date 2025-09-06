## 🔍 Model Overview

This FD prediction model uses **XGBoost**, a powerful gradient boosting algorithm, to estimate fixed deposit interest rates based on user inputs like bank name, tenure, and customer tier (regular/senior citizen). XGBoost was chosen for its:

- High accuracy on structured/tabular data
- Robust handling of noisy or incomplete inputs
- Fast training and inference—ideal for real-time predictions in a Flask app
- Built-in feature importance metrics for transparency

The model was trained on a cleaned dataset (`indianbank.xlsx`) containing FD rates across multiple banks and tiers. Tenure inputs are parsed from natural language (e.g., "3 year 6 months") and encoded for prediction.

numpy ,pandas etc..
