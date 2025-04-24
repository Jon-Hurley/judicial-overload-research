

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def count_decisions_by_chief(df):
    # Known chronological order of Chief Justices
    chief_order = ['Vinson', 'Warren', 'Burger', 'Rehnquist', 'Roberts']
    counts = df['chief'].value_counts()
    return counts.reindex(chief_order)

def plot_decisions_by_chief(decision_counts):
    plt.figure(figsize=(10, 6))
    decision_counts.plot(kind='bar', color='mediumseagreen')
    plt.title('Number of Supreme Court Decisions by Chief Justice')
    plt.xlabel('Chief Justice')
    plt.ylabel('Number of Decisions')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(axis='y')
    plt.show()

if __name__ == '__main__':
    file_path = 'scdata/SCDB_2024_01_caseCentered_Citation.csv'  # Update as needed
    df = load_data(file_path)
    decision_counts = count_decisions_by_chief(df)
    plot_decisions_by_chief(decision_counts)