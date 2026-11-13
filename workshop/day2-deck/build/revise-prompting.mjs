const C={navy:'#17213D',muted:'#4B5470',teal:'#0F766E',purple:'#7B4DFF',orange:'#C9530A',white:'#FFFFFF',green:'#DFF3E6'};
import { fileURLToPath } from 'node:url';
const ASSETS=fileURLToPath(new URL('../assets/', import.meta.url)).replace(/\/$/, '');
const SOURCE='Prompting background: https://developers.openai.com/api/docs/guides/prompt-engineering and https://www.anthropic.com/ai-fluency/deep-dive-2-effective-prompting-techniques . These support clear tasks, relevant context, output requirements, examples and iterative refinement. The classroom wording and examples are adapted for this workshop.';
const SETUP='Two groups of about five. Free DeepSeek on a facilitator-signed-in laptop; Kimi, Gemini or ChatGPT are backups. Learners never create accounts or enter personal information. A clearer prompt helps steer an answer but does not guarantee truth. Use the prepared examples if internet access fails. Printed instruction support: UP partner may adapt the English/Filipino wording to local usage.';
function get(s,n){const x=s.shapes.items.find(x=>x.name===n);if(!x)throw Error(`Missing ${n}`);return x;}
function set(s,n,t){get(s,n).text=t;}
function pos(s,n,x,y,w,h){get(s,n).position={left:x,top:y,width:w,height:h};}
function style(s,n,v){get(s,n).text.style=v;}
function addText(s,n,t,x,y,w,h,size=28,color=C.navy,bold=false,font='Lexend'){
 return s.shapes.add({name:n,geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0},text:{text:t,style:{typeface:font,fontSize:size,color,bold,insets:0,autoFit:'none',wrap:'square'}}});
}
function bubble(s,n,x,y,w,h,fill){const b=s.shapes.add({name:n,geometry:'roundRect',position:{left:x,top:y,width:w,height:h},fill,line:{fill:'none',width:0},borderRadius:18});b.sendToBack();}
function note(s,t,body){s.speakerNotes.text=`BILLY — DAY 2. ${t}\n\n${body}\n\n${SETUP}\n\n${SOURCE}`;}

