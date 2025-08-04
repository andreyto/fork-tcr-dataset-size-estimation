import pandas as pd

for fold in range(1, 6):
    df = pd.read_csv(f'predictions_fold{fold}.csv')
    df = df.rename(columns={'CDR3a': 'cdr3a', 'CDR3b': 'cdr3b', 'score': 'y_score', 'binder': 'y_true'})
    df['y_true'] = df['y_true'].astype(int)
    df = df[['peptide', 'cdr3b', 'y_true', 'y_score']]
    df.to_csv(f'fold_{fold}.csv', index=False)