# Teaching Guide - Laboratory 1: Context of Use Analysis

## 📋 Laboratory Technical Sheet

| Aspect | Detail |
|---------|---------|
| **Laboratory Name** | Context of Use Analysis - Tourism Booking Platform |
| **Applied ISO Standard** | ISO 9241-11:2018 - Ergonomics of human-system interaction - Part 11: Usability: Definitions and concepts |
| **Total Duration** | 8-9 hours (3h preparation + 2h in-person + 3-4h final work) |
| **Modality** | Hybrid (autonomous preparation + in-person session + final deliverable) |
| **Complexity Level** | ⭐⭐⭐ Medium |
| **Team Size** | 2-3 students |
| **Prerequisites** | None (this is the first laboratory) |
| **Assumed Knowledge** | Basic use of web browsers, word processors, generative AI |

---

## 🎯 Learning Objectives (Bloom's Taxonomy)

Upon completion of this laboratory, students will be able to:

### Level 1 - Remember
- **Define** the three components of usability according to ISO 9241-11: effectiveness, efficiency, and satisfaction
- **Identify** the elements that make up the context of use: users, tasks, equipment, and environment

### Level 2 - Understand
- **Explain** the difference between effectiveness, efficiency, and satisfaction with concrete examples
- **Interpret** how the context of use affects the usability requirements of a system

### Level 3 - Apply
- **Implement** a context of use analysis following the ISO 9241-11 methodology
- **Use** generative AI tools to create personas and usage scenarios

### Level 4 - Analyze
- **Distinguish** between different user profiles and their specific needs
- **Examine** how tasks, equipment, and environments vary according to user type

### Level 5 - Evaluate
- **Judge** the quality and completeness of a context of use analysis
- **Validate** whether the defined usability metrics are appropriate for each context

### Level 6 - Create
- **Design** detailed personas based on user research
- **Develop** specific usability metrics for identified contexts of use

---

## 📚 Required Materials

### For the Instructor

**Materials included in this laboratory:**
- ✅ This teaching guide (guia_docente.md)
- ✅ Student material (material_estudiante.md)
- ✅ Preparatory readings with references (lecturas_preparatorias.md)
- ✅ Tested and ready AI prompts (prompts_ia.md)
- ✅ Detailed evaluation rubric (rubrica_evaluacion.md)
- ✅ Reference solution (solucion_referencia.md)
- ✅ Introduction presentation (create PowerPoint/PDF based on this guide)

**Materials the instructor must prepare:**
- [ ] LMS access (Moodle, Canvas, Blackboard) to upload materials
- [ ] Reading comprehension quiz (5-7 questions, see section 6)
- [ ] Pre-reading report template (Word/Google Docs document)
- [ ] Context of use analysis template (Excel/Google Sheets)
- [ ] Final technical report template (Word/Google Docs document)

**Necessary technological tools:**
- [ ] Access to generative AI (at least one of):
  - ChatGPT (free version sufficient, Plus recommended)
  - Claude (Anthropic)
  - Gemini (Google)
  - Copilot (Microsoft)
- [ ] Updated web browser
- [ ] Projector/screen for in-person session
- [ ] Visible timer (project chronometer)

### For Students

**Materials they will receive:**
- Student material with case description
- Preparatory readings (PDF articles)
- Document templates
- Ready-to-use AI prompts
- Evaluation checklist

**Tools they need:**
- Account on at least one generative AI platform (free)
- Word processor
- Spreadsheet
- Web browser

---

## ⏱️ Detailed Time Planning

### PHASE 1: Preparatory Work (Autonomous - 3 hours)

**Objective:** Students arrive at the in-person session with solid understanding of ISO 9241-11

#### Activities (Estimated time: 2.5-3 hours)

**[00:00 - 01:30] Theoretical Material Reading (90 min)**

1. **Mandatory reading 1: ISO 9241-11:2018** (45 min)
   - Specific sections:
     - Introduction (pages 1-3)
     - Section 3: Terms and definitions (pages 4-6)
     - Section 5: Context of use (pages 8-11)
     - Section 6: Usability measures (pages 11-14)
   
   📌 **Instructor note:** Provide PDF of these specific sections. The complete standard has ~30 pages, but they only need these sections for this lab.

2. **Mandatory reading 2: Academic paper** (45 min)
   - Bevan, N., Carter, J., & Harker, S. (2015). "ISO 9241-11 Revised: What Have We Learnt About Usability Since 1998?"
   - Alternatively: Any paper on context of use analysis in tourism/e-commerce
   
   📌 **Instructor note:** Provide PDF in /readings folder

**[01:30 - 02:15] Complete Comprehension Quiz (45 min)**

