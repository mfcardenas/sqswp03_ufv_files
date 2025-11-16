````markdown
# AI Prompts for Persona Generation - Lab 1

## 📋 Introduction

This document contains **tested and optimized prompts** for generating detailed personas using generative AI (ChatGPT, Claude, Gemini, etc.).

**How to use this document:**
1. Read the complete base prompt
2. Personalize it with data from your analysis (replace [PLACEHOLDERS])
3. Copy it to your preferred generative AI
4. Iterate based on refinement examples

---

## 🤖 Base Prompt: Complete Persona Generation

### Complete Version (Recommended)

```
Act as an expert in user experience design (UX) and context of use analysis 
according to ISO 9241-11.

I need you to generate a detailed persona for a tourism experience booking 
platform called "TravelEase".

PROJECT CONTEXT:
TravelEase is a digital platform that connects travelers with tourism service 
providers (hotels, tours, activities, restaurants). It competes with Booking.com, 
Airbnb Experiences, GetYourGuide. Its differentiator is the focus on personalized 
and curated experiences.

USER PROFILE TO DEVELOP:
- User type: [INSERT: e.g., "Young backpacker tourist"]
- Age range: [INSERT: e.g., "22-28 years"]
- Technological competence: [INSERT: e.g., "High - digital native"]
- Main travel motivation: [INSERT: e.g., "Adventure, low budget, 
  cultural discovery"]
- Main devices: [INSERT: e.g., "Smartphone (iOS), occasionally laptop"]
- Typical usage context: [INSERT: e.g., "On the move, airports, hostels, 
  variable WiFi connection"]
- Frustrations with current platforms: [INSERT: e.g., "Booking only shows 
  expensive hotels, difficult to find authentic experiences, complex interfaces"]

GENERATE A DETAILED PERSONA with the following structure:

1. DEMOGRAPHIC DATA:
   - Full name (realistic, not generic)
   - Specific age
   - Detailed occupation (not just "professional", but specific job)
   - Location (city, country)
   - Marital status / family situation
   - Socioeconomic level

2. PERSONAL BACKGROUND:
   - Brief personal history (2-3 paragraphs)
   - Travel experience (frequency, previous destinations, travel style)
   - Technology experience (adoption level, favorite apps)
   - Personality (key traits)

3. OBJECTIVES AND MOTIVATIONS:
   - What do they seek in a tourism booking platform? (3-5 concrete objectives)
   - What motivates them to travel?
   - What do they value most? (price, comfort, authenticity, security, flexibility, etc.)
   - Booking priorities (order from most to least important)

4. FRUSTRATIONS AND PAIN POINTS:
   - What specific problems have they had with platforms like Booking, Airbnb, 
     TripAdvisor? (3-5 concrete frustrations)
   - What do they find difficult, annoying or frustrating when planning trips online?
   - What current needs are NOT covered by existing platforms?

5. TECHNOLOGICAL COMPETENCIES:
   - Skill level (specify level: beginner/intermediate/advanced/expert)
   - Apps and platforms they use frequently (at least 5-7 specific apps)
   - Devices they own and usage frequency
   - Platform preferences (desktop web, mobile web, native apps)
   - Attitude toward new technologies (early adopter, mainstream, late adopter)

6. DEVICES AND USAGE ENVIRONMENT:
   - Main device for booking trips
   - Secondary devices
   - Typical connection (home WiFi, public WiFi, mobile data)
   - Typical usage conditions (sitting at desk, in transit, in bed before 
     sleeping, etc.)

7. BEHAVIORS AND HABITS:
   - How do they research destinations? (Google, Instagram, YouTube, blogs, friends)
   - How much time do they dedicate to planning a trip?
   - Do they book in advance or last minute?
   - Do they prefer flexibility or structured itineraries?
   - Do they travel alone, with partner, with family, with friends?

8. REPRESENTATIVE QUOTE:
   - An authentic phrase that captures their attitude, need or main frustration
   - Must sound natural, as if this person really said it

9. DETAILED USAGE SCENARIO:
   - Create a narrative of 400-500 words where this person:
     * Has a concrete travel need (specify destination, dates, context)
     * Discovers TravelEase (how they reached the platform)
     * Navigates through the system (what they search, how they filter, what catches their attention)
     * Makes decisions (what they compare, what they prioritize)
     * Completes (or doesn't) a booking
     * Include their thoughts, emotions, doubts at each step
   
   The narrative must be CONCRETE, not generic. Use real place names, 
   specific dates, vivid details.

OUTPUT FORMAT:
- Use Markdown format with clear sections
- Include emojis for better readability
- Make the persona feel REAL and CREDIBLE, not stereotyped
- Avoid clichés ("loves to travel", "seeks new experiences" without specifics)
- Be specific with numbers, brands, places, apps

Understood? Generate the persona now.
```

