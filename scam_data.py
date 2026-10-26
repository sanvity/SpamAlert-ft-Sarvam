"""
TrapAlert - Scam Data & Simulation Knowledge Base
Curated real-world Indian cyber-scam patterns, presets, and interactive training simulations.
"""

# Presets for 1-click testing in the UI
SAMPLE_RECORDINGS = [
    {
        "id": "hindi_sample",
        "title": "Hindi Scam Recording (Electricity Bill APK)",
        "file_path": "samples/hindi_bijli_scam.wav",
        "language_name": "Hindi (hi-IN)",
        "raw_transcript": "प्रिय ग्राहक, आपका बिजली कनेक्शन आज रात काट दिया जाएगा। तुरंत एपीके डाउनलोड करें bit.ly/bijli-pay",
        "translation": "Dear customer, your electricity connection will be cut tonight. Download APK immediately bit.ly/bijli-pay",
        "risk_level": "High",
        "why_flagged": "Threatens immediate utility disconnection and instructs downloading an untrusted .apk file via a shortened bit.ly URL.",
        "suspicious_evidence": [
            {
                "phrase": "बिजली कनेक्शन आज रात काट दिया जाएगा",
                "explanation": "Manufactures urgency to induce panic so the victim acts without verifying."
            },
            {
                "phrase": "एपीके डाउनलोड करें bit.ly/bijli-pay",
                "explanation": "Electricity departments never distribute .apk files; this is malicious Android malware used to steal banking OTPs."
            }
        ],
        "recommended_action": [
            "Do NOT click the link or download any .apk file.",
            "Never contact numbers or follow links sent via unofficial SMS.",
            "Verify your electricity bill status only through the official Discom portal or app.",
            "Report the sender to the National Cyber Crime Helpline at 1930."
        ],
        "report": {
            "risk_level": "High",
            "why_flagged": "Threatens immediate utility disconnection and instructs downloading an untrusted .apk file via a shortened bit.ly URL.",
            "suspicious_evidence": [
                {
                    "phrase": "बिजली कनेक्शन आज रात काट दिया जाएगा",
                    "explanation": "Manufactures urgency to induce panic so the victim acts without verifying."
                },
                {
                    "phrase": "एपीके डाउनलोड करें bit.ly/bijli-pay",
                    "explanation": "Electricity departments never distribute .apk files; this is malicious Android malware used to steal banking OTPs."
                }
            ],
            "recommended_action": [
                "Do NOT click the link or download any .apk file.",
                "Never contact numbers or follow links sent via unofficial SMS.",
                "Verify your electricity bill status only through the official Discom portal or app.",
                "Report the sender to the National Cyber Crime Helpline at 1930."
            ]
        }
    },
    {
        "id": "hinglish_sample",
        "title": "Hinglish Scam Recording (UPI Cashback PIN Trap)",
        "file_path": "samples/hinglish_upi_scam.wav",
        "language_name": "Hinglish (hi-Latn)",
        "raw_transcript": "Badhaai ho! Aapko PhonePe pe ₹4,999 cashback mila hai. Paisa lene ke liye link pe click karein aur UPI PIN enter karein.",
        "translation": "Congratulations! You have received a ₹4,999 cashback reward on PhonePe. Click the link to receive money and enter your UPI PIN.",
        "risk_level": "High",
        "why_flagged": "Classic UPI reverse pay trap asking user to enter a UPI PIN to receive money or rewards.",
        "suspicious_evidence": [
            {
                "phrase": "UPI PIN enter karein",
                "explanation": "UPI PIN is only for SENDING money. Entering your PIN will instantly deduct money from your bank account."
            },
            {
                "phrase": "₹4,999 cashback mila hai",
                "explanation": "Unsolicited cash reward bait used to deceive users into authorizing a fraudulent collect request."
            }
        ],
        "recommended_action": [
            "Do NOT enter your UPI PIN on any request, link, or scratch card.",
            "Decline any collect request in your UPI app immediately.",
            "Report and block the sender on WhatsApp/SMS and on Sanchar Saathi (Chakshu).",
            "If PIN was entered, contact your bank immediately to freeze your account."
        ],
        "report": {
            "risk_level": "High",
            "why_flagged": "Classic UPI reverse pay trap asking user to enter a UPI PIN to receive money or rewards.",
            "suspicious_evidence": [
                {
                    "phrase": "UPI PIN enter karein",
                    "explanation": "UPI PIN is only for SENDING money. Entering your PIN will instantly deduct money from your bank account."
                },
                {
                    "phrase": "₹4,999 cashback mila hai",
                    "explanation": "Unsolicited cash reward bait used to deceive users into authorizing a fraudulent collect request."
                }
            ],
            "recommended_action": [
                "Do NOT enter your UPI PIN on any request, link, or scratch card.",
                "Decline any collect request in your UPI app immediately.",
                "Report and block the sender on WhatsApp/SMS and on Sanchar Saathi (Chakshu).",
                "If PIN was entered, contact your bank immediately to freeze your account."
            ]
        }
    },
    {
        "id": "benign_sample",
        "title": "Benign Bank Alert (Swiggy Debit Notification)",
        "file_path": "samples/benign_bank_alert.wav",
        "language_name": "English (en-IN)",
        "raw_transcript": "Dear Customer, INR 450.00 debited from account for Swiggy Bangalore on 26 October. If not done by you, call 1800-11-2211.",
        "translation": "Dear Customer, INR 450.00 debited from account for Swiggy Bangalore on 26 October. If not done by you, call 1800-11-2211.",
        "risk_level": "Low",
        "why_flagged": "Standard regulatory bank debit confirmation with legitimate merchant details and official toll-free dispute number. No requests for OTP, PIN, or external link downloads.",
        "suspicious_evidence": [],
        "recommended_action": [
            "If you made this purchase on Swiggy, no action is needed.",
            "If you did NOT authorize this debit, call the official bank toll-free number (1800-11-2211) immediately to block your card/UPI."
        ],
        "uncertainty_note": "A Low risk rating is an indicator of typical legitimate communications, not a guarantee of safety. Always verify senders and transactions independently.",
        "report": {
            "risk_level": "Low",
            "why_flagged": "Standard regulatory bank debit confirmation with legitimate merchant details and official toll-free dispute number. No requests for OTP, PIN, or external link downloads.",
            "suspicious_evidence": [],
            "recommended_action": [
                "If you made this purchase on Swiggy, no action is needed.",
                "If you did NOT authorize this debit, call the official bank toll-free number (1800-11-2211) immediately to block your card/UPI."
            ],
            "uncertainty_note": "A Low risk rating is an indicator of typical legitimate communications, not a guarantee of safety. Always verify senders and transactions independently."
        }
    }
]

