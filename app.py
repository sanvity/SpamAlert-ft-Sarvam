"""
TrapAlert - Voice Scam Detection & Awareness Coach
Workflow: Record audio → Sarvam transcript → English translation → Scam report
Tagline: "Pause. Verify. Stay safe."
Includes persistent analysis history & older logs preservation.
"""

import os
import json
from datetime import datetime
import streamlit as st
import sarvam_client
from scam_data import (
    SAMPLE_RECORDINGS,
    SIMULATION_SCENARIOS,
    OFFICIAL_HELPLINES,
)

HISTORY_FILE = "analysis_history.json"


def load_history_from_file():
    """Load saved analysis logs from persistent JSON file."""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_history_to_file(logs):
    """Save analysis logs to persistent JSON file."""
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def add_log_entry(transcript, translation, report, language):
    """Add a new analysis log entry if not already present."""
    if not transcript or not report:
        return
    # Check if identical entry already exists at the top
    if st.session_state.history_logs:
        last = st.session_state.history_logs[0]
        if (
            last.get("transcript", "").strip() == transcript.strip()
            and last.get("report", {}).get("risk_level") == report.get("risk_level")
        ):
            return

    new_entry = {
        "id": f"log_{int(datetime.now().timestamp())}",
        "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p"),
        "language": language or "Detected Language",
        "transcript": transcript,
        "translation": translation or "",
        "report": report,
    }
    st.session_state.history_logs.insert(0, new_entry)
    save_history_to_file(st.session_state.history_logs)


