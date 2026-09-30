import streamlit as st
import pandas as pd
import joblib

# Load the saved model and feature columns
model = joblib.load('nsl_kdd_model.pkl')
model_columns = joblib.load('model_columns.pkl')

st.set_page_config(page_title="Network Anomaly Detector", layout="centered")

st.title("🛡️ Adaptive Network Traffic Anomaly Classification")
st.markdown("Enter network flow parameters below to detect potential intrusions.")

# Create input fields matching our filtered dataset
col1, col2 = st.columns(2)
with col1:
    duration = st.number_input("Flow Duration", min_value=0, value=0)
    src_bytes = st.number_input("Source Bytes", min_value=0, value=250)
    protocol_type = st.selectbox("Protocol Type", ["tcp", "udp", "icmp"])

with col2:
    count = st.number_input("Packet Count", min_value=0, value=8)
    dst_bytes = st.number_input("Destination Bytes", min_value=0, value=5300)

if st.button("Classify Traffic", type="primary"):
    # Structure the input as a DataFrame
    input_data = pd.DataFrame({
        'duration': [duration],
        'src_bytes': [src_bytes],
        'dst_bytes': [dst_bytes],
        'count': [count],
        'protocol_type': [protocol_type]
    })
    
    # Apply dummy encoding to match training data
    input_data = pd.get_dummies(input_data, columns=['protocol_type'])
    
    # Align the input DataFrame with the model's expected columns (fill missing dummies with 0)
    input_data = input_data.reindex(columns=model_columns, fill_value=0)
    
    # Run prediction
    prediction = model.predict(input_data)
    
    st.divider()
    if prediction[0] == 1:
        st.error("🚨 **ANOMALY DETECTED!** This traffic profile matches known attack signatures.")
    else:
        st.success("✅ **NORMAL TRAFFIC.** No malicious patterns detected.")