- Quiz in LMS (5-7 multiple choice questions + 2-3 short open questions)
- Example questions (see section 6 of this guide)
- **Requirement:** Pass with minimum 70% to access in-person session
- **Attempts:** 2 attempts allowed

📌 **Instructor note:** The quiz is FUNDAMENTAL to ensure everyone arrives prepared. It's not punitive (only 5-10% of grade), but mandatory.

**[02:15 - 03:00] Write Pre-reading Report (45 min)**

Using the provided template, each student individually must:

1. **Conceptual summary** (1 page):
   - What is usability according to ISO 9241-11?
   - What are the 4 components of context of use?
   - How are effectiveness, efficiency, and satisfaction measured?

2. **Personal reflection** (½ page):
   - What system/application that you use regularly has good usability? Why?
   - What system has poor usability? What fails?

3. **Questions for class** (3-5 questions):
   - Conceptual doubts about the standard
   - Questions about practical applicability

**Submission:** Upload to LMS 24 hours before in-person session

📌 **Instructor note:** Quickly review these reports before class. Identify common questions to address in the introduction.

---

### PHASE 2: In-person Laboratory Session (2 hours)

**Classroom setup:**
- Students in teams of 2-3 people (formed previously or at the beginning)
- Each team with computer and internet access
- Projector with visible timer
- Whiteboard/screen for key concepts

#### [00:00 - 00:15] INTRODUCTION AND CONTEXTUALIZATION (15 min)

**Instructor activities:**

1. **Welcome and objectives of the day** (3 min)
   - Present session agenda
   - Explain expected deliverables
   - Resolve logistical doubts

2. **Review of key ISO 9241-11 concepts** (7 min)
   - Presentation with 8-10 slides:
     - Slide 1: What is ISO 9241?
     - Slide 2: Definition of usability (effectiveness, efficiency, satisfaction)
     - Slide 3: The 4 components of context of use
     - Slide 4: Users (types, characteristics, competencies)
     - Slide 5: Tasks (objectives, steps, frequency)
     - Slide 6: Equipment (hardware, software, materials)
     - Slide 7: Environments (physical, technical, social, cultural)
     - Slide 8: Usability metrics (concrete examples)
   
   📌 **Pedagogical tip:** Use visual examples. Show screenshots of known systems (Amazon, Booking, Google Maps).

3. **Resolution of common questions** (3 min)
   - Address 2-3 questions that appeared in reading reports
   - Clarify conceptual confusions identified in the quiz

4. **Presentation of practical case: "TravelEase"** (2 min)
   - Explain that it's a tourism experience booking platform
   - Show visual example (can be simple wireframe or similar competitor)
   - Assign roles in teams (see section 4 of this guide)

📌 **Checkpoint:** Verify that all teams have access to generative AI and materials.

---

#### [00:15 - 00:45] PHASE 1: CONTEXT OF USE ANALYSIS (30 min)

**Objective:** Teams identify and document the context of use of TravelEase

**Team activities:**

1. **Identify user profiles** (10 min)
   - Read the case in material_estudiante.md
   - Brainstorming: What types of users would use TravelEase?
   - Document at least 5 different profiles
   - For each profile, note:
     - Approximate age
     - Technological competencies
     - Travel motivations
     - Devices they would use

   📌 **Partial deliverable:** List of profiles in template

2. **Define main tasks by profile** (10 min)
   - Select 2-3 main profiles
   - For each one, list 5-8 tasks they would perform
   - Classify tasks by:
     - Frequency (daily, weekly, occasional)
     - Complexity (simple, medium, complex)
     - Criticality (high, medium, low)

   📌 **Partial deliverable:** Table of tasks by profile

3. **Analyze equipment and environments** (10 min)
   - Equipment: What devices does each profile use? (mobile, tablet, desktop)
   - Environments:
     - Physical: Where would they use the system? (home, office, airport, destination)
     - Technical: What connectivity? (WiFi, 4G/5G, variable)
     - Social: Alone or accompanied? (individual, family, group)
     - Cultural: What languages? What level of familiarity with digital platforms?

   📌 **Partial deliverable:** Complete context analysis

**Instructor role during this phase:**
- ✅ Circulate between teams constantly
- ✅ Ask triggering questions:
  - "Have you considered users with disabilities?"
  - "What happens if the user is abroad with limited data?"
  - "Does a 70-year-old tourist use the system the same as a 25-year-old?"
- ✅ DO NOT give direct answers, but guide with questions
- ✅ Identify teams going too fast → give them additional challenge
- ✅ Identify stuck teams → give them specific hint

**⏰ Checkpoint (minute 25):** 
- Stop everyone momentarily
- Ask: "How many user profiles have you identified?" (quick responses)
- Give general tip if necessary

---

#### [00:45 - 01:30] PHASE 2: PERSONA GENERATION WITH AI (45 min)

