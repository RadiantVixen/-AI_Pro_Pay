import React from "react";
import axios from "axios";
import { loadStripe } from "@stripe/stripe-js";

const stripePromise = loadStripe("your_stripe_publishable_key");  // Replace with your key

const PaymentButton = () => {
  const handlePayment = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/create-checkout-session/");
      window.location.href = `https://checkout.stripe.com/pay/${response.data.sessionId}`;
    } catch (error) {
      console.error("Payment Error:", error);
    }
  };

  return (
    <button onClick={handlePayment} className="bg-blue-500 text-white px-4 py-2 rounded">
      Buy AI Pro Plan - $9
    </button>
  );
};

export default PaymentButton;
