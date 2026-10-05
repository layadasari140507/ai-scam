import streamlit as st
import joblib
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Scam & Fraud Detector",
    page_icon="🛡️",
    layout="centered"
)

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("scam_detector_model.pkl")


model = load_model()


# Extract suspicious indicators
def find_red_flags(message):
    flags = []

    message_lower = message.lower()

    # Urgency
    urgency_words = [
        "urgent",
        "immediately",
        "now",
        "hurry",
        "within 10 minutes",
        "act fast"
    ]

    if any(word in message_lower for word in urgency_words):
        flags.append("⚠️ Creates a sense of urgency")

    # OTP
    if "otp" in message_lower:
        flags.append("🔐 Requests or mentions an OTP")

    # Bank details
    bank_words = [
        "bank details",
        "account number",
        "card number",
        "cvv",
        "credit card",
        "debit card"
    ]

    if any(word in message_lower for word in bank_words):
        flags.append("🏦 Requests financial information")

    # Prize / lottery
    prize_words = [
        "lottery",
        "winner",
        "won",
        "prize",
        "reward",
        "cashback",
        "free iphone"
    ]

    if any(word in message_lower for word in prize_words):
        flags.append("🎁 Contains a suspicious prize/reward claim")

    # Payment
    payment_words = [
        "pay",
        "payment",
        "shipping charges",
        "registration fee",
        "customs fee"
    ]

    if any(word in message_lower for word in payment_words):
        flags.append("💳 Requests payment")

    # Link
    if re.search(r"https?://|www\.", message_lower):
        flags.append("🔗 Contains a link")

    # KYC
    if "kyc" in message_lower:
        flags.append("🪪 Mentions KYC verification")

    return flags


# UI
st.title("🛡️ AI Scam & Fraud Message Detector")

st.write(
    "Paste an SMS, WhatsApp message, email, or suspicious message "
    "to check whether it looks like a scam."
)

st.divider()

message = st.text_area(
    "📩 Enter the message",
    height=200,
    placeholder="Example: Congratulations! You won Rs 10,00,000. Click this link to claim your prize..."
)

if st.button("🔍 Detect Scam", type="primary"):

    if not message.strip():
        st.warning("Please enter a message first.")

    else:
        # Prediction
        prediction = model.predict([message])[0]

        # Probability
        probabilities = model.predict_proba([message])[0]
        classes = model.classes_

        probability_dict = dict(zip(classes, probabilities))

        scam_probability = probability_dict.get("scam", 0)
        safe_probability = probability_dict.get("safe", 0)

        # Red flags
        flags = find_red_flags(message)

        st.divider()

        if prediction == "scam":

            st.error("🚨 POSSIBLE SCAM / FRAUD")

            st.metric(
                "Scam Probability",
                f"{scam_probability * 100:.1f}%"
            )

            st.write(
                "⚠️ This message contains patterns commonly "
                "associated with scam or fraudulent messages."
            )

        else:

            st.success("✅ LIKELY SAFE")

            st.metric(
                "Safe Probability",
                f"{safe_probability * 100:.1f}%"
            )

            st.write(
                "This message does not strongly match the "
                "scam patterns learned by the model."
            )

        # Red flags section
        st.subheader("🚩 Detected Red Flags")

        if flags:
            for flag in flags:
                st.write(flag)
        else:
            st.write("No obvious red flags detected.")

        # Safety advice
        st.subheader("🛡️ Safety Advice")

        if prediction == "scam":
            st.warning(
                "Do not click suspicious links, share OTPs, "
                "passwords, CVV, or bank details. Verify the "
                "message through the organization's official website "
                "or phone number."
            )
        else:
            st.info(
                "Even if a message is classified as safe, "
                "avoid sharing sensitive information unless "
                "you have verified the sender."
            )

st.divider()

st.caption(
    "AI Scam & Fraud Message Detector | "
    "TF-IDF + Logistic Regression"
)
