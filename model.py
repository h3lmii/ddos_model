import streamlit as st
import pickle
import joblib
#load the saved machine learning model
loaded_model = joblib.load(open('ddos_model.pkl', 'rb'))

#function that return the prediction 
def label_predict(a):
	if a[0]==1:
		result='this is a DDOS attack'
	else:
		result='Not a DDOS attack'
	return result

#the main function that will run
def main():
	st.title("Identify type of CyberSecurity Attack Using Machine Learning")
	
#some style of streamlit
	col1, col2, col3 , col4 = st.columns(4)

	with col1:
		#inputs of the 4 features
		number1 = st.number_input('Bwd Packet Length Std',key=1)
	with col2:
		number2 = st.number_input('Total Backward Packets',key=2)
	with col3:
		number3 = st.number_input('Insert Flow Duration',key=3)
	with col4:
		number4 = st.number_input('Insert Flow IAT Min',key=4)

#the button to run the prediction and show the result
	if st.button("Process"):
		result= label_predict(loaded_model.predict([[number1,number2,number3,number4]]))
		st.header(result)


	st.header('Identify type of CyberSecurity Attack Using the difference of features (from the DATASET)')
	st.image('img1.png')
	st.image('img2.png')
	st.image('img3.png')

if __name__ == '__main__':
    main()
