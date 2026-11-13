import { fileURLToPath } from 'node:url';
const ROOT = fileURLToPath(new URL('../', import.meta.url)).replace(/\/$/, '');
const A = `${ROOT}/assets`;
const R = fileURLToPath(new URL('../../day1-deck/build/figures/', import.meta.url));
const C = {cream:'#FEF6E9',navy:'#17213D',muted:'#4B5470',teal:'#0F766E',green:'#178A50',purple:'#7B4DFF',orange:'#C9530A',yellow:'#FFC83A',blue:'#2F6BFF',coral:'#D93A25',white:'#FFFFFF',paleGreen:'#DFF3E6',palePurple:'#ECE5FF'};
function text(s,name,content,x,y,w,h,size=30,color=C.navy,font='Lexend',bold=false,align='left') {
  return s.shapes.add({name,geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0},text:{text:content,style:{typeface:font,fontSize:size,bold,color,alignment:align,verticalAlignment:'top',insets:0,autoFit:'none',wrap:'square'}}});
}
function box(s,name,x,y,w,h,fill=C.white,border='none',radius=20){
  return s.shapes.add({name,geometry:'roundRect',position:{left:x,top:y,width:w,height:h},fill,line:{fill:border,width:border==='none'?0:2},borderRadius:radius});
}
function img(s,file,x,y,w,h,alt){return s.images.add({path:file,position:{left:x,top:y,width:w,height:h},fit:'contain',alt});}
function base(p,num,title,action='TALK',part=1,bg=C.cream){
  const s=p.slides.add({width:1280,height:720});s.background.fill=bg;
  const accent=part===1?C.teal:C.orange;
  text(s,'section',part===1?'PROMPT POWER-UP':'FLASHCARD STUDIO',64,34,800,28,18,accent,'Lexend',true);
  text(s,'action',action,1070,34,146,30,19,accent,'Lexend',true,'right');
  text(s,'title',title,64,88,1152,82,48,C.navy,'Fredoka',true);
  text(s,'page',String(num).padStart(2,'0'),1160,675,56,24,16,C.muted,'Lexend',false,'right');
  return s;
}
function footer(s,content,color=C.teal){text(s,'takeaway',content,64,625,1100,45,28,color,'Fredoka',true);}
function step(s,n,title,body,y,x=68,w=680){
  text(s,`number-${n}`,String(n),x,y,45,52,40,C.teal,'Fredoka',true);
  text(s,`step-${n}`,title,x+66,y,w-66,48,31,C.navy,'Lexend',true);
  if(body)text(s,`step-detail-${n}`,body,x+66,y+47,w-66,54,24,C.muted);
}
function notes(s,timing,script){s.speakerNotes.text=`BILLY — DAY 2. ${timing}\n\n${script}\n\nTeaching setup: two groups of about five Primary 5–6 learners. Use facilitator-signed-in laptops and free tools only. Do not ask learners to create accounts or enter private information.\nVisuals: original illustrations generated with OpenAI image generation for this lesson, plus the established Day 1 Robi artwork. Images illustrate fictional classroom scenes. All slide wording remains editable.`;}

