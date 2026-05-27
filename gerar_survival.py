"""Gera survival_lc840.html — Modo Sobrevivência: 3 vidas, responda até errar 3 vezes"""

import json

# Mix de múltipla escolha do quiz_lc840 + algumas novas
QUESTOES = [
    {"cat":"Provimento","q":"A posse deve ocorrer em até quantos dias após a publicação do ato de nomeação?","opts":["15 dias","30 dias","45 dias","60 dias"],"a":1,"art":"Art. 17, §1º","tip":"Posse = 30 dias. Não tomando posse, o ato é tornado sem efeito."},
    {"cat":"Provimento","q":"Após a posse, o servidor tem quantos dias úteis para entrar em exercício?","opts":["3 dias úteis","5 dias úteis","10 dias úteis","15 dias úteis"],"a":1,"art":"Art. 19, §2º","tip":"Exercício = 5 dias úteis. Se não entrar, é exonerado."},
    {"cat":"Provimento","q":"O estágio probatório tem duração de:","opts":["1 ano","2 anos","3 anos","5 anos"],"a":2,"art":"Art. 22","tip":"3 anos de efetivo exercício."},
    {"cat":"Provimento","q":"O concurso público tem validade de até:","opts":["1 ano","2 anos","3 anos","4 anos"],"a":1,"art":"Art. 12","tip":"Até 2 anos, prorrogável 1 vez por igual período."},
    {"cat":"Provimento","q":"O percentual mínimo de cargos em comissão para servidores de carreira é:","opts":["20%","50%","70%","80%"],"a":2,"art":"Art. 10, §1º","tip":"70% dos CC devem ser providos por servidores de carreira."},
    {"cat":"Provimento","q":"A reserva de vagas para PCD no concurso é de:","opts":["5%","10%","15%","20%"],"a":3,"art":"Art. 13","tip":"20% das vagas, desprezada a parte decimal."},
    {"cat":"Retorno","q":"Qual é o prazo para retornar ao cargo na REVERSÃO?","opts":["5 dias úteis","10 dias úteis","15 dias úteis","30 dias"],"a":2,"art":"Art. 34, §1º","tip":"Reversão = 15 dias úteis. Reintegração = 5 dias. Recondução = dia seguinte."},
    {"cat":"Retorno","q":"Qual é o prazo para retornar ao cargo na REINTEGRAÇÃO?","opts":["1 dia útil","5 dias úteis","10 dias úteis","15 dias úteis"],"a":1,"art":"Art. 36, §3º","tip":"Reintegração = 5 dias úteis."},
    {"cat":"Retorno","q":"Na RECONDUÇÃO, o servidor deve retornar:","opts":["No mesmo dia","No dia seguinte à ciência do ato","Em 5 dias úteis","Em 15 dias"],"a":1,"art":"Art. 37, §2º","tip":"Recondução = dia seguinte. O mais rápido dos retornos."},
    {"cat":"Retorno","q":"No APROVEITAMENTO (disponibilidade), o servidor tem quantos dias para retornar?","opts":["5 dias úteis","15 dias","30 dias","60 dias"],"a":2,"art":"Art. 40, §1º","tip":"Aproveitamento = 30 dias."},
    {"cat":"Retorno","q":"A remuneração do servidor em disponibilidade nunca pode ser inferior a:","opts":["1/5 do que percebia","1/4 do que percebia","1/3 do que percebia","1/2 do que percebia"],"a":2,"art":"Art. 38, §único","tip":"Disponibilidade: mínimo 1/3."},
    {"cat":"Jornada","q":"Qual é a jornada do servidor efetivo?","opts":["20 horas semanais","30 horas semanais","36 horas semanais","40 horas semanais"],"a":1,"art":"Art. 57","tip":"Efetivo = 30h. CC = 40h."},
    {"cat":"Jornada","q":"Qual é o adicional por serviço extraordinário?","opts":["25%","50%","75%","100%"],"a":1,"art":"Art. 84","tip":"Hora extra = 50% sobre a hora normal."},
    {"cat":"Jornada","q":"Qual é o adicional noturno (22h às 5h)?","opts":["25%","50%","75%","100%"],"a":0,"art":"Art. 85","tip":"Noturno = 25%. Hora noturna = 52min30s."},
    {"cat":"Jornada","q":"O abono de ponto corresponde a quantos dias por ano?","opts":["3 dias","5 dias","7 dias","10 dias"],"a":1,"art":"Art. 151","tip":"5 dias por ano, sem faltas injustificadas."},
    {"cat":"Jornada","q":"O prazo para usar o abono de ponto extingue-se em:","opts":["31/12 do ano aquisitivo","30/06 do ano seguinte","31/12 do ano seguinte","2 anos após o aquisitivo"],"a":2,"art":"Art. 151, §2º","tip":"31/12 do ANO SEGUINTE ao aquisitivo."},
    {"cat":"Férias","q":"As férias podem ser acumuladas em até quantos períodos?","opts":["1","2","3","4"],"a":1,"art":"Art. 125, §4º","tip":"Até 2 períodos, por necessidade do serviço."},
    {"cat":"Férias","q":"As férias podem ser parceladas em até quantos períodos?","opts":["2","3","4","5"],"a":1,"art":"Art. 125, §5º","tip":"Até 3 parcelas, nenhuma inferior a 10 dias."},
    {"cat":"Férias","q":"No parcelamento das férias, nenhum período pode ser inferior a:","opts":["5 dias","7 dias","10 dias","15 dias"],"a":2,"art":"Art. 125, §5º","tip":"Mínimo de 10 dias por parcela."},
    {"cat":"Faltas","q":"Configura abandono de cargo a ausência injustificada por mais de:","opts":["15 dias consecutivos","30 dias consecutivos","45 dias consecutivos","60 dias consecutivos"],"a":1,"art":"Art. 64, I","tip":"Abandono = +30 dias CONSECUTIVOS. Punição: demissão."},
    {"cat":"Faltas","q":"Configura inassiduidade habitual a ausência injustificada por mais de:","opts":["30 dias interpolados","45 dias interpolados","60 dias interpolados","90 dias interpolados"],"a":2,"art":"Art. 64, II","tip":"Inassiduidade = +60 dias INTERPOLADOS em 12 meses."},
    {"cat":"Faltas","q":"Casamento ou falecimento de familiar garante ao servidor quantos dias de ausência?","opts":["3 dias","5 dias úteis","8 dias consecutivos","15 dias"],"a":2,"art":"Art. 62, III","tip":"8 dias CONSECUTIVOS, incluído o dia do evento."},
    {"cat":"Faltas","q":"Alistamento eleitoral garante quantos dias de ausência justificada?","opts":["1 dia","2 dias","3 dias","5 dias"],"a":1,"art":"Art. 62, II","tip":"2 dias para alistamento ou transferência eleitoral."},
    {"cat":"Licenças","q":"A licença-maternidade para servidora efetiva tem duração de:","opts":["120 dias","150 dias","180 dias","240 dias"],"a":2,"art":"Art. 149-A","tip":"180 dias, antecipável em até 28 dias."},
    {"cat":"Licenças","q":"A licença-paternidade tem duração de:","opts":["5 dias","7 dias consecutivos","10 dias úteis","15 dias"],"a":1,"art":"Art. 150","tip":"7 dias CONSECUTIVOS, incluído o dia do nascimento."},
    {"cat":"Licenças","q":"A licença por doença em familiar pode ser concedida com remuneração por até:","opts":["90 dias/ano","120 dias/ano","180 dias/ano","365 dias/ano"],"a":2,"art":"Art. 134, §3º","tip":"Máximo 180 dias/ano com remuneração."},
    {"cat":"Licenças","q":"A licença para acompanhar cônjuge deslocado pode durar até:","opts":["1 ano","2 anos","3 anos","5 anos"],"a":3,"art":"Art. 133, §1º","tip":"Até 5 anos, sem remuneração."},
    {"cat":"Licenças","q":"A licença-servidor é devida a cada:","opts":["3 anos","4 anos","5 anos","10 anos"],"a":2,"art":"Art. 139","tip":"3 meses a cada 5 anos (quinquênio) de efetivo exercício."},
    {"cat":"Licenças","q":"A proteção contra exoneração de ofício da gestante comissionada vai até:","opts":["O nascimento","2 meses após o parto","5 meses após o parto","12 meses após o parto"],"a":2,"art":"Art. 53","tip":"5 MESES após o parto, inclusive para comissionadas."},
    {"cat":"Acumulação","q":"O prazo para apresentar opção na acumulação ilegal é:","opts":["5 dias","10 dias improrrogáveis","15 dias","30 dias"],"a":1,"art":"Art. 48","tip":"10 dias IMPRORROGÁVEIS da ciência da notificação."},
    {"cat":"Petição","q":"O prazo para recurso ou pedido de reconsideração é de:","opts":["15 dias","30 dias","60 dias","120 dias"],"a":1,"art":"Art. 172","tip":"Recurso e reconsideração = 30 dias."},
    {"cat":"Petição","q":"O direito de requerer prescreve em 5 anos nos casos de:","opts":["Demais casos em geral","Demissão e interesse patrimonial","Recursos administrativos","Apenas interesse patrimonial"],"a":1,"art":"Art. 175, I e II","tip":"5 anos: demissão, cassação e interesse patrimonial."},
    {"cat":"Petição","q":"Nos demais casos, o direito de requerer prescreve em:","opts":["30 dias","60 dias","90 dias","120 dias"],"a":3,"art":"Art. 175, III","tip":"120 dias para os demais casos."},
    {"cat":"Disciplinar","q":"O registro da advertência é cancelado após quantos anos sem nova infração?","opts":["1 ano","2 anos","3 anos","5 anos"],"a":2,"art":"Art. 201","tip":"Advertência: 3 anos. Suspensão: 5 anos."},
    {"cat":"Disciplinar","q":"O registro da suspensão é cancelado após quantos anos sem nova infração?","opts":["2 anos","3 anos","5 anos","7 anos"],"a":2,"art":"Art. 201","tip":"Suspensão: 5 anos. Advertência: 3 anos."},
    {"cat":"Disciplinar","q":"A prescrição disciplinar para demissão é de:","opts":["2 anos","3 anos","5 anos","10 anos"],"a":2,"art":"Art. 208, I","tip":"Demissão = 5 anos. Suspensão = 2 anos. Advertência = 1 ano."},
    {"cat":"Disciplinar","q":"A prescrição disciplinar para suspensão é de:","opts":["1 ano","2 anos","3 anos","5 anos"],"a":1,"art":"Art. 208, II","tip":"Suspensão = 2 anos."},
    {"cat":"Disciplinar","q":"A prescrição disciplinar para advertência é de:","opts":["6 meses","1 ano","2 anos","3 anos"],"a":1,"art":"Art. 208, III","tip":"Advertência = 1 ano."},
    {"cat":"Disciplinar","q":"O prazo da sindicância é de:","opts":["15 + 15 dias","30 + 30 dias","45 + 30 dias","60 + 60 dias"],"a":1,"art":"Art. 214, §2º","tip":"Sindicância: 30 + 30 dias."},
    {"cat":"Disciplinar","q":"O prazo do PAD é de:","opts":["30 + 30 dias","45 + 45 dias","60 + 60 dias","90 + 30 dias"],"a":2,"art":"Art. 217, §1º","tip":"PAD: 60 + 60 dias."},
    {"cat":"Disciplinar","q":"O afastamento preventivo tem duração máxima de:","opts":["30 dias improrrogáveis","30 + 30 dias","60 + 60 dias","90 dias improrrogáveis"],"a":2,"art":"Art. 222","tip":"60 + 60 dias, sem prejuízo de remuneração."},
    {"cat":"Disciplinar","q":"O prazo para defesa escrita no PAD com 1 acusado é de:","opts":["5 dias","10 dias","15 dias","20 dias"],"a":1,"art":"Art. 250","tip":"1 acusado: 10 dias. 2+ acusados: 20 dias."},
    {"cat":"Disciplinar","q":"O prazo para julgamento do PAD é de:","opts":["10 dias","20 dias dos autos","30 dias","60 dias"],"a":1,"art":"Art. 256","tip":"20 dias do recebimento dos autos."},
    {"cat":"Disciplinar","q":"A suspensão do Grupo I não pode ultrapassar:","opts":["15 dias","30 dias","60 dias","90 dias"],"a":1,"art":"Art. 200, §1º, I","tip":"Grupo I: até 30 dias. Grupo II: até 90 dias."},
    {"cat":"Remuneração","q":"O adicional de insalubridade no grau MÁXIMO é de:","opts":["10%","20%","30%","40%"],"a":3,"art":"Art. 88","tip":"Mínimo: 10%, Médio: 20%, Máximo: 40%."},
    {"cat":"Remuneração","q":"O adicional de periculosidade é de:","opts":["20%","25%","30%","40%"],"a":2,"art":"Art. 89","tip":"Periculosidade = 30%."},
]

