import streamlit as st
import pandas as pd

st.title("英語並び替え問題")

# CSV読み込み（※dfはここで初めて定義される）
df = pd.read_csv("english_order_questions.csv")

# CSV読み込み
df = load_questions()

# 初期化
if "current" not in st.session_state:
    st.session_state.current = random.randint(0, len(df)-1)

# 現在の問題
row = df.iloc[st.session_state.current]

st.subheader("語句を並べ替えて正しい英文を作りましょう")

choices = [
    row["word1"], row["word2"], row["word3"],
    row["word4"], row["word5"], row["word6"]
]

random.shuffle(choices)

st.write("語句：", " / ".join(choices))

user_answer = st.text_input("英文を入力（スペース区切り）")

if st.button("回答する"):
    correct = row["answer"].strip().lower()
    user = user_answer.strip().lower()

    if correct == user:
        st.success("正解！")
    else:
        st.error(f"不正解… 正解は: {correct}")

    # 次の問題へ
    st.session_state.current = random.randint(0, len(df)-1)
    st.experimental_rerun()