PRESET_MESSAGES = [
    {
        "id": "bijli_apk_hindi",
        "title": "⚡ Bijli Vibhag Disconnection (Hindi)",
        "channel": "SMS / WhatsApp",
        "language": "Hindi",
        "text": "प्रिय ग्राहक, आपका बिजली कनेक्शन आज रात 9:30 बजे काट दिया जाएगा क्योंकि आपका पिछले महीने का बिल अपडेट नहीं हुआ है। तुरंत हमारे बिजली अधिकारी 9876543210 पर संपर्क करें या बिल अपडेट करने के लिए apk डाउनलोड करें: bit.ly/bijli-pay-bill",
        "category": "Utility Impersonation / Malicious APK",
        "expected_risk": "CRITICAL",
    },
    {
        "id": "upi_cashback_hinglish",
        "title": "💸 UPI Cashback / PhonePe Scratch Card (Hinglish)",
        "channel": "WhatsApp / SMS",
        "language": "Hinglish",
        "text": "Badhaai ho! Aapko PhonePe pe ₹4,999 ka cashback reward mila hai. Paisa apne bank account me lene ke liye neeche diye link pe click karein aur apna 6-digit UPI PIN enter karein: https://phonepe-rewards-claim.in/collect?id=8831",
        "category": "UPI PIN Trap / Collect Request",
        "expected_risk": "CRITICAL",
    },
    {
        "id": "digital_arrest_english",
        "title": "🚨 Digital Arrest / CBI Mumbai Police (English)",
        "channel": "Call Transcript / WhatsApp",
        "language": "English",
        "text": "ATTENTION: This is Inspector Ajay Kumar from Mumbai Cyber Crime Branch. A FedEx parcel sent under your Aadhaar card number containing 5 expired passports and 140 grams of narcotics was intercepted at customs. An arrest warrant has been issued in your name under PMLA. Stay on this WhatsApp video call immediately for confidential verification or our local unit will arrive at your address within 2 hours.",
        "category": "Digital Arrest / Extortion / Impersonation",
        "expected_risk": "CRITICAL",
    },
    {
        "id": "telegram_job_hinglish",
        "title": "📱 Part-time YouTube Like Job (Hinglish)",
        "channel": "WhatsApp / Telegram",
        "language": "Hinglish",
        "text": "Hello dear! Main Global Media HR Pooja baat kar rahi hoon. Hamare paas flexible work from home task hai. Bas daily 5 YouTube videos like karke screenshot bhejna hai. Har like ka ₹150 milega (daily ₹3000-₹8000). Direct UPI transfer guaranteed. Join our VIP Telegram channel @india_earn_tasks to receive task 1 right now!",
        "category": "Task / Advance Fee Investment Scam",
        "expected_risk": "HIGH_RISK",
    },
    {
        "id": "sbi_kyc_pan_english",
        "title": "🏦 SBI YONO PAN Card Block (English)",
        "channel": "SMS",
        "language": "English",
        "text": "Dear SBI User, your YONO NetBanking account has been temporarily blocked due to pending PAN card verification. To avoid permanent suspension and fine, update your PAN immediately by logging in at: http://sbi-kyc-verification.top/login",
        "category": "Banking Phishing / Credential Harvesting",
        "expected_risk": "CRITICAL",
    },
    {
        "id": "genuine_bank_sms",
        "title": "✅ Legitimate Bank Transaction Alert (English)",
        "channel": "SMS",
        "language": "English",
        "text": "Dear Customer, INR 450.00 debited from A/C **1234 on 26-Oct-26 at SWIGGY BANGALORE via UPI Ref 429910293847. Avail Bal: INR 18,240.50. If not done by you, SMS BLOCK UPI to 567676 or call 1800-11-2211 - State Bank of India.",
        "category": "Legitimate Bank Alert",
        "expected_risk": "SAFE",
    },
]

