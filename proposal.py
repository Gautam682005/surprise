from nicegui import ui

# ---------- GLOBAL STATE ----------
current_step = 0
PASSWORD = "gautam"

messages = [
    "Pata hai… jab se tum meri life me aaye ho,\nsab kuch thoda zyada special lagne laga hai 😊",
    "Tumhari ek smile,\nmera poora din better bana deti hai 💕",
    "Main perfect nahi hoon,\npar tumhare saath rehna mujhe perfect feel karata hai 🫶",
]

# ---------- THEME + ANIMATION ----------
ui.add_head_html("""
<style>

/* ---------- CARD (GLASS + ROMANTIC) ---------- */
.card {
    background: linear-gradient(
        135deg,
        rgba(255,255,255,0.85),
        rgba(255,255,255,0.65)
    );
    backdrop-filter: blur(16px);
    border-radius: 28px;
    padding: 28px;
    box-shadow:
        0 25px 45px rgba(236, 72, 153, 0.15),
        inset 0 0 0 1px rgba(255,255,255,0.4);
    animation: cardFloat 0.8s ease;
}

@keyframes cardFloat {
    from { opacity: 0; transform: translateY(20px) scale(0.97); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}

.title {
    font-size: 2.1rem;
    font-weight: 700;
    background: linear-gradient(135deg, #ec4899, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
}

.main-text {
    font-size: 1.35rem;
    color: #374151;
    text-align: center;
    white-space: pre-line;
    line-height: 1.7;
}

/* ---------- FLOWER FALL ---------- */
.flower {
    position: fixed;
    top: -40px;
    z-index: 9999;
    pointer-events: none;
    animation-name: flowerFall;
    animation-timing-function: linear;
}

@keyframes flowerFall {
    from { transform: translateY(-50px) rotate(0deg); }
    to { transform: translateY(110vh) rotate(360deg); }
}
</style>

<!-- ✅ CONFETTI LIBRARY (CORRECT PLACE) -->
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
""")
# ---------- FLOWER FALL (SAFE JS) ----------
def start_flower_fall():
    ui.run_javascript("""
    setInterval(() => {
        const f = document.createElement('div');
        f.className = 'flower';
        f.innerText = ['🌸','🌷','🌹','💐'][Math.floor(Math.random()*4)];
        f.style.left = Math.random() * 100 + 'vw';
        f.style.fontSize = '24px';
        f.style.animationDuration = (6 + Math.random() * 4) + 's';
        document.body.appendChild(f);
        setTimeout(() => f.remove(), 10000);
    }, 600);
    """)
# ---------- CONFETTI / CRACKERS ----------
def start_crackers():
    ui.run_javascript("""
    const duration = 4 * 1000;
    const end = Date.now() + duration;

    (function frame() {
        confetti({
            particleCount: 6,
            angle: 60,
            spread: 55,
            origin: { x: 0 }
        });
        confetti({
            particleCount: 6,
            angle: 120,
            spread: 55,
            origin: { x: 1 }
        });

        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    })();
    """)
# ---------- CONTAINER ----------
container = ui.column().classes('w-full h-screen flex items-center justify-center')

def clear():
    container.clear()

# ---------- PASSWORD SCREEN ----------
def check_password():
    if pwd.value == PASSWORD:
        start_flower_fall()
        start_app()
    else:
        ui.notify("Hint: Ek handsome name 😜", color="red")

# ---------- APP FLOW ----------
def start_app():
    global current_step
    current_step = 0
    show_message()

def show_message():
    global current_step
    clear()
    with container:
        with ui.card().classes('card w-96'):
            ui.label(messages[current_step]).classes('main-text')
            ui.button(
                "Next 💗",
                on_click=next_message
            ).classes('w-full mt-4 bg-pink-400 text-white rounded-full')

def next_message():
    global current_step
    current_step += 1
    if current_step < len(messages):
        show_message()
    else:
        show_letter()

def show_letter():
    clear()
    with container:
        with ui.card().classes('card w-[420px]'):
            ui.label("💌 Ek pyara sa Letter 4U").classes('title')
            ui.separator()
            ui.label(
                "ye letter pyar se aap ke liye likha hai,\n"
                "Tum bhut sweet aur pyari💗 hoo…\n\n"
                "Tum meri life ka beautiful part ho,\n"
                "Mera goal aur aim to tum hi hoo,\n"
                "tumhare bina sab incomplete sa lagta hai.\n\n"
                "Thank you…\n"
                "for being you,\n"
                "for being mine (thoda sa 😌) 💖"
            ).classes('main-text')
            ui.button(
                "Aage 💞",
                on_click=show_cute_buttons
            ).classes('w-full mt-4 bg-pink-400 text-white rounded-full')

def show_cute_buttons():
    clear()
    with container:
        with ui.card().classes('card w-96'):
            ui.label("🤍 Thodi Si Cute Baatein").classes('title')
            ui.separator()

            ui.button(
                "Why I Like You 💗",
                on_click=lambda: ui.notify("ku ki tum meri ho aur pyari to ho hi 💕")
            ).classes('w-full mt-2')

            ui.button(
                "Tum Mere Liye Kya Ho 🫶",
                on_click=lambda: ui.notify("Tum meri partner ho aur mare liye ek khaas mittar 🤍")
            ).classes('w-full mt-2')

            ui.button(
                "Ek romantic Baat😜 ",
                on_click=lambda: ui.notify(" i like your 🍑or🍒 😍")
            ).classes('w-full mt-2')

            ui.button(
                "Last Page 💍",
                on_click=show_proposal
            ).classes('w-full mt-4 bg-pink-400 text-white rounded-full')

def show_proposal():
    clear()
    with container:
        with ui.card().classes('card w-96'):
            ui.label("Toh ek sawal hai…").classes('title')
            ui.label("Will you be my person? 💖").classes('main-text')

            ui.button(
                "YES 😊",
                on_click=final_yes
            ).classes('w-full mt-3 bg-green-400 text-white rounded-full')

            ui.button(
                "Obviously YES 😭",
                on_click=final_yes
            ).classes('w-full mt-2 bg-green-500 text-white rounded-full')

def final_yes():
    start_crackers()
    clear()
    with container:
        with ui.card().classes('card w-96'):
            ui.label("Yayyy 🥹💖").classes('title')
            ui.label(
                "Tumne mujhe bohot special feel karaya.\n"
                "Thank you for saying YES 💕\n\n"
                "Ye website yahin khatam hoti hai,\n"
                "par meri feelings nahi.\n\n"
                "I’m really lucky to have you ✨"
            ).classes('main-text')

# ---------- START (PASSWORD SCREEN) ----------
with container:
    with ui.card().classes('card w-96'):
        ui.label("🔐 Secret Entry").classes('title')
        pwd = ui.input("Password").props('type=password')
        ui.button(
            "Unlock 💕",
            on_click=check_password
        ).classes('w-full mt-4 bg-pink-400 text-white rounded-full')

ui.run()