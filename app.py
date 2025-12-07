import streamlit as st
import pandas as pd
import random

def load_questions():
    df = pd.read_csv("english_order_questions.csv")
    # BOM対策
    df.columns = df.columns.str.replace('\ufeff', '', regex=False)
    return df

# CSV読み込み（ここだけでOK！）
df = load_questions()

# 列名確認（デバッグ用）
st.write("Columns:", df.columns.tolist())

# 初期化
if "current" not in st.session_state:
    st.session_state.current = random.randint(0, len(df)-1)

# 現在の問題
row = df.iloc[st.session_state.current]

st.title("英語並び替え問題")

row = df.sample(1).iloc[0]

words = [
    row["word1"], row["word2"], row["word3"],
    row["word4"], row["word5"], row["word6"]
]

random.shuffle(words)

user_answer = st.text_input("並び替えた英文を入力", "")

if st.button("回答"):
    correct = row["correct"]
    if user_answer.strip() == correct.strip():
        st.success("正解！")
    else:
        st.error(f"不正解。正解は：{correct}")

    # 次の問題へ
    st.session_state.current = random.randint(0, len(df)-1)
    st.experimental_rerun()