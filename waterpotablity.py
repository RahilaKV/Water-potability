import streamlit as st
import pickle
from PIL import Image

#create a function
def main():
    #to add title (st means streamlit)
    st.title(':red[WATER POTABILITY PREDICTION]')
    #to read image
    image=Image.open(r"C:\Users\user\Desktop\water potablity\waterimage.jpg")
    st.image(image,width=600)

    #identify the features

    #input features
    ph=st.text_input('ph','Type Here')
    Hardness=st.text_input('Hardness','Type Here')
    Solids=st.text_input('Solids','Type Here') 
    Chloramines=st.text_input('Chloramines','Type Here') 
    Sulfate=st.text_input('Sulfate','Type Here') 
    Conductivity=st.text_input('Conductivity','Type Here') 
    Organic_carbon=st.text_input('Organic_carbon','Type Here') 
    Trihalomethanes=st.text_input('Trihalomethanes','Type Here')     
    Turbidity=st.text_input('Turbidity','Type Here')
   

    #store all features in a variable
    f=[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]
    #load the stored model and scalar
    model1 = pickle.load(open(r"C:\Users\user\Desktop\water potablity\water1", "rb"))
    scaler1 = pickle.load(open(r"C:\Users\user\Desktop\water potablity\scaler1", "rb"))


    #to predict we add a button

    pred=st.button('PREDICT')


    #enable button
    prediction = None  # default value

    if pred:
        prediction=model1.predict(scaler1.transform([f]))#single squre bracket bcz features already in list format
        if prediction==0:
        #to print use write
            st.write('water is not potable')
        else:
            st.write('water is potable')
            st.balloons()
main()
           







