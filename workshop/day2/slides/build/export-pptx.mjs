import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {Presentation, PresentationFile} from '@oai/artifact-tool';

const here=path.dirname(fileURLToPath(import.meta.url));
const proto=JSON.parse(await fs.readFile(path.join(here,'export-cache/presentation.json'),'utf8'));
const p=Presentation.load(proto);
// The cloud snapshot references hosted images. Embed the matching local originals.
const assets=path.resolve(here,'../assets');
const figures=path.resolve(here,'../../../day1/slides/build/figures');
const media=[['robi_explains.png'],[],['volcano.png'],['laptop_group.png'],['privacy_card.png'],[],[],['robi_guide.png'],['flashcard_team.png'],['robi_monster.png','privacy_card.png'],['robi_artist.png'],['football_card.png','privacy_card.png'],['robi_thinking.png'],['robi_buddy.png']];
for (let i=0;i<media.length;i++) {
 const images=p.slides.getItem(i).images.items;
 if(images.length!==media[i].length)throw Error(`Unexpected images on slide ${i+1}`);
 for(let j=0;j<images.length;j++){
  const name=media[i][j];
  const file=path.join(['robi_guide.png','robi_monster.png','robi_artist.png','robi_thinking.png','robi_buddy.png'].includes(name)?figures:assets,name);
  images[j].replace({blob:new Uint8Array(await fs.readFile(file)),contentType:'image/png'});
 }
}
await (await PresentationFile.exportPptx(p)).save(path.join(here,'export-cache/candidate.pptx'));
console.log('Exported',p.slides.items.length,'slides');