# -----------------------------------------------------------------------------
# Streamlit Configuration & Clean Minimal Typography
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="TrapAlert — Pause. Verify. Stay safe.",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    }

    /* Minimal Clean Header */
    .app-brand {
        font-size: 2.1rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 2px;
        color: #f8fafc;
    }
    .app-tagline {
        font-size: 1.05rem;
        color: #94a3b8;
        margin-bottom: 24px;
        font-weight: 500;
    }

    /* Risk Level Badges */
    .badge-high {
        display: inline-block;
        background: rgba(239, 68, 68, 0.15);
        color: #ef4444;
        border: 1px solid rgba(239, 68, 68, 0.35);
        padding: 4px 12px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 0.95rem;
    }
    .badge-medium {
        display: inline-block;
        background: rgba(245, 158, 11, 0.15);
        color: #f59e0b;
        border: 1px solid rgba(245, 158, 11, 0.35);
        padding: 4px 12px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 0.95rem;
    }
    .badge-low {
        display: inline-block;
        background: rgba(34, 197, 94, 0.15);
        color: #22c55e;
        border: 1px solid rgba(34, 197, 94, 0.35);
        padding: 4px 12px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 0.95rem;
    }

    /* Evidence item card */
    .evidence-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 10px;
        padding: 12px 16px;
        margin-bottom: 10px;
    }
    .evidence-quote {
        font-family: 'JetBrains Mono', monospace;
        color: #fca5a5;
        background: rgba(239, 68, 68, 0.12);
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.95rem;
        font-weight: 600;
    }

    /* Uncertainty disclaimer */
    .uncertainty-box {
        background: rgba(148, 163, 184, 0.08);
        border: 1px dashed rgba(148, 163, 184, 0.3);
        border-radius: 8px;
        padding: 10px 14px;
        color: #94a3b8;
        font-size: 0.85rem;
        margin-top: 12px;
    }

    /* History Log Card */
    .log-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 10px;
        padding: 14px 18px;
        margin-bottom: 14px;
    }

    /* Simulation card */
    .sim-card {
        background: #1e293b;
        border-left: 4px solid #6366f1;
        border-radius: 0 10px 10px 0;
        padding: 16px 20px;
        margin-bottom: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# Session State Initialization
# -----------------------------------------------------------------------------
if "audio_key_counter" not in st.session_state:
    st.session_state.audio_key_counter = 0
if "active_audio_bytes" not in st.session_state:
    st.session_state.active_audio_bytes = None
if "current_transcript" not in st.session_state:
    st.session_state.current_transcript = ""
if "recognized_language" not in st.session_state:
    st.session_state.recognized_language = ""
if "english_translation" not in st.session_state:
    st.session_state.english_translation = None
if "scam_report" not in st.session_state:
    st.session_state.scam_report = None
if "last_analyzed_transcript" not in st.session_state:
    st.session_state.last_analyzed_transcript = ""
if "active_sample_id" not in st.session_state:
    st.session_state.active_sample_id = None
if "pipeline_error" not in st.session_state:
    st.session_state.pipeline_error = None
if "history_logs" not in st.session_state:
    st.session_state.history_logs = load_history_from_file()

# Scam Lab State
if "lab_round" not in st.session_state:
    st.session_state.lab_round = 0
if "lab_score" not in st.session_state:
    st.session_state.lab_score = 0
if "lab_selected_option" not in st.session_state:
    st.session_state.lab_selected_option = None

def reset_for_new_log():
    """Resets the active evaluation workspace while keeping all historical logs preserved."""
    st.session_state.audio_key_counter = st.session_state.get("audio_key_counter", 0) + 1
    st.session_state.active_audio_bytes = None
    st.session_state.current_transcript = ""
    st.session_state.recognized_language = ""
    st.session_state.english_translation = None
    st.session_state.scam_report = None
    st.session_state.last_analyzed_transcript = ""
    st.session_state.active_sample_id = None
    st.session_state.pipeline_error = None
    if "transcript_editor_input" in st.session_state:
        st.session_state["transcript_editor_input"] = ""
    if "pasted_text_input" in st.session_state:
        st.session_state["pasted_text_input"] = ""
    st.toast("✨ Started a new log. Ready for a new voice or text message!")

# Sidebar: Sarvam API Key & Actions
with st.sidebar:
    st.subheader("Workspace")
    if st.button("➕ Start a New Log", key="btn_sidebar_start_new_log", use_container_width=True, help="Clear active screen to analyze a new message while keeping older logs saved."):
        reset_for_new_log()
        st.rerun()

    st.markdown("---")
    st.subheader("Settings")
    env_key = sarvam_client.get_configured_api_key()
    user_key = st.text_input(
        "Sarvam Subscription Key",
        value=env_key if env_key else "",
        type="password",
        help="Reads from SARVAM_API_KEY in .env or enter here.",
    )
    active_key = user_key.strip() if user_key else None

    st.markdown("---")
    st.markdown("##### Emergency Helpline (India)")
    st.markdown("**📞 1930** — National Cyber Crime Helpline")
    st.markdown("[cybercrime.gov.in](https://cybercrime.gov.in)")

# -----------------------------------------------------------------------------
# Minimal Header & Prominent Quick Action
# -----------------------------------------------------------------------------
header_col1, header_col2 = st.columns([3, 1])
with header_col1:
    st.markdown('<div class="app-brand">🛡️ TrapAlert</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-tagline">Pause. Verify. Stay safe.</div>', unsafe_allow_html=True)
with header_col2:
    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
    if st.button("➕ Start a New Log", key="btn_header_start_new_log", type="primary", use_container_width=True, help="Clear active screen to analyze a new message while keeping older logs saved."):
        reset_for_new_log()
        st.rerun()

# -----------------------------------------------------------------------------
# Primary Navigation (Voice Analyzer, Saved Logs, Scam Lab)
# -----------------------------------------------------------------------------
tab_voice, tab_history, tab_lab = st.tabs([
    "🎙️ Voice Scam Analyzer",
    f"📜 Saved Logs ({len(st.session_state.history_logs)})",
    "🧪 Scam Lab",
])

# =============================================================================
# TAB 1: PRIMARY WORKFLOW (Record audio → Transcript → Translation → Scam Report)
# =============================================================================
with tab_voice:
    # Primary Action: Microphone Input & Start New Log
    h_c1, h_c2 = st.columns([3, 1])
    with h_c1:
        st.markdown("##### Record Audio")
    with h_c2:
        if st.button("➕ Start a New Log", key="btn_start_new_log_top", use_container_width=True, help="Clear active screen to analyze a new message while keeping older logs saved."):
            reset_for_new_log()
            st.rerun()

    mic_audio = st.audio_input(
        "Record suspicious call or voice note:",
        key=f"mic_audio_input_{st.session_state.audio_key_counter}"
    )

    # Secondary Action: Pre-recorded Samples & Paste Text
    with st.expander("Or select a test recording / paste text", expanded=False):
        st.markdown("**Test Recordings (Hindi, Hinglish, Benign):**")
        sample_cols = st.columns(len(SAMPLE_RECORDINGS))
        for idx, sample in enumerate(SAMPLE_RECORDINGS):
            with sample_cols[idx]:
                if st.button(sample["title"], key=f"btn_sample_{sample['id']}", use_container_width=True):
                    if os.path.exists(sample["file_path"]):
                        with open(sample["file_path"], "rb") as f:
                            st.session_state.active_audio_bytes = f.read()
                    st.session_state.current_transcript = sample["raw_transcript"]
                    st.session_state["transcript_editor_input"] = sample["raw_transcript"]
                    st.session_state.recognized_language = sample["language_name"]
                    st.session_state.english_translation = sample["translation"]
                    st.session_state.scam_report = sample.get("report")
                    st.session_state.last_analyzed_transcript = sample["raw_transcript"]
                    st.session_state.active_sample_id = sample["id"]
                    st.session_state.pipeline_error = None
                    add_log_entry(sample["raw_transcript"], sample["translation"], sample.get("report"), sample["language_name"])
                    st.rerun()

        st.markdown("---")
        pasted_text = st.text_area(
            "Or paste text (SMS / WhatsApp):",
            placeholder="e.g. Dear customer, electricity bill pending. Download APK bit.ly/bijli-pay",
            height=80,
            key="pasted_text_input",
        )
        if st.button("Process Pasted Text", key="btn_process_text"):
            if pasted_text.strip():
                st.session_state.active_audio_bytes = None
                st.session_state.current_transcript = pasted_text.strip()
                st.session_state["transcript_editor_input"] = pasted_text.strip()
                st.session_state.recognized_language = "Text Input"
                st.session_state.english_translation = None
                st.session_state.scam_report = None
                st.session_state.last_analyzed_transcript = ""
                st.session_state.active_sample_id = None
                st.session_state.pipeline_error = None
                st.rerun()

    # Detect new microphone audio
    if mic_audio is not None:
        audio_data = mic_audio.read()
        if st.session_state.active_audio_bytes != audio_data:
            st.session_state.active_audio_bytes = audio_data
            st.session_state.current_transcript = ""
            st.session_state["transcript_editor_input"] = ""
            st.session_state.english_translation = None
            st.session_state.scam_report = None
            st.session_state.last_analyzed_transcript = ""
            st.session_state.pipeline_error = None

            # Execute Stage 1: Transcription
            with st.spinner("Transcribing speech with Sarvam Saaras AI..."):
                transcript, lang, err, is_live = sarvam_client.transcribe_audio(
                    audio_bytes=audio_data,
                    api_key=active_key,
                )
                if transcript:
                    st.session_state.current_transcript = transcript
                    st.session_state["transcript_editor_input"] = transcript
                    st.session_state.recognized_language = lang or "Detected Language"
                    st.session_state.pipeline_error = None
                else:
                    st.session_state.pipeline_error = f"Transcription Error: {err or 'Empty audio response'}"

    # Pipeline Execution: Stage 2 (Translation) and Stage 3 (Scam Report)
    if st.session_state.current_transcript and not st.session_state.english_translation and not st.session_state.pipeline_error:
        # Run Stage 2: English Translation
        with st.spinner("Translating to English with Sarvam AI..."):
            tr_eng, src_lang, err_tr, _ = sarvam_client.translate_to_english(
                text=st.session_state.current_transcript,
                source_language_code="auto",
                api_key=active_key,
            )
            if tr_eng:
                st.session_state.english_translation = tr_eng
                st.session_state.pipeline_error = None
            else:
                matched = next((s for s in SAMPLE_RECORDINGS if s["raw_transcript"] == st.session_state.current_transcript), None)
                if matched:
                    st.session_state.english_translation = matched["translation"]
                    st.session_state.pipeline_error = None
                else:
                    st.session_state.pipeline_error = f"Translation Error: {err_tr or 'Could not translate transcript'}"

        # Run Stage 3: Scam Report
        if st.session_state.english_translation and not st.session_state.scam_report:
            with st.spinner("Generating Scam Alert report..."):
                report, err_rep, _ = sarvam_client.generate_scam_report(
                    transcript=st.session_state.current_transcript,
                    translation=st.session_state.english_translation,
                    api_key=active_key,
                )
                if report:
                    st.session_state.scam_report = report
                    st.session_state.last_analyzed_transcript = st.session_state.current_transcript
                    add_log_entry(
                        transcript=st.session_state.current_transcript,
                        translation=st.session_state.english_translation,
                        report=report,
                        language=st.session_state.recognized_language,
                    )
                else:
                    matched = next((s for s in SAMPLE_RECORDINGS if s["raw_transcript"] == st.session_state.current_transcript), None)
                    if matched and matched.get("report"):
                        st.session_state.scam_report = matched["report"]
                        st.session_state.last_analyzed_transcript = st.session_state.current_transcript
                        add_log_entry(
                            transcript=st.session_state.current_transcript,
                            translation=st.session_state.english_translation,
                            report=matched["report"],
                            language=st.session_state.recognized_language,
                        )
                    else:
                        st.session_state.pipeline_error = f"Scam Analysis Error: {err_rep or 'Could not complete analysis'}"

    # Display Pipeline Error if any stage failed
    if st.session_state.pipeline_error:
        st.error(st.session_state.pipeline_error)
        if st.button("Retry Processing", key="btn_retry_pipeline"):
            st.session_state.pipeline_error = None
            st.rerun()

    # -------------------------------------------------------------------------
    # VERTICAL STAGES IN EXACT ORDER:
    # 1. Transcript → 2. English Translation → 3. Scam Alert
    # -------------------------------------------------------------------------
    if st.session_state.current_transcript:
        st.markdown("---")

        # ---------------------------------------------------------------------
        # SECTION 1: CAPTURED AUDIO TRANSCRIPT
        # ---------------------------------------------------------------------
        st.subheader("Transcript")

        if st.session_state.active_audio_bytes:
            st.audio(st.session_state.active_audio_bytes, format="audio/wav")

        if st.session_state.recognized_language:
            st.caption(f"Recognized Language: **{st.session_state.recognized_language}**")

        edited_transcript = st.text_area(
            "Original Transcript (edit if speech recognition made mistakes):",
            value=st.session_state.current_transcript,
            height=90,
            key="transcript_editor_input",
            help="Editing the transcript will invalidate the previous translation and report, and re-run analysis.",
        )

        # Detect modifications and invalidate previous stages
        if edited_transcript != st.session_state.current_transcript:
            st.session_state.current_transcript = edited_transcript
            st.session_state.english_translation = None
            st.session_state.scam_report = None
            st.session_state.pipeline_error = None
            st.rerun()

        is_stale = (
            st.session_state.last_analyzed_transcript
            and st.session_state.current_transcript != st.session_state.last_analyzed_transcript
        )
        if is_stale:
            st.warning("Transcript has been modified. Please re-analyze to update the English translation and Scam Alert.")
            if st.button("🔄 Re-analyze Edited Transcript", type="primary", key="btn_reanalyze_edited"):
                st.session_state.english_translation = None
                st.session_state.scam_report = None
                st.session_state.last_analyzed_transcript = ""
                st.rerun()

        # ---------------------------------------------------------------------
        # SECTION 2: ENGLISH TRANSLATION
        # ---------------------------------------------------------------------
        if st.session_state.english_translation and not is_stale:
            st.markdown("---")
            st.subheader("English Translation")
            st.info(st.session_state.english_translation)

        # ---------------------------------------------------------------------
        # SECTION 3: SCAM REPORT
        # ---------------------------------------------------------------------
        if st.session_state.scam_report and not is_stale:
            st.markdown("---")
            st.subheader("Scam Alert")

            rep = st.session_state.scam_report
            risk_level = str(rep.get("risk_level", "Medium")).strip().capitalize()
            if risk_level not in ["High", "Medium", "Low"]:
                risk_level = "Medium"

            badge_class = "badge-high" if risk_level == "High" else ("badge-medium" if risk_level == "Medium" else "badge-low")

            # Risk Level
            st.markdown(
                f"""
                <div style="margin-bottom: 14px;">
                    <span style="font-size: 0.95rem; font-weight: 600; color: #94a3b8; margin-right: 8px;">Risk Level:</span>
                    <span class="{badge_class}">{risk_level}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Why it was flagged
            st.markdown(f"**Why it was flagged:** {rep.get('why_flagged', 'Potential deception indicators detected.')}")

            # Suspicious evidence
            evidence_items = rep.get("suspicious_evidence", [])
            if evidence_items:
                st.markdown("**Suspicious evidence:**")
                for ev in evidence_items:
                    phrase = ev.get("phrase", "")
                    expl = ev.get("explanation", "")
                    st.markdown(
                        f"""
                        <div class="evidence-box">
                            <span class="evidence-quote">"{phrase}"</span>
                            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 6px;">{expl}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

            # Recommended action
            actions = rep.get("recommended_action", [])
            if actions:
                st.markdown("**Recommended action:**")
                for act in actions:
                    st.markdown(f"- {act}")

            # Uncertainty disclaimer
            if risk_level == "Low":
                unc_note = rep.get("uncertainty_note", "Note: A Low risk rating is not a guarantee that a message is safe. Always verify transactions through official banking channels.")
                st.markdown(
                    f"""
                    <div class="uncertainty-box">
                        ⚠️ {unc_note}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            st.markdown("---")
            b_c1, b_c2 = st.columns([2, 1])
            with b_c1:
                st.caption("✓ Result automatically archived to Saved Logs")
            with b_c2:
                if st.button("➕ Start a New Log", key="btn_start_new_log_bottom", type="primary", use_container_width=True):
                    reset_for_new_log()
                    st.rerun()

# =============================================================================
# TAB 2: SAVED ANALYSIS LOGS (History Preservation)
# =============================================================================
with tab_history:
    st.subheader("Saved Analysis Logs")
    st.caption("Archive of older voice and text evaluations with complete transcripts, translations, and scam reports.")

    if not st.session_state.history_logs:
        st.info("No saved logs yet. Process an audio recording or text to see its results archived here.")
        if st.button("➕ Start a New Log", key="btn_new_log_empty_history", type="primary"):
            reset_for_new_log()
            st.rerun()
    else:
        h_col1, h_col2, h_col3 = st.columns([1, 1, 1])
        with h_col1:
            if st.button("➕ Start a New Log", key="btn_new_log_from_history", type="primary", use_container_width=True):
                reset_for_new_log()
                st.rerun()
        with h_col2:
            st.download_button(
                "📥 Export All Logs (JSON)",
                data=json.dumps(st.session_state.history_logs, ensure_ascii=False, indent=2),
                file_name="trapalert_analysis_logs.json",
                mime="application/json",
                use_container_width=True,
            )
        with h_col3:
            if st.button("🗑️ Clear History", use_container_width=True):
                st.session_state.history_logs = []
                save_history_to_file([])
                st.rerun()

        st.markdown("---")

        for idx, entry in enumerate(st.session_state.history_logs):
            e_rep = entry.get("report", {})
            e_risk = str(e_rep.get("risk_level", "Medium")).strip().capitalize()
            risk_icon = "🔴" if e_risk == "High" else ("🟠" if e_risk == "Medium" else "🟢")
            tr_snippet = entry.get("transcript", "")[:50]

            expander_title = f"{risk_icon} [{e_risk}] • {entry.get('timestamp', '')} • {entry.get('language', '')} • \"{tr_snippet}...\""

            with st.expander(expander_title, expanded=(idx == 0)):
                st.markdown("##### 1. Transcript")
                st.write(entry.get("transcript", ""))

                if entry.get("translation"):
                    st.markdown("##### 2. English Translation")
                    st.info(entry.get("translation", ""))

                st.markdown("##### 3. Scam Alert Report")
                b_class = "badge-high" if e_risk == "High" else ("badge-medium" if e_risk == "Medium" else "badge-low")
                st.markdown(f'<span class="{b_class}">Risk Level: {e_risk}</span>', unsafe_allow_html=True)
                st.markdown(f"**Why Flagged:** {e_rep.get('why_flagged', 'N/A')}")

                evs = e_rep.get("suspicious_evidence", [])
                if evs:
                    st.markdown("**Evidence:**")
                    for item in evs:
                        st.markdown(f"- **\"{item.get('phrase', '')}\"**: {item.get('explanation', '')}")

                acts = e_rep.get("recommended_action", [])
                if acts:
                    st.markdown("**Recommended Actions:**")
                    for a in acts:
                        st.markdown(f"- {a}")

                if st.button("📥 Load into Active Analyzer", key=f"btn_load_log_{idx}"):
                    st.session_state.current_transcript = entry.get("transcript", "")
                    st.session_state["transcript_editor_input"] = entry.get("transcript", "")
                    st.session_state.recognized_language = entry.get("language", "")
                    st.session_state.english_translation = entry.get("translation", "")
                    st.session_state.scam_report = entry.get("report", {})
                    st.session_state.last_analyzed_transcript = entry.get("transcript", "")
                    st.session_state.pipeline_error = None
                    st.success("Loaded log into Active Analyzer! Check the 'Voice Scam Analyzer' tab.")
                    st.rerun()

# =============================================================================
# TAB 3: SCAM LAB (Simulation & Education)
# =============================================================================
with tab_lab:
    st.subheader("Scam Lab: Interactive Reflex Arena")
    st.caption("Practice recognizing manipulation tactics on simulated Indian fraud scenarios.")

    total_scens = len(SIMULATION_SCENARIOS)
    curr_round = st.session_state.lab_round
    score = st.session_state.lab_score

    col_s1, col_s2 = st.columns([1, 1])
    with col_s1:
        st.metric("Scenario", f"{curr_round + 1} of {total_scens}")
    with col_s2:
        st.metric("Reflex Score", f"{score} pts")

    st.progress(curr_round / total_scens)

    if curr_round < total_scens:
        scen = SIMULATION_SCENARIOS[curr_round]

        st.markdown(
            f"""
            <div class="sim-card">
                <div style="font-size: 0.8rem; font-weight: 700; color: #94a3b8; text-transform: uppercase;">
                    📱 {scen['channel']} • {scen['sender']}
                </div>
                <div style="margin-top: 6px; font-size: 1.05rem; font-weight: 600; color: #f8fafc;">
                    "{scen['message']}"
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(f"**Question:** {scen['question']}")

        for idx, opt in enumerate(scen["options"]):
            if st.button(opt["text"], key=f"lab_opt_{curr_round}_{idx}", use_container_width=True):
                st.session_state.lab_selected_option = opt
                if opt["is_correct"]:
                    st.session_state.lab_score += 10
                st.rerun()

        if st.session_state.lab_selected_option:
            sel = st.session_state.lab_selected_option
            st.markdown("---")
            if sel["is_correct"]:
                st.success(sel["feedback"])
            else:
                st.error(sel["feedback"])

            st.info(f"**Tactics Explained:** {scen['tactics_explained']}")

            if st.button("Next Scenario ➡️", type="primary", key="btn_next_lab_scen"):
                st.session_state.lab_round += 1
                st.session_state.lab_selected_option = None
                st.rerun()
    else:
        st.balloons()
        st.success(f"Simulation completed! Final Score: {score} / {total_scens * 10} points.")
        if st.button("Restart Scam Lab", type="primary"):
            st.session_state.lab_round = 0
            st.session_state.lab_score = 0
            st.session_state.lab_selected_option = None
            st.rerun()

# -----------------------------------------------------------------------------
# Clean Footer
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #64748b; font-size: 0.8rem; padding: 10px 0;">
        <strong>TrapAlert</strong> • Pause. Verify. Stay safe. • National Cyber Helpline: <strong>1930</strong>
    </div>
    """,
    unsafe_allow_html=True,
)
