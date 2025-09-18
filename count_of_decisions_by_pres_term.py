import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_csv(file_path)
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

def count_decisions_by_president(df):
    df['dateDecision'] = pd.to_datetime(df['dateDecision'], errors='coerce')
    df = df.dropna(subset=['dateDecision'])
    df['president'] = df['dateDecision'].apply(assign_president)
    presidents_order = [p[0] for p in [
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
    ]]
    counts = df['president'].value_counts()
    return counts.reindex(presidents_order)

def plot_decisions_by_president(decision_counts):
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
    ax = decision_counts.plot(kind='bar', color='steelblue')
    plt.title('Number of Supreme Court Decisions by Presidential Term')
    plt.xlabel('President')
    plt.ylabel('Number of Decisions')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(axis='y')

    # Add Chief Justice labels
    for i, president in enumerate(decision_counts.index):
        chief = president_to_chief.get(president, '')
        count = decision_counts[president]
        ax.text(i, count + 5, chief, ha='center', va='bottom', fontsize=8, color='black')

    # plt.show()
    # save plot
    plt.savefig('figures/decisions_by_presidential_term.png')

if __name__ == '__main__':
    file_path = 'scdata/SCDB_2024_01_caseCentered_Citation.csv'  # Update as needed
    df = load_data(file_path)
    decision_counts = count_decisions_by_president(df)
    plot_decisions_by_president(decision_counts)