function slide2(p){
 const s=base(p,2,'Which answer helps a younger child?','WATCH');
 box(s,'first-example',64,190,552,390,C.white);
 box(s,'clearer-example',640,190,576,390,C.paleGreen);
 text(s,'first-label','PROMPT 1',88,211,250,28,20,C.purple,'Lexend',true);
 text(s,'first-prompt','“Tell me about volcanoes.”',88,255,496,82,31,C.navy,'Fredoka',true);
 text(s,'first-answer','Volcanoes are vents in Earth’s crust through which magma, volcanic gases and ash may reach the surface.',88,370,496,173,29,C.muted);
 text(s,'second-label','PROMPT 2',664,211,250,28,20,C.teal,'Lexend',true);
 text(s,'second-prompt','“Explain volcanoes for Grade 1.\nUse two short sentences.”',664,255,520,92,31,C.navy,'Fredoka',true);
 text(s,'second-answer','A volcano is an opening in the ground. Hot melted rock, ash and gases can come out.',664,370,510,173,31,C.navy);
 text(s,'example-label','Example answers',64,588,500,24,18,C.muted);
 footer(s,'Which words made a difference?');
 notes(s,'3 minutes. First block, minutes 1–4.',`Say: Here are two example answers. Which one could a younger child understand? Point to Prompt 1 and ask a learner to find a difficult word. Read Prompt 2 and ask what extra information it gives. Invite a show of hands, then one reason from each group. The learning point is audience and format, not that a longer prompt always gives a better or correct answer.\n\nLive demonstration: use free DeepSeek. Type each prompt in a new chat so the comparison is fair. Keep the combined live wait to about 45 seconds; use the prepared slide examples if the connection is slow. These slide answers are authored teaching examples, not recorded DeepSeek outputs. A live answer may differ.\n\nScience check: a volcano can refer to an opening or vent that releases molten rock and gases. Ash consists of small rock/glass fragments; do not call the plume ordinary smoke. The child-facing answer is a simplified paraphrase. Sources: https://pubs.usgs.gov/gip/volc/nature.html and https://spaceplace.nasa.gov/volcanoes2/en/ .`);
}
function slide3(p){
 const s=base(p,3,'Our recipe for a clear explanation','SAY');
 const rows=[['TOPIC','Volcanoes',C.purple],['TASK','Explain what a volcano is',C.blue],['READER','For a Grade 1 child',C.teal],['FORMAT','Two short sentences. Easy words.',C.orange]];
 rows.forEach((r,i)=>{const y=190+i*91;text(s,`label-${i}`,r[0],68,y,170,35,22,r[2],'Lexend',true);text(s,`value-${i}`,r[1],248,y-3,590,62,31,C.navy,'Fredoka',true);});
 img(s,`${A}/volcano.png`,900,205,310,330,'A simplified volcanic mountain with a crater, lava and a small pale plume.');
 footer(s,'A useful prompt tells AI what we need.');
 notes(s,'1 minute. First block, minutes 4–5.',`Connect to Day 1: Our picture recipe described who, doing what, where and style. Today our explanation recipe tells AI the topic, task, reader and format. Read the four example lines aloud with the class. Keep this explanation brief; the next slide starts group work. Combined prompt: Explain what a volcano is to a Grade 1 child. Use two short sentences and easy words. Explain any science word you need.\n\nThe generated volcano is a simplified illustration, not a scale model or a photograph of a particular volcano. It does not imply that all volcanoes have this shape or are currently erupting. Definition source: https://pubs.usgs.gov/gip/volc/nature.html .`);
}
function slide4(p){
 const s=base(p,4,'Your group’s first prompt','DO');
 text(s,'word-bank','Pick a word:  data   /   privacy   /   volcano',68,179,1100,48,30,C.teal,'Fredoka',true);
 step(s,1,'Write your first prompt.','Who will read the answer?',267,68,620);
 step(s,2,'Show your helper.','They will type it for your group.',374,68,620);
 step(s,3,'Read the answer together.','Point to a word that feels too difficult.',481,68,620);
 img(s,`${A}/laptop_group.png`,747,278,465,335,'Three learners plan a prompt together while an adult facilitator types on their shared laptop.');
 footer(s,'Everyone adds an idea.  You have 6 minutes.');
 notes(s,'6 minutes. First block, minutes 5–11.',`Give each group a paper prompt sheet. Assign a writer, two idea helpers, a reader and a reporter; combine roles if needed. Offer three words: data, privacy or volcano. One minute to choose the word, two minutes to write, one minute for facilitator entry, and two minutes to read/discuss. Ask the reader to explain the answer in their own words. Each learner should contribute, including shy learners who can point or whisper to a partner. The facilitator operates the signed-in laptop.\n\nPrompt sheet instruction in English: Choose a word. Write your prompt. Read the answer together. Filipino support: Pumili ng salita. Isulat ang inyong prompt. Basahin nang sama-sama ang sagot. Invite the UP partner to adapt wording to the learners’ everyday language.\n\nOffline fallback: each group chooses one prepared explanation from this slide deck’s notes and rewrites a prompt for it. Prepared examples: Data means information, such as pictures or numbers. Privacy means choosing what personal information to share and keeping some information to yourself. A volcano is an opening in the ground; hot melted rock, ash and gases can come out.`);
}
function slide5(p){
 const s=base(p,5,'One change can help','DO');
 text(s,'intro','What would make your answer easier to understand?',68,174,1100,62,29,C.muted);
 const rows=[['Too long?','“Use two short sentences.”',C.purple],['A difficult word?','“Explain that word with easy words.”',C.teal],['Still unclear?','“Give one example from school.”',C.orange]];
 rows.forEach((r,i)=>{const y=268+i*100;text(s,`problem-${i}`,r[0],68,y,340,45,31,r[2],'Fredoka',true);text(s,`fix-${i}`,r[1],410,y,780,56,30,C.navy);});
 footer(s,'Pick one change. Try again. Compare both answers.');
 notes(s,'7 minutes. First block, minutes 11–18.',`Leave this slide visible throughout the activity. Groups spend two minutes naming one problem in their first answer, one minute writing a follow-up or revised prompt, and up to two minutes reading the new answer. Use the final two minutes to compare. The three options are examples, not compulsory steps. If the first answer is already suitable, ask for one helpful school example and judge whether it improves understanding.\n\nAsk: Which version could a younger child explain back to us? What exactly changed? Do not reward length or praise alone. Record a before-and-after prompt pair and one reason per group. A good outcome is a simpler, accurate explanation after one improvement. If the new answer is worse, learners may keep the first one and explain why.\n\nFilipino support for the instruction card: Pumili ng isang babaguhin. Subukan muli. Ihambing ang dalawang sagot.`);
}
function slide6(p){
 const s=base(p,6,'What did your group change?','TALK');
 text(s,'share-sentence','We added __________\nbecause __________.',68,208,775,150,44,C.navy,'Fredoka',true);
 text(s,'share-question','Can a younger child explain it back?',68,393,750,65,31,C.teal,'Lexend',true);
 img(s,`${R}/robi_guide.png`,920,186,275,345,'Robi as a guide with a compass and a map.');
 box(s,'check-reminder',64,512,1152,110,C.navy);
 text(s,'check-line','A clear answer can still be wrong.',92,532,1090,52,35,C.yellow,'Fredoka',true);
 text(s,'next','After the break: Fact-Check Detectives',92,584,1040,28,21,C.white);
 notes(s,'2 minutes. First block, minutes 18–20.',`Invite each group’s reporter to complete the sentence. Listen for a specific change and reason, such as adding Grade 1 so the explanation uses easier words. Ask one learner to explain their group’s chosen word without reading the AI answer. Outcome: each group improves a prompt once and can identify a useful change.\n\nLink to the Monster/Guide theme: Copying an answer without thinking can create a Monster moment. We use AI as a Guide when we ask clearly, check and choose what to use. A clearer prompt does not guarantee truth. Say: After our 10-minute break, Raiyan will help us check AI answers.\n\nIMPORTANT RUN ORDER: Stop Billy’s first block here. The combined Day 2 deck must insert the break, Raiyan’s Fact-Check Detectives, Yelina’s privacy activity, Payton’s Flashcard Studio 1, and the second break before Billy’s next slide. Slide 7 is not the immediate next classroom activity.`);
}
function slide7(p){
 const s=base(p,7,'Our cards can help someone learn','LOOK',2);
 text(s,'purpose','Let’s make your ideas\neasy for a younger\nchild to read.',68,198,565,180,43,C.navy,'Fredoka',true);
 text(s,'goal','Your group’s goal:\n8–10 clear flashcards.',68,449,480,105,31,C.orange,'Lexend',true);
 img(s,`${A}/flashcard_team.png`,655,197,565,421,'Children make learning flashcards together with Robi.');
 notes(s,'1 minute. Second block, minutes 0–1.',`Start only after Payton’s Flashcard Studio 1 and the second break. Learners should arrive with checked text for 8–10 cards. Show the existing group text and say: You have the ideas. Now we will make them easy for a younger child to read.\n\nBefore class: prepare one Canva copy per group with ten card slots, consistent large title/picture/sentence areas, and numbered text placeholders. Coordinate with Payton to supply approved text in order; paste it into the template during the break. Target ten cards for a straightforward 3 knowledge / 3 applications / 4 ethics balance. At least eight completed designed cards is the proposal’s evaluation threshold. If a group has eight or nine, preserve the intended balance as closely as practical.\n\nOne facilitator operates each group’s laptop. Children choose the visual content, colours and wording. Billy moves between groups. Slides 7–12 total 20 minutes.`);
}
function slide8(p){
 const s=base(p,8,'Which card would you choose?','TALK',2);
 box(s,'card-a',64,186,540,390,'#F1D9EE','#D7BDD6',16);
 text(s,'a-label','A',87,203,60,45,31,C.purple,'Fredoka',true);
 text(s,'a-title','PERSONAL INFORMATION\nAND DIGITAL PRIVACY',155,218,405,90,29,'#704C71','Lexend',true);
 img(s,`${R}/robi_monster.png`,78,331,162,166,'A distracting robot on the deliberately cluttered practice card.');
 text(s,'a-sentence','Protect your personal information by avoiding the disclosure of your residential address and confidential passwords to online systems.',254,344,314,166,24,'#9F7A9E');
 text(s,'a-extra','READ!  THINK!  LEARN!',103,522,440,35,21,'#AB80A5','Lexend',true);
 box(s,'card-b',640,186,576,390,C.white,'#CFE4D9',16);
 text(s,'b-label','B',663,203,60,45,31,C.teal,'Fredoka',true);
 text(s,'b-title','Keep it private',733,217,440,55,40,C.navy,'Fredoka',true);
 img(s,`${A}/privacy_card.png`,835,283,173,176,'A child holds a closed box with a padlock, showing privacy.');
 text(s,'b-sentence','Keep your address and\npasswords private.',676,474,504,80,31,C.navy,'Lexend',false,'center');
 footer(s,'Large letters. Short sentences. Helpful pictures.',C.orange);
 notes(s,'2 minutes. Second block, minutes 1–3.',`Ask learners to vote A or B, then tell a partner why. Card A is intentionally difficult: long wording, weak contrast and a distracting picture. Card B keeps one idea, uses a short sentence, larger legible text and a relevant picture. Do not spend time asking children to read the difficult card in full. Point to each improvement only after learners notice it.\n\nClarify: Big words on the page means large letters, not difficult vocabulary. A clear card can still contain an error, so the words must already have been checked. This comparison is an authored teaching example, not a real learner’s work. Reusing the privacy illustration later is intentional so pupils can connect a card’s message to the matching picture.`);
}
function slide9(p){
 const s=base(p,9,'Two cards, two AI pictures','PLAN',2);
 text(s,'two','2',68,184,190,180,150,C.orange,'Fredoka',true);
 text(s,'two-meaning','AI pictures\nfor your group',270,224,560,117,43,C.navy,'Fredoka',true);
 text(s,'selection','Which two cards need a picture most?',68,399,760,56,31,C.navy,'Lexend',true);
 text(s,'rest','For the other cards, draw your own\nor choose a Canva picture.',68,480,775,100,30,C.muted);
 img(s,`${R}/robi_artist.png`,925,215,270,345,'Robi holds art supplies, ready to help make a picture.');
 footer(s,'Your ideas come first.',C.orange);
 notes(s,'2 minutes. Second block, minutes 3–5.',`Each group chooses exactly two key cards for AI illustrations. This is two pictures per group, not per learner. The rest use learners’ drawings or free Canva graphics. Two learners describe the chosen images, two draw or choose other images, and one reads the text and checks the matches; let roles rotate and let everyone approve the final deck.\n\nReuse Day 1’s WHO + DOING WHAT + WHERE + STYLE recipe. Picture prompt example: A child holding a closed box with a padlock, on a plain background, friendly cartoon style. No words or letters. Keep private information out. This is also a practical link to Yelina’s Energy Tokens; avoid repeating generations just for decoration. Do not assign a fixed real-world water or energy amount to a token.\n\nFree image tools: facilitator uses Gemini or ChatGPT according to availability. Have saved relevant pictures ready if image generation is slow.`);
}
function slide10(p){
 const s=base(p,10,'Does the picture match the message?','CHECK',2);
 text(s,'message','Our card says: “Keep it private.”',68,174,1100,55,34,C.orange,'Fredoka',true);
 img(s,`${A}/football_card.png`,154,262,260,300,'Option A: a child playing football.');
 img(s,`${A}/privacy_card.png`,667,262,300,300,'Option B: a child protects a closed box with a padlock.');
 text(s,'choice-a','A',115,271,45,45,31,C.purple,'Fredoka',true);
 text(s,'choice-b','B',630,271,45,45,31,C.teal,'Fredoka',true);
 text(s,'reason','Which picture fits?\nTell us why.',988,356,225,142,31,C.navy,'Fredoka',true);
 footer(s,'Now check your own pictures. Anything missing or strange?',C.orange);
 notes(s,'4 minutes. Second block, minutes 5–9.',`Spend about 45 seconds on the picture choice. Answer: B supports the privacy message. A is a perfectly good football picture, but it does not explain this card. Emphasise that a beautiful image can still be the wrong image for a message. Both are intentionally prepared practice pictures, not real outputs from the same prompt.\n\nThen facilitators generate the two chosen pictures per group. Children check that each picture matches the meaning, depicts people fairly and has no obvious mistakes such as extra fingers or confusing objects. Other children keep drawing or selecting free graphics while generation runs. If a picture fails, use a drawing or prepared suitable image rather than spending the whole session retrying.\n\nDisplay this slide during image work. No personal photos or information go into prompts. The AI image is a draft that people must check.`);
}
function slide11(p){
 const s=base(p,11,'Your flashcard studio','DO',2);
 step(s,1,'Match a picture to each idea.','AI pictures, your drawings or Canva pictures.',191,68,830);
 step(s,2,'Choose colours that are easy to read.','Dark words on a light background work well.',322,68,830);
 step(s,3,'Read every card aloud.','Keep the meaning. Fix any confusing words.',453,68,830);
 img(s,`${R}/robi_thinking.png`,955,266,241,305,'Robi thinks carefully while checking the group’s work.');
 footer(s,'Your helper puts the cards together.  You have 8 minutes.',C.orange);
 notes(s,'8 minutes. Second block, minutes 9–17.',`Leave this slide visible during the Canva assembly. This is making time rather than an extended software tutorial. The facilitator places checked text and learner-approved images into the pre-filled Canva template. Children choose colours and pictures, read aloud and request corrections.\n\nSuggested pace: first four minutes place pictures; next two minutes check size, colour and meaning; last two minutes read the completed deck and fix one issue. Keep the same simple layout throughout. Do not let decoration displace readability or fact checking. Protect the group’s original ideas.\n\nMinimum outcome: eight designed cards; target ten with the agreed content balance. Completion means title, relevant visual and readable checked sentence. If short on time, use prepared free graphics for unfinished image slots. Offline fallback: use the prepared paper card sheets, learners’ drawings and printed picture options; photograph or scan the completed set later.\n\nFilipino support for the instruction card: Itugma ang larawan sa ideya. Pumili ng mga kulay na madaling basahin. Basahin nang malakas ang bawat kard.`);
}
function slide12(p){
 const s=base(p,12,'Ready for another reader?','CHECK',2);
 const checks=['Can a younger child read it?','Does the picture match?','Have we checked the facts?'];
 checks.forEach((v,i)=>{text(s,`check-number-${i}`,String(i+1),68,206+i*105,55,55,43,C.teal,'Fredoka',true);text(s,`check-${i}`,v,145,214+i*105,800,65,36,C.navy,'Lexend',true);});
 img(s,`${R}/robi_buddy.png`,974,215,230,310,'Robi reads a book happily.');
 box(s,'handover',64,545,1152,101,C.navy);
 text(s,'next-title','Next: swap cards with another group',91,560,1080,45,34,C.yellow,'Fredoka',true);
 text(s,'feedback','Tell them one thing you like and one thing to improve.',91,610,1080,30,24,C.white);
 notes(s,'3 minutes. Second block, minutes 17–20.',`Use the first two minutes for a final check of every card. Count at least eight complete cards and verify the agreed content balance. Each learner reads at least one card or explains its picture. The facilitator records one learner design choice and one correction as evidence of learning, beyond the finished product.\n\nDuring the final minute, save the editable Canva copy and export a PDF for printing. Name files with a group nickname, not personal learner details. Confirm the file opens and is ready on screen for Yelina. Say: Another group will now try your cards. They will tell you one thing they like and one thing you could improve.\n\nThis slide hands over to Yelina’s 10-minute Flashcard TEST Swap. Do not conduct the full peer review inside Billy’s 20 minutes. The Day 2 whole-day recap, gallery, exit ticket and any Kahoot belong in the combined team deck, outside these two Billy blocks.`);
}

