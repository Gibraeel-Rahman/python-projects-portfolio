THREAT_LIBRARY = {
                "phishing": {"keywords": ["email", "verify", "account", "urgent", "invoice", "link"],
                    "impact": "Credentials or payments may be handed to an attacker.", "defence": "Check the sender, hover over links, verify using a known route and use MFA." },
                "smishing": {"keywords": ["text", "sms", "delivery", "parcel", "bank alert"],
                    "impact": "Victims may tap a malicious link from a trusted phone channel.","defence": "Do not act on unexpected texts; open the real app or call a trusted number." },
                "vishing": {"keywords": ["call", "phone", "voice", "police", "it support"],
                    "impact": "A caller may pressure the victim into sharing credentials or payment details.", "defence": "End the call and call back using an official number you already know." },
                "usb baiting": {"keywords": ["usb", "memory stick", "car park", "reception"],
                    "impact": "A single plugged-in infected drive can compromise a network.","defence": "Never plug in unknown drives; follow policy and disable unused USB ports." },
                "open wi-fi / mitm": {"keywords": ["wifi", "wi-fi", "hotspot", "cafe", "intercept"],
                    "impact": "An attacker may read or alter traffic on an unsecured connection.","defence": "Avoid sensitive tasks, use HTTPS/VPN, and secure any access point you run." },
                "dns/pharming": {"keywords": ["dns", "redirect", "fake website", "certificate", "address"],
                    "impact": "Users can be silently redirected to a fake website and lose credentials.","defence": "Use patched trusted DNS, check HTTPS, and heed certificate warnings." },
                "insecure api": {"keywords": ["api", "endpoint", "records", "data leak", "permission"],
                    "impact": "Weak API protection can leak thousands of records very quickly.","defence": "Use keys, permissions, rate limits, validation and thorough testing."}
}

def analyse_report(report_text):
    report = report_text.lower()

report= input('Incident report: ')
result = analyse_report(report)
print(result)

def calculate_risk(likelihood, impact):
    score = likelihiood * impact
    if score >= 16:
        return score, 'High', True
    elif score >=8:
        return score, 'Medium', False
    else:
        return score, 'Low', False

score, level, urgent = calculate_risk(4, 5)
print( score, level, urgent)

EVENTS = [
    {'source': 'email', 'report': 'urgent verify link', 'likelihood': 4, 'impact': 4},
    {'source': 'reception', 'report': 'unknown USB found', 'likelihoodd': 3, 'impact': 5},
    ]

for event in EVENTS:
    analysis = analyse_report(event['report'])
    score = event['likelihood'] * event['impact']
    print(event['source'], analysis['threat'], score)

import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title('TrustGuard SOC Dashboard')
window.geometry('950x640')
