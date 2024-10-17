import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# streamlit run app.py --server.port PORT_NO
# PORT_NO
# TODO: Refactoring to React.js, FastAPI
def main():
    st.title('Start') # Header
    st.write("""
             Body
             """)

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig) # streamlit: plot update

if __name__ =="__main__":
    main()