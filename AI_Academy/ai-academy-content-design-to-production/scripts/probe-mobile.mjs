import { chromium } from 'playwright';
const br=await chromium.launch(); const p=await (await br.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();
for (let t=0;t<4;t++){ await p.goto(''+(process.env.BASE||'http://localhost:3100')+'/login',{waitUntil:'networkidle'}); await p.waitForTimeout(1500); await p.fill('input[placeholder^="Ví dụ"]',(process.env.APP_USER||'cmc001')); await p.fill('input[type=password]',(process.env.APP_PASS||'Password123!')); await p.keyboard.press('Enter'); try{await p.waitForURL(u=>!u.pathname.startsWith('/login'),{timeout:30000});break;}catch{} }
for (const [n,id] of JSON.parse(process.env.MODS||'[]')) {
  await p.goto(''+(process.env.BASE||'http://localhost:3100')+'/module/'+id,{waitUntil:'networkidle'}); await p.waitForTimeout(2000);
  const r=await p.evaluate(()=>({tables:[...document.querySelectorAll('table')].map(t=>{const w=t.parentElement;return w.scrollWidth>w.clientWidth+2?`OVER ${w.scrollWidth}/${w.clientWidth} cols=${t.rows[0].cells.length}`:'ok'}),img:[...document.querySelectorAll('main img')].map(i=>({w:i.getBoundingClientRect().width,nat:i.naturalWidth}))}));
  console.log(n,JSON.stringify(r));
  const img=p.locator('main img').first(); if(await img.count()){ await img.scrollIntoViewIfNeeded(); await img.screenshot({path:`evidence/${n}-svg-mobile-v2.png`}); }
}
await br.close();
