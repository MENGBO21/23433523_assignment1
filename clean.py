import pandas as pd
import argparse
def clean(input1, input2, output):
    df_contact = pd.read_csv(input1)
    df_other = pd.read_csv(input2)
    merged_df = pd.merge(df_contact, df_other, left_on='respondent_id', right_on='id')
    merged_df.drop(columns='id', inplace=True)
    merged_df.dropna(inplace=True)
    cleaned_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]
    cleaned_df.to_csv(output, index=False)
    output_df = pd.read_csv(args.output)
    print("Output file shape is:", output_df.shape)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='respondent_contact.csv file')
    parser.add_argument('input2', help='respondent_other.csv file')
    parser.add_argument('output', help='Output file')
    args = parser.parse_args()
    clean(args.input1, args.input2, args.output)