**Objective:** Use generative AI to create detailed personas and usage scenarios

**Team activities:**

1. **Select 3 priority profiles** (5 min)
   - From the identified profiles, choose the 3 most important
   - Justify selection based on:
     - System usage frequency
     - Business impact
     - Diversity of needs

2. **Generate personas with AI** (25 min)
   - Use the prompts provided in prompts_ia.md
   - For each of the 3 profiles, generate:
     - **Detailed persona** with:
       - Name, age, occupation, location
       - Personal and professional background
       - Objectives and motivations
       - Frustrations and pain points
       - Technological competencies
       - Devices and tools they use
       - Representative quote
     - **Usage scenario** with concrete narrative

   📌 **Important instruction:** Students must:
   - Copy the base prompt from prompts_ia.md
   - Customize it with their analysis data
   - Execute in AI
   - **NOT accept the first response if not detailed enough**
   - Iterate with AI to improve

   **Iteration example:**
   ```
   First AI response → very generic
   Student: "Make it more specific. This user travels frequently 
   for business to Asia. Give concrete details of their frustrations 
   with current platforms."
   Second AI response → much better
   ```

3. **Validate and refine personas** (10 min)
   - Review generated personas
   - Verify they include:
     - ✅ Realistic demographic information
     - ✅ Clear technological competencies
     - ✅ Concrete objectives (not vague)
     - ✅ Specific frustrations
     - ✅ Well-defined context of use
   - Edit manually if something doesn't make sense

4. **Document the process** (5 min)
   - Capture screenshots of AI conversations
   - Note which prompts worked better
   - Document iterations performed

   📌 **This is important for the final report**

