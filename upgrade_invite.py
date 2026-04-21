import os

def upgrade_html():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    b64_path = os.path.join(script_dir, 'b64.txt')
    if not os.path.exists(b64_path):
        print("b64.txt not found")
        return

    with open(b64_path, 'r') as f:
        b64_string = f.read().strip()

    # Use f-string but escape all {{ and }} in CSS
    html_content = f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>החגיגה של חן ושלומי</title>
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}

        html, body {{
            width: 100%;
            overflow-x: hidden;
            font-family: 'Heebo', sans-serif;
            direction: rtl;
            color: #fff;
            background: #111;
        }}

        #page {{
            min-height: 100vh;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 70px 16px 60px;
            position: relative;
        }}

        /* Background via pseudo-element — avoids z-index issues */
        #page::before {{
            content: '';
            position: fixed;
            inset: 0;
            background-image: url('data:image/jpeg;base64,{b64_string}');
            background-size: cover;
            background-position: calc(50% - 2cm) center;
            filter: brightness(0.4);
            z-index: 0;
        }}

        #content {{
            position: relative;
            z-index: 1;
            width: 100%;
            max-width: 460px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 22px;
        }}

        h1 {{
            font-family: 'Playfair Display', serif;
            font-size: 2.6rem;
            font-weight: 700;
            text-align: center;
            background: linear-gradient(45deg, #d4af37, #f7e681, #d4af37);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.2;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }}

        .names {{
            font-size: 1.4rem;
            font-weight: 400;
            letter-spacing: 2px;
            text-align: center;
            text-shadow: 0 1px 3px rgba(0,0,0,0.5);
        }}

        .meta {{
            text-align: center;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}

        .date {{ font-size: 1.25rem; font-weight: 700; color: #d4af37; text-shadow: 0 1px 2px rgba(0,0,0,0.5); }}
        .loc  {{ font-size: 1.1rem; opacity: 0.9; font-weight: 400; }}

        .divider {{
            width: 40%;
            height: 1px;
            background: linear-gradient(to left, transparent, rgba(212,175,55,0.6), transparent);
        }}

        .glass {{
            width: 100%;
            background: rgba(0, 0, 0, 0.25);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 20px;
            padding: 28px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 22px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }}

        .invite-text {{
            font-size: 1.25rem;
            line-height: 1.6;
            text-align: center;
            color: #fff;
            font-weight: 400;
        }}

        #toggle-btn {{
            padding: 14px 28px;
            background: rgba(212, 175, 55, 0.15);
            border: 1px solid rgba(212, 175, 55, 0.4);
            border-radius: 50px;
            color: #f7e681;
            font-size: 1.1rem;
            font-weight: 600;
            font-family: 'Heebo', sans-serif;
            cursor: pointer;
            -webkit-tap-highlight-color: transparent;
            outline: none;
            transition: all 0.3s;
        }}

        #details {{
            display: none;
            width: 100%;
        }}

        .items-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
            width: 100%;
        }}

        .item {{
            display: flex;
            align-items: flex-start;
            gap: 10px;
        }}

        .dot {{
            width: 7px; height: 7px;
            border-radius: 50%;
            background: #d4af37;
            flex-shrink: 0;
            margin-top: 6px;
        }}

        .item p {{ font-size: 1.1rem; line-height: 1.5; color: #fff; }}

        .sep {{ width: 100%; height: 1px; background: rgba(255,255,255,0.1); margin: 8px 0; }}

        .menu-box {{
            width: 100%;
            background: rgba(212,175,55,0.08);
            border: 1px solid rgba(212,175,55,0.25);
            border-radius: 14px;
            padding: 14px;
        }}

        .menu-title {{ font-size: 1.15rem; font-weight: 700; color: #f7e681; margin-bottom: 8px; text-align: right; }}
        .menu-items {{ font-size: 1.05rem; color: #fff; line-height: 1.5; text-align: right; }}

        .nav-btns {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            width: 100%;
            align-items: center;
            margin-top: 4px;
        }}

        .nav-btn {{
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 12px 24px;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 600;
            font-family: 'Heebo', sans-serif;
            text-decoration: none;
            white-space: nowrap;
            transition: transform 0.2s;
        }}

        .btn-maps {{ background: rgba(212,175,55,0.1); border: 1px solid rgba(212,175,55,0.4); color: #d4af37; }}
        .btn-waze {{ background: rgba(100,180,255,0.1); border: 1px solid rgba(100,180,255,0.4); color: #64b4ff; }}
        .nav-btn svg {{ width: 15px; height: 15px; flex-shrink: 0; }}

        .closing {{
            text-align: center;
            padding-top: 8px;
            font-family: 'Playfair Display', serif;
            font-size: 1.4rem;
            font-style: italic;
            font-weight: 700;
            background: linear-gradient(45deg, #d4af37, #f7e681, #d4af37);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
    </style>
</head>
<body>
    <div id="page">
        <div id="content">
            <h1>חפלת נדרים</h1>
            <p class="names">חן &amp; שלומי</p>
            <div class="meta">
                <span class="date">15.05.2026</span>
                <span class="loc">ירוק עז, אילניה</span>
            </div>

            <div class="divider"></div>

            <div class="glass">
                <p class="invite-text">אנחנו מתרגשים להזמין אתכם לחגוג איתנו את המסע המשותף שלנו</p>

                <button id="toggle-btn" type="button">כל הפרטים החשובים ▼</button>

                <div id="details">
                    <div class="items-list">
                        <div class="item"><div class="dot"></div><p>באים מתי שרוצים</p></div>
                        <div class="item"><div class="dot"></div><p>אפשר להישאר לישון (יש מקלחות ומזרנים)</p></div>
                        <div class="item"><div class="dot"></div><p><strong>לא מביאים צ׳קים</strong></p></div>
                        <div class="item"><div class="dot"></div><p>תתארגנו על בייביסיטר</p></div>
                    </div>

                    <div class="sep"></div>

                    <div class="menu-box">
                        <p class="menu-title">בתפריט:</p>
                        <p class="menu-items">ריקודים, כיבוד קל, פינות ישיבה, מדורה ובריכה</p>
                    </div>

                    <div class="nav-btns">
                        <a class="nav-btn btn-maps" href="https://maps.app.goo.gl/19NHz21dpq71rDXp6" target="_blank">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                            </svg>
                            ניווט עם Google Maps
                        </a>
                        <a class="nav-btn btn-waze" href="https://ul.waze.com/ul?venue_id=23200072.232066252.2121120&overview=yes" target="_blank">
                            <svg viewBox="0 0 24 24" fill="currentColor">
                                <path d="M20.54 7.27C19.27 3.05 15.37 0 11 0 5.49 0 1 4.49 1 10c0 2.74 1.11 5.22 2.9 7.04L3 22l5.22-.92C9.35 21.65 10.16 22 11 22c5.51 0 10-4.49 10-10 0-1.65-.41-3.2-1.13-4.57l.67.17z"/>
                            </svg>
                            ניווט עם Waze
                        </a>
                    </div>

                    <p class="closing">מצפים לראותכם!</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        var btn = document.getElementById('toggle-btn');
        var details = document.getElementById('details');
        var isOpen = false;

        btn.addEventListener('click', function() {{
            isOpen = !isOpen;
            details.style.display = isOpen ? 'block' : 'none';
            btn.textContent = isOpen ? 'פחות פרטים ▲' : 'כל הפרטים החשובים ▼';
        }});
    </script>
</body>
</html>"""

    desktop_path = os.path.expanduser('~/Desktop/wedding_invitation.html')
    local_path = os.path.join(script_dir, 'index.html')

    for path in [desktop_path, local_path]:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html_content)

    print(f"Done!\n  {desktop_path}\n  {local_path}")

if __name__ == "__main__":
    upgrade_html()