---

## 🔄 Refinement Prompts (Iterations)

After getting the first response, use these prompts to improve:

### Refinement 1: More Specificity

```
Very good, but I need you to be MORE SPECIFIC in several sections:

1. In BACKGROUND: Don't just say "likes to travel". Give me concrete details: 
   How many trips per year? What was their last trip? Where? What did they do?

2. In FRUSTRATIONS: Don't just say "platforms are confusing". Give me CONCRETE 
   examples: "On Booking, when I searched for hostels in Barcelona, it kept 
   showing me 4-star hotels even though I set the low price filter".

3. In TECH COMPETENCIES: Don't just say "uses apps". Give me SPECIFIC names of apps 
   they use DAILY, WEEKLY, and OCCASIONALLY.

4. In USAGE SCENARIO: I want real names (specific city, not "a European city"), 
   concrete dates (not "in summer", but "from July 15th to 22nd"), 
   specific budget (not "low budget", but "maximum €800 for 7 days").

Regenerate the sections with these levels of specificity.
```

### Refinement 2: Avoid Stereotypes

```
This persona sounds too stereotyped. Make it more REALISTIC and NUANCED:

- Not all millennials are the same
- Don't use clichés like "loves Instagram" without context
- Give them realistic contradictions (e.g.: "Likes to plan everything in advance, 
  but also seeks spontaneous experiences")
- Include real limitations (budget, time, responsibilities)
- Make their frustrations SPECIFIC to real experiences

Regenerate with more authenticity.
```

### Refinement 3: Align with ISO 9241-11

```
Now I need you to EXPAND the CONTEXT OF USE section following ISO 9241-11:

Add detailed analysis of:

1. PHYSICAL ENVIRONMENT:
   - Where are they when using TravelEase? (specific places)
   - Lighting conditions (natural light, artificial, screen in sun)
   - Noise level and distractions
   - Posture (sitting comfortably, standing, lying down, moving)

2. TECHNICAL ENVIRONMENT:
   - Connection type (home WiFi, café WiFi, mobile data, international roaming)
   - Typical connection speed
   - Technical limitations (limited data, low battery, small screen)

3. SOCIAL ENVIRONMENT:
   - Do they use the system alone or consult with others? (partner, friends, family)
   - Are there interruptions? (children, work, notifications)
   - Do they share the booking decision with someone?

4. CULTURAL ENVIRONMENT:
   - Languages they master
   - Familiarity with e-commerce
   - Level of trust in online payments
   - Cultural expectations (e.g.: if from high-context or low-context culture)

Regenerate adding these dimensions of context of use.
```

### Refinement 4: Improve Narrative Scenario

```
The usage scenario is too linear and perfect. Make it more REALISTIC:

- Include OBSTACLES they encounter along the way
- Show moments of DOUBT ("is this platform trustworthy?")
- Include COMPARISON with other platforms (opens Booking in another tab to compare)
- Add SENSORY and EMOTIONAL details:
  * What are they thinking?
  * What generates anxiety?
  * What excites them?
  * At what moment do they almost give up?
  * What finally convinces them?

- Make the scenario last at least 10-15 minutes of real time (don't compress everything 
  into "quickly searches and books")

Regenerate the scenario with more drama, realism and psychological depth.
```

---

## 🎯 Specialized Prompts by Profile Type

### Profile 1: Young Tourist (18-28 years)

```
[Use base prompt and add:]

SPECIFIC CHARACTERISTICS OF GENERATION Z / YOUNG MILLENNIALS:
- Social media influence (Instagram, TikTok) on travel decisions
- Search for "Instagrammable moments"
- Community and social connection (meetups, social hostels)
- Sustainability and responsible tourism
- Experiences > material possessions
- FOMO (fear of missing out) and viral trends
- Use of multiple apps simultaneously
- Expectation of AI-based personalization

Include how these factors affect their use of TravelEase.
```