**Instructor role during this phase:**
- ✅ Help with AI technical problems (e.g., prompt doesn't work, AI gives error)
- ✅ Review generated personas in real time
- ✅ Give feedback: "This persona is very generic, ask AI for more concrete details"
- ✅ Share good examples between teams (without revealing authorship)
- ✅ Have backup prompts if some don't work

**⏰ Checkpoint (minute 70):** 
- "All teams should have at least 2 personas generated. Does anyone need help?"

📌 **Common problem:** AI generates personas that are too generic or stereotypical.
**Solution:** Teach students to give specific context in the prompt. See prompts_ia.md for examples.

---

#### [01:30 - 01:50] PHASE 3: USABILITY METRICS DEFINITION (20 min)

**Objective:** Define specific metrics for effectiveness, efficiency, and satisfaction for each context

**Team activities:**

1. **Review ISO 9241-11 on metrics** (5 min)
   - Reread section 6 of the standard (pages 11-14)
   - Remember definitions:
     - **Effectiveness:** Accuracy and completeness with which users achieve objectives
     - **Efficiency:** Resources employed in relation to accuracy and completeness
     - **Satisfaction:** Degree to which user needs are satisfied

2. **Define metrics for each persona** (12 min)
   - For each of the 3 created personas, define:
   
   **Effectiveness Metrics:**
   - How would you measure if they achieve their objective?
   - Examples: % of successful bookings, % of completed tasks, error rate
   
   **Efficiency Metrics:**
   - How would you measure the resources employed?
   - Examples: Time to complete booking, number of clicks/steps, time on page
   
   **Satisfaction Metrics:**
   - How would you measure their satisfaction?
   - Examples: SUS score (System Usability Scale), NPS (Net Promoter Score), post-use rating

   📌 **Metrics must be:**
   - ✅ Specific (not vague like "good experience")
   - ✅ Measurable (with number or scale)
   - ✅ Relevant for that user profile
   - ✅ Realistic to obtain

3. **Document in template** (3 min)
   - Complete metrics table
   - Suggested format:

   | Persona | Effectiveness Metric | Efficiency Metric | Satisfaction Metric |
   |---------|---------------------|-------------------|-------------------|
   | Laura (Young tourist) | 95% successful bookings | < 3 min to book | SUS > 80 |
   | ... | ... | ... | ... |

**Instructor role:**
- ✅ Verify that metrics are **specific and measurable**
- ✅ Challenge vague metrics: "How would you measure exactly that?"
- ✅ Give examples of good metrics if necessary
- ✅ Connect with real cases: "How do you think Booking measures its usability?"

---

#### [01:50 - 02:00] CLOSURE AND FINAL DELIVERABLE ASSIGNMENT (10 min)

**Instructor activities:**

1. **Concept recap** (4 min)
   - Summarize what they did today:
     - ✅ Analyzed context of use (users, tasks, equipment, environments)
     - ✅ Created detailed personas with AI
     - ✅ Defined specific usability metrics
   - Connect with ISO 9241-11:
     - "This is exactly what the standard asks for in the context analysis phase"

2. **Explain final deliverable** (4 min)
   - **What:** Technical report of context of use analysis (see rubrica_evaluacion.md)
   - **When:** [X days after this session, e.g., 1 week]
   - **How:** Upload PDF to LMS
   - **Structure:** See provided template
   - **Length:** 8-12 pages (not counting annexes)

3. **Questions and doubts** (2 min)
   - Answer doubts about the deliverable
   - Clarify evaluation criteria

4. **Preview of Lab 2** (30 sec)
   - "In the next laboratory we will take these personas and design the search interface applying the 7 dialogue principles of ISO 9241-110"
   - Generate expectation and continuity

📌 **Advice:** Send by email/LMS the same day:
- Summary of key concepts (1 page)
- Delivery date reminder
- Link to final report template
- Consultation/tutoring schedule if available

---

### PHASE 3: Post-Laboratory Work (Autonomous - 3-4 hours)

**Objective:** Complete and polish the final technical report

#### Team activities (Estimated time: 3-4 hours)

**[00:00 - 01:30] Complete analysis and refinement (90 min)**

1. **Review and improve personas** (30 min)
   - Reread personas generated in the session
   - Add missing details
   - Ensure coherence between the 3 personas
   - Optional: Generate illustrative images (with AI or image banks)

2. **Expand usage scenarios** (30 min)
   - Develop complete narratives for each persona
   - Describe a typical trip using TravelEase
   - Include emotions, thoughts, friction points

3. **Validate metrics** (30 min)
   - Review that defined metrics are complete
   - Add target values (e.g., "booking time < 3 min")
   - Justify why those metrics are adequate

**[01:30 - 03:30] Technical report writing (120 min)**

Using the provided template, write report with structure:

1. **Cover page** (5 min)
   - Laboratory title
   - Team member names
   - Date
   - Subject

2. **Executive summary** (15 min)
   - ½ page with analysis synthesis
   - Main findings
   - Key conclusions

3. **Introduction** (20 min)
   - TravelEase case context
   - Analysis objectives
   - Methodology used (analysis according to ISO 9241-11)

4. **Context of use analysis** (40 min)
   - **4.1 User identification**
     - Identified profiles (brief description of all)
     - Justification for selection of 3 main profiles
   - **4.2 Task analysis**
     - Table of tasks by profile
     - Description of critical tasks
   - **4.3 Equipment and environments**
     - Analysis of devices used
     - Usage contexts (physical, technical, social, cultural)

5. **Personas and scenarios** (30 min)
   - Presentation of the 3 personas (1-2 pages each)
   - Narrative usage scenarios
   - Screenshots of AI generation (annex)

6. **Usability metrics** (20 min)
   - Complete metrics table
   - Justification for each metric
   - Relationship with ISO 9241-11

7. **Reflection and learnings** (15 min)
   - What did you learn about context of use analysis?
   - How did AI help you in the process?
   - What challenges did you encounter?
   - How would you apply this in a real project?

8. **Conclusions** (10 min)
   - Synthesis of findings
   - Importance of context analysis for design

9. **References** (5 min)
   - ISO 9241-11:2018
   - Papers read
   - Other sources consulted

**[03:30 - 04:00] Final review and submission (30 min)**

- Review format and spelling
- Verify it meets rubric (self-evaluation)
- Generate PDF
- Upload to LMS before deadline

---

## 👥 Team Management and Roles

### Team Size
**Recommended:** 2-3 students per team

**Justification:**
- 2 people: Good for small classes, allows more teams, but may be limited for brainstorming
- 3 people: **Ideal** - sufficient diversity of ideas, clear roles, not too large
- 4+ people: NOT recommended - risk of passengers, difficult to coordinate

### Role Assignment (Rotate in each lab)

**ROLE 1: ISO Analyst** 🔍
- Responsibilities:
  - Interpret ISO 9241-11 standard
  - Verify that analysis meets requirements
  - Lead usability metrics definition
  - Document decisions based on standard
- Skills developed:
  - Reading and interpretation of technical documents
  - Critical thinking
  - Attention to detail

**ROLE 2: Prompt Engineer** 🤖
- Responsibilities:
  - Manage interactions with generative AI
  - Adapt prompts to specific needs
  - Iterate to improve AI results
  - Document generation process
- Skills developed:
  - Prompt engineering
  - Communication with AI
  - Iteration and refinement

**ROLE 3: Information Synthesizer** 📊
- Responsibilities:
  - Organize collected information
  - Complete templates and tables
  - Coordinate final report writing
  - Ensure document coherence
- Skills developed:
  - Information organization
  - Technical writing
  - Project management

📌 **Important note:** In teams of 2, combine roles 2 and 3.

### Rotation Strategy

| Laboratory | Student A | Student B | Student C |
|-------------|-----------|-----------|-----------|
| Lab 1 | ISO Analyst | Prompt Engineer | Synthesizer |
| Lab 2 | Synthesizer | ISO Analyst | Prompt Engineer |
| Lab 3 | Prompt Engineer | Synthesizer | ISO Analyst |
| ... | (rotation continues) | | |

**Benefit:** Everyone develops all skills.

---

## 🎓 Pedagogical Strategies

### BEFORE the In-person Session

#### 1 Week Before
- [ ] Upload all materials to LMS in organized folder:
  ```
  Lab 1 - Context of Use Analysis/
  ├── 📘 Student Guide
  ├── 📚 Preparatory Readings/
  │   ├── ISO_9241-11_Extract.pdf
  │   └── Paper_Context_of_Use.pdf
  ├── 📝 Templates/
  │   ├── Pre_Reading_Report_Template.docx
  │   ├── Context_Analysis_Template.xlsx
  │   └── Final_Report_Template.docx
  ├── 🤖 AI Prompts
  └── ✅ Evaluation Rubric
  ```
- [ ] Send email/announcement reminding:
  - In-person session date
  - Importance of completing readings
  - Deadline for quiz and pre-reading report

#### 3 Days Before
- [ ] Verify that at least 80% of students have accessed materials
- [ ] Send reminder to those who haven't accessed
- [ ] Test that AI prompts work (may change if models update)

#### 1 Day Before
- [ ] Review submitted pre-reading reports
- [ ] Identify common questions to address in class
- [ ] Identify students with incorrect concepts (contact if critical)
- [ ] Prepare additional examples if I detect widespread confusion
- [ ] Form teams (if not formed before) - consider:
  - Skill diversity
  - Personality balance (avoid teams of only shy or only dominant)
  - Optional: Use tool like TeamMaker

#### Day of Session (Before Class)
- [ ] Arrive 15 min early to prepare classroom
- [ ] Verify projector, internet, timer
- [ ] Have presentation open
- [ ] Have backup prompts in separate document
- [ ] Print evaluation checklist (1 per team)
- [ ] Have water/coffee (it's important!)

---

### DURING the In-person Session

#### Active Facilitation Techniques

**1. Constant Circulation (80% of time)**
- DO NOT stay seated at desk
- Visit each team at least 3 times during session
- Suggested pattern: systematic rotation, don't always go to the same ones

**2. Triggering Questions (Don't give direct answers)**

Instead of saying "You should consider senior users", ask:
- ❓ "What age ranges have you considered?"
- ❓ "Do all tourists use technology the same way?"
- ❓ "What about people with physical or cognitive limitations?"

**Bank of triggering questions for this lab:**
- "Have you thought about international users who don't speak Spanish?"
- "What device would someone at the airport use?"
- "How does context of use change if you're planning vs. already traveling?"
- "What frustrations would you have when booking a trip online?"
- "Is this metric really measurable? How would you obtain it?"

**3. Pace Management**

**Teams going too fast:**
- Give additional challenges:
  - "Consider an extreme user profile (e.g., tourist with visual impairment)"
  - "Generate a fourth persona with very different characteristics"
  - "Research what metrics Booking.com or Airbnb actually use"

**Teams going slow:**
- Identify the blockage:
  - Don't understand the concept?
  - Technical problems with AI?
  - Analysis paralysis?
- Give "calibrated help":
  - Show example from another team (without identifying)
  - Give concrete first step: "Start describing someone from your family who travels"
  - Simplify: "For now focus on just 2 profiles, not 5"

**4. Group Checkpoints**

Every 20-25 minutes, stop everyone for 1-2 minutes:
- "Where are you at? Raise your hand if you already have X"
- "Team 3, quickly share an interesting profile you identified"
- "General tip: I've noticed some are... Remember that..."

**Benefit:** 
- Synchronizes pace
- Allows sharing learnings between teams
- Gives micro mental break

**5. Foster Respectful Debate**

When discussions arise in teams (it's good!):
- ✅ Allow debate (don't intervene immediately)
- ✅ If they get stuck, ask: "What does ISO 9241-11 say about this?"
- ✅ If disagreement persists: "Interesting. Document both perspectives in your report"

**6. Technical Problem Management**

**AI doesn't work / generates garbage:**
- Have tested backup prompts
- Suggest changing AI (ChatGPT → Claude → Gemini)
- If everything fails: have pre-generated persona examples as emergency resource

**Internet down:**
- Plan B: Work in offline templates
- Generate personas manually based on examples
- Continue with conceptual analysis

---

### AFTER the In-person Session

#### Same Day
- [ ] Send by email/LMS:
  - Summary of key concepts (1 page PDF)
  - Final deliverable reminder with date
  - Answers to common questions that arose
  - Best practices observed (without naming teams)

#### During Autonomous Work Period
- [ ] Be available for consultations (define tutoring schedule)
- [ ] Answer questions by email/forum within 24 hours maximum
- [ ] Optional: Online group consultation session (30-45 min) at mid-term

#### After Receiving Submissions
- [ ] Evaluate using rubric (see rubrica_evaluacion.md)
- [ ] Give individual feedback per team within 48-72 hours
- [ ] Identify common errors to address in next lab
- [ ] Select 2-3 best works (anonymous) to share as reference

#### Effective Feedback (Constructive Feedback Model)

**Individual feedback structure per team:**

```
Team X - Lab 1: Context of Use Analysis
Grade: [X/10 or letter according to system]

🎯 STRENGTHS (what you did very well):
- [Specific well-achieved aspect]
- [Concrete example from your work]

📈 AREAS FOR IMPROVEMENT (to grow):
- [Specific aspect to improve]
- [Concrete suggestion on how to improve it]

💡 RECOMMENDATIONS for Lab 2:
- [Specific advice applicable to next lab]

📋 EVALUATION DETAIL:
[See attached rubric with scores by criterion]
```

---

## ⚠️ Critical Points and Solutions

### Problem 1: Students don't complete preparatory readings

**Signals:**
- Quiz with approval rates < 60%
- Very superficial or copied reading reports
- Basic questions in class that reveal not having read

**Impact:**
- In-person session becomes theoretical class (waste of lab time)
- Teams cannot do quality analysis without conceptual base

**Preventive solutions:**
- ✅ Make quiz **mandatory** and worth % of grade (even if small, 5-10%)
- ✅ Don't allow entry to in-person session without approved quiz (strict policy)
- ✅ Send reminders 1 week, 3 days and 1 day before
- ✅ Make readings more accessible (extracts, not complete document)

**Corrective solutions (if it already happened):**
- Plan B: Convert first 30 min of session to mini theoretical class
- Reduce complexity of activities
- Give more direct guidance (less discovery)

---

### Problem 2: AI doesn't generate expected code/content

**Signals:**
- Students say "AI doesn't work"
- Very generic or irrelevant results
- Visible frustration with tool

**Common causes:**
- Poorly formulated prompts (too vague or too complex)
- AI down or usage limit reached
- Students don't understand how to iterate with AI

**Preventive solutions:**
- ✅ Test all prompts 1-2 days before session
- ✅ Have tested prompts in multiple AIs (ChatGPT, Claude, Gemini)
- ✅ Include examples of "good iteration" in materials
- ✅ Briefly explain prompt engineering at start

**Corrective solutions:**
- Have examples of already generated personas as backup
- Help students reformulate prompts
- Allow use of another alternative AI
- In extreme case: provide base content and ask them to adapt it

---

### Problem 3: Teams finish too quickly (and superficially)

**Signals:**
- Team says "we're done" at minute 40 of 120
- Very brief or superficial deliverables
- Generic personas like "Maria, 30 years old, likes to travel"

**Cause:**
- Lack of depth in analysis
- Didn't understand expected level of detail

**Preventive solutions:**
- ✅ Show examples of good personas vs. bad personas at start
- ✅ Have clear evaluation rubric (so they see superficial = low grade)
- ✅ Prepare "additional challenges" beforehand

**Corrective solutions:**
- Ask questions that reveal superficiality:
  - "Why did you choose that metric specifically?"
  - "How did you validate this persona is representative?"
  - "What does ISO 9241-11 say about this element?"
- Assign analysis extension:
  - "Generate a fourth persona of very different profile"
  - "Research metrics used by real platform and compare them"
  - "Develop usage scenario with more narrative detail"

---

### Problem 4: Teams going very slowly (analysis paralysis)

**Signals:**
- Minute 60 and still haven't generated anything with AI
- Endless discussions about minor details
- Visible anxiety, concern about "doing it perfectly"

**Cause:**
- Excessive perfectionism
- Lack of confidence to make decisions
- Fear of making mistakes

**Preventive solutions:**
- ✅ Emphasize it's an iterative process (can improve later)
- ✅ Establish strict timeboxing: "In X minutes we move to next phase"
- ✅ Show there's no "one correct answer"

**Corrective solutions:**
- Direct intervention: "Make a decision now, you have 2 minutes"
- Simplify scope: "For now work with 2 profiles, not 5"
- Give permission for imperfection: "The important thing is applying the process, you can refine later"
- Provide example/base for them to modify (don't start from scratch)

---

### Problem 5: Discrepancies in standard interpretation

**Signals:**
- Teams reach different conclusions about same concept
- Confusion about whether something meets ISO 9241-11 or not
- Questions like "is this right or wrong?"

**Reality:**
- This is NOT a problem! It's DESIRED
- ISO 9241 requires interpretation and application to context

**Pedagogical handling:**
- ✅ Foster debate: "What do other teams think?"
- ✅ Make them justify with standard: "Show me where it says that in ISO 9241-11"
- ✅ Allow multiple valid interpretations if well-founded
- ✅ DO NOT give "the correct answer" if not necessary

**In the report:**
- Ask them to document their interpretation and justification
- Value reasoning, not coincidence with "model answer"

---

### Problem 6: Team dynamics problems

**Signals:**
- One member dominates, others don't participate
- Visible conflicts, tension
- One member does all the work

**Preventive solutions:**
- ✅ Assign clear roles with specific responsibilities
- ✅ Rotate roles in each lab (dominant can't always be leader)
- ✅ Individual evaluation besides group (see rubric)

**Corrective solutions:**
- Talk with team: "How are you distributing the work?"
- Intervene if necessary: "I want to hear the opinion of [quiet person]"
- If serious: allow team change or individual work (last resort)

---

## 📊 Evaluation and Rubric

### Grade Distribution

| Component | Weight | Moment |
|-----------|--------|---------|
| **Pre-reading report** | 10% | Before session |
| **In-person session participation** | 15% | During session |
| **Final technical report** | 75% | Post-session |
| **TOTAL** | **100%** | |

---

### Detailed Rubric

See complete file: `rubrica_evaluacion.md`

**Summary of main criteria:**

1. **Understanding of ISO 9241-11** (20%)
   - Correct definition of usability
   - Identification of context of use components
   - Adequate application of standard

2. **Quality of context analysis** (25%)
   - Diversity and depth of user profiles
   - Completeness of task analysis
   - Consideration of equipment and environments

3. **Personas and scenarios** (20%)
   - Detail and realism of personas
   - Coherence and relevance of scenarios
   - Effective use of generative AI

4. **Usability metrics** (15%)
   - Specificity and measurability
   - Alignment with ISO 9241-11
   - Adequacy to context

5. **Report quality** (15%)
   - Structure and organization
   - Writing and clarity
   - Format and presentation

6. **Reflection and learning** (5%)
   - Depth of reflection
   - Theory-practice connection
   - Constructive self-criticism

---

## 📝 Reading Comprehension Quiz (Examples)

### Multiple Choice Questions (5-7 questions)

**Question 1:**
According to ISO 9241-11, usability is defined as:
- a) The ease of use of a system
- b) The degree to which a system is intuitive
- c) The extent to which a product can be used by specified users to achieve specified goals with effectiveness, efficiency and satisfaction in a specified context of use ✅
- d) The quality of user experience

**Question 2:**
The four components of context of use according to ISO 9241-11 are:
- a) Users, objectives, constraints and results
- b) Users, tasks, equipment and environments ✅
- c) Personas, scenarios, devices and metrics
- d) Effectiveness, efficiency, satisfaction and accessibility

