import { chromium } from 'playwright';
import fs from 'fs';
const jobs = JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const S=+(process.argv[3]||1200);
const browser = await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const page = await browser.newPage({viewport:{width:S,height:S}});
page.on('pageerror', e=>console.log('pageerror:',e.message));
await page.goto('http://localhost:8765/web/robi.html?s='+S);
await page.waitForFunction(()=>window.ready===true,null,{timeout:60000});
const meta={};
for (const j of jobs){ const r=await page.evaluate(o=>window.renderRobi(o), j.o); fs.writeFileSync(j.out, Buffer.from(r.png.split(',')[1],'base64')); meta[j.out]=r.anchors; console.log('ok',j.out); }
fs.writeFileSync(process.argv[4]||'out/robi_meta.json', JSON.stringify(meta,null,1));
await browser.close();
