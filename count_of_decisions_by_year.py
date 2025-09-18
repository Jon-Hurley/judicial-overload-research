import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def count_decisions_by_year(df):
    # Group by the 'term' field, which represents the year the case was decided
    decision_counts = df['term'].value_counts().sort_index()
    return decision_counts

def plot_decisions_by_year(decision_counts):
    plt.figure(figsize=(12, 6))
    decision_counts.plot(kind='bar', color='steelblue')
    plt.title('Number of Supreme Court Decisions by Year')
    plt.xlabel('Term Year')
    plt.ylabel('Number of Decisions')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.grid(axis='y')
    # plt.show()
    # save plot
    plt.savefig('figures/decisions_by_year.png')

if __name__ == '__main__':
    file_path = 'scdata/SCDB_2024_01_caseCentered_Citation.csv'  # Update as needed
    df = load_data(file_path)
    decision_counts = count_decisions_by_year(df)
    plot_decisions_by_year(decision_counts)