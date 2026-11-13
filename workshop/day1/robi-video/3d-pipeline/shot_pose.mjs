import { chromium } from 'playwright';
import fs from 'fs';
const jobs = JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const browser = await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const page = await browser.newPage({viewport:{width:+(process.argv[4]||1000),height:+(process.argv[4]||1000)}});
page.on('pageerror', e=>console.log('pageerror:',e.message));
page.on('console', m=>{ if(m.type()==='error') console.log('console:',m.text()); });
await page.goto('http://localhost:8765/web/'+(process.argv[3]||'hand.html')+'?s='+(process.argv[4]||1000));
await page.waitForFunction(()=>window.ready===true,null,{timeout:60000});
const meta={}; for (const j of jobs){ const r=await page.evaluate(o=>window.renderHand(o), j.o); const d=typeof r==='string'?r:r.png; fs.writeFileSync(j.out, Buffer.from(d.split(',')[1],'base64')); if(r.handBox) meta[j.out]=r.handBox; console.log('ok',j.out); }
if (process.argv[5]) fs.writeFileSync(process.argv[5], JSON.stringify(meta,null,1));
await browser.close();
