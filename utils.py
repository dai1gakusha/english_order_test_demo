import pandas as pd

def load_questions(csv_path="english_order_questions.csv"):
    return pd.read_csv(csv_path)