export async function reviseCore({presentation}){
 if(presentation.slides.items.length!==12)throw Error('Expected the inspected 12-slide first draft.');
 const [s1,s2,s3,s4,s5,s6]=presentation.slides.items;
 set(s1,'subtitle','How can we help AI make\nthe answer we need?');
 note(s1,'1 minute. Prompt block, minutes 0–1.',`Start after Payton’s bias lesson. Say: You helped AI make fairer pictures. Today we will tell AI what we need, show it an example, and keep the conversation going. Ask: If an answer does not help, what could you tell AI? Accept two quick ideas. This is an invitation, not a long AI recap. Slides 1–8 total 20 minutes. Slides 9–14 are Billy’s separate 20-minute flashcard design block, later in the day.`);
 note(s2,'2 minutes. Prompt block, minutes 1–3.',`Compare the two volcano prompts on screen. Ask: What does Prompt 2 tell AI that Prompt 1 leaves out? Expected answers: who will read it and how long it should be. Invite one learner to identify a difficult word in the first example answer. Explain that Grade 1 is a reader choice, not a special magic phrase. Different jobs need different readers and formats.\n\nDemonstrate the two prompts in separate fresh DeepSeek chats to avoid carrying the first answer into the comparison. Keep waiting time below about 45 seconds combined. The displayed answers are prepared teaching examples, not recorded live outputs, so actual replies may differ. In the follow-up activity, learners will deliberately stay in one chat instead.\n\nScience sources: https://pubs.usgs.gov/gip/volc/nature.html and https://spaceplace.nasa.gov/volcanoes2/en/ . A volcano can mean an opening or vent releasing molten rock and gases. The simple answer is a paraphrase. Do not call volcanic ash ordinary smoke.`);
 set(s3,'title','What does AI need to know?');
 const labels=['THE TASK','THE PURPOSE','THE READER','THE FORMAT'];
 const values=['Explain what a volcano is','For our science flashcard','For a Grade 1 child','A short title and one sentence'];
 for(let i=0;i<4;i++){set(s3,`label-${i}`,labels[i]);set(s3,`value-${i}`,values[i]);pos(s3,`label-${i}`,68,190+i*91,205,38);pos(s3,`value-${i}`,289,187+i*91,610,65);style(s3,`value-${i}`,{fontSize:30});}
 s3.images.items[0].position={left:933,top:240,width:280,height:300};
 set(s3,'takeaway','You choose what you need. Then tell AI.');
 note(s3,'1 minute. Prompt block, minutes 3–4.',`Move beyond easier wording: a prompt can specify the task, why the answer is needed, its reader and the required format. Point to the four parts. Format means what the answer should look like, such as a list, a table, a title with one sentence, or a question and answer. Ask the class to choose the format for a flashcard.\n\nRead a combined example: Explain what a volcano is for our Grade 1 science flashcard. Give it a short title and one simple sentence. Compare this output request with the two-sentence answer on the previous slide. Children need only the details relevant to their task; they do not have to fill every label mechanically or write a long prompt. A role such as Act as a friendly teacher may help set tone, but it cannot replace a clear task or guarantee accuracy.\n\nScience source: https://pubs.usgs.gov/gip/volc/nature.html . The generated volcano is a simplified illustration, not a particular real volcano.`);
 set(s4,'step-1','Write a clear first prompt.');set(s4,'step-detail-1','What do you need? Who is it for?');
 set(s4,'step-detail-3','What fits? What needs to change?');
 set(s4,'takeaway','Everyone adds an idea. You have 4 minutes.');
 note(s4,'4 minutes. Prompt block, minutes 4–8.',`Each group chooses data, privacy or volcano and writes a prompt for a younger learner. Use the four-part recipe where helpful. Aim for about one minute to choose and plan, one minute to write, one minute for facilitator entry, and one minute to read the response. Assign a writer, a reader, a reporter and two idea helpers. Give each child a way to contribute.\n\nKeep the conversation open. Record Prompt 1 and one useful or unsuitable feature of the answer. Do not start the follow-up yet; the next two slides model how.\n\nEnglish instruction card: Choose a word. Write what you need. Read the answer together. Filipino support: Pumili ng salita. Isulat kung ano ang kailangan ninyo. Basahin nang sama-sama ang sagot.\n\nOffline fallback: provide a prepared answer with an unfamiliar word or an unsuitable length. Learners write a prompt for the answer they actually want. They can still practise follow-ups on paper. Use the checked definitions in the earlier draft: data means information such as pictures or numbers; privacy involves choosing what personal information to share and keeping some to yourself; a volcano is an opening through which hot melted rock, ash and gases can come out.`);
 // The existing activity slide becomes slide 7 after two teaching slides are inserted.
 set(s5,'title','What will you ask next?');
 set(s5,'intro','Stay in your chat. Choose what your answer needs.');
 const rows=[['A difficult word?','“What does ___ mean? Use easy words.”',C.purple],['Need an example?','“Give one example from school.”',C.teal],['Need a flashcard?','“Use a short title and one sentence.”',C.orange],['Like one part?','“Keep the example. Make the rest shorter.”',C.teal]];
 for(let i=0;i<3;i++){set(s5,`problem-${i}`,rows[i][0]);set(s5,`fix-${i}`,rows[i][1]);pos(s5,`problem-${i}`,68,246+i*88,330,58);pos(s5,`fix-${i}`,410,246+i*88,790,70);style(s5,`problem-${i}`,{fontSize:29,color:rows[i][2]});style(s5,`fix-${i}`,{fontSize:28});}
 addText(s5,'problem-3',rows[3][0],68,510,330,58,29,rows[3][2],true,'Fredoka');
 addText(s5,'fix-3',rows[3][1],410,510,790,70,28);
 set(s5,'takeaway','Try a follow-up. Compare the answers. Try another if it helps.');style(s5,'takeaway',{fontSize:27});
 note(s5,'6 minutes. Prompt block, minutes 12–18.',`This is practice time, not six minutes of teacher explanation. Learners continue the same chat they started on slide 4. First name one problem or a part worth keeping. Choose a follow-up that addresses it. Aim for one useful follow-up per group; groups that are ready can try a second, for example changing the explanation into a flashcard.\n\nSuggested pace: one minute identify the need; one minute write a follow-up; two minutes read and compare; two minutes try another useful change or explain why the first is enough. Learners may show AI an example from slide 5 as a follow-up. Do not demand random changes when the answer already works. A worse revision can be rejected.\n\nA good follow-up can ask about an unclear word, request an example, change the format, or preserve a useful part while changing another part. For a possible factual error, offer this additional starter: Our fact sheet says ___. Check your answer against it. Then check the actual source again; AI agreeing is not proof. Do not turn this into Raiyan’s full fact-checking lesson.\n\nRecord the original answer, the learner’s follow-up and the new answer. Assess the choice and comparison rather than a polished result alone. Filipino support: Ituloy ang usapan. Sabihin kung ano ang babaguhin. Ihambing ang mga sagot.`);
 set(s6,'share-sentence','We asked AI to __________\nbecause __________.');style(s6,'share-sentence',{fontSize:40});pos(s6,'share-sentence',68,208,820,150);
 set(s6,'share-question','What improved? What still needs checking?');style(s6,'share-question',{fontSize:29});pos(s6,'share-question',68,393,830,72);
 note(s6,'2 minutes. Prompt block, minutes 18–20.',`Each group’s reporter names a problem, reads the follow-up, and explains whether the result improved. Ask a learner to explain the chosen word without simply reading AI text. Success: each group uses at least one suitable prompting method or follow-up, produces an explanation for younger children, and can justify the change.\n\nRecap in the learners’ words: tell AI the task and useful background; say what the answer should look like; show an example when helpful; continue the same chat to ask or change something. The second answer is not automatically better, and a clear answer can still be wrong. Link to the Monster/Guide theme: we guide AI by reading, checking and making choices.\n\nHANDOVER: After this slide, the combined Day 2 deck has the 10-minute break, Raiyan’s Fact-Check Detectives, Yelina’s privacy activity, Payton’s Flashcard Studio 1, and the second break. Billy’s Flashcard Studio 2 starts at slide 9 of this personal deck. Do not teach the two Billy blocks back-to-back.`);
 return{count:presentation.slides.items.length,updated:'Prompt content and timing'};
}

