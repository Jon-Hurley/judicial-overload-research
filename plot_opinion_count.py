import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def plot_opinion_count(df):
    plt.figure(figsize=(14, 6))
    plt.bar(df['year'], df['texts'], color='mediumseagreen')
    plt.title('Number of Supreme Court Opinions per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Opinions')
    plt.grid(axis='y')
    plt.tight_layout()
    # plt.show()
    # save plot
    plt.savefig('supreme_court_opinions_per_year.png')

if __name__ == '__main__':
    file_path = 'courtdata/supreme_court_opinion_lengths.csv'  # Update if needed
    df = load_data(file_path)
    plot_opinion_count(df)