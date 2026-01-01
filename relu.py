import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("ReLU Activation Function")

st.write(
    "This web application visualises the Rectified Linear Unit (ReLU) activation function. "
    "It shows how negative input values are converted to zero, while positive values remain unchanged. "
    "ReLU is commonly used in deep neural networks to introduce non-linearity."
)

x = np.linspace(-10, 10, 400)
y = np.maximum(0, x)

plt.figure()
plt.plot(x, y)
plt.xlabel("Input (x)")
plt.ylabel("ReLU(x)")
plt.title("Rectified Linear Unit (ReLU)")
plt.grid(True)

st.pyplot(plt)