# Offline / Fallback detailed analyses for realistic demonstration when API key is not present or offline
CURATED_ANALYSES = {
    "bijli_apk_hindi": {
        "risk_level": "CRITICAL",
        "confidence_score": 98,
        "scam_category": "नकली बिजली बिल व दुर्भावनापूर्ण APK घोटाला (Utility Bill APK Scam)",
        "simple_explanation": "यह संदेश एक गंभीर साइबर धोखाधड़ी है। कोई भी वैध बिजली बोर्ड (Discom) कभी भी व्यक्तिगत मोबाइल नंबर या संदिग्ध bit.ly लिंक से APK ऐप डाउनलोड करने के लिए नहीं कहता। यदि आप इस लिंक पर क्लिक करके APK इंस्टॉल करेंगे, तो स्कैमर आपके फोन का पूरा एक्सेस ले लेंगे और आपके बैंक खाते से पैसे निकाल लेंगे।",
        "psychological_triggers": [
            "आपातकाल और डर (Urgency & Fear): 'आज रात 9:30 बजे बिजली काट दी जाएगी'",
            "आधिकारिक दबाव (Authority Trap): नकली बिजली अधिकारी का हवाला",
            "निजी नंबर का उपयोग (Suspicious Contact): व्यक्तिगत 10-अंकीय नंबर दिया गया है"
        ],
        "red_flags": [
            {
                "phrase": "आज रात 9:30 बजे काट दिया जाएगा",
                "explanation": "जल्दबाजी पैदा करके पीड़ित को सोचने या परिवार से सलाह लेने का मौका न देने की रणनीति।",
                "severity": "CRITICAL"
            },
            {
                "phrase": "apk डाउनलोड करें",
                "explanation": "बिजली विभाग कभी APK फ़ाइल नहीं भेजता। APK एक मैलवेयर/रिमोट एक्सेस ट्रोजन (RAT) है।",
                "severity": "CRITICAL"
            },
            {
                "phrase": "bit.ly/bijli-pay-bill",
                "explanation": "संदिग्ध शॉर्ट-URL जो असली गंतव्य को छिपाता है और अनधिकृत सर्वर पर ले जाता है।",
                "severity": "HIGH"
            },
            {
                "phrase": "हमारे बिजली अधिकारी 9876543210 पर संपर्क करें",
                "explanation": "आधिकारिक बिजली विभाग हमेशा 1912 या आधिकारिक टोल-फ्री हेल्पलाइन प्रदान करते हैं, निजी मोबाइल नंबर नहीं।",
                "severity": "HIGH"
            }
        ],
        "how_the_scam_works": "1. पीड़ित घबराकर दिए गए bit.ly लिंक पर क्लिक करता है।\n2. एक फर्जी ऐप (APK) डाउनलोड होती है जो SMS और स्क्रीन परमिशन मांगती है।\n3. स्कैमर पीड़ित से ₹10 या ₹20 का टेस्ट भुगतान करने को कहता है।\n4. पीड़ित जैसे ही UPI PIN डालता है, मैलवेयर उसका OTP और PIN चुरा लेता है और पूरा खाता खाली कर देता है।",
        "immediate_actions": [
            "दिए गए लिंक पर बिल्कुल क्लिक न करें और न ही कोई APK फाइल डाउनलोड करें।",
            "संदेश में दिए गए मोबाइल नंबर पर कभी कॉल न करें।",
            "अगर बिल का संदेह है, तो केवल आधिकारिक बिजली बिल ऐप (जैसे TPADL, BSES, UPPCL) या आधिकारिक वेबसाइट पर जाकर चेक करें।",
            "इस नंबर को तुरंत WhatsApp / SMS पर ब्लॉक और रिपोर्ट करें।",
            "यदि गलती से APK डाउनलोड हो गया है, तो तुरंत फोन को Airplane Mode में डालें और इंटरनेट बंद करें।"
        ],
        "helpline_info": "यदि पैसे कट गए हों, तो तुरंत राष्ट्रीय साइबर हेल्पलाइन 1930 पर कॉल करें या cybercrime.gov.in पर रिपोर्ट दर्ज करें।",
        "shareable_warning": "🚨 *बिजली बिल का नया फ्रॉड अलर्ट!* 🚨\nसावधान रहें! बिजली काटने (Power cut) के नाम पर फर्जी SMS आ रहे हैं जिसमें APK डाउनलोड करने को कहा जा रहा है। बिजली विभाग कभी APK या पर्सनल नंबर नहीं भेजता। किसी लिंक पर क्लिक न करें। यह चेतावनी अपने परिजनों के साथ साझा करें!"
    },
    "upi_cashback_hinglish": {
        "risk_level": "CRITICAL",
        "confidence_score": 99,
        "scam_category": "UPI PIN Trap / Fake Cashback Scam",
        "simple_explanation": "Yeh 100% fraud hai! Golden rule of UPI yaad rakhein: **PAISE RECIEVE KARNE KE LIYE KABHI BHI UPI PIN ENTER NAHI KARNA PADTA!** Agar aapne UPI PIN enter kiya, toh aapke account me paise aayenge nahi, balki aapke account se paise kat jayenge.",
        "psychological_triggers": [
            "Laalach (Greed / Free Money): 'Aapko ₹4,999 ka cashback reward mila hai'",
            "False Brand Trust: PhonePe ke naam ka galat istemal",
            "Technical Misdirection: 'Paisa lene ke liye PIN enter karein'"
        ],
        "red_flags": [
            {
                "phrase": "apna 6-digit UPI PIN enter karein",
                "explanation": "UPI PIN sirf paise BHEJNE ke liye hota hai. Receive karne ke liye PIN ki bilkul zaroorat nahi hoti.",
                "severity": "CRITICAL"
            },
            {
                "phrase": "phonepe-rewards-claim.in",
                "explanation": "PhonePe ka official domain phonepe.com hai. Yeh ek fake phishing website hai jo credentials churane ke liye banayi gayi hai.",
                "severity": "CRITICAL"
            },
            {
                "phrase": "Badhaai ho! Aapko ₹4,999 ka cashback reward mila",
                "explanation": "Unsolicited reward offer jo users ko bina soche link click karne ke liye attract karti hai.",
                "severity": "HIGH"
            }
        ],
        "how_the_scam_works": "1. Scammer ek fake collect request ya phishing web page banata hai jo PhonePe jaisa dikhta hai.\n2. User link pe click karke samajhta hai ki cashback claim ho raha hai.\n3. Screen par 'Pay' request hoti hai, aur user apna UPI PIN enter kar deta hai.\n4. Account se instant ₹4,999 cut hokar scammer ke mule account me chale jaate hain.",
        "immediate_actions": [
            "Link par click bilkul na karein.",
            "KISI KO BHI apna UPI PIN, OTP ya card CVV na batayein.",
            "Yaad rakhein: Paise receive karne ke liye sirf aapka mobile number ya QR code kaafi hai, PIN nahi.",
            "Number aur link ko Chakshu portal (sancharsaathi.gov.in) par report karein."
        ],
        "helpline_info": "Agar paise cut chuke hain, toh agle 1 ghante ke andar National Cyber Crime Helpline 1930 par call karein taaki payment freeze ki ja sake.",
        "shareable_warning": "⚠️ *UPI Fraud Warning!* ⚠️\nPhonePe/GPay par cashback claim karne ke naam par fake message aa rahe hain. Yaad rakhein: *PAISE LENE KE LIYE KABHI BHI UPI PIN NAHI LAGTA!* Kisi link par PIN na daalein. Apne doston aur family ko alert karein."
    },
    "digital_arrest_english": {
        "risk_level": "CRITICAL",
        "confidence_score": 99,
        "scam_category": "Digital Arrest / Extortion & Police Impersonation",
        "simple_explanation": "This is a dangerous and illegal extortion scam known as 'Digital Arrest'. Indian law enforcement, CBI, Customs, or Police NEVER conduct arrests or judicial verification over WhatsApp video calls or Skype, nor do they demand money to clear your name. These scammers use fake police backdrops, badges, and forged legal documents to terrorize victims.",
        "psychological_triggers": [
            "Extreme Fear & Intimidation: Allegations of drug trafficking (MDMA) and fake passports",
            "Urgency & Threat of Imprisonment: 'detained within 2 hours'",
            "Isolation / Secrecy: 'confidential verification', keeping the victim on video call so they cannot consult lawyers or family"
        ],
        "red_flags": [
            {
                "phrase": "Stay on this WhatsApp video call immediately",
                "explanation": "Police never interrogate suspects or conduct legal proceedings via WhatsApp video calls. Real police issue formal physical notices under Section 41A CrPC.",
                "severity": "CRITICAL"
            },
            {
                "phrase": "parcel sent under your Aadhaar card number containing ... narcotics",
                "explanation": "Classic digital arrest script. Scammers acquire leaked Aadhaar numbers and fabricate fake courier seizures (FedEx/DHL).",
                "severity": "CRITICAL"
            },
            {
                "phrase": "local unit will arrive at your address within 2 hours",
                "explanation": "Manufactured deadline to provoke sheer panic so the victim complies with extortion demands.",
                "severity": "CRITICAL"
            }
        ],
        "how_the_scam_works": "1. Scammers contact victim claiming their Aadhaar is linked to illegal contraband (drugs, passports, money laundering).\n2. They transfer the call to a fake 'Police Inspector' or 'CBI Officer' on video wearing a fake uniform in a fake station setup.\n3. They keep the victim isolated under 'Digital Arrest' for hours or days.\n4. They demand the victim transfer all savings into a 'Reserve Bank verification account' to clear funds, then disappear with the money.",
        "immediate_actions": [
            "IMMEDIATELY DISCONNECT the call. Do not engage, apologize, or argue.",
            "Do NOT transfer any money under any circumstances.",
            "Do NOT share bank account details, Aadhaar OTPs, or financial statements.",
            "Report immediately to 1930 and file a complaint at cybercrime.gov.in.",
            "Inform family members or visit your local police station in person for peace of mind."
        ],
        "helpline_info": "National Cyber Crime Helpline: 1930. The Prime Minister and Indian Home Ministry have issued public notices warning that 'Digital Arrest' has no legal basis in India.",
        "shareable_warning": "🚨 *CRITICAL ALERT: Fake Police / Digital Arrest Scam* 🚨\nNo police, CBI, or customs officer will ever call you on WhatsApp video or threaten 'Digital Arrest' over a FedEx parcel. If anyone calls pretending to be police and demands you stay on video call, HANG UP IMMEDIATELY and dial 1930. Please warn elders in your family!"
    },
    "telegram_job_hinglish": {
        "risk_level": "HIGH_RISK",
        "confidence_score": 96,
        "scam_category": "Part-Time Task & Crypto Investment Fraud",
        "simple_explanation": "Yeh ek well-known 'Task Scam' hai. Shuru me aapko YouTube video like karne ke ₹150-₹300 sach me de dete hain taaki aapka bharosa jeet sakein. Uske baad Telegram VIP group me 'Prepaid Task' ya 'Crypto Investment' ke naam par ₹10,000 se lekar ₹5,00,000 tak deposit karwa lete hain aur withdrawal block kar dete hain.",
        "psychological_triggers": [
            "Easy Money Illusion: 'Bas 5 videos like karke daily ₹3000-₹8000 kamayein'",
            "Sunk Cost & Commitment: Chhote rewards dekar bada trap lagana",
            "Exclusivity Trap: 'VIP Telegram channel'"
        ],
        "red_flags": [
            {
                "phrase": "daily ₹3000-₹8000 ... like 3 YouTube videos",
                "explanation": "Aisi koi legal job exist nahi karti jisme sirf video like karne par hazaron rupaye roz milein.",
                "severity": "CRITICAL"
            },
            {
                "phrase": "Join our VIP Telegram channel",
                "explanation": "Telegram channels anonymity provide karte hain, jahan scammers fake screenshots aur fake proof post karte hain.",
                "severity": "HIGH"
            },
            {
                "phrase": "HR Pooja ... Global Media",
                "explanation": "Fake HR identity without any official email (@company.com), company registration, or verifiable contract.",
                "severity": "HIGH"
            }
        ],
        "how_the_scam_works": "1. Phase 1 (Bait): Aap 3 video like karte hain, wo aapko ₹300 UPI se bhejte hain.\n2. Phase 2 (Hook): Aapko VIP Telegram group me add karte hain jahan sab fake members croron ka profit dikha rahe hote hain.\n3. Phase 3 (Trap): Bolte hain agle task ke liye ₹5,000 deposit karo, ₹7,000 milega. Shuru me virtual wallet me balance dikhata hai.\n4. Phase 4 (Extortion): Badi amount (₹50k+) deposit karwa lene ke baad withdraw karne ke liye 'tax fee' mangte hain aur block kar dete hain.",
        "immediate_actions": [
            "Kisi bhi Telegram channel ya group ko join na karein.",
            "Agar shuru ke ₹150-₹300 mile bhi hain, toh turant unka number block karein aur aage koi paisa na bhejein.",
            "Apni personal bank details ya UPI ID aise anjaan logon ko na dein.",
            "WhatsApp aur Telegram par is contact ko 'Spam/Fraud' report karein."
        ],
        "helpline_info": "National Cyber Crime Reporting Portal: cybercrime.gov.in ya Helpline 1930.",
        "shareable_warning": "⚠️ *Fake Work-From-Home Scam Alert!* ⚠️\nWhatsApp/Telegram par video like karne ya Google review likhne ke badle daily ₹3,000-₹8,000 kamane ke jhoothe offers aa rahe hain. Yeh pehle ₹200 dekar baad me laakhon rupaye thag lete hain. Kisi anjaan group me paise na lagayein!"
    },
    "sbi_kyc_pan_english": {
        "risk_level": "CRITICAL",
        "confidence_score": 97,
        "scam_category": "Banking Phishing & NetBanking Credential Theft",
        "simple_explanation": "This message is a malicious phishing attempt targeting State Bank of India customers. Banks NEVER send unverified links with domains like `.top`, `.xyz`, or shortened URLs to update PAN or KYC. The provided link leads to a clone website designed to steal your NetBanking username, password, and OTP.",
        "psychological_triggers": [
            "Fear of Financial Disruption: 'account temporarily blocked'",
            "Urgency: 'update PAN immediately to avoid permanent suspension and fine'",
            "Official Impersonation: Mimicking SBI YONO"
        ],
        "red_flags": [
            {
                "phrase": "http://sbi-kyc-verification.top/login",
                "explanation": "Fake domain (.top). SBI's only official portal is onlinesbi.sbi or onlinesbi.com. No bank uses unsecure HTTP or suspicious TLDs.",
                "severity": "CRITICAL"
            },
            {
                "phrase": "account has been temporarily blocked due to pending PAN",
                "explanation": "Banks never block your active NetBanking without official postal notices or registered email alerts.",
                "severity": "HIGH"
            },
            {
                "phrase": "avoid permanent suspension and fine",
                "explanation": "Fabricated consequence designed to make users panic and bypass basic caution.",
                "severity": "HIGH"
            }
        ],
        "how_the_scam_works": "1. User clicks the fraudulent `.top` link.\n2. A replica of the SBI YONO login screen appears asking for Username, Password, and Mobile Number.\n3. Once submitted, the fake site requests the OTP received on the victim's phone.\n4. The scammers enter the OTP into the genuine bank portal in real-time, transferring out your entire account balance.",
        "immediate_actions": [
            "DO NOT click the link.",
            "If already clicked, DO NOT enter username, password, MPIN, or OTP.",
            "If you entered your password, immediately login to the official SBI portal (onlinesbi.sbi) and change your password, or call 1800-11-2211 to lock NetBanking access.",
            "Forward the SMS to 1909 (TRAI DND) or report it on the Chakshu portal."
        ],
        "helpline_info": "SBI Customer Care: 1800 1234 / 1800 2100. National Cyber Helpline: 1930.",
        "shareable_warning": "⚠️ *Bank KYC Phishing Alert!* ⚠️\nFraud SMS are circulating claiming SBI/YONO accounts are blocked for PAN update. Do NOT click on any link ending in .top, .xyz or shortened URLs. Banks never ask for KYC updates via SMS links. Forward this to protect your family!"
    },
    "genuine_bank_sms": {
        "risk_level": "SAFE",
        "confidence_score": 95,
        "scam_category": "Legitimate Bank Debit Alert",
        "simple_explanation": "This is a legitimate transactional SMS from State Bank of India confirming an authentic debit of INR 450.00 at Swiggy Bangalore. It contains standard masking (A/C **1234), official reference number, available balance, and legitimate official bank helpline numbers (1800-11-2211). It does NOT ask for OTP, PIN, password, or to click any unverified link.",
        "psychological_triggers": [
            "No manipulative urgency or threats detected.",
            "Provides legitimate dispute instructions if unauthorized."
        ],
        "red_flags": [],
        "how_the_scam_works": "Not a scam. This is a standard regulatory-compliant debit notification mandated by RBI for transaction awareness.",
        "immediate_actions": [
            "If you made this purchase at Swiggy, no action is needed.",
            "If you did NOT make this purchase, call the official number 1800-11-2211 or SMS 'BLOCK UPI' to 567676 immediately to freeze unauthorized transactions.",
            "Never share the OTP with anyone calling claiming to be from Swiggy or the bank."
        ],
        "helpline_info": "State Bank of India Toll-Free: 1800 11 2211 / 1800 425 3800.",
        "shareable_warning": "ℹ️ *Safety Tip:* Genuine bank SMS will show your masked account number (e.g., **1234) and will NEVER ask you to click a link or reply with your UPI PIN to cancel a transaction."
    }
}