### Profile 2: Senior Tourist (55+ years)

```
[Use base prompt and add:]

SPECIFIC CHARACTERISTICS OF SENIOR USERS:
- Variable level of technological competence (DON'T assume low level)
- Higher budget, but greater risk aversion
- Valuation of comfort, security, accessibility
- Preference for human customer service backup
- May have physical limitations (vision, mobility, hearing)
- More time to travel (retirees) but more health sensitivity
- Possible need for large text, high contrast
- Distrust of new platforms (needs to build trust)

DO NOT STEREOTYPE: Many seniors are tech-savvy. Create nuanced persona.
```

### Profile 3: Business Tourist (30-50 years)

```
[Use base prompt and add:]

SPECIFIC CHARACTERISTICS OF BUSINESS TRAVELERS:
- Time is the scarcest resource (efficiency > price)
- Need for flexibility (last-minute changes)
- Corporate bookings (company policies, invoices)
- Use in professional contexts (tablet on plane, laptop in hotel)
- Brand loyalty (points, memberships)
- Expectation of premium service
- Frequent use (several times per month)
- Mix of business + leisure travel (bleisure)

Include scenario where they have important meeting and must adjust itinerary.
```

### Profile 4: Family with Children

```
[Use base prompt and add:]

SPECIFIC CHARACTERISTICS OF FAMILIES:
- Multiple stakeholders (children's needs, partner, in-laws)
- Priority: safety, convenience, kid-friendly activities
- Large but distributed budget (many people)
- Planning well in advance
- Need for detailed information (e.g.: is there a crib? children's menu?)
- Search for educational experiences for children
- Shared system use (both parents plan together)
- Logistical coordination stress

Create scenario where family of 4 (2 adults, 7-year-old child, 18-month baby) 
plans trip to beach destination.
```

### Profile 5: Backpacker/Digital Nomad

```
[Use base prompt and add:]

SPECIFIC CHARACTERISTICS OF DIGITAL NOMADS:
- Extended travel (months, not days)
- Remote work (need for reliable WiFi, coworking spaces)
- Tight but sustainable long-term budget
- Extreme flexibility (no fixed dates)
- Community of other nomads
- Search for immersive experiences (live like a local)
- Multi-destination (route through several countries)
- Intensive use of productivity apps, VPNs, digital tools

Create scenario where digital nomad seeks 1-month accommodation in Bali with 
good WiFi for working.
```

---

## 💡 Prompt Engineering Tips

### DO ✅

1. **Be specific with examples:**
   - ❌ "Give me a young person"
   - ✅ "Give me a 24-year-old person, freelance graphic designer, lives in Madrid, 
     travels 3-4 times a year with budget of €600-800 per trip"

2. **Give project context:**
   - Explain what TravelEase is, who it competes with, what makes it different
   - AI can generate more relevant personas with context

3. **Ask for structured format:**
   - Specify sections, Markdown format, use of tables if useful
   - AI generates more organized outputs

4. **Iterate, don't expect perfection on first attempt:**
   - First iteration → base structure
   - Second iteration → refinement and details
   - Third iteration → final adjustments

5. **Use clear imperative language:**
   - ✅ "Generate", "Create", "Include specifically"
   - ❌ "Could you maybe...", "I would like you to..."

### DON'T ❌

1. **Don't use prompts that are too short:**
   - ❌ "Create a persona for TravelEase"
   - AI needs context to give useful results

2. **Don't accept generic responses:**
   - If AI says "María, 30 years old, likes to travel" → ITERATE
   - Ask for concrete details, specific examples

3. **Don't copy textually without validating:**
   - AI can generate incorrect or contradictory information
   - READ, VALIDATE, EDIT manually if necessary

4. **Don't mix multiple personas in one prompt:**
   - Generate one persona at a time
   - If you want 3 personas, make 3 separate conversations (or at least 3 sequential prompts)

5. **Don't forget to document the process:**
   - Take screenshots of iterations
   - You'll need to show the process in your report

