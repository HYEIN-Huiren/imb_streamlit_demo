import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# streamlit run app.py --server.port PORT_NO
# PORT_NO
# TODO: Refactoring to React.js, FastAPI
def main():
    st.title('Start') # Title
    st.write("""
             Body
             """)
    with st.sidebar:
        st.header('sider') # Sidebar Header

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig) # streamlit: plot update

    tab1, tab2, tab3 = st.sidebar.tabs(["Tab2", "Tab1", "Tab3"])

    with tab1:
        st.write('tab1')

    with tab2:
        st.write('tab2')
    
    with tab3:
        st.write('tab3')
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.write('col1')
    
    with col2:
        st.write('col2')

    with col3:
        st.write('col3')

if __name__ =="__main__":
    main()