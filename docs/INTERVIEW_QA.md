# Interview Questions and Sample Answers

**1. What is the goal of this project?**  
To demonstrate an end-to-end workflow for cleaning monthly climate-like data, summarizing trends, flagging statistical outliers, and communicating findings.

**2. Why use Pandas?**  
Pandas provides convenient tabular data structures, date parsing, missing-value handling, grouping, and CSV input/output.

**3. What is feature engineering here?**  
Deriving year, month, and season from each timestamp so observations can be grouped and compared over time.

**4. How is the temperature trend calculated?**  
The project aggregates observations into yearly mean temperature and fits a Linear Regression model with year as the predictor. The slope is the estimated change in °C per year within this dataset.

**5. Is this a climate forecast?**  
No. The fitted line is descriptive and can be extrapolated only with strong caveats. Reliable climate projections require appropriate physical models, scenarios, data, and uncertainty analysis.

**6. What does Isolation Forest do?**  
It isolates observations using random feature splits. Points that are easier to isolate receive anomaly labels. The output is a candidate list, not a verified list of extreme events.

**7. Why clean missing values?**  
Many analyses and models require usable numeric values. The project interpolates numeric gaps and uses a median fallback, but real scientific data may require source-specific treatment.

**8. Why generate synthetic data?**  
It makes the software reproducible and testable without credentials or data access. It does not establish real climate conclusions.

**9. How would you improve scientific validity?**  
Use a documented public dataset, check units and station metadata, quantify uncertainty, compare robust trend tests, validate assumptions, and document limitations.

**10. How would you test the project?**  
Use unit tests for expected columns, row counts, missing-value handling, yearly aggregation, and anomaly output; add integration tests for the full pipeline and reproducibility checks.
