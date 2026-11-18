import streamlit as st 
import pandas as pd 
import joblib 

model=joblib.load("KNN_heart.pkl")
scaler=joblib.load("scaler.pkl")
expected_columns=joblib.load("columns.pkl")

st.title("HEART STROKE PREDICTION BY KARTIK")
st.markdown("provide the following details")

st.slider("Age",18,100,40)
st.selectbox("SEX",["M","F"])
chest_pain=st.selectbox("chest pain type ",["ATA","NAP","TA","ASY"])
resting_bp=st.number_input("resting blood pressure(mm hg)",80,200,120)
cholestrol=st.number_input("cholestrol(mg/dl)",100,600,200)
fasting_bs=st.selectbox("fasting blood sugar > 120 (mg/dl)",[0,1])
resting_ecg=st.selectbox("resting ecg",["NORMAL","ST","LVH"])
max_hr=st.slider("Max heart rate",60,220,150)
exercise_angina=st.selectbox("Exercise included angina",["Y","N"])
oldpeak=st.slider("Oldpeak(ST DEPRESSION)",0.0,6.0,1.0)
st_slope=st.selectbox("ST Slope",["UP","FLAT","DOWN"])

if st.button("Predict"):
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }
input_df=pd.Dataframe(["raw_input"])
for col in expected_columns:
    if column not in input_df.columns:
         input_df[col]=0

input_df=input_df[expected_columns]
scaled_input=scaler.transform(input_df)
prediction=model.predict(scaled_input)[0]


if prediction == 1:
    st.error("⚠️ High Risk of Heart Disease")
else:
    st.success("✅ Low Risk of Heart Disease")
         