export async function addExample({presentation}){
 if(presentation.slides.items.length!==12)throw Error('Expected 12 slides before the example slide.');
 const s=presentation.slides.addCopy(presentation.slides.getItem(1).copy());
 set(s,'title','An example shows AI what you want');set(s,'page','05');
 pos(s,'first-example',64,190,420,390);pos(s,'clearer-example',508,190,708,390);
 set(s,'first-label','GIVE AI THIS EXAMPLE');pos(s,'first-label',88,211,340,28);
 set(s,'first-prompt','Keep it private');pos(s,'first-prompt',88,258,365,60);style(s,'first-prompt',{fontSize:36});
 set(s,'first-answer','Never share your password.');pos(s,'first-answer',88,487,365,76);style(s,'first-answer',{fontSize:30,color:C.navy});
 s.images.add({path:`${ASSETS}/privacy_card.png`,position:{left:191,top:329,width:163,height:149},fit:'contain',alt:'The same privacy picture helps learners recognise the flashcard example.'});
 set(s,'second-label','THEN ADD THIS REQUEST');pos(s,'second-label',532,211,640,28);
 set(s,'second-prompt','“Use this pattern. Write a tip\nabout checking AI answers.”');pos(s,'second-prompt',532,257,650,100);style(s,'second-prompt',{fontSize:30});
 addText(s,'possible-answer','POSSIBLE ANSWER',532,382,640,28,20,C.teal,true);
 set(s,'second-answer','Check it first\nUse a book and ask a teacher\nto check AI’s answer.');pos(s,'second-answer',532,423,650,132);style(s,'second-answer',{fontSize:31,color:C.navy});
 set(s,'example-label','Teaching example');set(s,'takeaway','Send the example and your request together.');
 note(s,'2 minutes. Prompt block, minutes 8–10.',`Show the privacy card as a model, then read the new prompt. Paste the example title and sentence before the new request in the same chat message. Explain that AI needs the example supplied in the chat; it cannot see the classroom slide automatically. Ask: What should stay the same in the next card? Take predictions before pointing to the possible answer. Expected: short title plus one sentence. The topic changes from privacy to checking AI answers. An example helps communicate a pattern, tone or format; children should not copy old facts into the new topic.\n\nRead the possible answer aloud. Let a learner identify the title and the sentence. Ask whether it follows the pattern. This demonstrates example-based prompting without teaching technical terms such as one-shot or few-shot. Learners can later paste or write a small example in their own chat. The displayed answer is prepared, not a guaranteed live output.\n\nThe reused privacy illustration is intentional teaching continuity. It shows the same card that appears in the flashcard design section. A useful optional follow-up is: Use the same title-and-sentence pattern for my explanation.`);
 return{count:presentation.slides.items.length,added:'Example-based prompting'};
}