CATS = sorted(set(q["cat"] for q in QUESTOES))

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #0d1117; color: #e6edf3; font-family: 'Segoe UI', sans-serif; min-height: 100vh; display: flex; flex-direction: column; align-items: center; padding: 20px; }
h1 { font-size: 1.4rem; color: #d29922; margin-bottom: 4px; }
.sub { color: #8b949e; font-size: .85rem; margin-bottom: 16px; text-align: center; }
.controls { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; justify-content: center; }
.controls label { background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 5px 10px; font-size: .78rem; cursor: pointer; display: flex; align-items: center; gap: 5px; }
.controls label:hover { border-color: #d29922; }
.controls input[type=checkbox] { accent-color: #d29922; }
.btn-start { background: #9e6a03; color: #fff; border: none; border-radius: 8px; padding: 10px 28px; font-size: 1rem; cursor: pointer; }
.btn-start:hover { background: #d29922; }
#game { display: none; width: 100%; max-width: 640px; }
.hud { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
.vidas { font-size: 1.4rem; letter-spacing: 4px; }
.record-txt { font-size: .78rem; color: #8b949e; }
#num-badge { background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 4px 10px; font-size: .8rem; }
.timer-wrap { height: 6px; background: #21262d; border-radius: 3px; margin-bottom: 14px; overflow: hidden; }
#timer-bar { height: 6px; border-radius: 3px; background: #d29922; transition: width 1s linear, background .5s; }
.card { background: #161b22; border: 2px solid #30363d; border-radius: 12px; padding: 22px; margin-bottom: 14px; transition: border-color .2s, background .2s; }
.card.flash-ok { border-color: #3fb950; background: rgba(63,185,80,.12); }
.card.flash-nok { border-color: #f85149; background: rgba(248,81,73,.12); }
.card.show-answer { border-color: #f85149; }
.cat-tag { font-size: .72rem; color: #8b949e; text-transform: uppercase; letter-spacing: .5px; margin-bottom: 8px; }
.question { font-size: 1rem; line-height: 1.6; }
.opts { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 16px; }
.opt { background: #0d1117; border: 2px solid #30363d; border-radius: 8px; padding: 12px; text-align: center; font-size: 1rem; font-weight: 700; cursor: pointer; transition: .12s; }
.opt:hover:not(:disabled) { border-color: #d29922; color: #d29922; }
.opt.correct { border-color: #3fb950; background: rgba(63,185,80,.15); color: #3fb950; }
.opt.wrong { border-color: #f85149; background: rgba(248,81,73,.15); color: #f85149; }
.opt:disabled { cursor: default; }
.feedback { margin-top: 10px; padding: 10px 12px; border-radius: 8px; font-size: .88rem; display: none; }
.feedback.show { display: block; background: rgba(248,81,73,.1); border: 1px solid #f85149; color: #f85149; }
.art-ref { font-size: .78rem; opacity: .8; margin-bottom: 3px; }
#result { display: none; text-align: center; padding: 30px; max-width: 640px; width: 100%; }
#result h2 { font-size: 1.6rem; margin-bottom: 6px; }
.score-big { font-size: 3.5rem; font-weight: 700; color: #d29922; margin: 10px 0; }
.score-label { color: #8b949e; margin-bottom: 8px; }
.record-badge { background: rgba(210,153,34,.15); border: 1px solid #d29922; color: #d29922; border-radius: 8px; padding: 8px 16px; font-size: .88rem; margin-bottom: 20px; display: inline-block; }
.btn-retry { background: #9e6a03; color: #fff; border: none; border-radius: 8px; padding: 12px 28px; font-size: .95rem; cursor: pointer; }
.btn-retry:hover { background: #d29922; }
"""

JS = r"""
const QUESTOES = __QUESTOES__;
const RECORD_KEY = 'survival_lc840_record';
let deck=[], idx=0, vidas=3, pontos=0, timer=null, secs=20, aguardando=false;

function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function getSelected(){return [...document.querySelectorAll('.controls input:checked')].map(i=>i.value);}
function getRecord(){return parseInt(localStorage.getItem(RECORD_KEY)||'0');}
function setRecord(n){localStorage.setItem(RECORD_KEY,n);}

function startGame(){
  const sel=getSelected();
  deck=shuffle(QUESTOES.filter(q=>sel.includes(q.cat)));
  if(!deck.length){alert('Selecione ao menos uma categoria!');return;}
  idx=0;vidas=3;pontos=0;aguardando=false;
  document.getElementById('setup').style.display='none';
  document.getElementById('game').style.display='block';
  document.getElementById('result').style.display='none';
  updateRecord();
  nextQ();
}

function updateRecord(){
  document.getElementById('rec-txt').textContent='Recorde: '+getRecord();
}

function renderVidas(){
  document.getElementById('vidas').textContent='❤️'.repeat(vidas)+'🖤'.repeat(3-vidas);
}

function nextQ(){
  if(idx>=deck.length) deck=shuffle([...QUESTOES.filter(q=>{const sel=getSelected();return sel.includes(q.cat);})]);
  aguardando=false;
  const q=deck[idx%deck.length];
  renderVidas();
  document.getElementById('num-badge').textContent='Q'+pontos;
  document.querySelector('.cat-tag').textContent=q.cat;
  document.querySelector('.question').textContent=q.q;
  const optsDiv=document.querySelector('.opts');
  optsDiv.innerHTML='';
  q.opts.forEach((o,i)=>{
    const b=document.createElement('button');
    b.className='opt'; b.textContent=o;
    b.onclick=()=>answer(i,q);
    optsDiv.appendChild(b);
  });
  document.querySelector('.card').className='card';
  document.querySelector('.feedback').className='feedback';
  startTimer(q);
}

function startTimer(q){
  clearInterval(timer);
  secs=20;
  const bar=document.getElementById('timer-bar');
  bar.style.transition='none'; bar.style.width='100%';
  bar.style.background='#d29922';
  setTimeout(()=>{ bar.style.transition='width 1s linear, background .5s'; bar.style.width='0%'; },30);
  timer=setInterval(()=>{
    secs--;
    const pct=secs/20*100;
    if(pct<40) bar.style.background='#e3b341';
    if(pct<20) bar.style.background='#f85149';
    if(secs<=0){clearInterval(timer);timeout(q);}
  },1000);
}

function timeout(q){
  perdeuVida(q);
}

function answer(i,q){
  if(aguardando) return;
  clearInterval(timer);
  const btns=document.querySelectorAll('.opt');
  btns.forEach(b=>b.disabled=true);
  const ok=(i===q.a);
  btns[i].classList.add(ok?'correct':'wrong');
  if(!ok) btns[q.a].classList.add('correct');
  if(ok){ pontos++; flashOk(); }
  else { btns[q.a].classList.add('correct'); perdeuVida(q); }
}

function flashOk(){
  aguardando=true;
  document.querySelector('.card').classList.add('flash-ok');
  setTimeout(()=>{idx++;nextQ();},350);
}

function perdeuVida(q){
  aguardando=true;
  vidas--;
  renderVidas();
  const fb=document.querySelector('.feedback');
  fb.innerHTML=`<div class="art-ref">${q.art}</div><div>${q.tip}</div>`;
  fb.className='feedback show';
  document.querySelector('.card').classList.add('flash-nok');
  if(vidas<=0){
    setTimeout(()=>showResult(),1800);
  } else {
    setTimeout(()=>{idx++;nextQ();},1800);
  }
}

function showResult(){
  document.getElementById('game').style.display='none';
  const res=document.getElementById('result');
  res.style.display='block';
  const rec=getRecord();
  const novoRec=pontos>rec;
  if(novoRec) setRecord(pontos);
  res.querySelector('h2').textContent=pontos>=20?'Impressionante! 🔥':pontos>=10?'Boa sequência! 💪':'Continue treinando! 📚';
  res.querySelector('.score-big').textContent=pontos;
  res.querySelector('.score-label').textContent='questões respondidas corretamente';
  const badge=document.getElementById('record-badge');
  if(novoRec && pontos>0){
    badge.textContent='🏆 Novo recorde! Antes: '+rec;
  } else {
    badge.textContent='Recorde atual: '+(novoRec?pontos:rec);
  }
}

function retryAll(){
  document.getElementById('result').style.display='none';
  document.getElementById('setup').style.display='block';
}
"""

def build_html():
    cats_checkboxes = "\n    ".join(
        f'<label><input type="checkbox" value="{c}" checked> {c}</label>'
        for c in CATS
    )
    js = JS.replace("__QUESTOES__", json.dumps(QUESTOES, ensure_ascii=False))
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Modo Sobrevivência — LC 840/2011</title>
<style>{CSS}</style>
</head>
<body>
<h1>💀 Modo Sobrevivência</h1>
<p class="sub">LC 840/2011 — 3 vidas • Timer 20s • Quantas questões você aguenta?</p>
<div id="setup" style="width:100%;max-width:640px">
  <p style="color:#8b949e;font-size:.82rem;margin-bottom:8px;text-align:center">Categorias:</p>
  <div class="controls">{cats_checkboxes}</div>
  <div style="text-align:center"><button class="btn-start" onclick="startGame()">💀 Iniciar</button></div>
</div>
<div id="game">
  <div class="hud">
    <div class="vidas" id="vidas">❤️❤️❤️</div>
    <span id="num-badge">Q0</span>
    <span class="record-txt" id="rec-txt">Recorde: 0</span>
  </div>
  <div class="timer-wrap"><div id="timer-bar" style="width:100%"></div></div>
  <div class="card">
    <div class="cat-tag"></div>
    <div class="question"></div>
    <div class="opts"></div>
    <div class="feedback"></div>
  </div>
</div>
<div id="result">
  <h2></h2>
  <div class="score-big"></div>
  <div class="score-label"></div>
  <div class="record-badge" id="record-badge"></div>
  <br>
  <button class="btn-retry" onclick="retryAll()">↩ Tentar novamente</button>
</div>
<script>{js}</script>
</body>
</html>"""

html = build_html()
with open(r"c:\Users\hacke\OneDrive - unb.br\estudo\survival_lc840.html","w",encoding="utf-8") as f:
    f.write(html)
print(f"Criado! survival_lc840.html — {len(QUESTOES)} questões, {len(html)//1024}KB")