**Question 3:**
Effectiveness in usability refers to:
- a) The speed with which a task is completed
- b) User satisfaction with the system
- c) The accuracy and completeness with which users achieve specific objectives ✅
- d) The number of errors committed

**Question 4:**
An appropriate efficiency metric would be:
- a) Percentage of satisfied users
- b) Time needed to complete a task ✅
- c) Number of available functionalities
- d) Quality of visual design

**Question 5:**
Which of the following is NOT an environment component according to ISO 9241-11?
- a) Physical environment (lighting, noise, etc.)
- b) Technical environment (platforms, connectivity)
- c) Competitive environment (other similar products) ✅
- d) Social and cultural environment

### Short Open Questions (2-3 questions)

**Question 6:**
Explain in your own words the difference between efficiency and effectiveness in usability. Give a concrete example of each.

**Expected answer (rubric):**
- Effectiveness = achievement of objectives (did they complete it?)
- Efficiency = resources employed (how much effort did it require?)
- Concrete and correct example of each

**Question 7:**
Why is it important to analyze context of use before designing a system? What could happen if it's not done?

**Expected answer:**
- Importance: design for real users/contexts, not assumed ones
- Consequences of not doing it: system not useful/usable, user rejection
- Mention at least 2 valid reasons

---

## 🔗 Connection with Other Laboratories