export async function addConversation({presentation}){
 if(presentation.slides.items.length!==13)throw Error('Expected 13 slides before the conversation slide.');
 // Copy the established text-row activity family and adapt its six principal text areas.
 const s=presentation.slides.addCopy(presentation.slides.getItem(4).copy());
 set(s,'title','A follow-up keeps the chat going');set(s,'action','WATCH');set(s,'page','06');
 set(s,'intro','A follow-up is your next message in the same chat.');pos(s,'intro',68,174,1148,44);style(s,'intro',{fontSize:27});
 const extras=(await presentation.inspect({select:'$.slides[13].elements[*]',include:['id','name']})).records.filter(x=>['problem-3','fix-3'].includes(x.name));
 presentation.delete(extras.map(x=>x.id));
 addText(s,'you-label','YOU',88,222,500,27,19,C.purple,true);
 addText(s,'ai-label','AI  /  EXAMPLE REPLIES',664,222,500,27,19,C.teal,true);
 const ys=[257,364,471],hs=[95,95,129];
 const questions=['Explain what a volcano is.','What does “molten” mean?\nUse easy words.','Now make a flashcard:\na title and one short sentence.'];
 const replies=['A volcano is an opening where molten rock, ash and gases can come out.','“Molten” means melted by heat.','Volcano\nHot melted rock, ash and gases\ncan come out of a volcano.'];
 for(let i=0;i<3;i++){
  bubble(s,`question-box-${i}`,64,ys[i],552,hs[i],C.white);bubble(s,`reply-box-${i}`,640,ys[i],576,hs[i],C.green);
  set(s,`problem-${i}`,questions[i]);pos(s,`problem-${i}`,88,ys[i]+12,504,hs[i]-20);style(s,`problem-${i}`,{typeface:'Lexend',fontSize:27,bold:false,color:C.navy});
  set(s,`fix-${i}`,replies[i]);pos(s,`fix-${i}`,664,ys[i]+12,528,hs[i]-20);style(s,`fix-${i}`,{typeface:'Lexend',fontSize:27,bold:false,color:C.navy});
 }
 set(s,'takeaway','Each new message tells AI what you need next.');style(s,'takeaway',{fontSize:28});
 note(s,'2 minutes. Prompt block, minutes 10–12.',`Walk through the chat from top to bottom. Read the first user message and its reply. Ask: Which word might a younger child not understand? Then show how the next message asks specifically about molten. Read the clarification, then the final request to turn the explanation into a flashcard. Use pointing or presentation highlighting to keep attention on one exchange at a time.\n\nDefine a follow-up: the next question or instruction in the same conversation. The earlier messages help provide context, so children can refer to a word or example already there. They should say exactly which part they mean. They do not have to restart the chat or repeat every instruction. This is conversation context, not a promise that the AI remembers forever or across new chats.\n\nDistinguish the purposes: the second user turn clarifies a word; the third changes the output format. Neither assumes the first answer is entirely wrong. These are authored example replies, not a transcript of a tested product. If showing DeepSeek live, keep one chat open for the full sequence.\n\nMolten means melted by heat. Volcano context: https://pubs.usgs.gov/gip/volc/nature.html . The final card gives one simple fact, while the earlier explanation supplies its meaning. Check factual content independently.`);
 return{count:presentation.slides.items.length,added:'Follow-up conversation'};
}

export async function orderAndCheck({presentation}){
 if(presentation.slides.items.length!==14)throw Error('Expected 14 slides before ordering.');
 const ids=(await presentation.inspect({select:'$.slides[*]',include:['id']})).records.map(x=>x.id);
 presentation.slides.reorder([...ids.slice(0,4),ids[12],ids[13],...ids.slice(4,12)]);
 presentation.slides.items.forEach((s,i)=>{const page=s.shapes.items.find(x=>x.name==='page');if(page)page.text=String(i+1).padStart(2,'0');});
 const s9=presentation.slides.getItem(8);
 s9.speakerNotes.text=String(s9.speakerNotes.text).replace('Slides 7–12 total 20 minutes.','Slides 9–14 total 20 minutes.');
 const timings=[1,2,1,4,2,2,6,2];
 if(timings.reduce((a,b)=>a+b,0)!==20)throw Error('Prompt block timing mismatch.');
 return{slides:14,promptMinutes:20,designMinutes:20,order:presentation.slides.items.map((s,i)=>({slide:i+1,title:s.shapes.items.find(x=>x.name==='title')?.text.toString()}))};
}
