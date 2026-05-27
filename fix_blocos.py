"""
Lê gerar_quiz_real.py, atualiza o campo bloco de cada questão
baseado no número do artigo, e regenera quiz_real_lc840.html.
"""
import re, json

# ── 1. Extrair QUESTOES do arquivo existente ──────────────────────────────────
with open("gerar_quiz_real.py", encoding="utf-8") as f:
    src = f.read()

# Isola o bloco QUESTOES = [ ... ] para eval
m = re.search(r"QUESTOES = (\[.*?\n\])", src, re.DOTALL)
QUESTOES = eval(m.group(1))   # seguro: só dicts com strings/ints

# ── 2. Mapeamento artigo → bloco ──────────────────────────────────────────────
def art_para_bloco(art_str):
    nums = re.findall(r"\d+", art_str)
    if not nums:
        return "Geral"
    n = int(nums[0])
    if   n <= 54:  return "Provimento (Arts. 4–54)"
    elif n <= 65:  return "Deveres e Proibições (Arts. 55–65)"
    elif n <= 99:  return "Jornada e Remuneração (Arts. 57–99)"
    elif n <= 124: return "Indenizações e Auxílios (Arts. 100–124)"
    elif n <= 129: return "Férias (Arts. 125–129)"
    elif n <= 155: return "Licenças (Arts. 130–155)"
    elif n <= 182: return "Outros Direitos (Arts. 156–182)"
    elif n <= 195: return "Responsabilidades (Arts. 183–195)"
    else:          return "Processo Disciplinar (Arts. 196–270)"

for q in QUESTOES:
    q["bloco"] = art_para_bloco(q["art"])

# ── 3. Mostrar distribuição ───────────────────────────────────────────────────
from collections import Counter
dist = Counter(q["bloco"] for q in QUESTOES)
print("\nQuestoes por bloco:")
for bloco, n in sorted(dist.items(), key=lambda x: x[0]):
    print(f"  {n:>3}  {bloco}")
print(f"\n  Total: {len(QUESTOES)} questões\n")

BANCAS = sorted(set(q["banca"] for q in QUESTOES))
BLOCOS = sorted(set(q["bloco"] for q in QUESTOES))

