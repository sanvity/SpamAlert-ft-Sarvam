# 🛡️ TrapAlert — Voice Scam Detection & Awareness Coach

> **Tagline:** *Pause. Verify. Stay safe.*  
> Built for the **Sarvam AI Hackathon**  
> Powered by Sarvam AI: **`saaras:v4`** (Speech-to-Text), **`mayura:v1`** (Translation), and **`sarvam-105b-conversations`** (Conversational Scam Analysis).

---

## 📌 Problem Statement

Every year, Indian citizens lose over **₹1,750+ Crores** to cybercrime through WhatsApp audio calls, fake police intimidation ("Digital Arrest"), utility bill disconnection threats with malicious APKs, and UPI reverse-pay cashback traps.

Most existing spam checkers only classify text or provide binary "Spam / Ham" labels without addressing multilingual Indian voice notes, call recordings, or code-mixed Hinglish.

---

## 💡 Solution: The 4-Stage Voice Pipeline

TrapAlert provides a clean, sequential workflow:

$$\text{Record Audio} \longrightarrow \text{Sarvam Transcript} \longrightarrow \text{English Translation} \longrightarrow \text{Scam Alert}$$

Displayed vertically in this exact order:

1. **Transcript**
   - Exact speech recognition output via Sarvam's **Saaras v4 / v3** model, preserving language & script (Hindi Devanagari, Hinglish Roman, English).
   - Shows recognized language code (e.g. `hi-IN`).
   - Integrated audio playback control.
   - Fully editable text area so users can correct misheard words. Editing invalidates previous stages and triggers fresh translation and analysis.

2. **English Translation**
   - Faithful, un-summarized English translation via Sarvam's official **Translation API** (`mayura:v1`).
   - Preserves original urgency, threats, and monetary requests without sanitization.

3. **Scam Alert**
   - Evaluates the final transcript with the English translation as supplementary context using **`sarvam-105b-conversations`**.
   - **Risk Level:** `High`, `Medium`, or `Low`.
   - **Why it was flagged:** Concise explanation.
   - **Suspicious evidence:** Exact phrases quoted directly from the original transcript with explanations.
   - **Recommended action:** Clear, practical next steps.
   - **Uncertainty handling:** Low risk includes an explicit reminder that it is not proof of safety.
   - **Deterministic security rules:** Immediate elevation to High for obvious UPI PIN demands to receive money, APK downloads for utility bills, and video-call arrest threats.

4. **🧪 Scam Lab**
   - Secondary practice arena for testing and building scam reflexes on simulated scenarios.

---

## 🛠️ Tech Stack & Sarvam AI Integration

- **Frontend:** Streamlit with minimal, typography-focused layout
- **Sarvam AI Python SDK:** `sarvamai` (v0.1.39+)
  - **Speech Transcription:** `client.speech_to_text.transcribe(model="saaras:v4", mode="codemix")`
  - **Text Translation:** `client.text.translate(model="mayura:v1", target_language_code="en-IN")`
  - **Conversational Scam Analysis:** `client.chat.completions(model="sarvam-105b-conversations")`
- **Environment Management:** `python-dotenv` for `SARVAM_API_KEY` (kept out of version control)

---

## 🚀 Quickstart Guide

### 1. Clone & Enter Directory
```bash
cd /path/to/SARVAM_KIVI
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
Copy the template and add your Sarvam AI API subscription key:
```bash
cp .env.example .env
```
Edit `.env`:
```env
SARVAM_API_KEY=your_sarvam_api_key_here
```
*(Note: You can also enter or override your API key directly in the Streamlit sidebar during live demonstration).*

### 4. Run the Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 🎮 Demo Walkthrough for Evaluators

1. **Test Real-World Indian Presets:**
   - Click on **⚡ Bijli Vibhag Disconnection (Hindi)**, **💸 UPI Cashback (Hinglish)**, or **🚨 Digital Arrest (English)**.
   - Switch between **English**, **हिंदी**, and **Hinglish** coaching modes to see Sarvam AI adapt its explanations.
   - Notice the highlighted red-flag phrases and breakdown of psychological manipulation levers.
2. **Baseline Legitimate Comparison:**
   - Click on **✅ Legitimate Bank Transaction Alert**.
   - Notice that TrapAlert correctly identifies legitimate regulatory alerts without false positives.
3. **Play the Scam Dojo (Simulation):**
   - Switch to the **🎯 Scam Dojo** tab.
   - Test your decision-making on scenarios like "UPI Accidental Transfer" or "CBI Courier Call".
   - Review the detailed tactical feedback and earn your Scam Shield Rank.
4. **Emergency Directory:**
   - Switch to the **🚨 Emergency Action Guide** for the 1930 Helpline and Golden Hour protocol.

---

## 🔐 Security & Privacy
- TrapAlert does not store or log analyzed messages or API keys.
- API keys are retrieved from environment variables or masked session inputs.
- `.env` is excluded via `.gitignore`.