# Interactive Simulation Scenarios for the "Scam Dojo" practice arena
SIMULATION_SCENARIOS = [
    {
        "id": "sim_1",
        "title": "Scenario 1: The Urgent Courier Customs Call",
        "channel": "WhatsApp Audio Call",
        "sender": "+92 301 9821456 (Profile: 'CBI Cyber Cell Inspector')",
        "message": "Sir, your Aadhaar is linked to a parcel detained at Mumbai Airport with 16 credit cards and narcotics. Supreme Court has issued immediate non-bailable arrest. Pay ₹35,000 security bond on this UPI ID to get instant clearance certificate.",
        "question": "What is the safest and correct response?",
        "options": [
            {
                "text": "Send the ₹35,000 immediately to avoid arrest, then complain later.",
                "is_correct": False,
                "feedback": "❌ DANGEROUS! Indian courts and police NEVER issue bail or clearances over WhatsApp, nor do they accept UPI security bonds. You will lose your money instantly!"
            },
            {
                "text": "Ask them to send a photo of their police ID card and Supreme Court order on WhatsApp to verify.",
                "is_correct": False,
                "feedback": "⚠️ RISKY! Scammers have fake police IDs, forged seals, and fabricated arrest warrants ready to deceive you. Continuing the conversation gives them psychological leverage."
            },
            {
                "text": "Immediately disconnect, do not pay a single rupee, block the number, and report to 1930 / cybercrime.gov.in.",
                "is_correct": True,
                "feedback": "✅ PERFECT! Real law enforcement never demands money via UPI or conducts interrogations on WhatsApp. Disconnecting immediately terminates their manipulation tactic."
            }
        ],
        "tactics_explained": "Digital Arrest & Extortion: Uses terror (arrest warrant, narcotics) combined with a foreign/spoofed number (+92) to induce panic."
    },
    {
        "id": "sim_2",
        "title": "Scenario 2: The UPI 'Accidental Transfer' Refund",
        "channel": "Phone Call & SMS",
        "sender": "Unknown Caller (+91 97112 00192)",
        "message": "Bhaiya galti se maine aapke Google Pay number par ₹25,000 bhej diye hain! Please mere bache ki hospital fees hai, wapas bhej dijiye. Maine aapko PhonePe pe 'Pay' request bheji hai, bas accept karke PIN daal dijiye.",
        "question": "The caller sounds desperate and crying. What should you do?",
        "options": [
            {
                "text": "Open PhonePe, click the 'Pay' request, and enter your UPI PIN to return the money.",
                "is_correct": False,
                "feedback": "❌ DISASTROUS TRAP! Entering your UPI PIN will DEDUCT ₹25,000 from YOUR bank account. You never enter a PIN to receive or refund money!"
            },
            {
                "text": "First open your bank statement / app independently to verify if ₹25,000 actually got credited. If yes, tell them to contact their bank for official reversal.",
                "is_correct": True,
                "feedback": "✅ BRILLIANT CYBER DEFENSE! Scammers send fake SMS alerts of money credited. Always verify through your actual banking app. Never use a 'Pay' request to return money."
            },
            {
                "text": "Transfer half the amount (₹12,500) as a humanitarian gesture while you verify.",
                "is_correct": False,
                "feedback": "❌ WRONG! Emotional manipulation (crying child, hospital fee) is a classic social engineering trick. You will lose ₹12,500 of your own money."
            }
        ],
        "tactics_explained": "Emotional Manipulation & UPI Reverse Pay Trap: Leverages empathy and confusion between 'Send' and 'Receive' on UPI."
    },
    {
        "id": "sim_3",
        "title": "Scenario 3: The Electricity Disconnection APK",
        "channel": "SMS",
        "sender": "VM-BIJLI (Sender ID)",
        "message": "Dear Consumer, your electricity power will be disconnected tonight at 10 PM by head office due to pending update. Call electricity officer at 9311029482 or pay ₹15 update charge on update-bijlibill.apk.",
        "question": "What is the biggest red flag in this message?",
        "options": [
            {
                "text": "The 10 PM deadline is inconvenient for the electricity office.",
                "is_correct": False,
                "feedback": "While true, the critical danger is requesting APK installation and contacting a private personal mobile number."
            },
            {
                "text": "Downloading an unknown .APK file and calling an unverified 10-digit mobile number.",
                "is_correct": True,
                "feedback": "✅ SPOT ON! Electricity boards never distribute APK files or use personal mobile numbers for billing. An APK can take complete remote control of your phone and intercept OTPs."
            },
            {
                "text": "The ₹15 update fee is too cheap.",
                "is_correct": False,
                "feedback": "Scammers purposely use small amounts like ₹10-₹15 so victims don't hesitate, but entering UPI PIN on the fake APK empties the entire account!"
            }
        ],
        "tactics_explained": "Remote Access Trojan (RAT) via APK: Uses fear of darkness/power cut to push a malicious app that steals banking OTPs."
    },
    {
        "id": "sim_4",
        "title": "Scenario 4: Work-From-Home YouTube Like Job",
        "channel": "Telegram",
        "sender": "@Global_Media_Task_Manager",
        "message": "Congratulations! You completed Task 1 and 2. We transferred ₹300 to your UPI. Now to unlock VIP Task 3 with 500% returns, deposit ₹5,000 into our commercial merchant escrow wallet.",
        "question": "They already paid you ₹300 real money. Should you trust them with ₹5,000?",
        "options": [
            {
                "text": "Yes, because they proved they are legitimate by paying ₹300 directly into my bank account.",
                "is_correct": False,
                "feedback": "❌ FATAL MISTAKE! The initial ₹300 is 'chum' (bait). Scammers happily sacrifice ₹300 to steal ₹5,000 to ₹5,00,000 in subsequent prepaid tasks."
            },
            {
                "text": "Deposit ₹2,500 and ask for a 50% discount on the escrow fee.",
                "is_correct": False,
                "feedback": "❌ NO! Any money deposited in these Telegram task scams is instantly laundered through crypto and cannot be recovered."
            },
            {
                "text": "No! This is the classic 'Task Scam Bait'. Keep the ₹300, leave the Telegram group immediately, and block them.",
                "is_correct": True,
                "feedback": "✅ SMART MOVE! You recognized the hook-and-switch. Legitimate employers never ask employees to pay money to unlock salary tasks."
            }
        ],
        "tactics_explained": "Advance-Fee & Sunk Cost Scam: Small initial payouts build false credibility before demanding exponential deposits."
    }
]