# ── 4. Gerar HTML (mesmo layout do original) ─────────────────────────────────
CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #0d1117; color: #e6edf3; font-family: 'Segoe UI', sans-serif; min-height: 100vh; display: flex; flex-direction: column; align-items: center; padding: 20px; }
h1 { font-size: 1.4rem; color: #58a6ff; margin-bottom: 4px; }
.sub { color: #8b949e; font-size: .85rem; margin-bottom: 16px; text-align: center; }
.filter-section { width: 100%; max-width: 640px; margin-bottom: 12px; }
.filter-label { color: #8b949e; font-size: .8rem; margin-bottom: 6px; text-transform: uppercase; letter-spacing: .5px; }
.controls { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 8px; }
.controls label { background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 5px 10px; font-size: .78rem; cursor: pointer; display: flex; align-items: center; gap: 5px; }
.controls label:hover { border-color: #58a6ff; }
.controls input[type=checkbox] { accent-color: #58a6ff; }
.btn-start { background: #238636; color: #fff; border: none; border-radius: 8px; padding: 10px 28px; font-size: 1rem; cursor: pointer; margin-top: 8px; }
.btn-start:hover { background: #2ea043; }
#game { display: none; width: 100%; max-width: 640px; }
.score-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; font-size: .88rem; color: #8b949e; }
#num-badge { background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 4px 10px; font-size: .8rem; }
.timer-wrap { height: 5px; background: #21262d; border-radius: 3px; margin-bottom: 14px; }
#timer-bar { height: 5px; border-radius: 3px; background: #3fb950; transition: width 1s linear, background .5s; }
.card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 20px; margin-bottom: 12px; }
.meta { display: flex; gap: 8px; margin-bottom: 10px; flex-wrap: wrap; }
.badge { font-size: .7rem; padding: 2px 8px; border-radius: 10px; border: 1px solid; }
.badge-banca { border-color: #58a6ff; color: #58a6ff; background: rgba(88,166,255,.1); }
.badge-bloco { border-color: #8b949e; color: #8b949e; }
.question { font-size: 1rem; line-height: 1.6; }
.opts { display: flex; gap: 12px; margin-top: 14px; }
.opt { flex: 1; background: #0d1117; border: 2px solid #30363d; border-radius: 8px; padding: 14px; text-align: center; font-size: 1rem; font-weight: 700; cursor: pointer; transition: .15s; }
.opt:hover:not(:disabled) { border-color: #58a6ff; color: #58a6ff; }
.opt.correct { border-color: #3fb950; background: rgba(63,185,80,.15); color: #3fb950; }
.opt.wrong { border-color: #f85149; background: rgba(248,81,73,.15); color: #f85149; }
.opt:disabled { cursor: default; }
.feedback { margin-top: 12px; padding: 12px 14px; border-radius: 8px; font-size: .88rem; line-height: 1.5; display: none; }
.feedback.show { display: block; }
.feedback.ok { background: rgba(63,185,80,.1); border: 1px solid #3fb950; color: #3fb950; }
.feedback.nok { background: rgba(248,81,73,.1); border: 1px solid #f85149; color: #f85149; }
.art-ref { font-size: .78rem; opacity: .8; margin-bottom: 4px; }
.btn-next { display: none; width: 100%; padding: 11px; background: #1f6feb; border: none; border-radius: 8px; color: #fff; font-size: .95rem; cursor: pointer; margin-top: 10px; }
.btn-next:hover { background: #388bfd; }
.btn-next.show { display: block; }
#result { display: none; text-align: center; padding: 30px; max-width: 640px; width: 100%; }
#result h2 { font-size: 1.6rem; margin-bottom: 8px; }
.score-big { font-size: 3rem; font-weight: 700; color: #58a6ff; margin: 12px 0; }
.score-label { color: #8b949e; margin-bottom: 20px; }
.stats-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 16px 0; }
.stat-card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 12px; }
.stat-val { font-size: 1.4rem; font-weight: 700; color: #58a6ff; }
.stat-lbl { font-size: .75rem; color: #8b949e; margin-top: 2px; }
.btn-retry { background: #238636; color: #fff; border: none; border-radius: 8px; padding: 12px 24px; font-size: .95rem; cursor: pointer; margin: 6px; }
.btn-retry:hover { background: #2ea043; }
.btn-wrongs { background: #b62324; color: #fff; border: none; border-radius: 8px; padding: 12px 24px; font-size: .95rem; cursor: pointer; margin: 6px; }
"""

JS = r"""
const QUESTOES = __QUESTOES__;
let deck=[], idx=0, score=0, total=0, wrongs=[], timer=null, secs=30;

function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function getChecked(cls){return [...document.querySelectorAll('.'+cls+' input:checked')].map(i=>i.value);}

function startGame(mode){
  const bancas=getChecked('filter-bancas');
  const blocos=getChecked('filter-blocos');
  let source = mode==='wrongs' ? wrongs : QUESTOES.filter(q=>bancas.includes(q.banca)&&blocos.includes(q.bloco));
  deck=shuffle([...source]);
  if(!deck.length){alert('Nenhuma questão com os filtros selecionados!');return;}
  idx=0;score=0;total=deck.length;wrongs=[];
  document.getElementById('setup').style.display='none';
  document.getElementById('game').style.display='block';
  document.getElementById('result').style.display='none';
  nextQ();
}

function nextQ(){
  if(idx>=deck.length){showResult();return;}
  const q=deck[idx];
  document.getElementById('num-badge').textContent=`${idx+1} / ${total}`;
  document.querySelector('.badge-banca').textContent=q.banca;
  document.querySelector('.badge-bloco').textContent=q.bloco;
  document.querySelector('.question').textContent=q.q;
  const optsDiv=document.querySelector('.opts');
  optsDiv.innerHTML='';
  q.opts.forEach((o,i)=>{
    const b=document.createElement('button');
    b.className='opt'; b.textContent=o;
    b.onclick=()=>answer(i,q);
    optsDiv.appendChild(b);
  });
  document.querySelector('.feedback').className='feedback';
  document.querySelector('.btn-next').className='btn-next';
  startTimer();
}

function startTimer(){
  clearInterval(timer); secs=30;
  const bar=document.getElementById('timer-bar');
  bar.style.transition='none'; bar.style.width='100%'; bar.style.background='#3fb950';
  setTimeout(()=>{ bar.style.transition='width 1s linear, background .5s'; bar.style.width='0%'; },50);
  timer=setInterval(()=>{
    secs--;
    const pct=secs/30*100;
    if(pct<40) bar.style.background='#d29922';
    if(pct<20) bar.style.background='#f85149';
    if(secs<=0){clearInterval(timer);timeout();}
  },1000);
}

function timeout(){
  const q=deck[idx];
  document.querySelectorAll('.opt').forEach(b=>b.disabled=true);
  document.querySelectorAll('.opt')[q.a].classList.add('correct');
  wrongs.push(q); showFeedback(false,q);
}

function answer(i,q){
  clearInterval(timer);
  const btns=document.querySelectorAll('.opt');
  btns.forEach(b=>b.disabled=true);
  const ok=(i===q.a);
  btns[i].classList.add(ok?'correct':'wrong');
  if(!ok){btns[q.a].classList.add('correct');wrongs.push(q);}
  if(ok) score++;
  showFeedback(ok,q);
}

function showFeedback(ok,q){
  const fb=document.querySelector('.feedback');
  fb.innerHTML=`<div class="art-ref">${q.art} — Gabarito: <strong>${q.opts[q.a]}</strong></div><div>${q.tip}</div>`;
  fb.className='feedback show '+(ok?'ok':'nok');
  document.querySelector('.btn-next').className='btn-next show';
  document.getElementById('score-val').textContent=score;
}

function nextQuestion(){idx++;nextQ();}

function showResult(){
  document.getElementById('game').style.display='none';
  const res=document.getElementById('result');
  res.style.display='block';
  const pct=Math.round(score/total*100);
  res.querySelector('h2').textContent=pct>=80?'Excelente! 🎯':pct>=60?'Bom trabalho! 💪':'Continue praticando! 📚';
  res.querySelector('.score-big').textContent=`${score}/${total}`;
  res.querySelector('.score-label').textContent=`${pct}% de acerto`;
  document.getElementById('stat-wrong').textContent=total-score;
  document.getElementById('stat-pct').textContent=pct+'%';
  document.getElementById('btn-wrongs').style.display=wrongs.length?'inline-block':'none';
}

function retryAll(){document.getElementById('result').style.display='none';document.getElementById('setup').style.display='block';}
function retryWrongs(){document.getElementById('result').style.display='none';startGame('wrongs');}
"""

def build_html():
    bancas_checkboxes = "\n    ".join(
        f'<label><input type="checkbox" value="{b}" checked> {b}</label>'
        for b in BANCAS
    )
    blocos_checkboxes = "\n    ".join(
        f'<label><input type="checkbox" value="{b}" checked> {b}</label>'
        for b in BLOCOS
    )
    js = JS.replace("__QUESTOES__", json.dumps(QUESTOES, ensure_ascii=False))

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Quiz Questões Reais — LC 840/2011</title>
<style>{CSS}</style>
</head>
<body>
<h1>📋 Quiz Questões Reais</h1>
<p class="sub">LC 840/2011 — {len(QUESTOES)} questões de prova • QUADRIX · CEBRASPE · IADES · IBFC · FCC<br>Timer 30s • Gabarito exibido após cada questão</p>

<div id="setup" style="width:100%;max-width:640px">
  <div class="filter-section">
    <div class="filter-label">Banca</div>
    <div class="controls filter-bancas">
      {bancas_checkboxes}
    </div>
    <div class="filter-label" style="margin-top:10px">Artigos</div>
    <div class="controls filter-blocos">
      {blocos_checkboxes}
    </div>
  </div>
  <div style="text-align:center">
    <button class="btn-start" onclick="startGame('all')">▶ Iniciar</button>
  </div>
</div>

<div id="game">
  <div class="score-bar">
    <span>Acertos: <span id="score-val" style="color:#3fb950">0</span></span>
    <span id="num-badge">1 / {len(QUESTOES)}</span>
  </div>
  <div class="timer-wrap"><div id="timer-bar" style="width:100%"></div></div>
  <div class="card">
    <div class="meta">
      <span class="badge badge-banca"></span>
      <span class="badge badge-bloco"></span>
    </div>
    <div class="question"></div>
    <div class="opts"></div>
    <div class="feedback"></div>
    <button class="btn-next" onclick="nextQuestion()">Próximo →</button>
  </div>
</div>

<div id="result">
  <h2></h2>
  <div class="score-big"></div>
  <div class="score-label"></div>
  <div class="stats-grid">
    <div class="stat-card"><div class="stat-val" id="stat-wrong"></div><div class="stat-lbl">Erros</div></div>
    <div class="stat-card"><div class="stat-val" id="stat-pct"></div><div class="stat-lbl">Aproveitamento</div></div>
  </div>
  <button class="btn-retry" onclick="retryAll()">↩ Novo simulado</button>
  <button class="btn-wrongs" id="btn-wrongs" onclick="retryWrongs()" style="display:none">🔁 Rever erros</button>
</div>

<script>{js}</script>
</body>
</html>"""

html = build_html()
path = r"c:\Users\hacke\OneDrive - unb.br\estudo\quiz_real_lc840.html"
with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"\n✅ quiz_real_lc840.html gerado — {len(QUESTOES)} questões, {len(html)//1024}KB")
