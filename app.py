import streamlit as st
import pandas as pd

from ai import generate_sql, generate_answer
from database import execute_query

st.set_page_config(page_title="AI MySQL Assistant", page_icon="🤖")

st.title("🤖 AI MySQL Assistant")
st.write("Ask questions about the database using normal language.")

question = st.text_input(
    "Ask your question",
    placeholder="Example: Show me all students from Chandigarh"
)

if st.button("Ask AI"):
    if not question:
        st.warning("Please enter a question.")
        st.stop()

    try:
        sql = generate_sql(question)

        st.subheader("Generated SQL")
        st.code(sql, language="sql")

        # Basic safety check: only SELECT queries are allowed.
        if not sql.lower().strip().startswith("select"):
            st.error("Only SELECT queries are allowed.")
            st.stop()

        result = execute_query(sql)

        st.subheader("Database Result")

        if result:
            df = pd.DataFrame(result)
            st.dataframe(df, use_container_width=True)

            answer = generate_answer(question, result)

            st.subheader("🤖 AI Answer")
            st.write(answer)
        else:
            st.info("No data found.")

    except Exception as e:
        st.error(f"Something went wrong: {str(e)}")
