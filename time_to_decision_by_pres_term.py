

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

def assign_president(date):
    presidents = [
        ('Truman', '1945-04-12', '1953-01-20'),
        ('Eisenhower', '1953-01-20', '1961-01-20'),
        ('Kennedy', '1961-01-20', '1963-11-22'),
        ('Johnson', '1963-11-22', '1969-01-20'),
        ('Nixon', '1969-01-20', '1974-08-09'),
        ('Ford', '1974-08-09', '1977-01-20'),
        ('Carter', '1977-01-20', '1981-01-20'),
        ('Reagan', '1981-01-20', '1989-01-20'),
        ('Bush41', '1989-01-20', '1993-01-20'),
        ('Clinton', '1993-01-20', '2001-01-20'),
        ('Bush43', '2001-01-20', '2009-01-20'),
        ('Obama', '2009-01-20', '2017-01-20'),
        ('Trump', '2017-01-20', '2021-01-20'),
        ('Biden', '2021-01-20', '2100-01-20')
    ]
    for name, start, end in presidents:
        if pd.Timestamp(start) <= date < pd.Timestamp(end):
            return name
    return 'Unknown'

def average_days_by_president(df):
    df['president'] = df['dateDecision'].apply(assign_president)
    presidents = [
        'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford',
        'Carter', 'Reagan', 'Bush41', 'Clinton', 'Bush43',
        'Obama', 'Trump', 'Biden'
    ]
    avg_days = df.groupby('president')['daysToDecision'].mean()
    return avg_days.reindex(presidents)

def plot_average_days_by_president(avg_days):
    president_to_chief = {
        'Truman': 'Vinson',
        'Eisenhower': 'Warren',
        'Kennedy': 'Warren',
        'Johnson': 'Warren',
        'Nixon': 'Burger',
        'Ford': 'Burger',
        'Carter': 'Burger',
        'Reagan': 'Burger',
        'Bush41': 'Rehnquist',
        'Clinton': 'Rehnquist',
        'Bush43': 'Rehnquist',
        'Obama': 'Roberts',
        'Trump': 'Roberts',
        'Biden': 'Roberts'
    }

    plt.figure(figsize=(12, 6))
    ax = avg_days.plot(kind='bar', color='salmon')

    plt.title('Average Days to Decision by Presidential Term')
    plt.xlabel('President')
    plt.ylabel('Average Days to Decision')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')

    # Add chief justice labels above each bar
    for i, president in enumerate(avg_days.index):
        chief = president_to_chief.get(president, '')
        value = avg_days[president]
        ax.text(i, value + 2, chief, ha='center', va='bottom', fontsize=8, color='black')

    plt.tight_layout()
    # plt.show()
    # save plot
    plt.savefig('figures/average_days_to_decision_by_president.png')

if __name__ == '__main__':
    file_path = 'scdata/SCDB_2024_01_caseCentered_Citation.csv'  # Update if needed
    df = load_and_prepare_data(file_path)
    avg_days_president = average_days_by_president(df)
    plot_average_days_by_president(avg_days_president)