---

## 📸 Example of Successful Conversation

```
══════════════════════════════════════════════════════════
YOU:
[Complete base prompt with "Young backpacker tourist" profile data]

──────────────────────────────────────────────────────────
AI (ChatGPT):
[Generates base persona, but somewhat generic]

María García
24 years old
Freelance graphic designer
Barcelona, Spain
...

══════════════════════════════════════════════════════════
YOU:
Good, but I need MORE specificity:

1. Full name (last name too)
2. Occupation: Not just "graphic designer", but what type of projects, 
   for what clients, approximate income
3. Frustrations: Give me CONCRETE examples of searches they did on Booking 
   or Airbnb that were frustrating
4. Apps: List of 10 apps they use daily/weekly with usage frequency

Regenerate with these details.

──────────────────────────────────────────────────────────
AI:
[Generates more detailed version]

Laura García Martínez
24 years old
Freelance graphic designer specialized in branding for startups
Barcelona, Spain
Income: €1,800-2,200/month (variable depending on projects)
...

Apps they use:
- DAILY: Instagram (2-3h/day), WhatsApp (all day), Google Maps, Notion
- WEEKLY: Canva, Adobe Illustrator, Spotify, YouTube
...

Specific frustrations:
- "3 months ago I searched for hostels in Lisbon for July. On Booking I set 
  filter 'less than €25/night' but it kept showing me €60-80 hotels. I had to 
  go to HostelWorld."
...

══════════════════════════════════════════════════════════
YOU:
Much better! Now generate the usage scenario with this structure:

1. Initial context (why they need to travel, when, with whom)
2. TravelEase discovery (how they reached the platform)
3. First exploration (what they search, what they filter)
4. Moment of doubt (something that makes them distrust or doubt)
5. Comparison with another platform (opens Booking in another tab)
6. Final decision (what convinces them of TravelEase or makes them abandon)

Make the scenario last 15 real minutes. Include their internal thoughts, 
emotions, and concrete details (specific destination, dates, exact budget).

──────────────────────────────────────────────────────────
AI:
[Generates detailed narrative scenario of 500+ words]

SCENARIO: Laura plans escape to Porto

It's Friday May 10th, 11:45 PM. Laura just finished an intense branding 
project for a Barcelona startup that had her working 12-hour days for 2 weeks. 
She's exhausted but happy - they paid her €2,400.

She sits on the sofa of her shared apartment in Gràcia with her MacBook Air. 
Her two roommates are already asleep. She opens Instagram while having a 
Estrella Damm beer and sees a Reel from a travel influencer in Porto...

[CONTINUES with vivid details, thoughts, emotions, specific searches, 
comparisons, doubts, decisions...]

══════════════════════════════════════════════════════════
YOU:
Perfect. Now format everything in Markdown with clear sections, emojis for 
better readability, and add a summary table at the beginning with key persona data.

──────────────────────────────────────────────────────────
AI:
[Generates complete persona in well-structured Markdown format]

# 👤 Persona: Laura García Martínez

## 📊 Quick Summary

| Aspect | Detail |
|---------|---------|
| **Age** | 24 years |
| **Occupation** | Freelance graphic designer (startup branding) |
| **Location** | Barcelona, Spain (Gràcia neighborhood) |
...

══════════════════════════════════════════════════════════
```

**Result:** Detailed, realistic, specific persona, ready to use in the report.

---

## 🔗 Prompts for Special Cases

### Generate Scenario with Problem/Friction

```
Generate a scenario where [PERSONA NAME] uses TravelEase but encounters 
PROBLEMS and FRICTIONS. I want to see:

1. A moment where the system does NOT meet their expectations
2. A moment of frustration or confusion
3. How they try to resolve the problem
4. Whether they finally achieve their goal or abandon

This scenario will serve to identify usability requirements in later laboratories. 
Make it realistic - not all scenarios are success stories.
```

### Generate Persona with Disability

```
Generate a persona with [DISABILITY TYPE: e.g. severe visual impairment, 
uses JAWS screen reader].

IMPORTANT:
- DO NOT STEREOTYPE: Disability is ONE aspect of the person, not their complete identity
- Include specific assistive technologies they use (hardware and software)
- Detail how their disability specifically affects use of tourism booking platforms
- Include frustrations with current accessibility barriers (concrete, with examples)
- Include technological competencies (many people with disabilities are power users)

Generate with sensitivity, realism and respect.
```

