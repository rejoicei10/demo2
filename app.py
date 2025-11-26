import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("insurance_model.pkl")

st.title("Insurance Cost Prediction")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=10, value=0)

data = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'children': [children]
})

if st.button("Predict"):
    prediction = model.predict(data)
    st.success(f"Estimated Insurance Cost: ${prediction[0]:,.2f}")

def run():
    image=Image.open('logo.png')
    image_hospital = Image.open('hospital.jpg')
 
    st.image(image)
    st.sidebar.info("This app is created to predict patient hospital charges")
    st.sidebar.image(image_hospital)
    add_selectbox = st.sidebar.selectbox("How would you like to predict?", ("Online","Batch"))
    st.title("Insurance charges prediction app")
    if add_selectbox=='Online':
        age = st.number_input('Age',min_value=1,max_value=100, value=25)
        sex = st.selectbox('Sex',['male','female'])
        bmi= st.number_input('BMI',min_value=10,max_value=50, value=10)
        children=st.selectbox('Children',[0,1,2,3,4,5,6,7,8,9,10])
        if st.checkbox('Smoker'):
            smoker='yes'
        else:
            smoker='no'
        region = st.selectbox('Region',['southwest','northwest','northeast','southeast'])
        output=""
 
        input_dict = {'age':age,'sex':sex,'bmi':bmi,'children':children,'smoker':smoker,'region': region}
        input_df=pd.DataFrame([input_dict])
 
        if st.button("Predict"):
            output=predict(model=model, input_df=input_df)
            output = "$"+str(output)
        st.success('This Output is {}'.format(output))
 
 
    if add_selectbox=='Batch':
        file_upload = st.file_uploader("Upload a csv file for predictions", type=["csv"])
 
        if file_upload is not None:
            data=pd.read_csv(file_upload)
            predictions = predict_model(estimator=model, data=data)
            st.write(predictions)
 
 
 
 
 
if __name__ =='__main__':
    run()
