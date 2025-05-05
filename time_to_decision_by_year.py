import pandas as pd
import matplotlib.pyplot as plt

def load_and_prepare_data(file_path):
    # Load the data
    df = pd.read_csv(file_path)

    # Convert date columns to datetime
    df['dateArgument'] = pd.to_datetime(df['dateArgument'], errors='coerce')
    df['dateDecision'] = pd.to_datetime(df['dateDecision'], errors='coerce')

    # Drop rows with missing or invalid dates
    df = df.dropna(subset=['dateArgument', 'dateDecision'])

    # Calculate days between argument and decision
    df['daysToDecision'] = (df['dateDecision'] - df['dateArgument']).dt.days

    return df

def average_days_by_year(df):
    # Chronological order of Chief Justices

    avg_days = df.groupby('term')['daysToDecision'].mean()
    return avg_days.sort_index()

def plot_average_days(avg_days_by_year):
    plt.figure(figsize=(10, 6))
    avg_days_by_year.plot(kind='bar', color='skyblue')
    plt.title('Average Days to Decision by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Days to Decision')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(axis='y')
    plt.show()

if __name__ == '__main__':
    file_path = 'scdata/SCDB_2024_01_caseCentered_Citation.csv'  # Change this to your actual file path
    df = load_and_prepare_data(file_path)
    avg_days = average_days_by_year(df)
    plot_average_days(avg_days)