### Generate International Persona (Non-Spanish speaker)

```
Generate a persona from [COUNTRY: e.g. Japan] who travels to Spanish-speaking countries.

Include specific cultural aspects:
- Language barriers
- Differences in UI conventions (e.g: right-to-left reading in Arabic)
- Different cultural expectations (e.g: formality levels)
- Payment preferences (e.g: in Asia PayPal/Alipay preferred over cards)
- Differences in data formats (date DD/MM/YYYY vs MM/DD/YYYY)

Make the usage scenario include moments where cultural differences 
create friction or confusion.
```

---

## ✅ Generated Persona Quality Checklist

Before finalizing a persona, verify:

**Demographic Data:**
- [ ] Full name (not just first name)
- [ ] Specific age (not range)
- [ ] Detailed occupation (not vague like "professional")
- [ ] Location with city and country
- [ ] Clear family context

**Background:**
- [ ] Personal history with concrete details (not generic)
- [ ] Travel experience quantified (e.g.: "3-4 trips/year")
- [ ] Technological experience with specific examples

**Objectives:**
- [ ] At least 3-5 concrete objectives
- [ ] Prioritized (what is MOST important)
- [ ] Related to TravelEase specifically

**Frustrations:**
- [ ] At least 3-5 specific frustrations
- [ ] Concrete examples of past experiences
- [ ] Related to existing platforms (Booking, Airbnb, etc.)

**Technological Competencies:**
- [ ] Clear level (beginner/intermediate/advanced/expert)
- [ ] List of 7-10 specific apps with usage frequency
- [ ] Specific devices (model, not just "smartphone")

**Context of Use:**
- [ ] Main and secondary devices
- [ ] Physical environment described (where, when, how)
- [ ] Technical environment (connection, limitations)
- [ ] Social environment (alone, with others, interruptions)
- [ ] Cultural environment (language, conventions)

**Quote:**
- [ ] Sounds natural and authentic (not forced)
- [ ] Captures key attitude or frustration
- [ ] In quotes

**Scenario:**
- [ ] Narrative (story, not list of steps)
- [ ] Concrete details (dates, places, specific budgets)
- [ ] Includes thoughts and emotions
- [ ] Shows complete process (not just result)
- [ ] At least 400-500 words
- [ ] Includes moments of doubt, comparison, decision

**Realism:**
- [ ] The person seems REAL (not stereotype)
- [ ] Has contradictions and nuances (like real people)
- [ ] Not caricature or exaggeration
- [ ] Includes realistic limitations (budget, time, knowledge)

**Diversity (among the 3 personas):**
- [ ] Diverse ages (not all similar)
- [ ] Diverse technological competencies
- [ ] Diverse travel motivations
- [ ] Diverse usage contexts
- [ ] At least one persona with special considerations (disability, language barrier, etc.)

---

## 🎯 Summary: Recommended Workflow

1. **Preparation** (5 min):
   - Read your context of use analysis
   - Identify the 3 priority profiles
   - Gather specific data for each profile

2. **First generation** (10 min):
   - Use complete base prompt
   - Personalize with data from your analysis
   - Generate first version

3. **First iteration** (5 min):
   - Review generated persona
   - Identify what's too generic
   - Use refinement prompt: "More specificity"

4. **Second iteration** (5 min):
   - Refine usage scenario
   - Use prompt: "Improve narrative scenario"
   - Add emotional and psychological details

5. **Third iteration (optional)** (5 min):
   - Align with ISO 9241-11
   - Expand context of use analysis
   - Format and presentation

6. **Validation and manual editing** (5 min):
   - Review quality checklist
   - Manually edit aspects that don't make sense
   - Ensure consistency among the 3 personas

**Total time per persona: 30-35 minutes**  
**Total time for 3 personas: ~90 minutes**

---

**Now you have all the tools to generate high-quality personas with generative AI!** 🚀

💡 **Remember:** AI is a powerful tool, but YOU are the one who analyzes, validates and makes decisions. Don't accept mediocre results - iterate until you get realistic and useful personas.

````