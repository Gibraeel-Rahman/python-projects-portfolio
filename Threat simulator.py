#Section for the graphic interface
import tkinter as tk

window = tl.TL()
window.title('Cyber Defence Dashboard')
window.geometry(620x360)
window.configure(bg='#07152e')

title = tk.label(window, text='SOC Threat Dashboard', fg='#4ae0ff', bg='#07152e',
                 font=('Consolas', 22, 'bold'))
title.pack(pady=15)

output = tk.text(window, width=68, height=11, bg='#020817', fg='#dff7ff)
                 output.pack(padx=15, pady=10)

#list for threats to identify
THREATS =   {
    'botnet': {
        'impact': 'Hijacked machines can be used together for crime',
        'defence': 'Use protection software and apply prompt upadtes.'
    },
    'ddos': {
        'impact': 'A service is flooded so real users cannot get through',
        'defence': 'Filter suspcious traffic and keep spare capacity.'
    },
    'ransomware': {
        'impact': 'Database is encrypted and payment is demanded.',
        'defence': 'Keep tested backups, patch systems and avoid unsafe downloads.'
    },
    'sql injection':{
        'impacts': 'Database commands are smuggled through input boxes.',
        'defence': 'Validate and sanitise input before using it.'
    }
}
def calculate_risk(likelihood, impact):
    score = float(likelihood * impact)
    if score>= 16:
        label = 'High'
        urgent = True
    elif score >= 8:
        label = 'medium'
        urgent = False
    else:
        label = 'low'
        urgent = False
        return score, label, urgent
#add questions to decide likelihood and urgency

#have this line collect inputs
score, label, urgent = calculate_risk(4, 5)
print(f'Risk score: {score} | Level: {label} | Urgent: {urgent}')

EVENTS = [
    {'source': 'web-form', 'threat': 'sql injection', 'impact': 4},
    {'source': 'server', 'threat': 'ddos', 'impact': 5},
    {'source':'laptop-12', 'threat': 'ransomware', 'impact': 5},
    {'source': 'pc-04', 'threat':'botnet', 'impact': 3},
    {'source': 'phone-03', 'threat': 'virus', 'impact': 3},
    {'source': 'watch-01', 'threat': 'virus', 'impact': 2},
    {'source': 'pc-02', 'threat' 'ransomware', 'impact': 4},
    {'source': 'server', 'threat': 'sql injection', 'impact': 4},
    {'source':}
    {'source':}
]

def analyse_events(events):
    count ={}
    for event in events:
        threat = event['threat']
        counts[threat] = count.get(threat, 0) + 1
    return counts

summary = analyse_events(EVENTS)
for threat, total in summary.items():
    print{f'{threat.title()}: {total} event(s)')
        


