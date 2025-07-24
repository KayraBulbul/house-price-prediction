### Model Evaluation Summary

The project began with a simple Linear Regression model as a baseline. While it achieved a reasonable R² score of 0.67, it struggled with high error values, especially for more expensive homes.

To improve performance, a Random Forest Regressor was trained. This model significantly reduced both the MAE and RMSE and increased the R² to 0.76, indicating a better fit to the data. Its ability to capture non-linear relationships and handle feature interactions made it a more robust choice for this dataset.

Based on these metrics, the Random Forest model was selected as the final model for deployment and interpretation.


| Model              | MAE       | RMSE      | R² Score |
|--------------------|-----------|-----------|----------|
| Linear Regression  | 239,889   | 1,271,484 | 0.67     |
| Random Forest      | 192,772   | 307,312   | 0.76     |
