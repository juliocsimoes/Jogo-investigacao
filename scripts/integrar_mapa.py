from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='/* NYC_MAP_INTEGRATION_V1 */'
if marker in s:
    print('Mapa ja integrado')
else:
    anchor='window.__test={};'
    assert anchor in s, 'Ponto de integracao nao encontrado: abortar sem alterar o jogo'
    code=r"""
/* NYC_MAP_INTEGRATION_V1 */
(function(){
  const btn=document.getElementById('carMap');
  if(!btn)return;
  btn.onclick=function(){
    let panel=document.getElementById('nycMapPanel');
    if(!panel){
      panel=document.createElement('div');
      panel.id='nycMapPanel';
      panel.setAttribute('role','dialog');
      panel.setAttribute('aria-modal','true');
      panel.setAttribute('aria-label','Mapa de Nova Iorque, 1992');
      panel.style.cssText='position:absolute;inset:2.5%;z-index:100;display:flex;flex-direction:column;background:#201e19;border:3px solid #d4c49a;box-shadow:0 12px 60px #000d;overflow:hidden';
      const bar=document.createElement('div');
      bar.style.cssText='display:flex;justify-content:space-between;align-items:center;background:#2a2b27;color:#e9dcb8;padding:6px 10px;font:12px monospace;letter-spacing:1px;min-height:38px';
      const title=document.createElement('span');title.textContent='NYPD • MAPA DE SERVIÇO • 1992';
      const close=document.createElement('button');close.textContent='✕ FECHAR';close.setAttribute('aria-label','Fechar mapa');close.style.cssText='padding:7px 12px;background:#d6c7a4;color:#28251d;border:0;font:bold 12px monospace;cursor:pointer';
      const frame=document.createElement('iframe');frame.src='mapa.html';frame.title='Mapa interativo de Nova Iorque';frame.style.cssText='width:100%;flex:1;border:0;background:#cbbd91';
      bar.append(title,close);panel.append(bar,frame);document.getElementById('stage').append(panel);
      close.onclick=()=>{panel.style.display='none';btn.focus({preventScroll:true})};
      document.addEventListener('keydown',e=>{if(e.key==='Escape'&&panel.style.display!=='none'){panel.style.display='none';btn.focus({preventScroll:true})}});
    }
    panel.style.display='flex';
    panel.querySelector('button').focus({preventScroll:true});
    if(typeof SND!=='undefined'&&SND.rustle&&typeof AC!=='undefined'&&AC&&sfxOn)SND.rustle();
  };
})();
"""
    s=s.replace(anchor,code+'\n'+anchor,1)
    p.write_text(s,encoding='utf-8')
    print('Mapa integrado no index.html')