export async function buildBatch({presentation,input}){
 if(input.repairCover){
   if(presentation.slides.items.length===2 && presentation.slides.getItem(0).shapes.items.length===0 && presentation.slides.getItem(0).images.items.length===0) presentation.slides.delete(0);
   const s=presentation.slides.getItem(0);
   const q=s.shapes.items;
   for(const x of q)x.text.style={typeface:['title','invitation'].includes(x.name)?'Fredoka':'Lexend'};
   q.find(x=>x.name==='title').position={left:64,top:155,width:660,height:190};
   q.find(x=>x.name==='subtitle').position={left:67,top:389,width:590,height:100};
   const im=s.images.items[0];im.replace({path:`${A}/robi_explains.png`,alt:'Robi and a younger child share a picture book about a volcano.'});im.position={left:708,top:204,width:525,height:390};im.fit='contain';
 }
 const fns={2:slide2,3:slide3,4:slide4,5:slide5,6:slide6,7:slide7,8:slide8,9:slide9,10:slide10,11:slide11,12:slide12};
 for(const n of (input.slides||[])){if(presentation.slides.items.length!==n-1)throw new Error(`Expected ${n-1} slides before adding ${n}, found ${presentation.slides.items.length}`);fns[n](presentation);}
 return {slideCount:presentation.slides.items.length};
}
