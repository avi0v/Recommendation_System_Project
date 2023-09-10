import pandas as pd 
import pickle as pkl
import streamlit as st
import numpy as np

st.title(' Book Recommendation System')

#similarity
user_sim_df=pkl.load(open('sim.pkl','rb'))

#user data
final_df=pkl.load(open('user.pkl','rb'))


#user id input
customer_id=st.text_input('Enter User Id',placeholder='22625')

# button css 
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #20b2aa ;
}
</style>""", unsafe_allow_html=True)

number=st.slider('No of Recommendations',min_value=5,max_value=100)



if st.button('Recommend'):
    customer_id=int(customer_id)
    
    try :
      tem = list(user_sim_df.sort_values([customer_id],ascending=False).head(100).index)
      book_list=[]
      for i in tem:
        #read by user
          book_list=book_list+list(final_df[final_df['user']==i]['book'])
        #not read by user
          nr=set(book_list)-set(final_df[final_df['user']==customer_id]['book'])
          nr=list(nr)
      st.title('You May Also Like')
      for i in nr[:number]:
         st.write(i)
         
    except :
       st.title( "This account has been suspended")
       st.markdown('contact admin for more information.')

