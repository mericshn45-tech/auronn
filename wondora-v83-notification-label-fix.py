from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit('Usage: python wondora-v83-notification-label-fix.py <index.html>')

p = Path(sys.argv[1])
s = p.read_text(encoding='utf-8')

repls = {
    "streak:'Seri Hatırlatmaları'": "streak:'7. Gün Özel Hatırlatması'",
    "streak:'Streak Reminders'": "streak:'Day 7 Special Reminder'",
    "streak:'Recordatorios de racha'": "streak:'Recordatorio especial del día 7'",
    "streak:'Lembretes de sequência'": "streak:'Lembrete especial do 7º dia'",
    "streak:'Serien-Erinnerungen'": "streak:'Spezial-Erinnerung für Tag 7'",
    "streak:'Rappels de série'": "streak:'Rappel spécial du 7e jour'",
    "streak:'Promemoria serie'": "streak:'Promemoria speciale del 7° giorno'",
    '<span id="v81NotifyStreakLabel">🔥 Seri Hatırlatmaları</span>': '<span id="v81NotifyStreakLabel">🌟 7. Gün Özel Hatırlatması</span>',
    "q('v81NotifyStreakLabel','🔥 '+l.streak)": "q('v81NotifyStreakLabel','🌟 '+l.streak)",
    "if(k==='streak')AndroidNotifications.cancel('streak_special')": ""
}

for old, new in repls.items():
    if old not in s:
        print('WARN missing:', old)
    s = s.replace(old, new)

# Preserve state.notifications.streak key for backward-compatible saved settings.
p.write_text(s, encoding='utf-8')
print('Patched:', p)