### Required Previous Laboratories
- **None** (This is Lab 1, introductory)

### This Laboratory Prepares For:

**Lab 2: Dialogue Principles (ISO 9241-110)**
- Personas created here are used to design search interface
- Usage contexts inform design decisions
- Defined metrics will be used to evaluate designs

**Lab 3: User-Centered Design (ISO 9241-210)**
- Context analysis is first phase of UCD process
- Personas are representative users for tests
- Identified tasks guide iterative design

**Labs 4-10:**
- All subsequent laboratories use personas and contexts defined here
- TravelEase system is built progressively considering these users

### Concepts that are Revisited:
- **None** (first laboratory)

---

## 📚 Additional Resources for Instructor

### Deepening Readings (Optional for instructors)

1. **Complete ISO 9241-11:2018**
   - To understand complete context of standard
   
2. **Bevan, N. (2009). "International standards for HCI"**
   - Encyclopedia of Human-Computer Interaction, Chapter on ISO 9241

3. **Norman, D. (2013). "The Design of Everyday Things"**
   - Chapter on User-Centered Design (complements ISO 9241-210)

4. **Cooper, A., Reimann, R., Cronin, D. (2014). "About Face: The Essentials of Interaction Design"**
   - Chapter on Personas (technique in depth)

### Recommended Videos (To show in class if there's time)