# Government & Banking Official Helplines in India
OFFICIAL_HELPLINES = [
    {
        "name": "National Cyber Crime Helpline",
        "number": "1930",
        "description": "24x7 toll-free helpline by Ministry of Home Affairs to freeze financial fraud within the golden hour.",
        "url": "https://cybercrime.gov.in",
        "badge": "Govt of India"
    },
    {
        "name": "Sanchar Saathi (Chakshu)",
        "number": "Online Portal",
        "description": "Report fraudulent SMS, calls, and WhatsApp numbers to Department of Telecommunications for disconnection.",
        "url": "https://sancharsaathi.gov.in",
        "badge": "DoT"
    },
    {
        "name": "State Bank of India (SBI)",
        "number": "1800 1234 / 1800 2100",
        "description": "Immediate card & NetBanking hotlisting / fraud dispute reporting.",
        "url": "https://onlinesbi.sbi",
        "badge": "Bank Helpline"
    },
    {
        "name": "HDFC Bank Cyber Cell",
        "number": "1800 1600 / 1800 2600",
        "description": "24x7 emergency helpline for unauthorized banking transactions.",
        "url": "https://hdfcbank.com",
        "badge": "Bank Helpline"
    },
    {
        "name": "RBI Sachet Portal",
        "number": "sachet.rbi.org.in",
        "description": "Reserve Bank of India portal to register complaints against unregistered entities offering illegal deposit/loan schemes.",
        "url": "https://sachet.rbi.org.in",
        "badge": "RBI"
    }
]
