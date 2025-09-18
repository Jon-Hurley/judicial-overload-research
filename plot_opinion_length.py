import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def compute_average_opinion_length(df):
    df['average_length'] = df['words'] / df['texts']
    return df

def plot_average_opinion_length(df):
    plt.figure(figsize=(14, 6))
    plt.plot(df['year'], df['average_length'], color='darkblue', linewidth=2)
    plt.title('Average Supreme Court Opinion Length by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Opinion Length (words)')
    plt.grid(True)
    plt.tight_layout()
    # plt.show()
    # save plot
    plt.savefig('figures/average_opinion_length_per_year.png')

if __name__ == '__main__':
    file_path = 'courtdata/supreme_court_opinion_lengths.csv'  # Update if needed
    df = load_data(file_path)
    df = compute_average_opinion_length(df)
    plot_average_opinion_length(df)