1. **"What is Usability?"** - Nielsen Norman Group (5 min)
   - Visual introduction to usability

2. **"Creating Personas"** - Interaction Design Foundation (8 min)
   - How to create effective personas

### Useful Tools

1. **Persona Generators:**
   - Xtensio User Persona Creator (visual templates)
   - HubSpot Make My Persona (interactive)

2. **Metrics Calculators:**
   - System Usability Scale (SUS) Calculator
   - NPS Calculator

3. **Image Banks for Personas:**
   - Generated Photos (AI-generated faces)
   - Unsplash, Pexels (free photos)

---

## ✅ Pre-Session Checklist for Instructor

**1 Week Before:**
- [ ] Materials uploaded to LMS
- [ ] Quiz configured and functional
- [ ] Templates created and accessible
- [ ] Announcement email sent

**3 Days Before:**
- [ ] Verify student access to materials (LMS analytics)
- [ ] Test AI prompts (ChatGPT, Claude, Gemini)
- [ ] Reminder sent

**1 Day Before:**
- [ ] Review submitted reading reports
- [ ] Identify concepts to reinforce
- [ ] Form teams (if applicable)
- [ ] Prepare presentation

**Day of Session:**
- [ ] Arrive 15 min early
- [ ] Verify technology (projector, internet, timer)
- [ ] Have backup prompts
- [ ] Print checklists (1 per team)
- [ ] Coffee/water ☕

