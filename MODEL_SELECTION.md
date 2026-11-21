# Model selection

Fill this in after you have trained your candidates in MLflow. Short sentences are fine. Use numbers from your runs.

## The question

The model predicts whether a customer is likely to churn (leave the service). A false negative may cause the company to miss an opportunity to retain a customer, while a false positive may lead to unnecessary retention offers and costs.

## Candidates

| Candidate | Why I tried it | AUC | F1 | F1 per slice (lowest) | p95 latency (ms) | Size (KB) | MLflow run ID |
|---|---|---:|---:|---:|---:|---:|---|
| Logistic Regression | Simple, fast, and interpretable baseline | 0.7982 | 0.4948 | 0.2500 (One year / Two year) | 4.9 | 4 | `80db626febc449e1aa917bd54d11b562` |
| Random Forest | To capture non-linear patterns and feature interactions | 0.7589 | 0.4536 | 0.2222 (One year) | 17.4 | 3160 | `9a865bac899647ebb5173c2205c72fa4` |
| Gradient Boosting | To test a boosting-based ensemble approach | 0.7476 | 0.4167 | 0.2222 (Two year) | 5.0 | 195 | `1ec53655b370412c8810aacdc5b0276f` |

## The champion

I selected **Logistic Regression** as the champion.

It achieved the highest overall F1 (0.4948) and AUC (0.7982). It also had the lowest p95 latency (4.9 ms) and the smallest model size (4 KB).

I accepted lower F1 performance on some contract slices: its F1 was 0.2500 for both One year and Two year contracts. Gradient Boosting performed better on One year contracts (0.4444), while Random Forest performed better on Two year contracts (0.3636).

## My promotion rules

- Latency budget (p95): **25 ms**, because all three candidates met this limit, and it provides a reasonable response-time constraint for the service.
- Minimum gain to replace the champion (F1 points): **0.005**, because a new model must improve F1 by at least 0.5 percentage points to justify replacing the current champion.

## What I would check next

I would investigate the low F1 scores for One year and Two year contract customers, especially the number of customers in each slice. I would also monitor changes in customer behavior and data distribution over time to ensure the model remains reliable in production.