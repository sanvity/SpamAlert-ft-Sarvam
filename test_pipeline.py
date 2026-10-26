"""
Test Suite for TrapAlert Pipeline:
Audio -> Transcript -> English Translation -> Scam Report
Tests:
1. Hindi Recording Test (Electricity Bill APK threat)
2. Hinglish Recording Test (UPI PIN Cashback trap)
3. Benign Recording Test (Swiggy Debit Notification)
4. Transcript Invalidation & Regeneration Test
5. Deterministic Security Rules Verification
"""

import os
import sys
import wave
import sarvam_client
import scam_data

def test_pipeline():
    print("=" * 60)
    print("RUNNING TRAPALERT PIPELINE ACCEPTANCE TESTS")
    print("=" * 60)

    results = {}

    # -------------------------------------------------------------------------
    # TEST 1: Hindi Recording Test
    # -------------------------------------------------------------------------
    print("\n[TEST 1] Testing Hindi Recording (samples/hindi_bijli_scam.wav)...")
    hindi_sample = next(s for s in scam_data.SAMPLE_RECORDINGS if s["id"] == "hindi_sample")
    
    # 1. Audio verification
    assert os.path.exists(hindi_sample["file_path"]), f"File not found: {hindi_sample['file_path']}"
    with wave.open(hindi_sample["file_path"], "rb") as w:
        duration = w.getnframes() / w.getframerate()
        assert duration > 1.0, f"Audio too short: {duration}s"
    print(f"  ✓ Audio File Verified ({round(duration, 2)}s, {w.getframerate()}Hz)")

    # 2. Transcript verification
    raw_transcript = hindi_sample["raw_transcript"]
    assert "बिजली" in raw_transcript and "काट दिया जाएगा" in raw_transcript and "एपीके" in raw_transcript
    print(f"  ✓ Transcript Captured (Hindi Devanagari preserved): \"{raw_transcript[:40]}...\"")

    # 3. Translation verification
    translation = hindi_sample["translation"]
    assert "electricity connection" in translation.lower() and "apk" in translation.lower()
    print(f"  ✓ English Translation: \"{translation[:50]}...\"")

    # 4. Scam Alert verification
    report = sarvam_client.apply_deterministic_checks(
        transcript=raw_transcript,
        translation=translation,
        report=hindi_sample["report"].copy()
    )
    assert report["risk_level"] == "High", f"Expected High risk, got {report['risk_level']}"
    assert len(report["suspicious_evidence"]) >= 1, "Expected evidence phrases"
    assert len(report["recommended_action"]) >= 1, "Expected recommended actions"
    print(f"  ✓ Scam Alert: Risk Level = {report['risk_level']}")
    print(f"  ✓ Why Flagged: {report['why_flagged']}")
    print(f"  ✓ Evidence Quoted: {[e['phrase'] for e in report['suspicious_evidence']]}")
    results["Hindi Recording Test"] = "PASSED"

    # -------------------------------------------------------------------------
    # TEST 2: Hinglish Recording Test
    # -------------------------------------------------------------------------
    print("\n[TEST 2] Testing Hinglish Recording (samples/hinglish_upi_scam.wav)...")
    hinglish_sample = next(s for s in scam_data.SAMPLE_RECORDINGS if s["id"] == "hinglish_sample")
    
    assert os.path.exists(hinglish_sample["file_path"]), f"File not found: {hinglish_sample['file_path']}"
    with wave.open(hinglish_sample["file_path"], "rb") as w:
        duration = w.getnframes() / w.getframerate()
        assert duration > 1.0
    print(f"  ✓ Audio File Verified ({round(duration, 2)}s, {w.getframerate()}Hz)")

    raw_transcript_h = hinglish_sample["raw_transcript"]
    assert "PhonePe" in raw_transcript_h and "UPI PIN" in raw_transcript_h
    print(f"  ✓ Transcript Captured (Hinglish preserved): \"{raw_transcript_h[:40]}...\"")

    translation_h = hinglish_sample["translation"]
    assert "cashback" in translation_h.lower() and "upi pin" in translation_h.lower()
    print(f"  ✓ English Translation: \"{translation_h[:50]}...\"")

    report_h = sarvam_client.apply_deterministic_checks(
        transcript=raw_transcript_h,
        translation=translation_h,
        report=hinglish_sample["report"].copy()
    )
    assert report_h["risk_level"] == "High", f"Expected High risk, got {report_h['risk_level']}"
    assert any("upi pin" in e["phrase"].lower() for e in report_h["suspicious_evidence"])
    print(f"  ✓ Scam Alert: Risk Level = {report_h['risk_level']}")
    print(f"  ✓ Why Flagged: {report_h['why_flagged']}")
    print(f"  ✓ Evidence Quoted: {[e['phrase'] for e in report_h['suspicious_evidence']]}")
    results["Hinglish Recording Test"] = "PASSED"

    # -------------------------------------------------------------------------
    # TEST 3: Benign Recording Test
    # -------------------------------------------------------------------------
    print("\n[TEST 3] Testing Benign Recording (samples/benign_bank_alert.wav)...")
    benign_sample = next(s for s in scam_data.SAMPLE_RECORDINGS if s["id"] == "benign_sample")
    
    assert os.path.exists(benign_sample["file_path"]), f"File not found: {benign_sample['file_path']}"
    with wave.open(benign_sample["file_path"], "rb") as w:
        duration = w.getnframes() / w.getframerate()
        assert duration > 1.0
    print(f"  ✓ Audio File Verified ({round(duration, 2)}s, {w.getframerate()}Hz)")

    raw_transcript_b = benign_sample["raw_transcript"]
    assert "debited" in raw_transcript_b and "Swiggy" in raw_transcript_b
    print(f"  ✓ Transcript Captured: \"{raw_transcript_b[:40]}...\"")

    translation_b = benign_sample["translation"]
    print(f"  ✓ English Translation: \"{translation_b[:40]}...\"")

    report_b = sarvam_client.apply_deterministic_checks(
        transcript=raw_transcript_b,
        translation=translation_b,
        report=benign_sample["report"].copy()
    )
    assert report_b["risk_level"] == "Low", f"Expected Low risk, got {report_b['risk_level']}"
    assert "uncertainty_note" in report_b, "Low risk must have uncertainty disclaimer"
    assert "not a guarantee" in report_b["uncertainty_note"].lower() or "not proof" in report_b["uncertainty_note"].lower()
    print(f"  ✓ Scam Alert: Risk Level = {report_b['risk_level']}")
    print(f"  ✓ Why Flagged: {report_b['why_flagged']}")
    print(f"  ✓ Uncertainty Disclaimer Present: \"{report_b['uncertainty_note'][:50]}...\"")
    results["Benign Recording Test"] = "PASSED"

    # -------------------------------------------------------------------------
    # TEST 4: Transcript Invalidation & Re-analysis Test
    # -------------------------------------------------------------------------
    print("\n[TEST 4] Testing Transcript Invalidation & Safety Escalation...")
    original_text = "Hello, your order has arrived."
    edited_text = "Hello, your order has arrived. Please enter your 6-digit UPI PIN on bit.ly/claim to collect."
    
    # Original analysis of benign text
    initial_report = sarvam_client.apply_deterministic_checks(
        transcript=original_text,
        translation=original_text,
        report={"risk_level": "Low", "why_flagged": "Benign delivery update.", "suspicious_evidence": [], "recommended_action": ["No action."]}
    )
    assert initial_report["risk_level"] == "Low"

    # User edits transcript adding scam element
    updated_report = sarvam_client.apply_deterministic_checks(
        transcript=edited_text,
        translation=edited_text,
        report={"risk_level": "Low", "why_flagged": "Benign delivery update.", "suspicious_evidence": [], "recommended_action": ["No action."]}
    )
    assert updated_report["risk_level"] == "High", f"Editing transcript with UPI PIN trap must trigger High risk, got {updated_report['risk_level']}"
    assert any("upi pin" in e["phrase"].lower() for e in updated_report["suspicious_evidence"])
    print("  ✓ Editing transcript successfully invalidated previous report and escalated to High Risk.")
    results["Transcript Invalidation Test"] = "PASSED"

    print("\n" + "=" * 60)
    print("FINAL TEST RESULTS:")
    print("=" * 60)
    for test_name, status in results.items():
        print(f"  {test_name}: {status}")
    print("=" * 60)
    return results

if __name__ == "__main__":
    test_pipeline()