**During Session:**
- [ ] Circulate constantly (don't stay seated)
- [ ] Ask triggering questions (don't give direct answers)
- [ ] Checkpoints every 20-25 min
- [ ] Monitor pace (help slow ones, challenge fast ones)

**Same Day Post-Session:**
- [ ] Send concept summary
- [ ] Remind delivery date
- [ ] Share observed best practices

---

## 🎓 Final Notes for Instructor

### Pedagogical Philosophy of This Laboratory

This laboratory is designed under the principles of:

1. **Active Learning:** Students construct knowledge by doing, not just listening
2. **Social Constructivism:** Teamwork, discussion, multiple perspectives
3. **Case-Based Learning:** Realistic case that motivates and gives context
4. **Metacognitive Reflection:** Students think about their own learning process
5. **Technology as Tool:** AI facilitates, doesn't substitute critical thinking

### Your Role as Instructor

**You are NOT:**
- ❌ An instructor who gives correct answers
- ❌ A technician who solves AI problems
- ❌ An evaluator who looks for errors

**You ARE:**
- ✅ A facilitator who guides discovery
- ✅ A designer of learning experiences
- ✅ A coach who develops thinking skills
- ✅ An expert who connects theory (ISO 9241) with practice (tourism case)

### Adaptability

This guide is **intentionally exhaustive** to cover multiple scenarios, but:

- ✅ **Adapt it** to your institutional context
- ✅ **Simplify it** if your group is small or has less time
- ✅ **Expand it** if you have additional resources
- ✅ **Personalize it** with examples from your region/culture

**What is essential NOT to change:**
1. Prior preparation with readings (students must arrive prepared)
2. Use of ISO 9241-11 as technical reference
3. AI as development tool (not manual programming)
4. Emphasis on analysis and evaluation (not just execution)
5. Explicit connection between standard theory and case practice

---

## 📧 Contact and Continuous Improvement

**For the Instructor Using This Material:**

After teaching this laboratory, consider:

1. **Self-evaluation:**
   - What worked well?
   - What would you adjust for next time?
   - Were the times realistic?

2. **Student Feedback:**
   - Include 2-3 feedback questions in final report
   - What was most useful? What was confusing?

3. **Material Improvement:**
   - Update this guide with learnings
   - Share best practices with colleagues
   - Adapt according to tool evolution (AI changes rapidly)

---

**Success with the laboratory! 🚀**

*This material is part of the series of 10 laboratories on ISO 9241 applied to tourism management systems.*