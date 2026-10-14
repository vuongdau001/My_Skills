import { chromium } from 'playwright';
import fs from 'fs';
const B=process.env.BASE||'http://localhost:3100', out=process.argv[2]||'evidence', tag=process.argv[3]||'';
const mods=JSON.parse(process.env.MODS||'[]'); // e.g. [["ref","testing-why-quality"],["1.1","ba-po-problem-vs-solution"]]
const USER=process.env.APP_USER||'cmc001', PASS=process.env.APP_PASS||'Password123!';
const vps={desktop:{width:1440,height:900},mobile:{width:390,height:844}};
const report={};
const br=await chromium.launch();
for (const [vn,vp] of Object.entries(vps)) {
  const ctx=await br.newContext({viewport:vp, deviceScaleFactor: vn==='mobile'?2:1});
  const p=await ctx.newPage(); const errs=[];
  p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,200))});
  for (let t=0;t<4;t++){ await p.goto(B+'/login',{waitUntil:'networkidle'}); await p.waitForTimeout(1500); await p.fill('input[placeholder^="Ví dụ"]',USER); await p.fill('input[type=password]',PASS); await p.keyboard.press('Enter'); try{await p.waitForURL(u=>!u.pathname.startsWith('/login'),{timeout:30000});break;}catch{} }
  for (const [n,id] of mods) {
    errs.length=0;
    await p.goto(`${B}/module/${id}`,{waitUntil:'networkidle',timeout:120000}); await p.waitForTimeout(2500);
    const stats=await p.evaluate(()=>{const a=document.querySelector('article, .prose')||document.body;return {chars:a.innerText.length,h2:a.querySelectorAll('h2').length,h3:a.querySelectorAll('h3').length,tables:a.querySelectorAll('table').length,mermaidSvg:a.querySelectorAll('svg[id^=mermaid], .mermaid svg').length,codeMermaidRaw:[...a.querySelectorAll('code')].filter(c=>/flowchart|graph |sequenceDiagram/.test(c.innerText)).length,imgs:a.querySelectorAll('img').length,brokenImgs:[...a.querySelectorAll('img')].filter(i=>!i.naturalWidth).length,overflowX:document.documentElement.scrollWidth>window.innerWidth,rawMd:(a.innerText.match(/\*\*|\[\[|<!--|\]\(/g)||[]).length}});
    await p.screenshot({path:`${out}/${n}-theory-${vn}${tag}.png`,fullPage:true});
    const done=p.locator('[data-testid=theory-read-done]'); if(await done.count()){await done.click(); await p.waitForTimeout(1500);}
    const sp=p.locator('[data-testid=start-practice]'); if(await sp.count()) await sp.click();
    await p.waitForTimeout(4000);
    await p.screenshot({path:`${out}/${n}-quiz-${vn}${tag}.png`,fullPage:true});
    report[`${n}-${vn}`]={...stats,consoleErrors:[...errs]};
  }
  await ctx.close();
}
await br.close(); fs.writeFileSync(`${out}/stats${tag}.json`,JSON.stringify(report,null,1)); console.log(JSON.stringify(report));
