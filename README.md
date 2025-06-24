# EmotionIQ: Decoding Human Feelings Through AI 

Link to download Dataset : https://drive.google.com/file/d/1T5KKJR2E1nbVSr-pEVjIJseF-ZiJzEb8/view?usp=sharing
pickle file link : https://drive.google.com/file/d/1NAH-kvJQ7ZeD5HaUNisjJPZxHccWxltx/view?usp=sharing

📌 Objective:
To develop a real-time web application that analyzes textual input and predicts the underlying human emotion using NLP and machine learning techniques, enabling deeper understanding of user sentiments.

⚙ How It Works:
🔹 User Interface (Front End) – Streamlit:
The application features a visually engaging and intuitive interface built with Streamlit, allowing users to enter a sentence and get instant emotion predictions.

Text Input: A text box for users to enter any sentence or phrase

Custom UI Styling: Dark-themed layout with a background image to reflect emotional depth

Emotion Output: Detected emotion is shown in real-time upon clicking "Predict Emotion"

🔹 Data Preprocessing and Transformation:
Upon receiving the user's sentence:

Vectorization: The text is transformed using a pre-trained CountVectorizer or TF-IDF vectorizer

Encoding: Emotions are mapped to integer labels using LabelEncoder for efficient prediction

Input Shape: The vectorized input is reshaped for compatibility with the ML model

🧠 Machine Learning Model – Back End:
A pre-trained ML classifier (such as Logistic Regression, SVM, or Random Forest) is used to classify emotions. The model, vectorizer, and label encoder are stored in a serialized .pkl file.

Model Output:

Predicts one of the emotions like joy, sadness, anger, fear, love, disgust, surprise, or neutral

Displays the predicted emotion in a success message with styled formatting

📊 Machine Learning Techniques Used:
Multiple classification models were tested, including:

Logistic Regression

Support Vector Machine (SVM)

Random Forest Classifier

Multinomial Naive Bayes

🏆 Best Model:
The final deployed model was selected based on accuracy, F1-score, and overall performance during cross-validation and testing. (Model details saved in emotions.pkl)

🌐 Deployment & Usability:
🔹 Interactive Web App: Built using Streamlit – no coding knowledge required for users
🔹 Real-Time Prediction: Users receive instant emotion feedback upon submitting text
🔹 Custom Design: A themed emotional background image enhances the user experience

