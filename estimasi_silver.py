import pickle
import streamlit as st

model = pickle.load(open('estimasi_silver.sav', 'rb'))

st.title('Estimasi Harga silver ')

Open = st.number_input('Input Harga Open')
High = st.number_input('Input Harga High')
Low = st.number_input('Input Harga Low')
Close = st.number_input('Input Harga Close')
Volume = st.number_input('Input Volume')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Estimasi harga silver dalam USD : ', predict)
    st.write ('Estimasi harga silver dalam IDR (Juta) :', predict*19000)