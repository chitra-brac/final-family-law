# Frontend Product Requirements Document

# Ain Bandhu (আইন বন্ধু) - AI Legal Assistant for Bangladeshi Women

**Version**: 2.0 (Complete & Accurate)
**Date**: 2025-11-26
**Status**: Ready for Development
**Backend API**: https://final-family-law-production.up.railway.app
**Backend PRD**: `docs/PRD.md` (2949 lines)

---

## Critical Understanding

**This is NOT a simple chatbot. This is an AI LAWYER.**

Ain Bandhu acts like a compassionate, knowledgeable lawyer who:

- Asks strategic questions to understand the full situation
- Assesses case strength, urgency, and available options
- Provides personalized recommendations based on individual circumstances
- Anticipates obstacles (police refusal, family pressure) and guides how to overcome them
- Prioritizes safety before legal procedures
- Explains complex legal concepts in simple Bengali accessible to women with primary school education

The frontend must support this sophisticated interaction pattern, not just display Q&A exchanges.

---

## Table of Contents

1. [Product Vision & Scope](#product-vision--scope)
2. [Complete Legal Coverage - 12 Intents](#complete-legal-coverage---12-intents)
3. [User Personas (Detailed)](#user-personas-detailed)
4. [Core Features - What Makes This Different](#core-features---what-makes-this-different)
5. [API Integration Specification](#api-integration-specification)
6. [User Flows & Conversation Patterns](#user-flows--conversation-patterns)
7. [UI/UX Requirements](#uiux-requirements)
8. [Technical Stack & Architecture](#technical-stack--architecture)
9. [Development Phases](#development-phases)
10. [Success Metrics](#success-metrics)
11. [Open Questions](#open-questions)

---

## Product Vision & Scope

### What is Ain Bandhu?

**Vision**: Democratize access to legal knowledge and procedural guidance for underprivileged Bangladeshi women who face family law issues but cannot afford legal representation.

**Mission**: Act as an accessible AI-powered lawyer that provides strategic, personalized legal guidance in simple Bengali, empowering women to navigate the legal system and access justice.

### Target Audience

Underprivileged Bangladeshi women facing family law issues including:

- Domestic violence (physical, emotional, sexual abuse by family members)
- Rape and sexual assault (recent incidents requiring urgent medical/legal action)
- Child marriage (underage or forced marriage of minors)
- Child custody disputes (after divorce or separation)
- Divorce/Talaq (ending marriage, understanding rights)
- Dowry harassment (dowry demands and related abuse)
- Polygamy issues (husband taking second wife without permission)
- Inheritance rights (property succession after death)
- Marriage registration (legal marriage documentation)
- Dower/Mehr (Islamic dower payment obligations)
- Maintenance (financial support for wife and children)
- Parent maintenance (elderly parents' rights to support from children)

### What Ain Bandhu is NOT

- ❌ **NOT a replacement for a lawyer** - Provides information and guidance, not legal representation
- ❌ **NOT legal advice** - Explains rights and procedures, doesn't advise on specific case outcomes
- ❌ **NOT emergency services** - Users in immediate danger should call 999
- ❌ **NOT a case filing service** - Guides users on how to file, but doesn't file on their behalf

---

## Complete Legal Coverage - 12 Intents

### MVP Coverage: 9/12 Fully Working (75%)

**Fully Functional Intents:**

1. **rape_sexual_violence**

   - Sexual assault, rape, molestation, unwanted sexual contact
   - **Key Law**: নারী ও শিশু নির্যাতন দমন আইন ২০০০ (Section 9)
   - **Guidance**: Emergency response, medical evidence collection (DNA test within 72 hours), FIR filing at One Stop Crisis Center, court process

2. **domestic_violence_general**

   - Physical violence, emotional abuse (non-sexual) by family member
   - **Key Law**: পারিবারিক সহিংসতা আইন ২০১০
   - **Guidance**: Protection orders, FIR filing, safety planning, temporary shelter, restraining orders

3. **dowry**

   - Dowry demands, harassment for dowry
   - **Key Law**: যৌতুক নিরোধ আইন ২০১৮
   - **Guidance**: FIR filing, evidence collection (messages, witnesses), legal remedies, punishment provisions

4. **child_marriage**

   - Underage marriage, forced marriage of minors
   - **Key Law**: বাল্যবিবাহ নিরোধ আইন ২০১৭
   - **Guidance**: Prevention mechanisms, reporting to child marriage prevention committee, local government officer duties

5. **divorce_talaq**

   - Divorce, talaq, separation, ending marriage
   - **Key Law**: মুসলিম পারিবারিক আইন অধ্যাদেশ ১৯৬১
   - **Guidance**: Islamic divorce procedures (talaq notice, 90-day iddat period), rights to maintenance and dower, custody considerations

6. **polygamy_second_marriage**

   - Second wife, multiple marriages without permission
   - **Key Law**: মুসলিম পারিবারিক আইন অধ্যাদেশ ১৯৬১ (Section 6)
   - **Guidance**: Permission requirements from arbitration council, legal challenges if permission not obtained, rights of first wife

7. **inheritance_succession**

   - Property inheritance rights after death
   - **Key Law**: উত্তরাধিকার আইন ১৯২৫, মুসলিম আইন
   - **Guidance**: Islamic succession rules, women's inheritance shares, legal process to claim inheritance

8. **marriage_registration**

   - Registering a marriage officially
   - **Key Law**: মুসলিম বিবাহ ও তালাক (নিবন্ধন) আইন ১৯৭৪
   - **Guidance**: Legal requirements (kabin nama), registration process, documents needed, costs

9. **dower_mehr**
   - Dower/mehr payment obligations
   - **Key Law**: মুসলিম আইন (দেনমোহর)
   - **Guidance**: Mehr rights, enforcement mechanisms if husband refuses payment, legal recourse

**Partially Working Intents** (need explicit legal terms in query):

10. **custody**

    - Child custody, guardianship after divorce/separation
    - **Key Law**: অভিভাবকত্ব ও প্রতিপালন আইন ১৮৯০, পারিবারিক আদালত অধ্যাদেশ ১৯৮৫
    - **Guidance**: Custody rights (mother until age 7 for son, puberty for daughter), family court process, factors courts consider
    - **Workaround**: Works if query mentions "হেফাজত সংক্রান্ত আইন" (custody-related law)

11. **maintenance**

    - Financial support, alimony, child support
    - **Key Law**: মুসলিম বিবাহবিচ্ছেদ আইন ১৯৩৯, পারিবারিক আদালত অধ্যাদেশ ১৯৮৫
    - **Guidance**: Wife's rights to maintenance during marriage and after divorce, child support obligations, enforcement through family court
    - **Workaround**: Works if query mentions "ভরণপোষণ আইন" (maintenance law)

12. **parent_maintenance**
    - Children's duty to care for elderly parents
    - **Key Law**: পিতামাতার ভরণপোষণ আইন ২০১৩
    - **Guidance**: Parents' legal rights to support from children, how to file case in family court
    - **Workaround**: Works but sometimes conflated with "maintenance" intent

**Note for Frontend**: These limitations are backend AI model constraints. Users can still get help by using explicit legal terminology. Future backend improvements will enhance detection.

---

## User Personas (Detailed)

### Primary Persona: Fatima - Domestic Violence Survivor

**Demographics:**

- **Age**: 28 years old
- **Location**: Mirpur, Dhaka (urban slum)
- **Education**: SSC passed (10 years of schooling)
- **Language**: Bangla (some English words, but uncomfortable with English-only content)
- **Occupation**: Garment worker (monthly income ~12,000 BDT)
- **Tech Literacy**: Medium
  - Uses Facebook daily (2-3 hours/day)
  - WhatsApp for family communication
  - Knows how to browse websites on mobile
  - Has used government e-services once (NID card)
- **Device**: Android smartphone (low-end, Samsung/Xiaomi)
- **Internet**: Mobile data (1GB/day package, sometimes runs out)

**Family Situation:**

- Married for 5 years
- Husband is a rickshaw puller (income irregular)
- 2 children (son age 4, daughter age 2)
- Lives with in-laws (joint family)
- Husband beats her when drinking
- Mother-in-law blames her for "provoking" him

**Crisis Moment**:
Last night, husband came home drunk and beat her severely. She has bruises on her arms and face. He threatened to "finish her" if she tells anyone. She's terrified but doesn't know where to go or what to do.

**Goals:**

1. **Immediate**: Understand if she can file a police case without her husband knowing
2. **Short-term**: Get a protection order to prevent further violence
3. **Medium-term**: Understand her rights to custody and maintenance if she leaves
4. **Long-term**: Legal separation or divorce if violence continues

**Pain Points:**

- Doesn't know legal terminology ("FIR" is unfamiliar, "protection order" is foreign)
- Afraid police won't take her seriously ("this is a family matter")
- Worried husband will discover she's researching legal options (phone privacy)
- Ashamed to discuss abuse with strangers (cultural stigma)
- Can't afford a lawyer (₹5,000-10,000 consultation fee is 50% of her monthly income)
- Doesn't trust free legal aid (thinks it's low quality or will take months)

**Behavior Pattern:**

- Searches late at night when husband is asleep (11pm-1am)
- Deletes browser history immediately after
- Prefers reading to talking (scared someone will overhear)
- Needs clear, step-by-step instructions (overwhelmed by complexity)
- Responds to empathy and validation ("this is not your fault")

**How Ain Bandhu Helps:**

- Available 24/7 (she can access at midnight)
- Anonymous (no login, no phone number required)
- Free (no financial barrier)
- Bengali language (understands her perfectly)
- Step-by-step guidance (where to go tomorrow morning, what to say)
- Safety-first (asks if she's safe, provides emergency numbers)
- Obstacle resolution (prepares her for police refusal scenario)

---

### Secondary Persona: Ayesha - Rape Survivor (Time-Critical)

**Demographics:**

- **Age**: 19 years old
- **Location**: Comilla (rural area, 2 hours from Dhaka)
- **Education**: HSC (12 years, currently in college)
- **Language**: Bangla only (very limited English)
- **Occupation**: Student
- **Tech Literacy**: High
  - Active on Facebook, Instagram, TikTok
  - Uses YouTube for study tutorials
  - Comfortable with apps and websites
- **Device**: Mid-range Android phone (Realme/Oppo)
- **Internet**: Home WiFi + mobile data

**Crisis Moment:**
Was raped by her cousin yesterday evening at a family gathering. She hasn't told anyone yet. She's in shock, doesn't know what to do. It's been 18 hours since the incident.

**Goals:**

1. **URGENT**: Understand if she should go to hospital for medical examination (within 72 hours for DNA evidence)
2. **URGENT**: Know where to go and what to say without telling her family
3. **Short-term**: File FIR against cousin
4. **Long-term**: Get justice through court process

**Pain Points:**

- Time-critical (only 54 hours left for DNA evidence collection)
- Severe social stigma (rape victim = "damaged goods" in her community)
- Family pressure expected (they'll ask her to stay silent to protect family honor)
- Doesn't know where One Stop Crisis Center is
- Afraid doctor will refuse examination without police FIR
- Worried about legal process (will she have to face her cousin in court?)

**How Ain Bandhu Helps:**

- IMMEDIATELY flags urgency (asks "when did this happen?")
- Prioritizes medical evidence ("go to hospital WITHIN 72 HOURS")
- Provides exact location of nearest OCC (Comilla Medical College Hospital)
- Explains process (medical exam first, then FIR - order matters!)
- Gives her script ("I was sexually assaulted. I need DNA test and examination for court evidence")
- Prepares her for obstacles (family pressure, doctor questions)
- Provides helpline numbers (BNWLA, ASK) for accompaniment

---

### Tertiary Persona: Shapla - Elderly Mother Seeking Maintenance

**Demographics:**

- **Age**: 65 years old
- **Location**: Sylhet (urban area)
- **Education**: Primary school only (5 years, limited literacy)
- **Language**: Bangla (Sylheti dialect), cannot read English
- **Occupation**: Homemaker (never worked outside home)
- **Tech Literacy**: Very low
  - Can make phone calls
  - Daughter helps her use apps
  - Cannot type well (uses voice typing on WhatsApp)
  - Needs help reading long texts
- **Device**: Basic smartphone (daughter's old phone)
- **Internet**: Uses daughter's mobile hotspot

**Family Situation:**

- Widowed 3 years ago (husband was a shopkeeper)
- Has 3 adult children (2 sons, 1 daughter)
- Sold small house after husband's death, gave money to sons for business
- Now sons refuse to support her financially
- Living with daughter (son-in-law is unhappy about it)
- No income, no savings left

**Crisis Moment:**
Daughter's husband has given ultimatum: "Your mother needs to go live with your brothers. We can't afford her." Daughter is crying, Shapla feels like a burden. She heard from a neighbor that there's a law where children must support parents, but doesn't know how to use it.

**Goals:**

1. Confirm if law exists (পিতামাতার ভরণপোষণ আইন)
2. Understand if she can force sons to support her
3. Learn simple procedure to file case
4. Not destroy family relationships if possible

**Pain Points:**

- Limited reading ability (can read simple Bangla, but long paragraphs are hard)
- Doesn't understand legal terminology
- Daughter is helping her use the chatbot
- Emotionally distressed (feels like burden, cries easily)
- Culturally hesitant (suing your own children feels wrong)
- No money for lawyer

**How Ain Bandhu Helps:**

- Uses VERY simple Bangla (primary school level)
- Short sentences, clear structure
- Asks "Do you have someone helping you?" (acknowledges daughter's presence)
- Explains law exists (reassures her)
- Gentle about family court (frames as "legal request" not "suing")
- Lists exact documents needed (NID, proof she has no income)
- Provides family court address in Sylhet
- Suggests mediation through Union Parishad first (less confrontational)

---

## Core Features - What Makes This Different

### Feature 1: Lawyer-Like Strategic Dialogue (P0 - Must Have)

**Why This Matters**: Real lawyers don't just answer questions. They ASK strategic questions to assess the case before giving advice.

**Backend Implementation** (already built):
The backend AI is prompted to act like a lawyer:

1. Ask clarifying questions ("When did this happen?" "Are you safe right now?" "Do you have witnesses?")
2. Assess case urgency (time-critical for rape evidence, immediate danger for DV)
3. Prioritize based on context (safety before legal procedure)
4. Provide personalized advice (based on user's specific situation)

**Frontend Requirements**:

- Display AI's questions prominently (make them feel like a conversation, not interrogation)
- Allow multi-turn dialogue (user answers questions, AI asks follow-ups)
- Show conversational flow (don't treat each message as independent Q&A)
- Visual indicators when AI is "thinking" or "assessing" the case

**Example Conversation Flow**:

```
[User]: আমার স্বামী আমাকে মারে। (My husband beats me.)

[AI]: আমি দুঃখিত আপনি এই পরিস্থিতিতে আছেন। আমাকে কিছু প্রশ্ন করতে দিন যাতে আমি আপনাকে সঠিক পরামর্শ দিতে পারি।

**প্রথম প্রশ্ন: আপনি কি এখন নিরাপদ?** আপনার স্বামী কি এখন বাড়িতে আছেন?

[User]: না, তিনি এখন বাইরে গেছেন। (No, he went outside.)

[AI]: ভালো। আমরা কথা বলার সময় আছে।

**দ্বিতীয় প্রশ্ন: এটি কখন ঘটেছিল?** সর্বশেষ কখন তিনি আপনাকে মেরেছেন?

[User]: গতকাল রাতে। আমার হাতে দাগ আছে। (Last night. I have marks on my arms.)

[AI]: বুঝেছি। **শারীরিক আঘাতের প্রমাণ থাকা খুবই গুরুত্বপূর্ণ।**

**তৃতীয় প্রশ্ন: কেউ কি এটি দেখেছিল?** কোনো সাক্ষী আছে?

[User]: আমার শাশুড়ি দেখেছিলেন, কিন্তু তিনি কিছু বলেননি। (My mother-in-law saw, but she didn't say anything.)

[AI]: ঠিক আছে। আমি এখন আপনার পরিস্থিতি বুঝতে পেরেছি। আপনার তিনটি আইনি বিকল্প আছে:

১. **তাৎক্ষণিক সুরক্ষা আদেশ** (Protection Order)
২. **থানায় FIR** (First Information Report)
৩. **পারিবারিক আদালতে মামলা** (Family Court case)

আমি আপনার জন্য প্রথম বিকল্পটি সুপারিশ করছি কারণ...
```

**Frontend Display Challenge**:

- Don't make it feel like a form (Q1, Q2, Q3...)
- Make it feel like a caring professional asking questions
- Show AI is listening (acknowledge answers before asking next question)
- Visual threading (connect questions to answers visually)

---

### Feature 2: Safety-First Approach (P0 - Must Have)

**Why This Matters**: In domestic violence and rape cases, user safety is paramount. Legal procedure is secondary.

**Backend Implementation** (already built):

- AI ALWAYS asks "আপনি কি এখন নিরাপদ?" (Are you safe right now?) for DV/rape intents
- Prioritizes emergency contacts (999, 10921, One Stop Crisis Center) before legal steps
- Detects keywords indicating immediate danger ("হত্যার হুমকি", "ছুরি", "আবার মারবে")
- Provides safety planning (where to go, what to pack, who to call)

**Frontend Requirements**:

1. **Emergency Contact Bar** (sticky, always visible):

   ```
   জরুরি অবস্থায়: ৯৯৯ (জাতীয় জরুরি সেবা) | ১০৯২১ (নারী ও শিশু হেল্পলাইন)
   ```

2. **Danger Detection Visual**:

   - When AI detects danger keywords, highlight response in orange/red
   - Show large "জরুরি নির্দেশনা" (Emergency Guidance) header
   - Make emergency contacts clickable (one-tap call on mobile)

3. **Quick Exit Button** (for users in danger):

   - Button in header: "দ্রুত বন্ধ করুন" (Quick Exit)
   - Clicking redirects to innocent website (weather.com or Google)
   - Clears recent chat from localStorage (privacy protection)

4. **Safety Notice** (if user mentions abuse):
   - Banner: "আপনার নিরাপত্তা সবচেয়ে গুরুত্বপূর্ণ। এই কথোপকথন মুছে ফেলার কথা মনে রাখবেন।"
   - (Your safety is most important. Remember to delete this conversation.)

---

### Feature 3: Procedural Guidance - Step-by-Step (P0 - Must Have)

**Why This Matters**: Knowing "you have rights" is useless. Women need "Go to X police station tomorrow morning. Say Y. Bring Z documents."

**Backend Implementation** (already built):
The `get_procedural_guidance` tool provides:

- **Exact steps** (numbered list: Step 1, Step 2, etc.)
- **Where to go** (specific office: "নিকটতম থানা চিহ্নিত করুন" - identify nearest police station)
- **What to say** (exact phrases: "আমি একটি FIR দায়ের করতে চাই")
- **Documents needed** (list: জাতীয় পরিচয়পত্র, মেডিকেল রিপোর্ট)
- **Costs** ("বিনামূল্যে - FIR করার জন্য কোনো টাকা লাগে না")
- **Timeline** ("সাধারণত ৭-১৫ দিনের মধ্যে তদন্ত শুরু হয়")

**Frontend Requirements**:

1. **Structured Display** of procedural steps:

   ```
   ✓ ধাপ ১: নিকটতম থানা চিহ্নিত করুন
     বিস্তারিত: যে এলাকায় অপরাধ ঘটেছে সেই এলাকার থানায় যান।
     টিপস: থানার ঠিকানা ও ফোন নম্বর আগে থেকে নোট করুন।

   ✓ ধাপ ২: থানায় গিয়ে FIR করতে চান বলুন
     কী বলবেন: "আমি একটি FIR দায়ের করতে চাই"
     টিপস: বিনয়ী কিন্তু দৃঢ় থাকুন। এটি আপনার অধিকার।
   ```

2. **Checklist Format** (for documents/requirements):

   - Use checkbox visual (even if not interactive)
   - Helps users prepare before taking action

3. **Cost Transparency**:

   - Clearly show "বিনামূল্যে" (Free) where applicable
   - Warn if costs expected ("আনুমানিক খরচ: ৫০০-১০০০ টাকা")

4. **Printable/Shareable Format** (future):
   - Option to "save as PDF" or "copy text"
   - User can show to helper/friend

---

### Feature 4: Obstacle Resolution Guidance (P0 - Must Have)

**Why This Matters**: Police often refuse to file FIR for "family matters". Users need to know how to handle this.

**Backend Implementation** (already built):
Procedural knowledge includes "common_obstacles" section:

```json
{
  "obstacle": "পুলিশ বলছে 'এটি পারিবারিক বিষয়, ঘরে গিয়ে মিটমাট করুন'",
  "solution": "বলুন: 'এটি অপরাধ, আইনত আপনি FIR নিতে বাধ্য।' OC এর সাথে কথা বলার দাবি করুন। BNWLA বা ASK এ কল করুন সাহায্যের জন্য।",
  "legal_backing": "ফৌজদারি কার্যবিধি ১৮৯৮ এর ধারা ১৫৪ অনুযায়ী পুলিশ FIR নিতে বাধ্য"
}
```

**Frontend Requirements**:

1. **Expandable "What if..." Sections**:

   ```
   ▼ সাধারণ সমস্যা এবং সমাধান

   ❓ যদি পুলিশ FIR নিতে অস্বীকার করে?
     → সমাধান: [expandable content]

   ❓ যদি পুলিশ বলে "এটি পারিবারিক বিষয়"?
     → সমাধান: [expandable content]

   ❓ যদি আমি ভয় পাই?
     → সমাধান: [expandable content]
   ```

2. **Escalation Path Visual**:

   - Show escalation ladder (try A, if fails try B, if fails try C)
   - Example: OC → থানার অভিযোগ বই → সুপার অফ পুলিশ → ম্যাজিস্ট্রেট

3. **Legal Backing Citation**:
   - Small text citing which law supports user's rights
   - Builds confidence ("you're not making this up, it's the law")

---

### Feature 5: Support Organization Directory (P1 - Should Have)

**Backend Implementation** (planned but check if built):
Provides contact info for:

- **Legal Aid**: BNWLA, ASK, BLAST
- **Emergency**: 999, 10921
- **One Stop Crisis Centers**: Locations by district
- **Shelters**: Safe houses for DV survivors

**Frontend Requirements**:

1. **Quick Access Panel** (sidebar or bottom sheet):

   ```
   📞 সহায়ক সংস্থা

   জরুরি
   🆘 ৯৯৯ (জাতীয় জরুরি)
   👩 ১০৯২১ (নারী ও শিশু হেল্পলাইন)

   আইনি সহায়তা
   ⚖️ BNWLA: [phone]
   ⚖️ ASK: [phone]
   ⚖️ BLAST: [phone]

   ওয়ান স্টপ ক্রাইসিস সেন্টার
   🏥 ঢাকা মেডিকেল কলেজ: [address]
   🏥 মিটফোর্ড হাসপাতাল: [address]
   ```

2. **Click-to-Call** on mobile (tel: links)

3. **Location-Based** (future):
   - Ask user's district
   - Show nearest OCC/legal aid office

---

### Feature 6: Structured Response Pattern (P0 - Already Implemented in Backend)

**Backend Response Structure**:
All AI responses follow this pattern:

1. **Empathy** - Acknowledges user's situation
2. **Law** - Explains relevant legal rights
3. **Steps** - Procedural guidance (what to do)
4. **Evidence** - What to collect/document
5. **Process** - Timeline and what to expect
6. **Support** - Organizations that can help

**Frontend Requirements**:

1. **Visual Sections** (optional enhancement):

   - Use subtle headers or icons to mark sections
   - Makes long responses easier to scan
   - Example:
     ```
     💙 [Empathy section]
     ⚖️ আপনার আইনি অধিকার
     📋 পদক্ষেপসমূহ
     📄 প্রয়োজনীয় প্রমাণ
     ⏱️ সময়রেখা
     🤝 সহায়তা সংস্থা
     ```

2. **Readable Formatting**:
   - Preserve line breaks from backend
   - Render numbered lists clearly
   - Bullet points for items

---

## API Integration Specification

### Base URL

```
Production: https://final-family-law-production.up.railway.app
Local Dev: http://localhost:8000
```

### Authentication

- ✅ None required for MVP
- ✅ All endpoints are public
- ✅ Anonymous but persistent tracking via session_id (stored in localStorage)

### Important Backend Architecture Notes

- Backend uses **profile-based tracking** internally (profile_id)
- API still uses `session_id` for frontend compatibility
- **Conversation history**: Backend stores up to 50 messages per profile
- **Smart context management**: Conversations >10 messages automatically summarize old context (transparent to frontend)
- **Persistence**: Same session_id = conversation continues from where it left off

---

### API Endpoint 1: POST /chat/new

**Purpose**: Initialize a new conversation and receive Bengali greeting

**Request**:

```http
POST /chat/new
Content-Type: application/json

{
  "metadata": {}
}
```

**Request Fields**:

- `metadata` (optional): Any additional context you want to track (can be empty object or omitted)

**Response**:

```json
{
  "session_id": "d0d40c64-de81-4606-beea-c1512209a098",
  "greeting": "আসসালামু আলাইকুম। আমি আইন বন্ধু, আপনার আইনি সহায়ক। আপনি কি ধরনের আইনি সমস্যার মুখোমুখি?",
  "timestamp": "2025-11-26T05:08:49.393051"
}
```

**Frontend Implementation**:

```javascript
const createNewSession = async () => {
  const response = await fetch(
    "https://final-family-law-production.up.railway.app/chat/new",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ metadata: {} }),
    }
  );

  const data = await response.json();

  // Store session_id in localStorage for persistence
  localStorage.setItem("ain_bandhu_session_id", data.session_id);

  return data;
};

// IMPORTANT: Session Management Strategy
// 1. On first visit: Create new session, store session_id
// 2. On return visit: Retrieve session_id from localStorage
// 3. User can manually start new conversation (creates new session_id)
// 4. Same session_id = conversation history is maintained
```

---

### API Endpoint 2: POST /chat

**Purpose**: Send user message and receive AI lawyer's response

**Request**:

```http
POST /chat
Content-Type: application/json

{
  "session_id": "d0d40c64-de81-4606-beea-c1512209a098",
  "message": "আমার স্বামী আমাকে মারে। আমি কি করতে পারি?"
}
```

**Request Fields**:

- `session_id` (required): Session ID from /chat/new or localStorage
- `message` (required): User's message (1-1000 characters, Bengali or English)

**Response**:

```json
{
  "session_id": "d0d40c64-de81-4606-beea-c1512209a098",
  "response": "আমি দুঃখিত যে আপনি এই পরিস্থিতিতে আছেন...\n\n**প্রথম প্রশ্ন: আপনি কি এখন নিরাপদ?**...",
  "intent": "domestic_violence_general",
  "urgency": null,
  "tools_used": ["get_legal_knowledge", "get_procedural_guidance"],
  "timestamp": "2025-11-26T05:09:15.123456"
}
```

**Response Fields**:

- `session_id` (string): Same session ID echoed back
- `response` (string): AI's response in Bengali (may contain markdown-like formatting)
- `intent` (string | null): Detected legal intent (one of 12 intents, or null if unclear)
- `urgency` (string | null): Urgency level - "critical" | "high" | "medium" | "low" | null
- `tools_used` (string[]): List of tools the AI called (e.g., ["get_legal_knowledge", "get_procedural_guidance"])
- `timestamp` (string): ISO timestamp of response

**AI Response Patterns to Expect**:

1. **Strategic Questions** (multi-turn):

   ```
   "আমাকে কিছু প্রশ্ন করতে দিন:"
   "প্রথম প্রশ্ন: আপনি কি এখন নিরাপদ?"
   "দ্বিতীয় প্রশ্ন: এটি কখন ঘটেছিল?"
   ```

2. **Safety Checks** (urgent cases):

   ```
   "⚠️ জরুরি: আপনি যদি এখন বিপদে থাকেন, অবিলম্বে ৯৯৯ নম্বরে কল করুন।"
   ```

3. **Numbered Steps**:

   ```
   "ধাপ ১: নিকটতম থানা চিহ্নিত করুন"
   "ধাপ ২: থানায় গিয়ে FIR করতে চান বলুন"
   ```

4. **Bold Emphasis** (markdown-like):
   ```
   "**গুরুত্বপূর্ণ:** এটি আপনার অধিকার।"
   ```

**Frontend Parsing**:

- Detect and render `**bold text**` as bold
- Preserve line breaks (`\n`)
- Detect numbered lists (ধাপ ১, ধাপ ২) and format accordingly
- Detect emoji/warning symbols and highlight

---

### API Endpoint 3: GET /health

**Purpose**: Check if backend is healthy (for monitoring, debugging)

**Request**:

```http
GET /health
```

**Response**:

```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2025-11-26T20:15:00.123456"
}
```

**Frontend Usage**:

```javascript
const checkBackendHealth = async () => {
  try {
    const response = await fetch(
      "https://final-family-law-production.up.railway.app/health"
    );
    const data = await response.json();
    return data.status === "healthy";
  } catch (error) {
    return false; // Backend down
  }
};

// Optional: Show offline banner if backend is down
```

---

### Complete Implementation Example

**Full Chat Component with All Features**:

```javascript
import { useState, useEffect, useRef } from "react";

const AinBandhuChat = () => {
  const [sessionId, setSessionId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const BASE_URL = "https://final-family-law-production.up.railway.app";

  // Initialize session on component mount
  useEffect(() => {
    const initSession = async () => {
      // Check if we have an existing session
      const existingSessionId = localStorage.getItem("ain_bandhu_session_id");

      if (existingSessionId) {
        setSessionId(existingSessionId);
        // Optionally: Load conversation history from localStorage
      } else {
        // Create new session
        try {
          const response = await fetch(`${BASE_URL}/chat/new`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ metadata: {} }),
          });

          const data = await response.json();
          setSessionId(data.session_id);
          localStorage.setItem("ain_bandhu_session_id", data.session_id);

          // Add greeting message
          setMessages([
            {
              role: "assistant",
              content: data.greeting,
              timestamp: data.timestamp,
            },
          ]);
        } catch (error) {
          console.error("Failed to create session:", error);
        }
      }
    };

    initSession();
  }, []);

  // Auto-scroll to bottom
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!inputMessage.trim() || !sessionId) return;

    const userMessage = {
      role: "user",
      content: inputMessage,
      timestamp: new Date().toISOString(),
    };

    // Add user message immediately
    setMessages((prev) => [...prev, userMessage]);
    setInputMessage("");
    setIsLoading(true);

    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 30000);

      const response = await fetch(`${BASE_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          session_id: sessionId,
          message: userMessage.content,
        }),
        signal: controller.signal,
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        throw new Error("Failed to get response");
      }

      const data = await response.json();

      // Add assistant message
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: data.response,
          intent: data.intent,
          urgency: data.urgency,
          timestamp: data.timestamp,
        },
      ]);
    } catch (error) {
      if (error.name === "AbortError") {
        setMessages((prev) => [
          ...prev,
          {
            role: "error",
            content: "অনুরোধটি অনেক সময় নিচ্ছে। দয়া করে আবার চেষ্টা করুন।",
            timestamp: new Date().toISOString(),
          },
        ]);
      } else {
        console.error("Error sending message:", error);
        setMessages((prev) => [
          ...prev,
          {
            role: "error",
            content:
              "দুঃখিত, একটি সমস্যা হয়েছে। অনুগ্রহ করে আবার চেষ্টা করুন।",
            timestamp: new Date().toISOString(),
          },
        ]);
      }
    } finally {
      setIsLoading(false);
    }
  };

  const formatMessage = (content) => {
    // Convert **bold** to <strong>
    return content
      .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
      .replace(/\n/g, "<br />");
  };

  return (
    <div className="chat-container">
      <div className="messages">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message message-${msg.role}`}>
            <div
              className="message-content"
              dangerouslySetInnerHTML={{ __html: formatMessage(msg.content) }}
            />
            {msg.urgency === "critical" && (
              <div className="urgency-badge critical">জরুরি</div>
            )}
          </div>
        ))}
        {isLoading && (
          <div className="message message-loading">
            <div className="typing-indicator">আইন বন্ধু লিখছে...</div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="input-container">
        <textarea
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          onKeyPress={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              sendMessage();
            }
          }}
          placeholder="আপনার আইনি সমস্যা লিখুন..."
          disabled={isLoading}
          maxLength={1000}
        />
        <button
          onClick={sendMessage}
          disabled={isLoading || !inputMessage.trim()}
        >
          পাঠান
        </button>
      </div>
    </div>
  );
};

export default AinBandhuChat;
```

---

### Error Handling & Edge Cases

**Timeout (30s)**:

```javascript
const sendMessage = async (sessionId, message) => {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 30000);

  try {
    const response = await fetch(
      "https://final-family-law-production.up.railway.app/chat",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ session_id: sessionId, message }),
        signal: controller.signal,
      }
    );

    clearTimeout(timeoutId);
    return await response.json();
  } catch (error) {
    clearTimeout(timeoutId);
    if (error.name === "AbortError") {
      throw new Error("অনুরোধটি অনেক সময় নিচ্ছে। দয়া করে আবার চেষ্টা করুন।");
    }
    throw error;
  }
};
```

**Session Invalid**:

```javascript
if (response.status === 404) {
  // Session doesn't exist, create new one
  const newSession = await createNewSession();
  // Retry message with new session
}
```

---

## User Flows & Conversation Patterns

### Flow 1: Domestic Violence - Strategic Questioning

```
[Page loads, auto-creates session]

BOT: আসসালামু আলাইকুম। আমি আইন বন্ধু, আপনার আইনি সহায়ক। আপনি কি ধরনের আইনি সমস্যার মুখোমুখি?

USER: আমার স্বামী আমাকে মারে।

BOT: আমি দুঃখিত যে আপনি এই পরিস্থিতিতে আছেন। গৃহ নির্যাতন একটি গুরুতর অপরাধ এবং আপনার আইনি সহায়তা পাওয়ার অধিকার আছে।

আমাকে কিছু প্রশ্ন করতে দিন যাতে আমি আপনাকে সঠিক পরামর্শ দিতে পারি।

**প্রথম প্রশ্ন: আপনি কি এখন নিরাপদ?** আপনার স্বামী কি এখন বাড়িতে আছেন?

USER: না, তিনি বাইরে গেছেন।

BOT: ভালো। আমরা কথা বলার সময় আছে।

**দ্বিতীয় প্রশ্ন: এটি কখন ঘটেছিল?** সর্বশেষ কখন তিনি আপনাকে মেরেছেন?

USER: গতকাল রাতে। আমার হাতে দাগ আছে।

BOT: বুঝেছি। শারীরিক আঘাতের প্রমাণ থাকা খুবই গুরুত্বপূর্ণ।

**তৃতীয় প্রশ্ন: কেউ কি এটি দেখেছিল?** কোনো সাক্ষী আছে?

USER: আমার শাশুড়ি দেখেছিলেন।

BOT: ঠিক আছে। আমি এখন আপনার পরিস্থিতি বুঝতে পেরেছি।

আপনার **তিনটি আইনি বিকল্প** আছে:

১. **সুরক্ষা আদেশ** (Protection Order) - দ্রুততম, ৭ দিনের মধ্যে
২. **থানায় FIR** - অপরাধ নিবন্ধন, তদন্ত শুরু হবে
৩. **পারিবারিক আদালতে মামলা** - দীর্ঘমেয়াদী সমাধান

আমি আপনার জন্য **সুরক্ষা আদেশ** সুপারিশ করছি কারণ:
- ⏱️ দ্রুত (৭ দিন)
- 💰 খরচ কম (আনুমানিক ৫০০ টাকা)
- 🛡️ আপনাকে অবিলম্বে সুরক্ষা দেবে

আপনি কি সুরক্ষা আদেশ কীভাবে পাবেন তা জানতে চান?

USER: হ্যাঁ

BOT: [Provides step-by-step procedure for protection order]
```

**Frontend Design Note**:

- This multi-turn conversation should feel natural
- Each bot message builds on previous context
- Don't show "session restarted" or other tech messages
- Make questions stand out (bold, color, or icon)

---

### Flow 2: Rape - Time-Critical Urgency

```
USER: আমি গতকাল ধর্ষণের শিকার হয়েছি।

BOT: ⚠️ **আমি গভীরভাবে দুঃখিত এই ঘটনা ঘটেছে। আপনার সাহস আছে যে আপনি সাহায্য খুঁজছেন।**

এটি খুবই **সময়-সংবেদনশীল** পরিস্থিতি।

**প্রথম এবং সবচেয়ে গুরুত্বপূর্ণ:**
আপনাকে **৭২ ঘণ্টার মধ্যে** (৩ দিন) মেডিকেল পরীক্ষা করাতে হবে DNA প্রমাণ সংগ্রহের জন্য। এখন প্রায় **১৮ ঘণ্টা** হয়ে গেছে, আপনার কাছে এখনও **৫৪ ঘণ্টা** আছে।

**এখনই করণীয়:**

1. **নিকটতম ওয়ান স্টপ ক্রাইসিস সেন্টার (OCC) এ যান**
   - যেকোনো সরকারি মেডিকেল কলেজ হাসপাতালে আছে
   - আপনি কোন এলাকায়?

USER: ঢাকা

BOT: **ঢাকায় OCC:**
- ঢাকা মেডিকেল কলেজ হাসপাতাল (বকশীবাজার)
- মিটফোর্ড হাসপাতাল

**এখন সকাল ১০টা, আপনি আজই যেতে পারবেন।**

**OCC এ গিয়ে এভাবে বলুন:**
"আমি গতকাল যৌন নির্যাতনের শিকার হয়েছি। আমার DNA পরীক্ষা এবং মেডিকেল পরীক্ষা প্রয়োজন আদালতের প্রমাণের জন্য।"

**আপনার জন্য OCC কী করবে:**
✓ বিনামূল্যে মেডিকেল পরীক্ষা
✓ DNA স্যাম্পল সংগ্রহ (প্রমাণ)
✓ মেডিকেল সার্টিফিকেট
✓ FIR ফাইল করতে সাহায্য
✓ মানসিক পরামর্শ
✓ প্রয়োজনে অস্থায়ী আশ্রয়

**⚠️ গুরুত্বপূর্ণ: FIR করার আগে মেডিকেল পরীক্ষা করান। ক্রম গুরুত্বপূর্ণ!**

আপনার কি কেউ আছে যে আপনার সাথে হাসপাতালে যেতে পারবে?

[Continues with procedural guidance, emotional support, legal process explanation]
```

**Frontend Design Note**:

- **URGENT** messages should be visually distinct (red/orange border, warning icon)
- Countdown timer showing "54 hours left" could be powerful (but sensitive)
- Make emergency contacts (OCC addresses) prominent and copyable
- Large, clear "এখন কল করুন" (Call Now) buttons

---

### Flow 3: Custody - Partial Intent Detection

```
USER: তালাকের পর আমার সন্তানের হেফাজত কীভাবে পাব?

BOT: [Generic response without tool calling, less detailed]

USER: তালাকের পর সন্তানের হেফাজত সংক্রান্ত আইন কী?

BOT: [NOW tools are called, detailed legal info provided]
```

**Frontend Solution**:

- Add helper text below input field:

  - "টিপস: 'হেফাজত আইন', 'ভরণপোষণ আইন' এর মতো আইনি শব্দ ব্যবহার করুন আরও বিস্তারিত তথ্যের জন্য"
  - (Tip: Use legal terms like 'হেফাজত আইন', 'ভরণপোষণ আইন' for more detailed information)

- Suggested prompts (buttons):
  - "সন্তানের হেফাজত আইন সম্পর্কে জানতে চাই"
  - "ভরণপোষণ আইন কী?"
  - "পিতামাতার ভরণপোষণ আইন"

---

## UI/UX Requirements

(Keeping the previous draft's UI specs, but adding more based on new understanding)

### Design Principles

1. **Empathy First**: This isn't a legal database, it's a friend helping you
2. **Simplicity**: One action at a time, no overwhelming choices
3. **Trust**: Professional design, accurate information, no spam
4. **Accessibility**: Works on cheap Android phones with slow internet
5. **Privacy**: No login, minimal tracking, easy to erase evidence
6. **Safety**: Quick exit button, emergency contacts always visible

---

### Visual Design (Enhanced)

**Color Palette**:

```
Primary (Legal/Trust):      #2D5F3F (Deep green - Bangladesh legal system)
Secondary (Hope):            #4A9D6F (Lighter green)
Urgent/Danger:               #D32F2F (Red - for emergency messages)
Warning:                     #F57C00 (Orange - for time-critical)
User Message:                #DCF8C6 (Light green - WhatsApp style, familiar)
Bot Message:                 #FFFFFF (White, professional)
Background:                  #F5F5F5 (Light grey) or #E8F5E9 (Very light green)
Text Primary:                #2C2C2C (Almost black, readable)
Text Secondary:              #666666 (Grey, for timestamps)
Success:                     #388E3C (Green checkmark)
Border:                      #E0E0E0 (Light grey)
```

**Typography**:

```
Primary Font:    Noto Sans Bengali (Google Fonts - free, great Bengali rendering)
Fallback:        'Kalpurush', 'Solaiman Lipi', system-ui, sans-serif

Sizes:
  App Title:       28px (bold) - আইন বন্ধু
  Section Headers: 20px (medium) - **আপনার আইনি অধিকার**
  Body Text:       17px (regular) - Main responses
  Steps/Lists:     16px (regular)
  Timestamps:      13px (light)
  Helper Text:     14px (regular, grey)

Line Height:     1.7 (Bengali needs more spacing than English)
Letter Spacing:  0.3px (slight increase for readability)
```

---

### New Components Based on Feature Understanding

#### Component: Strategic Question Display

**Purpose**: Make AI's questions feel conversational, not interrogative

```html
<div class="ai-question-block">
  <div class="question-context">
    <p>আমাকে কিছু প্রশ্ন করতে দিন যাতে আমি আপনাকে সঠিক পরামর্শ দিতে পারি।</p>
  </div>

  <div class="question-item">
    <span class="question-number">প্রথম প্রশ্ন:</span>
    <span class="question-text">আপনি কি এখন নিরাপদ?</span>
  </div>
</div>
```

**Styling**:

- Slightly larger font for the question text (18px)
- Question number in secondary color
- Gentle background highlight (very light green)
- Indent the question to show it's part of a flow

---

#### Component: Emergency Alert

**Purpose**: Highlight urgent safety information

```html
<div class="emergency-alert">
  <div class="alert-icon">⚠️</div>
  <div class="alert-content">
    <p class="alert-title">জরুরি নির্দেশনা</p>
    <p class="alert-message">
      আপনি যদি এখন বিপদে থাকেন, অবিলম্বে ৯৯৯ নম্বরে কল করুন।
    </p>
    <button class="call-button" onclick="window.location.href='tel:999'">
      ৯৯৯ তে কল করুন
    </button>
  </div>
</div>
```

**Styling**:

- Red/orange background (#FFF3E0 light orange)
- Border: 2px solid #F57C00 (orange)
- Large icon (24px)
- Call button: Red background, white text, large touch target (48px height)

---

#### Component: Procedural Steps

**Purpose**: Display step-by-step instructions clearly

```html
<div class="procedure-steps">
  <div class="step">
    <div class="step-header">
      <span class="step-number">ধাপ ১</span>
      <span class="step-title">নিকটতম থানা চিহ্নিত করুন</span>
    </div>
    <div class="step-details">
      <p class="detail-text">যে এলাকায় অপরাধ ঘটেছে সেই এলাকার থানায় যান।</p>
      <div class="step-tips">
        <span class="tip-label">টিপস:</span>
        <span class="tip-text">থানার ঠিকানা ও ফোন নম্বর আগে থেকে নোট করুন</span>
      </div>
    </div>
  </div>

  <!-- Repeat for each step -->
</div>
```

**Styling**:

- Step number: Circular badge with primary color background
- Step title: Bold, slightly larger (18px)
- Indent details under each step
- Tips: Light background (#F5F5F5), smaller font
- Visual connector line between steps (left border)

---

#### Component: Document Checklist

**Purpose**: Show required documents

```html
<div class="document-checklist">
  <p class="checklist-title">প্রয়োজনীয় কাগজপত্র:</p>
  <ul class="checklist-items">
    <li class="checklist-item">
      <span class="checkbox-icon">☐</span>
      <span class="item-text">জাতীয় পরিচয়পত্র</span>
    </li>
    <li class="checklist-item">
      <span class="checkbox-icon">☐</span>
      <span class="item-text">মেডিকেল রিপোর্ট (যদি শারীরিক আঘাত থাকে)</span>
    </li>
    <!-- More items -->
  </ul>
</div>
```

---

#### Component: Quick Exit Button

**Purpose**: Allow users to quickly close app if in danger

```html
<div class="quick-exit-container">
  <button class="quick-exit-btn" onclick="quickExit()">
    <span class="exit-icon">✕</span>
    <span class="exit-text">দ্রুত বন্ধ করুন</span>
  </button>
</div>

<script>
  function quickExit() {
    // Clear conversation history
    localStorage.removeItem("ain_bandhu_session_id");
    localStorage.removeItem("ain_bandhu_messages");

    // Redirect to innocent site
    window.location.replace("https://www.weather.com/");
  }
</script>
```

**Styling**:

- Fixed position in header (top-right)
- Small, not too prominent (don't scare users)
- Red color when hovered
- 40px x 100px touch target

---

#### Component: Support Organization Panel

**Purpose**: Quick access to help resources

```html
<div class="support-panel">
  <button class="panel-toggle" onclick="togglePanel()">📞 সহায়ক সংস্থা</button>

  <div class="panel-content" id="supportPanel" style="display: none;">
    <div class="support-category">
      <h4>জরুরি নম্বর</h4>
      <div class="contact-item">
        <span class="contact-name">জাতীয় জরুরি সেবা</span>
        <a href="tel:999" class="contact-number">৯৯৯</a>
      </div>
      <div class="contact-item">
        <span class="contact-name">নারী ও শিশু হেল্পলাইন</span>
        <a href="tel:10921" class="contact-number">১০৯২১</a>
      </div>
    </div>

    <div class="support-category">
      <h4>আইনি সহায়তা</h4>
      <div class="contact-item">
        <span class="contact-name">BNWLA</span>
        <span class="contact-number">[phone]</span>
      </div>
      <!-- More organizations -->
    </div>
  </div>
</div>
```

---

### Screen Layouts (Updated)

#### Mobile Layout with All Components

```
┌─────────────────────────────────────┐
│  আইন বন্ধু        [দ্রুত বন্ধ করুন] │ Header (64px)
│  [📞 সহায়ক সংস্থা] [নতুন কথোপকথন] │
├─────────────────────────────────────┤
│ [Disclaimer Banner - first visit]   │
├─────────────────────────────────────┤
│ জরুরি: ৯৯৯ | ১০৯২১                 │ Emergency Bar (sticky, 40px)
├─────────────────────────────────────┤
│                                     │
│ BOT: আসসালামু আলাইকুম...          │
│                                     │
│            USER: আমার স্বামী আমাকে │
│                  মারে।              │
│                                     │
│ BOT: [Strategic Question Display]   │
│      প্রথম প্রশ্ন: আপনি কি নিরাপদ? │
│                                     │
│            USER: হ্যাঁ               │
│                                     │
│ BOT: [Procedural Steps Component]   │
│      ধাপ ১: নিকটতম থানা...         │
│      ধাপ ২: ...                     │
│                                     │
│ [Typing indicator if bot is typing] │
│                                     │
│ (Scrollable)                        │
├─────────────────────────────────────┤
│ [Input field: আপনার প্রশ্ন লিখুন...]│ Input (56px)
│ [Send button →]                     │
├─────────────────────────────────────┤
│ টিপস: আইনি শব্দ ব্যবহার করুন      │ Helper (optional, 30px)
└─────────────────────────────────────┘
```

---

## Technical Stack & Architecture

### Recommended: React + Vite + TypeScript + Tailwind

**Why this stack?**

1. **React**: Component-based, perfect for conversational UI
2. **Vite**: Fast development, optimized builds
3. **TypeScript**: Type safety for API integration
4. **Tailwind**: Rapid UI development, mobile-first utilities

**Project Setup**:

```bash
npm create vite@latest ain-bandhu-frontend -- --template react-ts
cd ain-bandhu-frontend
npm install
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

**Key Dependencies**:

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-markdown": "^9.0.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "@vitejs/plugin-react": "^4.2.0",
    "typescript": "^5.3.0",
    "vite": "^5.0.0",
    "tailwindcss": "^3.4.0",
    "autoprefixer": "^10.4.0",
    "postcss": "^8.4.0"
  }
}
```

---

### Project Structure

```
ain-bandhu-frontend/
├── public/
│   ├── favicon.ico
│   └── fonts/
│       └── NotoSansBengali-Regular.woff2
├── src/
│   ├── assets/
│   │   ├── logo.svg
│   │   └── icons/
│   ├── components/
│   │   ├── chat/
│   │   │   ├── ChatMessage.tsx           # Message bubble component
│   │   │   ├── ChatInput.tsx             # Input field + send button
│   │   │   ├── TypingIndicator.tsx       # "লিখছে..." animation
│   │   │   ├── StrategicQuestion.tsx     # AI question display
│   │   │   ├── ProceduralSteps.tsx       # Step-by-step display
│   │   │   └── EmergencyAlert.tsx        # Urgent safety messages
│   │   ├── layout/
│   │   │   ├── Header.tsx                # App header
│   │   │   ├── EmergencyBar.tsx          # Sticky emergency contacts
│   │   │   ├── QuickExit.tsx             # Quick exit button
│   │   │   └── SupportPanel.tsx          # Support organizations
│   │   ├── onboarding/
│   │   │   ├── DisclaimerBanner.tsx      # First-visit disclaimer
│   │   │   └── WelcomeMessage.tsx        # Initial guidance
│   │   └── common/
│   │       ├── Button.tsx
│   │       ├── LoadingSpinner.tsx
│   │       └── ErrorMessage.tsx
│   ├── services/
│   │   ├── api.ts                        # API integration
│   │   └── storage.ts                    # LocalStorage wrapper
│   ├── hooks/
│   │   ├── useChatSession.ts             # Session management
│   │   ├── useLocalStorage.ts            # LocalStorage hook
│   │   └── useMessageFormatter.ts        # Format bot messages
│   ├── types/
│   │   └── index.ts                      # TypeScript types
│   ├── utils/
│   │   ├── formatBengaliText.ts          # Bengali text formatting
│   │   ├── detectUrgency.ts             # Detect emergency keywords
│   │   └── errorMessages.ts             # Error translation map
│   ├── constants/
│   │   ├── emergencyContacts.ts          # 999, 10921, etc.
│   │   └── legalTerms.ts                 # Helper text for intents
│   ├── App.tsx                           # Main app component
│   ├── main.tsx                          # Entry point
│   ├── index.css                         # Global styles + Tailwind
│   └── vite-env.d.ts
├── .env.example
├── .gitignore
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.js
├── postcss.config.js
└── README.md
```

---

### Key Implementation Files

#### `src/types/index.ts`

```typescript
export interface Message {
  id: string;
  role: "user" | "assistant";
  content: string;
  timestamp: Date;
  isUrgent?: boolean; // For emergency messages
  hasSteps?: boolean; // Has procedural steps
  hasQuestions?: boolean; // Has strategic questions
}

export interface ChatSession {
  sessionId: string;
  userId: string;
  messages: Message[];
}

export interface NewSessionResponse {
  session_id: string;
  greeting: string;
  timestamp: string;
}

export interface ChatResponse {
  session_id: string;
  response: string;
  tools_used: ToolCall[];
  tokens_used: number;
  response_time_ms: number;
  timestamp: string;
}

export interface ToolCall {
  tool: string;
  args: Record<string, any>;
}

export interface EmergencyContact {
  name: string;
  nameBengali: string;
  number: string;
  category: "emergency" | "legal_aid" | "medical";
}
```

---

#### `src/utils/detectUrgency.ts`

```typescript
export const detectUrgency = (text: string): boolean => {
  const urgentKeywords = [
    "ধর্ষণ",
    "rape",
    "৭২ ঘণ্টা",
    "DNA",
    "জরুরি",
    "emergency",
    "বিপদ",
    "danger",
    "হত্যা",
    "kill",
    "আত্মহত্যা",
    "suicide",
    "ছুরি",
    "knife",
    "মারবে",
    "will kill",
  ];

  return urgentKeywords.some((keyword) =>
    text.toLowerCase().includes(keyword.toLowerCase())
  );
};
```

---

#### `src/hooks/useMessageFormatter.ts`

```typescript
import { useMemo } from "react";

export const useMessageFormatter = (message: string) => {
  return useMemo(() => {
    // Detect strategic questions
    const hasQuestions = /প্রথম প্রশ্ন:|দ্বিতীয় প্রশ্ন:|তৃতীয় প্রশ্ন:/.test(
      message
    );

    // Detect procedural steps
    const hasSteps = /ধাপ ১:|ধাপ ২:|ধাপ ৩:/.test(message);

    // Detect urgency
    const isUrgent = detectUrgency(message);

    // Parse bold text **text** → <strong>text</strong>
    const formattedMessage = message.replace(
      /\*\*(.*?)\*\*/g,
      "<strong>$1</strong>"
    );

    return {
      formattedMessage,
      hasQuestions,
      hasSteps,
      isUrgent,
    };
  }, [message]);
};
```

---

#### `src/services/api.ts`

```typescript
const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ||
  "https://final-family-law-production.up.railway.app";

export const api = {
  async createNewSession(userId: string): Promise<NewSessionResponse> {
    const response = await fetch(`${API_BASE_URL}/chat/new`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId }),
    });

    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return response.json();
  },

  async sendMessage(sessionId: string, message: string): Promise<ChatResponse> {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 30000);

    try {
      const response = await fetch(`${API_BASE_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ session_id: sessionId, message }),
        signal: controller.signal,
      });

      clearTimeout(timeoutId);

      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    } catch (error) {
      clearTimeout(timeoutId);
      if (error instanceof Error && error.name === "AbortError") {
        throw new Error("TIMEOUT");
      }
      throw error;
    }
  },
};
```

---

## Development Phases

### Phase 1: Core Chat Functionality (Week 1)

**Goal**: Basic chat working with all API endpoints

**Tasks**:

- [ ] Project setup (React + Vite + TypeScript + Tailwind)
- [ ] API service layer implementation
- [ ] Session management (create, store, retrieve)
- [ ] Basic chat message components
- [ ] Message sending and receiving
- [ ] Bengali font integration (Noto Sans Bengali)
- [ ] Mobile-responsive layout
- [ ] Test on real mobile devices

**Deliverable**: Working chat that sends/receives messages

---

### Phase 2: Feature Components (Week 2)

**Goal**: Implement all special components for lawyer-like interaction

**Tasks**:

- [ ] Strategic question display component
- [ ] Procedural steps component
- [ ] Emergency alert component
- [ ] Document checklist component
- [ ] Loading states (typing indicator)
- [ ] Error handling UI
- [ ] Message formatting (bold, lists, line breaks)
- [ ] Disclaimer banner
- [ ] Test multi-turn conversations

**Deliverable**: Full-featured chat UI with all components

---

### Phase 3: Safety & Support Features (Week 3)

**Goal**: Add safety features and support resources

**Tasks**:

- [ ] Emergency contacts bar (sticky)
- [ ] Quick exit button
- [ ] Support organization panel
- [ ] Click-to-call functionality
- [ ] Privacy features (clear history on exit)
- [ ] Urgency detection (client-side highlighting)
- [ ] Accessibility improvements (screen reader, contrast)
- [ ] Performance optimization (lazy loading, code splitting)

**Deliverable**: Production-ready, safe application

---

### Phase 4: Polish & Deployment (Week 4)

**Goal**: Production deployment and final testing

**Tasks**:

- [ ] Cross-browser testing (Chrome, Firefox, Safari on Android/iOS)
- [ ] Slow network testing (3G throttling)
- [ ] Bengali text rendering verification
- [ ] Animation polish
- [ ] Build optimization
- [ ] Deploy to Vercel/Netlify
- [ ] Configure environment variables
- [ ] User acceptance testing with target users
- [ ] Fix bugs from UAT

**Deliverable**: Live website accessible to users

---

## Success Metrics

### User Engagement

- **Daily active users**: Number of unique sessions per day
- **Messages per session**: Average = 8-12 (indicates users are getting help)
- **Session duration**: Average = 5-10 minutes (thorough conversation)
- **Returning users**: % of users who create multiple sessions (indicates value)

### User Satisfaction

- **Task completion**: Did user get answer to their question? (inferred from conversation length)
- **Bounce rate**: % of users who leave after one message (target < 20%)
- **Intent distribution**: Which legal topics are most requested (informs content expansion)

### Technical Performance

- **Page load time**: < 2 seconds on 3G (target: 1.5s)
- **Time to interactive**: < 3 seconds
- **Message send latency**: < 500ms (excluding AI response time)
- **API success rate**: > 95%
- **Error rate**: < 5% of messages

### Business Impact

- **Cost per conversation**: Infrastructure + API (target: $0.001-0.01)
- **Users helped**: Total cumulative users who received guidance
- **Support organization referrals**: Users who contacted BNWLA/ASK after chatbot guidance

---

## Open Questions & Decisions Needed

### Design Decisions

**Q1**: Should we show "tools used" information to users?

- Option A: Hide completely (users don't need technical details)
- Option B: Show as subtle "📚 Sources consulted: পারিবারিক সহিংসতা আইন ২০১০"
- Option C: Detailed transparency (show exact tools and args)

**Recommendation**: Option A for MVP (simplicity), consider Option B post-launch

---

**Q2**: How to handle very long AI responses (2000+ characters)?

- Option A: Show full response in one bubble (current plan)
- Option B: "Show more" button to expand
- Option C: Paginate long responses

**Recommendation**: Option A, revisit if users complain

---

**Q3**: Should we implement conversation history export?

- Option A: No export (privacy-first)
- Option B: "Copy to clipboard" button
- Option C: "Download as PDF" (requires backend support)

**Recommendation**: Option B (simple, useful, doesn't compromise privacy)

---

### Technical Decisions

**Q4**: Should we implement offline support?

- Service worker to cache app shell
- Queue messages when offline, send when online
- Complexity: Medium

**Recommendation**: Not for MVP. Just show "offline" message.

---

**Q5**: Should we add suggested prompts / quick replies?

- Option A: No suggestions (keep it simple)
- Option B: Intent-specific suggestions ("সন্তানের হেফাজত আইন", "FIR কীভাবে করব")
- Option C: Dynamic suggestions based on conversation context (complex)

**Recommendation**: Option B for intents with detection issues (custody, maintenance, parent_maintenance)

---

**Q6**: Voice input/output support?

- Bengali speech-to-text via Web Speech API (limited browser support)
- Text-to-speech for illiterate users
- Complexity: High

**Recommendation**: Post-MVP (nice-to-have for accessibility)

---

### Content Decisions

**Q7**: Should we add a FAQ section?

- Common questions in sidebar
- Reduces AI API calls
- Might distract from conversational flow

**Recommendation**: No FAQ for MVP. Chatbot handles all queries.

---

**Q8**: Legal disclaimer wording - need approval?

- Current: "আইন বন্ধু শুধুমাত্র তথ্য প্রদান করে, আইনি পরামর্শ নয়।"
- Should legal team review?

**Recommendation**: YES - get legal team approval before launch

---

### Deployment Decisions

**Q9**: Hosting platform?

- Vercel (recommended - free tier, auto-deploys from GitHub)
- Netlify (similar to Vercel)
- Railway (same as backend - consolidation)

**Recommendation**: Vercel for frontend (best DX), Railway for backend

---

**Q10**: Custom domain?

- ainbandhu.org or ainbandhu.bd
- Cost: $10-15/year
- Better for trust and SEO

**Recommendation**: Use Vercel subdomain for MVP (ain-bandhu.vercel.app), get custom domain when funding confirmed

---

**Q11**: Analytics?

- Google Analytics (privacy concerns, but most complete)
- Plausible (privacy-friendly, paid $9/month)
- No analytics (most privacy-friendly)

**Recommendation**: No analytics for MVP (privacy-first), add Plausible post-launch if needed

---

## Appendix: Complete Intent List with Examples

### 1. rape_sexual_violence

**User Query Examples**:

- "আমি ধর্ষণের শিকার হয়েছি"
- "আমার সাথে যৌন নির্যাতন হয়েছে"
- "কেউ আমার সাথে জোর করে..."

**AI Response Pattern**:

- ⚠️ URGENT: Time-critical (72 hours for DNA)
- Safety check first
- OCC location and process
- Medical exam before FIR
- Emotional support
- Legal process explanation

---

### 2. domestic_violence_general

**User Query Examples**:

- "আমার স্বামী আমাকে মারে"
- "পারিবারিক সহিংসতা"
- "শ্বশুরবাড়িতে নির্যাতন"

**AI Response Pattern**:

- Safety check ("আপনি কি এখন নিরাপদ?")
- Strategic questions (when, witnesses, injuries)
- Protection order recommendation
- FIR process
- Safety planning
- Support organizations

---

### 3. dowry

**User Query Examples**:

- "আমার স্বামী যৌতুক চাইছে"
- "শ্বশুর যৌতুকের জন্য অত্যাচার করছে"

**AI Response Pattern**:

- Legal prohibition of dowry
- Evidence collection (messages, witnesses)
- FIR process
- Family court option
- Punishment provisions

---

### 4. child_marriage

**User Query Examples**:

- "আমার মেয়ের বিয়ে হয়ে গেছে কিন্তু সে ১৫ বছর বয়সী"
- "বাল্যবিবাহ"

**AI Response Pattern**:

- Prevention mechanisms
- Reporting to child marriage prevention committee
- Local government officer duties
- Legal age (18 for girls, 21 for boys)

---

### 5. divorce_talaq

**User Query Examples**:

- "আমি তালাক চাই"
- "আমার স্বামী তালাক দিয়েছে"
- "বিবাহবিচ্ছেদ"

**AI Response Pattern**:

- Talaq procedure (notice, 90-day iddat period)
- Maintenance rights
- Custody considerations
- Family court process
- Dower rights

---

### 6. custody (partial)

**User Query Examples**:

- ❌ "তালাকের পর আমার সন্তানের হেফাজত কীভাবে পাব?" (doesn't trigger)
- ✅ "সন্তানের হেফাজত আইন কী?" (triggers)

**AI Response Pattern**:

- Custody rights (mother until age 7 for son, puberty for daughter)
- Family court process
- Best interests of child
- Father's visitation rights

---

### 7. maintenance (partial)

**User Query Examples**:

- ❌ "তালাকের পর আমার জন্য টাকা পাব?" (doesn't trigger)
- ✅ "ভরণপোষণ আইন কী?" (triggers)

**AI Response Pattern**:

- Wife's maintenance rights (during marriage and after divorce)
- Child support
- Family court enforcement
- Amount calculation

---

### 8. polygamy_second_marriage

**User Query Examples**:

- "আমার স্বামী দ্বিতীয় বিয়ে করেছে"
- "একাধিক বিবাহ"

**AI Response Pattern**:

- Permission requirement from arbitration council
- Legal challenges if no permission
- First wife's rights
- Family court remedies

---

### 9. inheritance_succession

**User Query Examples**:

- "আমার বাবা মারা গেছেন, আমি কি সম্পত্তি পাব?"
- "উত্তরাধিকার আইন"

**AI Response Pattern**:

- Islamic succession rules
- Women's inheritance shares
- Legal process to claim
- Court procedures if contested

---

### 10. marriage_registration

**User Query Examples**:

- "বিয়ে রেজিস্ট্রি করতে হবে"
- "কাবিন নামা"

**AI Response Pattern**:

- Legal requirements
- Registration process
- Documents needed
- Costs
- Timeline

---

### 11. dower_mehr

**User Query Examples**:

- "আমার স্বামী দেনমোহর দিচ্ছে না"
- "মোহর"

**AI Response Pattern**:

- Mehr rights
- Enforcement if husband refuses
- Family court process
- Prompt vs. deferred mehr

---

### 12. parent_maintenance (partial)

**User Query Examples**:

- ❌ "আমার ছেলে আমাকে টাকা দিচ্ছে না" (might not trigger)
- ✅ "পিতামাতার ভরণপোষণ আইন" (triggers)

**AI Response Pattern**:

- Children's legal duty to support parents
- Family court process
- Evidence needed
- Mediation option (Union Parishad)

---

## Conclusion

This comprehensive Frontend PRD captures the full scope and sophistication of Ain Bandhu - an AI LAWYER, not just a chatbot.

**Key Takeaways**:

1. **12 legal intents**, not 6 - covering comprehensive family law topics
2. **Lawyer-like interaction** - strategic questioning, personalized advice, obstacle anticipation
3. **Safety-first approach** - urgent danger detection, emergency contacts, quick exit
4. **Procedural focus** - exact steps, documents, costs, timelines, what to say
5. **Simple Bengali** - accessible to women with primary education
6. **Privacy & anonymity** - no login, minimal tracking, easy to erase
7. **Mobile-first** - optimized for cheap Android phones on slow networks

**Backend is ready and deployed**. Frontend development can begin immediately.

**Estimated Timeline**: 4 weeks to production
**Team Size**: 1-2 frontend developers
**Budget**: $0-50/month (hosting on Vercel free tier, optional Plausible analytics)

---

**Built with ❤️ for underprivileged Bangladeshi women**

_Last Updated: 2025-11-26_
_Version: 2.0 (Complete & Accurate)_
