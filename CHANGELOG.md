For the model evaluation code in `bootstrap.ipynb`:
- Parallellized inner and outer loops with joblib
- Loop over all data in one go - data layout refactured to hold all experiments at once
- Skip over non-existing model outputs
- Apply weighted AUC-ROC from scikit-learn: combined weight of each peptide is unchanged 
  when example count is <=40 (~20 positives) and set to 40 for larger counts. Weight is
  computed on each bootstrapped replica
- Apply per-peptide nested bootstrap to correctly estimate CIs in the presense of clustering
  of examples at the peptides, with peptides resampled **without replacement** to
  mitigate inflation of variance from weight being dependent on replica variation. Examples
  within each peptide are resampled with replacement.
- Censor those test examples which have their TCRs found in the training set