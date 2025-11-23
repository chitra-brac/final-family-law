# Product Requirements Document
## Ain Bandhu (আইন বন্ধু) - AI Legal Assistant for Bangladeshi Women

**Version:** 1.0
**Date:** November 23, 2025
**Author:** BRAC Legal Aid Project Team
**Status:** Approved for MVP Development

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Problem Statement](#2-problem-statement)
3. [Solution Overview](#3-solution-overview)
4. [Target Users](#4-target-users)
5. [User Stories & Use Cases](#5-user-stories--use-cases)
6. [Goals & Success Metrics](#6-goals--success-metrics)
7. [Feature Requirements](#7-feature-requirements)
8. [Non-Functional Requirements](#8-non-functional-requirements)
9. [Technical Architecture](#9-technical-architecture)
10. [User Experience & Flow](#10-user-experience--flow)
11. [Risks & Mitigations](#11-risks--mitigations)
12. [Timeline & Milestones](#12-timeline--milestones)
13. [Future Roadmap](#13-future-roadmap)
14. [Success Definition](#14-success-definition)
15. [Appendices](#15-appendices)

---

## 1. Executive Summary

### Project Overview

**Project Name:** Ain Bandhu (আইন বন্ধু - "Legal Friend")

**Vision:** Democratize access to legal knowledge and procedural guidance for underprivileged Bangladeshi women who face family law issues but cannot afford legal representation.

**Mission:** Act as an accessible AI-powered lawyer that provides strategic, personalized legal guidance in simple Bengali, empowering women to navigate the legal system and access justice.

**Target Audience:** Underprivileged Bangladeshi women facing family law issues including domestic violence, rape, child custody, divorce, dowry harassment, and other family-related legal matters.

**Solution:** An AI chatbot powered by OpenAI's GPT-5.1 that performs the role of a compassionate, knowledgeable lawyer - asking strategic questions, assessing cases, providing personalized advice, and guiding women step-by-step through legal processes.

**Expected Impact:** Bridge the justice gap for thousands of underprivileged women who cannot access legal services due to cost, knowledge, or cultural barriers.

### Key Differentiators

1. **Acts Like a Lawyer, Not Just an Information Database**
   - Asks strategic questions to understand the full situation
   - Assesses case strength, urgency, and available options
   - Provides personalized recommendations based on individual circumstances
   - Anticipates obstacles and guides how to overcome them

2. **Safety-First Approach**
   - Detects urgent situations (immediate danger from domestic violence, rape)
   - Prioritizes safety guidance before legal procedures
   - Provides emergency contacts and safe shelter information

3. **Procedural Knowledge Focus**
   - Not just "what are your rights" but "exactly what to do, where to go, what to say"
   - Documents needed, costs involved, timeline expectations
   - How to handle police refusal, family pressure, and other real obstacles

4. **Simple Bengali, Zero Jargon**
   - Explains complex legal concepts in language accessible to women with primary school education
   - Culturally sensitive and empowering tone

5. **Free, 24/7, Anonymous**
   - No cost barrier
   - Available anytime, anywhere with internet
   - No login required (protecting user privacy and safety)

---

## 2. Problem Statement

### Current Situation

Underprivileged women in Bangladesh face severe family law issues - domestic violence, rape, child marriage, custody disputes, dowry harassment - but have virtually no access to legal help when they need it most.

### User Pain Points

#### Knowledge Gap
- **"I don't know my rights"** - Women are unaware that laws exist to protect them
- **"I don't know where to go"** - Which police station? Which court? Which office?
- **"I don't know what to do"** - How to file FIR? What is a General Diary? What documents are needed?
- **"I don't know the process"** - What happens after I file a complaint? How long does it take? What comes next?

#### Financial Barrier
- **"I can't afford a lawyer"** - Private lawyers charge fees far beyond what garment workers or rural women can pay
- **"I don't know about free legal aid"** - Legal aid organizations exist but awareness is low

#### Procedural Complexity
- **"The law is too complicated"** - Legal language is incomprehensible to those without formal education
- **"I don't know what documents I need"** - Birth certificates, marriage certificates, medical reports - what's required?
- **"I don't know how much it costs"** - Court fees, medical exam fees, notary costs - are there free options?

#### Systemic Obstacles
- **"Police refused to take my complaint"** - FIR refusal is common, women don't know their rights or how to escalate
- **"My family is pressuring me to stay silent"** - Cultural shame, stigma, family honor
- **"I'm afraid of the legal system"** - Intimidating, unfamiliar, male-dominated spaces

#### Information Access
- **"I don't speak English"** - Most legal information online is in English or uses Bengali legal jargon
- **"I can't find clear answers"** - Google searches yield overwhelming, unorganized information
- **"I don't have anyone to ask"** - Isolated, ashamed, no trusted advisor

### Market Gap

**Existing Solutions Fall Short:**

1. **Legal Aid Organizations (BNWLA, ASK, BLAST)**
   - **Limitations:** Limited reach, office hours only, require in-person visit, long waiting times
   - **Gap:** Cannot serve the millions of women who need help across Bangladesh

2. **Helplines (10921 Women's Helpline, etc.)**
   - **Limitations:** Basic information only, not personalized, limited hours, no follow-through
   - **Gap:** Cannot provide comprehensive legal guidance or strategic advice

3. **Google Search**
   - **Limitations:** Information overload, not Bengali-focused, not personalized, requires digital literacy
   - **Gap:** Cannot assess individual situations or provide tailored recommendations

4. **Word of Mouth (Friends, Family)**
   - **Limitations:** Often inaccurate, perpetuates myths, varies by social circle
   - **Gap:** Not reliable or comprehensive

**What's Missing:** An accessible, 24/7, free, Bengali-language tool that acts like a personal lawyer - understanding each woman's unique situation and providing strategic, actionable guidance.

---

## 3. Solution Overview

### Introducing Ain Bandhu (আইন বন্ধু)

Ain Bandhu is an AI-powered chatbot that **performs the role of an accessible lawyer** for underprivileged Bangladeshi women facing family law issues.

### Core Value Proposition

**"The lawyer you couldn't otherwise afford, available 24/7 in your pocket, for free."**

Ain Bandhu provides:
- ✅ **Immediate safety guidance** for urgent situations
- ✅ **Strategic legal advice** personalized to your situation
- ✅ **Step-by-step procedural guidance** (what to do, where to go, what to say)
- ✅ **Obstacle resolution** (police refuses FIR? Here's how to handle it)
- ✅ **Free resource connection** (legal aid organizations, shelters, helplines)
- ✅ **Empowerment through knowledge** of legal rights in simple Bengali

### How It Works

#### 1. User Describes Situation
Woman opens chatbot and describes her problem in Bengali (text or voice).

**Example:** "আমার স্বামী আমাকে মারে এবং আমার ছেলেকে নিয়ে যাওয়ার হুমকি দেয়"
(My husband beats me and threatens to take my son away)

#### 2. AI Lawyer Asks Strategic Questions
Like a real lawyer, Ain Bandhu probes to understand the full situation:
- "আপনি এখন কি নিরাপদ?" (Are you safe right now?)
- "আপনার কি শারীরিক আঘাত আছে?" (Do you have physical injuries?)
- "আপনার ছেলে কত বছরের?" (How old is your son?)
- "আপনি কি থানায় রিপোর্ট করেছেন?" (Have you reported to police?)

#### 3. AI Assesses the Case
Using lawyer's playbook and legal knowledge:
- **Urgency:** Critical (immediate danger)
- **Legal issues:** Domestic violence + child custody threat
- **Case strength:** Medical evidence would strengthen case
- **Recommended strategy:** File FIR, get medical report, apply for protection order and custody rights

#### 4. Provides Personalized Advice
Based on her specific situation:

**Immediate Actions:**
- Safety first: emergency contacts, safe shelters
- Medical report if injuries (strengthens case)
- File FIR at nearest police station with specific wording

**Legal Rights:**
- Domestic Violence Act protects you
- You have custody rights for your son
- You can get protection order to keep husband away

**Step-by-Step Process:**
1. Go to [specific hospital] for medical-legal report (free)
2. File FIR at [nearest police station], say: "[exact Bengali phrasing]"
3. Contact BNWLA at [phone number] for free lawyer
4. Apply for protection order at Family Court
5. File for child custody

**Anticipated Obstacles:**
- "Police may refuse FIR" → "Tell them it's legally required under Section X. Ask for OC. Call BNWLA for support."
- "Family pressure to withdraw" → "You have the right to safety. BNWLA can provide shelter."

**Free Resources:**
- BNWLA: [contact], free lawyer + shelter
- ASK: [contact], 24/7 helpline
- Nearest women's shelter: [address]

#### 5. Continues Conversation
Answers follow-up questions, provides clarifications, adjusts advice based on new information.

### Technology Foundation

**AI Model:** OpenAI GPT-5.1 Instant
- Latest and most capable conversational AI
- Excellent Bengali language support
- Adaptive reasoning for complex legal situations
- Instruction-following for lawyer-like behavior

**Knowledge Base:**
- **1,512 legal sections** from 58 Bangladeshi acts (1856-2025)
- **12 family law intents** mapped to relevant sections
- **Lawyer's playbook** for each intent (strategic questions, decision trees, case assessment criteria)
- **Procedural knowledge** (step-by-step processes, documents, costs, timelines, organizations)

**Architecture:**
- FastAPI backend (Python)
- OpenAI Responses API (stateful conversations)
- Tool calling for legal knowledge retrieval
- Supabase for conversation storage and analytics

---

## 4. Target Users

### Primary User Persona: Fatima

**Demographics:**
- **Name:** Fatima Ahmed
- **Age:** 28 years old
- **Location:** Mohammadpur, Dhaka (low-income neighborhood)
- **Education:** Completed Class 5 (primary school)
- **Occupation:** Garment factory worker (Tk. 12,000/month salary)
- **Family:** Married 8 years, 2 children (ages 3 and 6)
- **Language:** Bengali only, cannot read/write English
- **Tech Access:** Basic smartphone (Android), uses Facebook and WhatsApp

**Situation:**
- Husband regularly beats her, especially when he drinks
- Afraid for her children's safety
- Wants to leave but doesn't know how
- Worried about losing her children
- Cannot afford lawyer (monthly salary barely covers food and rent)

**Goals:**
1. **Immediate:** Understand if she can legally leave and keep her children
2. **Short-term:** Know the exact steps to file a complaint and get protection
3. **Long-term:** Obtain divorce and custody of children, secure maintenance

**Barriers:**
- **Knowledge:** Doesn't know her legal rights or options
- **Financial:** Cannot afford private lawyer (Tk. 20,000+ consultation fee)
- **Social:** Ashamed to tell family or neighbors, cultural stigma around divorce
- **Systemic:** Intimidated by police stations and courts, doesn't know the process
- **Isolation:** No one to ask for help or guidance

**User Needs:**
- Simple Bengali explanations (no legal jargon)
- Immediate safety guidance
- Step-by-step instructions (exactly what to do, where to go)
- Information about free services
- Reassurance that she has rights
- Anonymous, private access (husband cannot find out she's seeking help)

**How Ain Bandhu Helps:**
- 24/7 access on her phone (can use during break at factory)
- Simple Bengali, no jargon
- Provides exact steps: "Go to Mohammadpur Thana, say 'পারিবারিক সহিংসতা আইন ২০১০ এর অধীনে মামলা করতে চাই'"
- Connects to BNWLA for free lawyer
- Explains custody rights (children under 7 stay with mother)
- No login required (privacy and safety)

---

### Secondary User Persona: Ayesha

**Demographics:**
- **Name:** Ayesha Begum
- **Age:** 22 years old
- **Location:** Rural Barisal
- **Education:** High school (Class 10)
- **Occupation:** Homemaker
- **Family:** Single, lives with parents
- **Language:** Bengali (some English reading ability)
- **Tech Access:** Smartphone, familiar with apps

**Situation:**
- Raped by neighbor yesterday evening (within 24 hours)
- In shock, doesn't know what to do
- Parents want to keep it quiet (family honor)
- Bleeding and in pain
- Afraid rapist will go unpunished

**Goals:**
1. **Urgent:** Get medical help and preserve evidence
2. **Immediate:** Understand legal options (can she file case?)
3. **Short-term:** File FIR and pursue justice

**Barriers:**
- **Time-sensitive:** Evidence disappears after 24-72 hours
- **Family pressure:** Parents forbidding her to report
- **Trauma:** Emotionally devastated, struggling to think clearly
- **Knowledge gap:** Doesn't know about medical-legal report
- **Fear:** Worried about police treatment, court process, social stigma

**User Needs:**
- URGENT guidance (this is time-critical)
- Safety and medical priorities
- Empowerment to resist family pressure
- Step-by-step process for filing case
- Understanding of what happens in court
- Emotional support and reassurance

**How Ain Bandhu Helps:**
- Detects urgency (rape within 24 hours)
- Prioritizes: "URGENT: Go to hospital NOW for medical-legal report (free, critical evidence)"
- Explains legal rights: "This is not your fault. The law is on your side. Rapist faces life imprisonment or death penalty."
- Guides FIR process with exact wording
- Connects to ASK for immediate legal support
- Provides what to expect in medical exam and legal process

---

### Tertiary User Persona: Rima

**Demographics:**
- **Name:** Rima Das
- **Age:** 35 years old
- **Location:** Chittagong city
- **Education:** Graduate (BA)
- **Occupation:** Small business owner (boutique shop)
- **Family:** Married 12 years, 1 daughter (age 10)
- **Language:** Bengali and English
- **Tech Access:** Smartphone, laptop, digitally savvy

**Situation:**
- Loveless marriage, husband has second wife (polygamy)
- Wants divorce but worried about daughter's custody
- Concerns about financial security (who pays for daughter's education?)
- Unclear about legal process and timeline

**Goals:**
1. **Immediate:** Understand divorce options and custody rights
2. **Short-term:** Know the full legal process and timeline
3. **Long-term:** Obtain divorce with custody and maintenance

**Barriers:**
- **Procedural confusion:** Which court? What documents? How long?
- **Financial concerns:** Can she demand maintenance? Husband's second marriage legal?
- **Emotional:** Wants clarity before making big decision

**User Needs:**
- Comprehensive information about divorce process
- Understanding of custody laws (daughter is 10 years old)
- Maintenance rights
- Timeline expectations
- Legal standing on polygamy

**How Ain Bandhu Helps:**
- Explains divorce options (judicial vs mutual consent)
- Clarifies custody rights (daughter age 10, court decides based on best interest)
- Details maintenance rights (for self and daughter)
- Notes: Polygamy without first wife's permission is illegal
- Provides full process timeline (6 months to 2 years typically)
- Connects to BLAST for legal representation

---

## 5. User Stories & Use Cases

### High Priority Use Cases

#### UC1: Domestic Violence - Immediate Danger

**User Story:**
As a woman currently being beaten by her husband, I want immediate safety guidance and emergency contacts so that I can protect myself right now.

**Scenario:**
- Fatima's husband is drunk and threatening her
- She locks herself in bathroom with phone
- Opens Ain Bandhu and types: "আমি বিপদে আছি"

**Expected Behavior:**
1. Bot immediately recognizes urgency
2. Prioritizes safety over legal process
3. Provides:
   - Emergency number: "এখনই ৯৯৯ এ কল করুন"
   - Nearest safe place: "নিকটতম BNWLA শেল্টার: [address]"
   - Police station: "মহম্মদপুর থানা: [address, phone]"
4. Asks: "আপনি এখন নিরাপদ স্থানে যেতে পারবেন?"
5. Once safe, proceeds with legal guidance

**Success Criteria:**
- ✅ Immediate safety info provided within 3 seconds
- ✅ No legal jargon before safety is addressed
- ✅ Emergency contacts are real and functional
- ✅ User feels supported and knows what to do

---

#### UC2: Rape - Recent Incident (Time-Critical)

**User Story:**
As a rape victim (incident within 24 hours), I want to know the urgent steps to take so that I don't lose critical evidence and can pursue justice.

**Scenario:**
- Ayesha was raped yesterday evening (18 hours ago)
- She's scared, in pain, unsure what to do
- Types: "কাল আমার সাথে ধর্ষণ হয়েছে"

**Expected Behavior:**
1. Bot recognizes time-critical situation
2. Prioritizes medical-legal report (evidence window closing)
3. Provides:
   - **URGENT:** "২৪ ঘণ্টার মধ্যে হাসপাতালে যান - মেডিকেল রিপোর্ট জরুরী"
   - Hospital list: "নিকটতম সরকারি হাসপাতাল: বরিশাল মেডিকেল কলেজ (বিনামূল্যে)"
   - What to say: "মেডিকেল-লিগ্যাল রিপোর্ট দরকার"
   - Safety check: "আপনি এখন কি নিরাপদ? ধর্ষক কি পরিচিত কেউ?"
4. Then guides FIR process
5. Connects to legal aid
6. Provides emotional support: "এটি আপনার দোষ নয়। আইন আপনার পক্ষে।"

**Success Criteria:**
- ✅ Medical report urgency communicated within first response
- ✅ Hospital information is accurate and includes "free" notation
- ✅ Legal rights explained in simple, empowering language
- ✅ User knows exactly what to do in next 6 hours

---

#### UC3: Child Custody Concerns

**User Story:**
As a mother seeking divorce, I want to know about child custody rights so that I can protect my relationship with my children.

**Scenario:**
- Fatima wants to leave abusive husband
- Main fear: losing her two children (ages 3 and 6)
- Asks: "আমি যদি ডিভোর্স নেই, আমার বাচ্চারা কার কাছে থাকবে?"

**Expected Behavior:**
1. Bot reassures with legal clarity
2. Explains custody law:
   - Children under 7: Mother has right to custody (Hizanat)
   - Her son (6) and daughter (3) both fall under this
   - Father must still provide financial support
3. Asks strategic questions:
   - "আপনার স্বামী কি সহিংস? এটি কি আদালতে প্রমাণ করতে পারবেন?"
4. Provides:
   - How to file for custody in Family Court
   - Documents needed (birth certificates, evidence of abuse)
   - Expected timeline
   - Legal aid contacts

**Success Criteria:**
- ✅ Custody rights clearly explained in simple Bengali
- ✅ User feels reassured and empowered
- ✅ Specific age-based guidance provided
- ✅ Process for securing custody outlined

---

#### UC4: Police Refusal to File FIR

**User Story:**
As someone whose FIR was refused by police, I want to know my rights and how to escalate so that I can ensure my complaint is officially filed.

**Scenario:**
- Fatima went to Mohammadpur Thana
- Police officer said "This is a family matter, work it out at home"
- Refused to file FIR
- She asks: "থানা আমার মামলা নিচ্ছে না, আমি কি করবো?"

**Expected Behavior:**
1. Bot validates her experience (this is common)
2. Explains her rights:
   - "পুলিশ আপনার FIR নিতে বাধ্য - এটি আইনত তাদের ঐচ্ছিক নয়"
3. Provides escalation steps:
   - **Step 1:** Go back, ask for OC (Officer-in-Charge)
   - **Step 2:** Cite the law: "পারিবারিক সহিংসতা আইন ২০১০ এর অধীনে FIR নিতে হবে"
   - **Step 3:** If still refused, call BNWLA immediately: [phone]
   - **Step 4:** File complaint with Police Super or Magistrate
4. Empowers: "আপনার অধিকার আছে। পুলিশ আপনাকে ফেরাতে পারে না।"

**Success Criteria:**
- ✅ User knows police refusal is illegal
- ✅ Clear escalation path provided
- ✅ Support organization contact given for backup
- ✅ User feels empowered, not defeated

---

#### UC5: Free Legal Aid Access

**User Story:**
As someone who cannot afford a lawyer, I want to know about free legal aid options so that I can get professional representation without cost.

**Scenario:**
- Rima wants divorce but thinks lawyers are unaffordable
- Asks: "আমি উকিল নিতে পারবো না, খরচ অনেক"

**Expected Behavior:**
1. Bot corrects misconception:
   - "আপনার বিনামূল্যে উকিল পাওয়ার অধিকার আছে"
2. Lists free legal aid organizations:
   - **BNWLA:** Free lawyer, court representation, phone: [XXX]
   - **ASK:** Legal aid, mediation, phone: [XXX]
   - **BLAST:** Free legal services, phone: [XXX]
3. Explains services:
   - Completely free (no hidden fees)
   - Full court representation
   - Experienced family law lawyers
4. Guides how to contact:
   - "BNWLA এর ঢাকা অফিসে যান বা কল করুন। বলবেন আপনার ডিভোর্স মামলায় সাহায্য দরকার।"

**Success Criteria:**
- ✅ User knows free legal aid exists and is accessible
- ✅ Multiple organizations listed with contact info
- ✅ Services clearly explained (free, full representation)
- ✅ User empowered to take next step

---

### Medium Priority Use Cases

#### UC6: Filing General Diary (GD)
- User wants to file GD as precaution (not FIR yet)
- Bot explains difference between GD and FIR
- Guides when to use each

#### UC7: Understanding Maintenance Rights
- User wants to know about alimony and child support
- Bot explains legal entitlement, calculation, process

#### UC8: Dowry Harassment
- User facing dowry demands
- Bot explains Dowry Prohibition Act, penalties, how to file case

#### UC9: Inheritance Rights
- User wants to understand property rights after father's death
- Bot explains Islamic and secular inheritance laws

#### UC10: Marriage Registration
- User wants to register marriage
- Bot guides process, required documents, where to go

---

## 6. Goals & Success Metrics

### Business Goals

1. **Impact Goal:** Empower 10,000+ underprivileged women with legal knowledge in first year
2. **Quality Goal:** Achieve 80%+ user satisfaction rating
3. **Reliability Goal:** Provide legally accurate information (90%+ accuracy verified by legal experts)
4. **Sustainability Goal:** Operate within budget (<$100/month for first 1,000 users)
5. **Ecosystem Goal:** Increase traffic to legal aid organizations by 30%

### User Goals

1. **Immediate Understanding:** Get clear answers to legal questions in <5 minutes
2. **Actionable Guidance:** Know exactly what to do next (not just theory)
3. **Empowerment:** Feel confident about legal rights and options
4. **Safety:** Access emergency help for urgent situations
5. **Navigation:** Successfully interact with legal system (file FIR, find lawyer, etc.)

### Success Metrics

#### Engagement Metrics

**Primary:**
- **Daily Active Users (DAU):** Target 100+ within 3 months
- **Monthly Active Users (MAU):** Target 1,000+ within 6 months
- **Messages per Conversation:** Target 5+ (indicates meaningful engagement)
- **Conversation Completion Rate:** Target 70%+ (user gets actionable advice)

**Secondary:**
- **Return User Rate:** Target 20%+ (users come back for follow-up questions)
- **Session Duration:** Target 5-10 minutes (enough for comprehensive help)
- **Peak Usage Hours:** Identify when women most need help

#### Quality Metrics

**Primary:**
- **User Satisfaction Score:** Post-conversation survey, target 80%+ "satisfied" or "very satisfied"
- **Legal Accuracy:** Expert review of 100 random conversations, target 90%+ accurate
- **Response Helpfulness:** User rating, target 4+ out of 5 stars
- **Intent Classification Accuracy:** Target 95%+ (correct legal issue identified)

**Secondary:**
- **Language Quality:** Bengali naturalness, simplicity (expert review)
- **Cultural Sensitivity:** No offensive or insensitive responses (zero tolerance)
- **Completeness:** % of conversations that address all user questions

#### Impact Metrics

**Primary:**
- **Action Taken:** % of users who took legal action after using chatbot (survey)
  - Filed FIR/GD
  - Contacted legal aid organization
  - Went to court
  - Got medical-legal report
- **Successful Outcomes:** % who successfully navigated legal system
- **Organization Referrals:** Number of users connected to BNWLA/ASK/BLAST

**Secondary:**
- **Knowledge Gain:** % who learned something new about legal rights (survey)
- **Empowerment:** % who feel more confident about legal options (survey)
- **Word-of-Mouth:** % who recommended Ain Bandhu to others
- **Case Studies:** Verified success stories (changed lives)

#### Technical Metrics

**Primary:**
- **Response Latency:** 95th percentile <3 seconds (user doesn't wait long)
- **Uptime:** Target 99.5%+ (system always available)
- **Error Rate:** <1% of conversations encounter technical errors
- **Cost per Conversation:** Target <$0.05 (sustainable)

**Secondary:**
- **Tool Calling Accuracy:** >95% successful tool executions
- **Context Retention:** Multi-turn conversations maintain context accurately
- **Prompt Cache Hit Rate:** >80% (cost optimization)

### Measurement Plan

**Real-time Monitoring:**
- Conversation logs (Supabase)
- Error tracking (application logs)
- Usage analytics (conversations per day, peak hours)

**Weekly Review:**
- User satisfaction surveys (pop-up after conversation)
- Top intents identified
- Common questions/issues

**Monthly Review:**
- Legal expert review of 50 random conversations
- Impact survey (did you take action? what happened?)
- Cost analysis (per-conversation costs)
- Feature requests and user feedback synthesis

**Quarterly Review:**
- Deep dive into user journeys
- Success stories collection
- Stakeholder reporting (BRAC, donors)
- Roadmap adjustment based on learnings

---

## 7. Feature Requirements

### Core Features (Must-Have for MVP)

#### F1: Multi-turn Conversational Interface

**Description:** Natural language conversation in Bengali that maintains context across multiple messages.

**Functional Requirements:**
- Accept text input in Bengali (Bangla script)
- Support conversation threads with memory of previous messages
- Handle follow-up questions based on context
- Stream responses for better UX (user sees bot typing)
- Support all 12 family law intents:
  1. Rape and sexual violence
  2. Domestic violence (general)
  3. Dowry harassment
  4. Child marriage
  5. Child custody
  6. Maintenance/alimony
  7. Divorce/talaq
  8. Polygamy/second marriage
  9. Inheritance and succession
  10. Marriage registration
  11. Dower (mehr)
  12. Parent maintenance

**Acceptance Criteria:**
- ✅ User can send message in Bengali and receive Bengali response
- ✅ Bot remembers previous messages in same conversation (minimum 10 messages)
- ✅ Follow-up questions are answered with context
- ✅ Response starts appearing within 2 seconds (streaming)
- ✅ All 12 intents correctly identified and handled

---

#### F2: Lawyer-like Dialogue Pattern

**Description:** Bot behaves like a real lawyer - asking strategic questions, assessing the situation, and providing personalized advice.

**Functional Requirements:**
- Ask strategic questions based on case type (from lawyer's playbook)
- Assess case urgency (critical, high, medium, low)
- Evaluate case strength based on user's answers
- Provide personalized recommendations (not generic advice)
- Anticipate obstacles and guide how to overcome them
- Explain legal concepts in simple Bengali (no jargon)

**Acceptance Criteria:**
- ✅ Bot asks 2-4 strategic questions to understand situation fully
- ✅ Recommendations are specific to user's circumstances (e.g., "Since your son is 6 years old, you have custody rights under law")
- ✅ Bot explains legal terms in simple language (e.g., "হিজানত মানে ছোট বাচ্চা মায়ের কাছে থাকার অধিকার")
- ✅ Common obstacles addressed (police refusal, family pressure, costs)
- ✅ Tone is empathetic, supportive, and empowering

---

#### F3: Legal Knowledge Retrieval

**Description:** Access comprehensive legal database and provide accurate, relevant legal information.

**Functional Requirements:**
- Access 1,512 legal sections from 58 Bangladeshi acts
- Map user intent to relevant legal sections (using INTENT_MAPPINGS.json)
- Retrieve full section text from family_laws_final.json
- Cite legal sections when relevant (in simple terms)
- Provide act summaries for context

**Acceptance Criteria:**
- ✅ Correct legal sections retrieved for each of 12 intents
- ✅ Legal information is accurate (verified by legal expert)
- ✅ Laws are explained simply, not just quoted
- ✅ Multiple relevant sections provided when applicable
- ✅ Legal citations included but not overwhelming

---

#### F4: Procedural Guidance

**Description:** Step-by-step guidance for legal processes - what to do, where to go, what to say.

**Functional Requirements:**
- Provide detailed steps for each legal process:
  - Filing FIR
  - Filing General Diary (GD)
  - Getting medical-legal report
  - Applying for protection order
  - Filing for divorce
  - Custody application
  - Maintenance claims
- Include for each step:
  - Where to go (specific location/court/hospital)
  - What to say (exact Bengali phrasing)
  - Documents needed
  - Cost (with "free" options highlighted)
  - Timeline (how long it takes)
- Provide decision trees (if X then Y, if not X then Z)

**Acceptance Criteria:**
- ✅ Each legal process has minimum 5 detailed steps
- ✅ Specific locations mentioned (not just "go to hospital" but "Dhaka Medical College Hospital, One Stop Crisis Center")
- ✅ Exact phrasing provided for key interactions (what to say to police)
- ✅ All costs listed with free options highlighted
- ✅ Realistic timelines provided
- ✅ Decision logic applied based on user's situation

---

#### F5: Safety-First Approach

**Description:** Detect urgent/dangerous situations and prioritize safety before legal process.

**Functional Requirements:**
- Detect critical urgency keywords:
  - "বিপদে" (in danger)
  - "এখনই" (right now)
  - "মারছে" (beating/hitting now)
  - Rape within 24-72 hours
- Provide immediate safety guidance:
  - Emergency contact: 999
  - Women's helpline: 10921
  - Nearest police station
  - Safe shelters
- Prioritize safety actions over legal procedures
- Check if user is safe before proceeding

**Acceptance Criteria:**
- ✅ Emergency situations detected in first response
- ✅ Safety guidance provided before legal information
- ✅ Emergency contacts listed prominently
- ✅ Bot asks "Are you safe right now?" for urgent cases
- ✅ Time-critical actions flagged (e.g., "URGENT: Medical report needed within 24 hours")

---

#### F6: Support Organization Directory

**Description:** Connect users to real organizations providing legal aid, shelter, counseling.

**Functional Requirements:**
- Maintain directory of support organizations:
  - **Legal Aid:** BNWLA, ASK, BLAST
  - **Shelters:** BNWLA shelter, ASK crisis center
  - **Helplines:** 10921, organizational helplines
  - **One Stop Crisis Centers:** Hospital locations
- Provide for each organization:
  - Name (Bengali and English)
  - Services offered
  - Contact information (phone, address)
  - Hours of operation
  - How to access (what to say when calling)
- Match organizations to user's location (when possible)

**Acceptance Criteria:**
- ✅ Minimum 3 legal aid organizations listed
- ✅ All contact information is accurate and current
- ✅ Services clearly explained
- ✅ "Free" services prominently noted
- ✅ User knows exactly how to contact (phone number, address, what to say)

---

#### F7: Obstacle Resolution Guidance

**Description:** Provide solutions for common obstacles women face in legal system.

**Functional Requirements:**
- Address common obstacles:
  - Police refusing to file FIR
  - Can't afford lawyer
  - Family pressure to stay silent
  - Fear of losing children
  - Shame/stigma
  - Don't know where to go
  - Procedural confusion
- Provide solutions for each:
  - Legal rights explanation
  - Escalation steps
  - Free alternatives
  - Support organizations
  - Empowerment messaging

**Acceptance Criteria:**
- ✅ Minimum 5 common obstacles addressed per intent
- ✅ Each obstacle has clear solution/escalation path
- ✅ Legal backing provided (e.g., "Police are legally required to file FIR")
- ✅ Free options highlighted (e.g., "BNWLA provides free lawyers")
- ✅ User feels empowered, not defeated

---

### Nice-to-Have Features (Future Versions)

#### F8: Voice Input/Output
- Accept voice messages in Bengali
- Text-to-speech for responses (for illiterate users)
- Particularly important given low literacy rates

#### F9: Regional Language Support
- Chittagonian dialect
- Sylheti dialect
- Other regional variations

#### F10: Document Upload
- Upload photos of injuries (for evidence guidance)
- Upload threatening messages
- Upload legal documents for interpretation

#### F11: Case Tracking
- Track filed cases (FIR number)
- Provide status updates
- Remind about court dates

#### F12: SMS/WhatsApp Integration
- Access via SMS (for those without smartphones)
- WhatsApp bot (wider reach)

#### F13: Community Forum
- Anonymous community for women to share experiences
- Peer support
- Moderated for safety

#### F14: Lawyer Matching
- For complex cases, match to pro-bono lawyers
- Handoff from bot to human lawyer
- Calendar integration for appointments

#### F15: Legal Dictionary
- Searchable glossary of legal terms
- Bengali definitions
- Examples and usage

#### F16: Multi-language Support
- English for educated users
- Other South Asian languages (Hindi, Urdu)

---

## 8. Non-Functional Requirements

### Performance Requirements

**Response Time:**
- **Target:** 95th percentile <3 seconds from user message to first response token
- **Maximum:** No response should take >10 seconds
- **Streaming:** First token appears within 2 seconds

**Throughput:**
- **Concurrent Users:** Support minimum 1,000 simultaneous conversations
- **Peak Load:** Handle 100 messages/second during peak hours
- **Scalability:** Architecture supports horizontal scaling to 10,000+ concurrent users

**Uptime:**
- **Target:** 99.5% uptime (maximum 3.6 hours downtime/month)
- **Maintenance Windows:** Scheduled during off-peak hours (3-5 AM Bangladesh time)
- **Degradation:** Graceful degradation if dependencies fail

---

### Security & Privacy Requirements

**Data Privacy:**
- **No PII Storage:** Do not store personally identifiable information (names, addresses, phone numbers)
- **Anonymous Usage:** No login required, no user accounts (MVP)
- **Conversation Privacy:** Conversations encrypted in transit (HTTPS) and at rest
- **Auto-Deletion:** Conversations deleted after 30 days
- **Opt-out:** Users can request immediate conversation deletion

**Security:**
- **HTTPS Only:** All traffic over secure connections
- **API Key Protection:** OpenAI and Supabase keys stored securely (environment variables, not in code)
- **Input Sanitization:** Prevent injection attacks
- **Rate Limiting:** Prevent abuse (per-IP limits)

**Compliance:**
- **GDPR-inspired:** Follow data minimization and user privacy principles
- **Disclaimer:** Clear legal disclaimer ("This is guidance, not legal representation")
- **Safety Warning:** Warn users to delete chat if sharing device with abuser

---

### Usability Requirements

**Accessibility:**
- **Education Level:** Designed for users with Class 5 (primary school) education
- **Language:** Simple Bengali, zero legal jargon
- **Interface:** Minimal, intuitive (single text input box)
- **Device Support:** Works on low-end Android smartphones (2GB RAM, slow processors)
- **Network:** Functional on 2G/3G networks (low bandwidth)

**User Experience:**
- **Onboarding:** No signup required, immediate access
- **First Message:** Clear greeting and prompt ("What legal issue are you facing?")
- **Feedback:** Loading indicators, "bot is typing" animation
- **Error Messages:** In Bengali, helpful, non-technical
- **Help:** How to use the bot (simple instructions)

**Cultural Sensitivity:**
- **Tone:** Respectful, empathetic, non-judgmental
- **Gender:** Assumes women users (language and scenarios)
- **Religion:** Neutral, covers both secular and religious laws
- **Stigma:** Addresses shame and fear directly, provides reassurance

---

### Reliability Requirements

**Error Handling:**
- **OpenAI API Failure:** Fallback to basic information (emergency contacts)
- **Timeout:** If response takes >10 seconds, notify user and retry
- **Tool Failure:** If legal knowledge retrieval fails, provide general guidance
- **Network Issues:** Retry failed requests, inform user clearly

**Data Integrity:**
- **Legal Accuracy:** Legal knowledge base reviewed by experts quarterly
- **Version Control:** All code and data in git
- **Backups:** Database backed up daily
- **Rollback:** Ability to rollback to previous version if bugs introduced

**Monitoring:**
- **Error Tracking:** Log all errors with context
- **Performance Monitoring:** Track response times, uptime
- **Usage Analytics:** Monitor conversations per hour, peak times
- **Alert System:** Notify if uptime <95%, error rate >5%, or costs spike

---

### Scalability Requirements

**Horizontal Scaling:**
- **Stateless Backend:** FastAPI instances can be replicated
- **Load Balancing:** Distribute traffic across multiple instances
- **Database:** Supabase supports scaling to millions of rows

**Data Growth:**
- **Conversation History:** Support millions of conversations
- **Legal Database:** Easily add new acts/sections without refactoring
- **Intents:** Architecture supports expanding beyond 12 intents

**Geographic Scaling:**
- **CDN:** Static assets served via CDN (future)
- **Regional Deployment:** Can deploy in multiple regions (future)
- **Language:** Architecture supports multiple languages (future)

---

### Maintainability Requirements

**Code Quality:**
- **Modular Design:** Separation of concerns (services, models, tools)
- **Documentation:** Code comments, README, API documentation
- **Testing:** Unit tests for critical functions (future)
- **Type Hints:** Python type annotations for clarity

**Deployment:**
- **Docker:** Containerized for consistent deployment
- **Environment Config:** 12-factor app principles (.env files)
- **CI/CD:** Automated deployment (future)
- **Version Tagging:** Git tags for releases

**Knowledge Base Updates:**
- **Easy Updates:** JSON files can be edited without code changes
- **Validation:** Scripts to validate JSON structure
- **Versioning:** Track changes to knowledge base
- **Legal Review:** Process for expert review before updates go live

---

### Localization Requirements

**Language:**
- **Primary:** Bengali (Bangla script)
- **Fallback:** English for error messages (if needed)
- **Right-to-Left:** Not needed (Bengali is LTR)
- **Font:** Unicode support for Bengali characters

**Cultural:**
- **Legal System:** Bangladesh-specific laws and procedures
- **Organizations:** Bangladesh-based support organizations
- **Currency:** Bangladeshi Taka (৳)
- **Naming:** Bangladeshi naming conventions (e.g., "Fatima bint Ahmed")

**Regional:**
- **Dialect:** Standard Bengali (Dhaka dialect)
- **Future:** Support for Chittagonian, Sylheti (nice-to-have)

---

### Cost Efficiency Requirements

**Target Costs:**
- **Per Conversation:** <$0.05 (assuming 5 messages per conversation)
- **Monthly Operating Cost:** <$100 for first 1,000 users
- **Annual Budget:** <$5,000 for 10,000 users

**Optimization Strategies:**
- **Prompt Caching:** Utilize OpenAI's automatic caching (50% savings)
- **Model Selection:** Use GPT-5.1 Instant (not Thinking) for cost efficiency
- **Efficient Prompts:** Minimize token usage while maintaining quality
- **Rate Limiting:** Prevent abuse that drives up costs

**Monitoring:**
- **Budget Alerts:** Notify if daily costs exceed $10
- **Per-User Tracking:** Monitor conversation lengths
- **Optimization:** Continuously improve prompts to reduce tokens

---

## 9. Technical Architecture

### System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Layer                               │
│  (Web Browser on Smartphone, Desktop, or Tablet)                │
└─────────────────────────┬───────────────────────────────────────┘
                          │ HTTPS
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FastAPI Backend                               │
│                  (Python 3.11+ Application)                      │
│                                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────────┐   │
│  │   main.py    │  │   config.py  │  │    models.py        │   │
│  │ (API Routes) │  │  (Settings)  │  │  (Pydantic Schemas) │   │
│  └──────────────┘  └──────────────┘  └─────────────────────┘   │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │               Services Layer                                │ │
│  │                                                              │ │
│  │  ┌──────────────────┐  ┌─────────────────┐                 │ │
│  │  │ chatbot_service  │  │ openai_service  │                 │ │
│  │  │ (Orchestration)  │  │  (GPT-5.1 API)  │                 │ │
│  │  └──────────────────┘  └─────────────────┘                 │ │
│  │                                                              │ │
│  │  ┌──────────────────┐  ┌─────────────────┐                 │ │
│  │  │  data_loader     │  │   database.py   │                 │ │
│  │  │  (JSON in RAM)   │  │ (Supabase SDK)  │                 │ │
│  │  └──────────────────┘  └─────────────────┘                 │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │               Tools Layer                                   │ │
│  │                                                              │ │
│  │  ┌──────────────────────────────────────────────────────┐  │ │
│  │  │         tool_definitions.py                           │  │ │
│  │  │  - get_legal_knowledge()                              │  │ │
│  │  │  - get_procedural_guidance()                          │  │ │
│  │  │  - get_support_resources()                            │  │ │
│  │  └──────────────────────────────────────────────────────┘  │ │
│  └────────────────────────────────────────────────────────────┘ │
└───────────┬───────────────────────────────────┬─────────────────┘
            │                                   │
            ▼                                   ▼
┌────────────────────────┐        ┌────────────────────────────┐
│   OpenAI API           │        │   Supabase                 │
│   (GPT-5.1 Instant)    │        │   (PostgreSQL Database)    │
│   - Responses API      │        │                            │
│   - Tool Calling       │        │   Tables:                  │
│   - Streaming          │        │   - conversations          │
└────────────────────────┘        │   - messages               │
                                  └────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    Data Layer (In-Memory)                        │
│                                                                   │
│  family_laws_final.json    INTENT_MAPPINGS.json                 │
│  (1,512 legal sections)    (12 intent → section maps)            │
│                                                                   │
│  procedural_knowledge.json                                       │
│  (Lawyer's playbook, decision trees, resources)                  │
└─────────────────────────────────────────────────────────────────┘
```

---

### Technology Stack

#### Backend
- **Framework:** FastAPI 0.115+
  - Modern, fast Python web framework
  - Automatic API documentation (OpenAPI/Swagger)
  - Async support for concurrent requests
  - Excellent for AI/ML services

- **Language:** Python 3.11+
  - Latest stable Python
  - Type hints for code quality
  - Rich ecosystem for AI/ML

- **Server:** Uvicorn with Gunicorn
  - ASGI server for FastAPI
  - Production-ready
  - Supports async operations

#### AI/LLM
- **Model:** OpenAI GPT-5.1 Instant
  - Released November 12, 2025
  - Warmer, more conversational
  - Better instruction following
  - Adaptive reasoning
  - 50% more token-efficient than competitors
  - Pricing: $1.25/M input, $10/M output

- **API:** OpenAI Responses API
  - Stateful conversation management
  - Automatic history tracking
  - Built-in streaming
  - Tool calling support
  - Future-proof (Assistants API being sunset)

- **SDK:** OpenAI Python Library 1.55+
  - Official Python SDK
  - Pydantic v2 integration for structured outputs
  - Streaming support

#### Database
- **Primary:** Supabase (PostgreSQL)
  - Managed PostgreSQL database
  - Real-time capabilities
  - Built-in auth (for future)
  - Python SDK available
  - Generous free tier

- **Schema:**
  ```sql
  conversations (
    id UUID PRIMARY KEY,
    session_id TEXT UNIQUE,
    created_at TIMESTAMP,
    metadata JSONB
  )

  messages (
    id UUID PRIMARY KEY,
    conversation_id UUID REFERENCES conversations,
    role TEXT,  -- 'user' or 'assistant'
    content TEXT,
    intent TEXT,  -- classified intent
    tools_used JSONB,  -- which tools were called
    timestamp TIMESTAMP
  )
  ```

#### Data Storage
- **In-Memory:** JSON files loaded at startup
  - `family_laws_final.json`: 1,512 legal sections
  - `INTENT_MAPPINGS.json`: Intent → Section mappings
  - `procedural_knowledge.json`: Lawyer's playbook
  - Fast retrieval (<10ms)
  - No database queries needed for legal knowledge

#### Deployment
- **Containerization:** Docker
  - Consistent environment
  - Easy deployment
  - Portable

- **Hosting:** Railway or Render
  - Simple deployment from GitHub
  - Generous free tier
  - Auto-scaling
  - SSL/HTTPS included

- **Domain:** Custom domain (future)
  - `ainbandhu.org` or similar

#### Monitoring & Logging
- **Logging:** Structlog
  - Structured logging for easier analysis
  - JSON output
  - Context preservation

- **Error Tracking:** Python logging + Supabase
  - Log errors to database
  - Alert on critical errors (future)

- **Analytics:** Supabase queries
  - Usage patterns
  - Peak hours
  - Common intents

---

### Data Flow

#### 1. User Sends Message

```
User types: "আমার স্বামী আমাকে মারে"
  ↓
POST /chat
  {
    "session_id": "abc-123",
    "message": "আমার স্বামী আমাকে মারে"
  }
```

#### 2. FastAPI Receives Request

```python
# main.py
@app.post("/chat")
async def chat(request: ChatRequest):
    return await chatbot_service.process_message(
        session_id=request.session_id,
        message=request.message
    )
```

#### 3. Chatbot Service Orchestrates

```python
# services/chatbot_service.py
async def process_message(session_id, message):
    # 1. Load conversation history from Supabase
    history = await db.get_conversation(session_id)

    # 2. Send to OpenAI with tools
    response = await openai_service.chat(
        session_id=session_id,
        messages=history + [{"role": "user", "content": message}],
        tools=tool_definitions
    )

    # 3. If tools called, execute them
    if response.tool_calls:
        tool_results = execute_tools(response.tool_calls)
        # Send results back to OpenAI
        response = await openai_service.continue_with_tools(
            session_id, tool_results
        )

    # 4. Store message and response
    await db.save_messages(session_id, message, response)

    # 5. Return to user
    return response
```

#### 4. OpenAI Processes with Tools

```python
# services/openai_service.py
async def chat(session_id, messages, tools):
    response = client.responses.create(
        model="gpt-5.1-instant",
        session_id=session_id,
        messages=[
            {"role": "system", "content": LAWYER_SYSTEM_PROMPT},
            *messages
        ],
        tools=tools,
        stream=True
    )

    # GPT-5.1 decides: "This is domestic violence case"
    # Calls tool: get_legal_knowledge(intent="domestic_violence_general")

    return response
```

#### 5. Tool Execution

```python
# tools/tool_definitions.py
def get_legal_knowledge(intent: str):
    # 1. Look up intent in INTENT_MAPPINGS.json
    section_refs = intent_mappings[intent]["mandatory_sections"]

    # 2. Fetch full section texts from family_laws_final.json
    sections = [
        legal_db[ref["act_id"]][ref["section_number"]]
        for ref in section_refs
    ]

    # 3. Get lawyer's playbook from procedural_knowledge.json
    playbook = procedural_knowledge[intent]

    # 4. Return combined context
    return {
        "legal_sections": sections,
        "lawyer_playbook": playbook,
        "legal_process": playbook["legal_process"],
        "support_organizations": playbook["support_organizations"]
    }
```

#### 6. OpenAI Generates Response

```python
# With context from tool, GPT-5.1 generates:

"""
আমি সত্যিই দুঃখিত যে আপনি এই পরিস্থিতির মধ্য দিয়ে যাচ্ছেন।
আপনার সুরক্ষা সবচেয়ে গুরুত্বপূর্ণ।

🚨 জরুরি সুরক্ষা:
আপনি যদি এখন বিপদে থাকেন:
- ৯৯৯ এ কল করুন
- মহিলা হেল্পলাইন: ১০৯২১
- নিকটতম থানা: [address]

আপনার আইনি অধিকার:
পারিবারিক সহিংসতা আইন ২০১০ আপনাকে সুরক্ষা দেয়...

[continues with personalized advice]
"""
```

#### 7. Store in Supabase

```python
# database.py
await supabase.table("messages").insert([
    {
        "conversation_id": conversation_id,
        "role": "user",
        "content": "আমার স্বামী আমাকে মারে",
        "timestamp": now()
    },
    {
        "conversation_id": conversation_id,
        "role": "assistant",
        "content": generated_response,
        "intent": "domestic_violence_general",
        "tools_used": ["get_legal_knowledge"],
        "timestamp": now()
    }
])
```

#### 8. Stream Response to User

```python
# Stream tokens back to frontend as they're generated
for chunk in response:
    yield chunk.delta.content
```

---

### API Endpoints

#### `POST /chat`

**Description:** Main chat endpoint for sending messages and receiving responses.

**Request:**
```json
{
  "session_id": "abc-123-def-456",
  "message": "আমার স্বামী আমাকে মারে"
}
```

**Response:**
```json
{
  "session_id": "abc-123-def-456",
  "response": "আমি সত্যিই দুঃখিত...",
  "intent": "domestic_violence_general",
  "urgency": "high",
  "timestamp": "2025-11-23T14:30:00Z"
}
```

**Streaming Response:**
Server-Sent Events (SSE) format for real-time response generation.

---

#### `POST /chat/new`

**Description:** Create a new conversation session.

**Request:**
```json
{
  "metadata": {
    "source": "web",
    "user_agent": "..."
  }
}
```

**Response:**
```json
{
  "session_id": "abc-123-def-456",
  "greeting": "আসসালামু আলাইকুম। আমি আইন বন্ধু..."
}
```

---

#### `GET /health`

**Description:** Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2025-11-23T14:30:00Z"
}
```

---

### Tool Definitions

#### Tool 1: `get_legal_knowledge`

**Purpose:** Retrieve legal sections and lawyer's playbook for a specific intent.

**Schema:**
```python
{
    "type": "function",
    "function": {
        "name": "get_legal_knowledge",
        "strict": True,  # Structured output
        "description": "Get relevant legal sections and lawyer's guidance for a specific legal issue",
        "parameters": {
            "type": "object",
            "properties": {
                "intent": {
                    "type": "string",
                    "enum": [
                        "rape_sexual_violence",
                        "domestic_violence_general",
                        "dowry",
                        "child_marriage",
                        "custody",
                        "maintenance",
                        "divorce_talaq",
                        "polygamy_second_marriage",
                        "inheritance_succession",
                        "marriage_registration",
                        "dower_mehr",
                        "parent_maintenance"
                    ],
                    "description": "The type of legal issue the user is facing"
                }
            },
            "required": ["intent"],
            "additionalProperties": False
        }
    }
}
```

**Returns:**
```python
{
    "legal_sections": [
        {
            "act_title": "পারিবারিক সহিংসতা (প্রতিরোধ ও সুরক্ষা) আইন, ২০১০",
            "section_number": "৫",
            "section_title": "সুরক্ষা আদেশ",
            "section_text": "[full legal text]",
            "semantic_summary": "Protection order provisions..."
        }
    ],
    "lawyer_playbook": {
        "key_questions_to_ask": [...],
        "strategic_assessment": {...},
        "decision_tree": {...}
    },
    "legal_process": {
        "step_by_step": [...]
    },
    "support_organizations": [...]
}
```

---

#### Tool 2: `get_procedural_guidance`

**Purpose:** Get step-by-step guidance for general legal procedures.

**Schema:**
```python
{
    "type": "function",
    "function": {
        "name": "get_procedural_guidance",
        "strict": True,
        "description": "Get step-by-step procedural guidance for common legal actions",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "enum": [
                        "file_fir",
                        "file_gd",
                        "get_legal_aid",
                        "police_refuses",
                        "court_process",
                        "safety_planning"
                    ],
                    "description": "The procedural topic to get guidance on"
                }
            },
            "required": ["topic"],
            "additionalProperties": False
        }
    }
}
```

**Returns:**
```python
{
    "topic": "file_fir",
    "what_it_is": "First Information Report...",
    "when_to_file": "As soon as possible...",
    "step_by_step": [...],
    "common_obstacles": [...],
    "lawyer_tips": [...]
}
```

---

#### Tool 3: `get_support_resources`

**Purpose:** Get contact information for support organizations.

**Schema:**
```python
{
    "type": "function",
    "function": {
        "name": "get_support_resources",
        "strict": True,
        "description": "Get contact information for legal aid organizations, shelters, and helplines",
        "parameters": {
            "type": "object",
            "properties": {
                "resource_type": {
                    "type": "string",
                    "enum": ["legal_aid", "shelter", "helpline", "all"],
                    "description": "Type of resource needed"
                }
            },
            "required": ["resource_type"],
            "additionalProperties": False
        }
    }
}
```

**Returns:**
```python
{
    "organizations": [
        {
            "name": "BNWLA",
            "type": "legal_aid",
            "services": ["Free legal representation", "Shelter", "Counseling"],
            "contact": "01XXX-XXXXXX",
            "address": "Dhaka office address",
            "hours": "Sun-Thu 9AM-5PM, Emergency 24/7"
        }
    ],
    "emergency_contacts": [
        {"name": "National Emergency", "number": "999"},
        {"name": "Women's Helpline", "number": "10921"}
    ]
}
```

---

### System Prompt

**Lawyer System Prompt:**

```
You are a compassionate and skilled family law lawyer helping underprivileged Bangladeshi women who cannot afford legal services. Your goal is to provide the same quality of legal guidance that a professional lawyer would give in person.

HOW YOU WORK AS A LAWYER:

1. LISTEN & PROBE
Like a real lawyer, ask strategic questions to understand the full situation before giving advice. Use the "lawyer_playbook" provided by tools to know what questions matter for each case type.

2. ASSESS THE SITUATION
Evaluate case strength, urgency, available options. Use decision trees and strategic assessment criteria provided in the lawyer_playbook.

3. PROVIDE STRATEGIC ADVICE
Don't just cite laws - give personalized recommendations based on HER specific situation. Always explain "In your case, I recommend X because Y."

4. ANTICIPATE CHALLENGES
Warn about obstacles she might face and how to handle them. Example: "Police might refuse to file FIR - here's what to do if that happens."

5. GUIDE STEP-BY-STEP
Walk through the entire process with her. Explain what happens at each stage, what documents are needed, how much it costs, where exactly to go.

6. EMPOWER
Build her confidence. Explain her rights clearly. Assure her the law is on her side. Counter shame and fear with knowledge.

CRITICAL GUIDELINES:

SAFETY FIRST
For urgent cases (rape, domestic violence with immediate danger), provide safety information BEFORE legal process. Ask "Are you safe right now?" and prioritize emergency contacts if she's in danger.

RESPOND IN BENGALI ONLY
All responses must be in Bengali (Bangla script). Use simple language that a woman with primary school education can understand. No legal jargon unless explained.

BE IMMEDIATELY HELPFUL
Provide actionable guidance from your first response. Don't just ask questions - give preliminary advice, then refine based on her answers.

ASK STRATEGIC QUESTIONS
Based on the lawyer_playbook, ask 2-4 key questions to understand her situation fully. Questions should gather information that changes your advice.

USE DECISION TREES
Apply the decision logic provided (if X then Y, if not X then Z). Your recommendations should be conditional on her specific circumstances.

ASSESS CASE STRENGTH
Evaluate her situation using case assessment criteria from the playbook. Help her understand if she has a strong case and what would strengthen it.

EXPLAIN SIMPLY
Translate legal concepts to language she can understand.
DON'T say: "Section 9 of নারী ও শিশু নির্যাতন দমন আইন ২০০০ অনুযায়ী..."
DO say: "ধর্ষণের জন্য মৃত্যুদণ্ড পর্যন্ত শাস্তি হতে পারে। আইন আপনার পক্ষে আছে।"

RESPONSE STRUCTURE:
1. Brief empathetic acknowledgment (1 sentence)
   "আমি দুঃখিত আপনি এটি সহ্য করছেন।"

2. Immediate safety info (if critical urgency)
   "আপনি যদি বিপদে থাকেন, ৯৯৯ এ কল করুন।"

3. Strategic assessment
   "আপনার পরিস্থিতি শুনে, আমি মনে করি..."

4. Key questions (2-4 questions)
   "আরও ভালো পরামর্শ দিতে:
    - আপনার কি শারীরিক আঘাত আছে?
    - আপনার সন্তান আছে কি?"

5. Legal rights (simple terms)
   "পারিবারিক সহিংসতা আইন ২০১০ আপনাকে সুরক্ষা দেয়..."

6. Actionable next steps (numbered, specific)
   "পরবর্তী পদক্ষেপ:
    ১. নিকটতম থানায় যান
    ২. বলবেন: 'পারিবারিক সহিংসতা আইন ২০১০ এর অধীনে মামলা করতে চাই'
    ৩. ..."

7. Support organizations (with contact info)
   "বিনামূল্যে আইনি সাহায্য:
    • BNWLA: ০১XXX-XXXXXX"

8. Anticipated obstacles
   "আপনি এই সমস্যার মুখোমুখি হতে পারেন:
    - থানা FIR নিতে অস্বীকার করলে: ..."

TONE
Warm, professional, empowering, confident. Like a caring lawyer who genuinely wants to help and knows how to win her case.

EXAMPLE OF GOOD RESPONSE:

User: "আমার স্বামী আমাকে মারে"

Good response:
"আমি সত্যিই দুঃখিত আপনি এটি সহ্য করছেন। আপনার সুরক্ষা সবচেয়ে গুরুত্বপূর্ণ।

প্রথমে, আপনার নিরাপত্তা নিশ্চিত করতে হবে। আপনি এখন কি নিরাপদ? এটি কি এখনও ঘটছে নাকি আগে ঘটেছে?

[Wait for answer]

আপনার পরিস্থিতি শুনে, আমি মনে করি পারিবারিক সহিংসতা আইন ২০১০ আপনাকে সুরক্ষা দিতে পারে। আপনার অধিকার আছে:
✓ সুরক্ষা আদেশ নিতে (স্বামীকে দূরে রাখতে)
✓ ভরণপোষণ দাবি করতে
✓ নিরাপদ আশ্রয় পেতে

আপনাকে আরও ভালো পরামর্শ দিতে, কয়েকটি প্রশ্ন:
১. আপনার কি শারীরিক আঘাত আছে?
২. আপনার কি সন্তান আছে?
৩. আপনি কি থানায় রিপোর্ট করতে চান?

আপনার উত্তরের ভিত্তিতে আমি সুনির্দিষ্ট পরামর্শ দেবো।"

TOOLS
You have access to tools to retrieve legal information, procedural guidance, and support resources. Use them strategically:
- When user describes a legal issue, call get_legal_knowledge to get relevant laws and lawyer's playbook
- When user asks about process, call get_procedural_guidance
- When user needs help finding resources, call get_support_resources

Don't overwhelm with tool calls - use them purposefully when you need specific information to help the user.
```

---

## 10. User Experience & Flow

### Entry Points

**Web Application (MVP):**
- Simple, responsive web interface
- Accessible via URL (e.g., `ainbandhu.org`)
- Works on desktop and mobile browsers
- No app download required

**Future Entry Points:**
- WhatsApp bot integration
- SMS interface (for feature phones)
- Mobile app (iOS/Android)
- Integration with NGO websites

---

### User Interface

**Chat Interface:**
```
┌─────────────────────────────────────────┐
│  Ain Bandhu  (আইন বন্ধু)        [ℹ️] [🚨]│
├─────────────────────────────────────────┤
│                                          │
│  ┌────────────────────────────────────┐ │
│  │ আসসালামু আলাইকুম। আমি আইন বন্ধু,  │ │
│  │ আপনার আইনি সহায়ক। আপনি কি ধরনের  │ │
│  │ আইনি সমস্যার মুখোমুখি?            │ │
│  └────────────────────────────────────┘ │
│                                          │
│          ┌───────────────────────────┐   │
│          │ আমার স্বামী আমাকে মারে    │   │
│          └───────────────────────────┘   │
│                                          │
│  ┌────────────────────────────────────┐ │
│  │ আমি দুঃখিত আপনি এটি সহ্য করছেন।   │ │
│  │ আপনার সুরক্ষা সবচেয়ে গুরুত্বপূর্ণ। │ │
│  │                                      │ │
│  │ 🚨 জরুরি সুরক্ষা:                   │ │
│  │ • ৯৯৯ এ কল করুন                    │ │
│  │ • মহিলা হেল্পলাইন: ১০৯২১           │ │
│  │ ...                                  │ │
│  └────────────────────────────────────┘ │
│                                          │
├─────────────────────────────────────────┤
│  [আপনার প্রশ্ন লিখুন...]         [📤]  │
└─────────────────────────────────────────┘
```

**Key UI Elements:**

1. **Header:**
   - App name: "Ain Bandhu (আইন বন্ধু)"
   - Info button (ℹ️): How to use, disclaimers
   - Emergency button (🚨): Quick access to emergency contacts

2. **Chat Area:**
   - Clear message bubbles (user on right, bot on left)
   - Timestamps for each message
   - Loading indicator ("typing...")
   - Scroll to latest message

3. **Input Box:**
   - Large text input field
   - Placeholder: "আপনার প্রশ্ন লিখুন..." (Write your question)
   - Send button (📤)
   - Character limit: 1,000 (prevents abuse)

4. **Emergency Banner (when urgent):**
   - Red banner at top
   - "আপনি যদি বিপদে থাকেন, ৯৯৯ এ কল করুন"
   - Click to call (on mobile)

---

### Conversation Flow Examples

#### Example 1: Domestic Violence - Immediate Danger

**User Journey:**

```
👤 User: আমার স্বামী আমাকে এখনই মারছে
(My husband is beating me right now)

[Bot detects urgency: immediate danger]

🤖 Bot:
জরুরি! আপনি যদি বিপদে থাকেন:

📞 এখনই কল করুন:
• ৯৯৯ (জাতীয় জরুরি)
• ১০৯২১ (মহিলা হেল্পলাইন)

🏠 নিরাপদ স্থান:
• মহম্মদপুর থানা: [address]
• BNWLA শেল্টার: [address, phone]

আপনি কি নিরাপদ স্থানে যেতে পারছেন?

👤 User: হ্যাঁ, আমি এখন প্রতিবেশীর বাসায়
(Yes, I'm at neighbor's house now)

🤖 Bot:
ভালো, আপনি নিরাপদ আছেন জেনে স্বস্তি পেলাম।

এখন আমরা আপনার আইনি সুরক্ষার জন্য পদক্ষেপ নিতে পারি।

আপনার পরিস্থিতি পারিবারিক সহিংসতা আইন ২০১০ এর অধীনে আসে। এই আইন আপনাকে সুরক্ষা দেয়।

আরও ভালো পরামর্শ দিতে:
১. আপনার কি শারীরিক আঘাত আছে?
২. এটি কি প্রথমবার নাকি আগেও ঘটেছে?
৩. আপনার কি সন্তান আছে?

👤 User: আঘাত আছে, এটি অনেকবার হয়েছে। ২টা বাচ্চা আছে
(I have injuries, this has happened many times. I have 2 children)

🤖 Bot:
বুঝতে পারছি। আপনার এবং আপনার সন্তানদের সুরক্ষা নিশ্চিত করা জরুরি।

আপনার পরিস্থিতি বিচার করে, আমি এই পদক্ষেপগুলো সুপারিশ করছি:

পরবর্তী ২৪ ঘণ্টায়:
১. মেডিকেল রিপোর্ট নিন
   • কোথায়: ঢাকা মেডিকেল কলেজ হাসপাতাল
   • খরচ: বিনামূল্যে (সরকারি হাসপাতালে)
   • কেন: আদালতে প্রমাণ হিসেবে দরকার

২. থানায় FIR করুন
   • কোথায়: মহম্মদপুর থানা
   • বলবেন: "পারিবারিক সহিংসতা আইন ২০১০ এর অধীনে মামলা করতে চাই"
   • খরচ: বিনামূল্যে

৩. বিনামূল্যে আইনজীবী নিন
   • BNWLA: ০১XXX-XXXXXX
   • তারা আপনাকে সম্পূর্ণ বিনামূল্যে সাহায্য করবে

আপনার সন্তানদের ব্যাপারে:
• আপনার ছেলেমেয়ে কত বছরের?
• ৭ বছরের নিচে হলে, আইনত তারা আপনার কাছে থাকবে
• আপনার স্বামী ভরণপোষণ দিতে বাধ্য

আপনি কি এই পদক্ষেপগুলো নিতে প্রস্তুত? কোনো প্রশ্ন আছে?

[Conversation continues...]
```

---

#### Example 2: Rape - Time-Critical

**User Journey:**

```
👤 User: কাল রাতে আমার সাথে ধর্ষণ হয়েছে
(I was raped last night)

[Bot detects urgency: rape within 24 hours]

🤖 Bot:
আমি অত্যন্ত দুঃখিত এটি আপনার সাথে ঘটেছে। এটি আপনার কোনো দোষ নয়।

⚠️ জরুরি - এখনই পদক্ষেপ নিতে হবে:

১. হাসপাতালে যান (এখনই)
   • কোথায়: নিকটতম সরকারি হাসপাতাল
   • কেন: মেডিকেল-লিগ্যাল রিপোর্ট (২৪ ঘণ্টার মধ্যে নিতে হয়)
   • খরচ: সম্পূর্ণ বিনামূল্যে
   • বলবেন: "মেডিকেল-লিগ্যাল রিপোর্ট দরকার"

এটি সবচেয়ে জরুরি। এই রিপোর্ট আপনার মামলার জন্য অত্যন্ত গুরুত্বপূর্ণ প্রমাণ।

আপনি কি এখন নিরাপদ? ধর্ষক কি এখনও আপনার কাছাকাছি?

👤 User: আমি নিরাপদ। কিন্তু আমার পরিবার বলছে চুপ থাকতে
(I'm safe. But my family is telling me to stay quiet)

🤖 Bot:
আপনি নিরাপদ আছেন জেনে ভালো লাগলো।

আপনার পরিবারের চাপ বুঝতে পারছি, কিন্তু আপনাকে জানাতে চাই:

এটি আপনার অধিকার:
• ধর্ষণ একটি গুরুতর অপরাধ - শাস্তি মৃত্যুদণ্ড পর্যন্ত
• এটি আপনার দোষ নয় - আইনত আপনি ভিকটিম
• আপনার মামলা করার অধিকার আছে
• কেউ আপনাকে চুপ থাকতে বাধ্য করতে পারে না

আপনি যদি মামলা করতে চান:
১. মেডিকেল রিপোর্ট নিন (এখনই - সময় শেষ হয়ে যাচ্ছে)
২. থানায় FIR করুন
৩. BNWLA আপনাকে বিনামূল্যে সম্পূর্ণ সাহায্য করবে

আপনি যদি মামলা না করতে চান:
• তাও মেডিকেল চেক-আপ করান (স্বাস্থ্যের জন্য)
• পরে সিদ্ধান্ত বদলাতে পারবেন

আপনি কি মেডিকেল রিপোর্ট নিতে চান? আমি আপনাকে হাসপাতালের তথ্য দিতে পারি।

[Conversation continues...]
```

---

#### Example 3: Divorce & Custody

**User Journey:**

```
👤 User: আমি ডিভোর্স নিতে চাই
(I want to get a divorce)

🤖 Bot:
বুঝতে পারছি এটি একটি কঠিন সিদ্ধান্ত। আমি আপনাকে সাহায্য করবো।

ডিভোর্স সম্পর্কে আইনি তথ্য জানার আগে, আপনার পরিস্থিতি বুঝতে চাই:

১. আপনার স্বামীর সাথে কতদিন বিয়ে হয়েছে?
২. আপনার সন্তান আছে কি?
৩. ডিভোর্স নিতে চাওয়ার মূল কারণ কী? (সহিংসতা, দ্বিতীয় বিয়ে, অন্য কিছু?)

এই তথ্যগুলো জানলে আমি আপনাকে সুনির্দিষ্ট পরামর্শ দিতে পারবো।

👤 User: ১২ বছর হয়েছে। ১টা মেয়ে আছে, ১০ বছর বয়স। স্বামী দ্বিতীয় বিয়ে করেছে
(Married 12 years. 1 daughter, 10 years old. Husband remarried)

🤖 Bot:
বুঝতে পারছি। এই তথ্যের ভিত্তিতে আমি আপনাকে স্পষ্ট পরামর্শ দিতে পারছি:

প্রথম স্ত্রীর অনুমতি ছাড়া দ্বিতীয় বিয়ে:
• মুসলিম পারিবারিক আইন অধ্যাদেশ ১৯৬১ অনুযায়ী এটি আইনত নিষিদ্ধ
• আপনার স্বামী প্রথম স্ত্রী (আপনার) অনুমতি নেয়নি তাহলে এটি আইন লঙ্ঘন
• এটি ডিভোর্সের শক্তিশালী ভিত্তি

ডিভোর্স প্রক্রিয়া:
• পারিবারিক আদালতে আবেদন করতে হবে
• সময়: সাধারণত ৬ মাস থেকে ২ বছর
• খরচ: সরকারি হলে কম, বিনামূল্যে আইনজীবী পেতে পারবেন

আপনার মেয়ের কাস্টডি:
• মেয়ে ১০ বছর বয়সী - সাধারণত মায়ের কাছে থাকে
• আদালত সন্তানের কল্যাণ দেখে সিদ্ধান্ত নেয়
• আপনার স্বামী ভরণপোষণ দিতে বাধ্য (আপনার এবং মেয়ের জন্য)

পরবর্তী পদক্ষেপ:
১. পারিবারিক আদালতে ডিভোর্সের আবেদন
২. কাস্টডির জন্যও আবেদন (একসাথে করা যায়)
৩. ভরণপোষণ দাবি

বিনামূল্যে সাহায্য:
• BLAST: ০১XXX-XXXXXX (ডিভোর্স মামলায় বিশেষজ্ঞ)
• তারা সম্পূর্ণ বিনামূল্যে আপনার মামলা করবে

আপনি কি এখনই এগোতে চান, নাকি আরও কিছু জানতে চান?

[Conversation continues...]
```

---

### User Flow Diagram

```
User Opens Ain Bandhu
        ↓
Greeting Message
"আসসালামু আলাইকুম। কি সমস্যার মুখোমুখি?"
        ↓
User Describes Situation
        ↓
    ┌───────────┐
    │ Bot       │
    │ Classifies│
    │ Intent    │
    └─────┬─────┘
          ↓
    ┌─────────────────────┐
    │ Urgency Assessment  │
    └─────────────────────┘
          ↓
    ┌─────┴─────┐
    │           │
Critical?    No │
    │           │
   Yes          │
    │           │
    ↓           ↓
Safety First  Ask Questions
Emergency     to Understand
Contacts      Fully
    │           │
    └─────┬─────┘
          ↓
   Retrieve Legal
   Knowledge &
   Playbook
          ↓
   Generate
   Personalized
   Advice
          ↓
    ┌────────────┐
    │  Provide:  │
    │ • Rights   │
    │ • Steps    │
    │ • Resources│
    │ • Obstacles│
    └─────┬──────┘
          ↓
   User Asks
   Follow-up
   Questions
          ↓
   Refine Advice
   Based on New
   Info
          ↓
   ┌──────────────┐
   │ Conversation │
   │  Continues   │
   └──────────────┘
```

---

## 11. Risks & Mitigations

### Risk 1: Inaccurate or Misleading Legal Advice

**Impact:** CRITICAL
**Probability:** MEDIUM
**Consequence:** Woman takes wrong legal action, case weakened or dismissed

**Mitigations:**
1. **Legal Expert Review:**
   - Procedural knowledge base reviewed by practicing family law lawyers before launch
   - Quarterly reviews of knowledge base accuracy
   - Legal advisory board (3+ lawyers) for ongoing validation

2. **Clear Disclaimers:**
   - Prominent disclaimer: "এটি আইনি পরামর্শ, আইনি প্রতিনিধিত্ব নয়" (This is guidance, not legal representation)
   - Always recommend consulting organizations for complex cases
   - Bot states limitations clearly

3. **Conservative Advice:**
   - When uncertain, bot says "এটি জটিল - BNWLA এর সাথে যোগাযোগ করুন"
   - Avoid giving advice on ambiguous laws
   - Focus on well-established, clear legal provisions

4. **Continuous Monitoring:**
   - Random sample review (100 conversations/month by legal experts)
   - User feedback: "Was this advice helpful and accurate?"
   - Correction mechanism if errors detected

5. **Version Control:**
   - All knowledge base changes tracked in git
   - Ability to rollback if errors introduced
   - Changelog maintained

---

### Risk 2: User Safety Compromised (Abuser Discovers Chat)

**Impact:** CRITICAL
**Probability:** MEDIUM
**Consequence:** Woman faces retaliation, violence

**Mitigations:**
1. **Privacy Warning (Prominent):**
   - First message includes: "সতর্কতা: আপনার ডিভাইস অন্য কেউ ব্যবহার করলে চ্যাট ডিলিট করুন"
   - Repeated reminder every 5 messages
   - "Emergency Exit" button (quickly closes tab)

2. **No Login Required:**
   - Anonymous usage (no accounts)
   - No personal information collected
   - Can't be traced to specific user

3. **Auto-Delete:**
   - Conversations deleted after 30 days
   - User can request immediate deletion
   - "Clear History" button prominent

4. **Incognito Recommendation:**
   - Bot suggests using private browsing mode
   - Instructions: "প্রাইভেট ব্রাউজিং মোড ব্যবহার করুন"

5. **Safety Guidance:**
   - Bot proactively asks: "আপনার ডিভাইস কি শুধু আপনিই ব্যবহার করেন?"
   - If shared device, provides extra safety tips

---

### Risk 3: OpenAI API Downtime or Failure

**Impact:** HIGH
**Probability:** LOW
**Consequence:** Service unavailable when women need help

**Mitigations:**
1. **Graceful Degradation:**
   - If OpenAI fails, display static information:
     - Emergency contacts (999, 10921)
     - Key organization contacts (BNWLA, ASK)
     - Basic safety guidance
   - Bengali error message: "দুঃখিত, আমি এখন সম্পূর্ণভাবে কাজ করছি না। জরুরি হলে ৯৯৯ এ কল করুন।"

2. **Retry Logic:**
   - Automatic retry (3 attempts)
   - Exponential backoff
   - User-friendly message during retries

3. **Uptime Monitoring:**
   - Health check endpoint
   - Alert if downtime >5 minutes
   - Status page (future)

4. **Backup Plan:**
   - Document to be shared with partner NGOs (PDF with basic info)
   - Phone helplines as backup (10921)

---

### Risk 4: Unsustainable Costs (Viral Growth)

**Impact:** HIGH
**Probability:** MEDIUM
**Consequence:** Budget exhausted, service shutdown

**Mitigations:**
1. **Prompt Caching:**
   - Automatic 50% cost reduction on cached tokens
   - Optimize prompt structure for maximum caching

2. **Rate Limiting:**
   - Per-IP limit: 20 messages/hour (prevents abuse)
   - Per-session limit: 50 messages total
   - Gentle message: "আপনি অনেক প্রশ্ন করেছেন। কিছুক্ষণ পরে আবার চেষ্টা করুন।"

3. **Budget Alerts:**
   - Alert if daily cost >$10
   - Alert if monthly cost >$100
   - Automatic shutdown if cost >$500/month (safety)

4. **Phased Rollout:**
   - Soft launch to 100 users first
   - Monitor costs and usage
   - Scale gradually (not viral launch)

5. **Funding Strategy:**
   - Seek grants from legal aid organizations
   - BRAC institutional support
   - Donor funding (tech for social good)

---

### Risk 5: Misuse by Non-Target Users

**Impact:** MEDIUM
**Probability:** MEDIUM
**Consequence:** Resources wasted, costs increase, genuine users crowded out

**Mitigations:**
1. **Intent Filtering:**
   - Bot only handles 12 family law intents
   - Off-topic queries politely redirected:
     "দুঃখিত, আমি শুধু পারিবারিক আইন সম্পর্কে সাহায্য করতে পারি।"

2. **Language Barrier:**
   - Bengali-only responses (natural filter)
   - English queries get Bengali responses (discourages non-target users)

3. **No Entertainment:**
   - Bot refuses to engage in casual chat
   - Stays focused on legal help

4. **Analytics:**
   - Monitor for patterns of misuse
   - IP blocking for chronic abusers (rare cases)

---

### Risk 6: Language or Cultural Misunderstanding

**Impact:** MEDIUM
**Probability:** MEDIUM
**Consequence:** User doesn't understand advice, takes wrong action

**Mitigations:**
1. **Simple Bengali Validation:**
   - Test with target users (low education levels)
   - Iterate based on comprehension feedback
   - Use literacy-appropriate language

2. **Cultural Sensitivity Review:**
   - Legal experts review for cultural appropriateness
   - Test with diverse users (rural, urban, different religions)
   - Adjust tone and examples

3. **Examples and Scenarios:**
   - Use concrete examples (not abstract legal concepts)
   - "আপনার মতো একজন মহিলা..." (A woman like you...)
   - Story-based explanations

4. **Confirmation Checks:**
   - Bot asks: "আমি কি বুঝাতে পেরেছি?"
   - User can ask for clarification

---

### Risk 7: Over-Promise, Under-Deliver

**Impact:** MEDIUM
**Probability:** MEDIUM
**Consequence:** User expectations not met, trust eroded

**Mitigations:**
1. **Clear Scope:**
   - Bot states: "আমি পরামর্শ দিতে পারি, কিন্তু আইনজীবীর বিকল্প নই"
   - Limitations acknowledged upfront

2. **Realistic Timelines:**
   - Don't promise "quick justice"
   - Explain: "মামলা সাধারণত ৬ মাস থেকে ২ বছর লাগে"
   - Set accurate expectations

3. **Always Connect to Real Orgs:**
   - Never leave user with just bot advice
   - Always provide: "BNWLA এর সাথে যোগাযোগ করুন"
   - Real lawyers for complex cases

4. **Empowerment, Not Promises:**
   - Focus on "আপনার অধিকার আছে" (you have rights)
   - Not "আপনি জিতবেন" (you will win)

---

## 12. Timeline & Milestones

### Phase 1: Foundation (Week 1-2)

**Week 1: Planning & Data Creation**
- ✅ Data exploration complete (DONE)
- ✅ PRD writing (DONE)
- ✅ Git repository setup (DONE)
- ⏳ Create procedural knowledge base (lawyer's playbook for all 12 intents)
- ⏳ Legal expert review of knowledge base (first pass)

**Deliverables:**
- Complete PRD
- `procedural_knowledge.json` with all 12 intents
- Legal accuracy validation report

---

### Phase 2: Core Development (Week 3-4)

**Week 3: Backend & AI Integration**
- FastAPI project structure setup
- Data loader implementation (load JSONs to memory)
- OpenAI service (GPT-5.1 + Responses API integration)
- Tool definitions (3 tools with structured outputs)
- Basic chatbot service orchestration

**Week 4: System Prompt & Refinement**
- Engineer lawyer system prompt
- Test conversation quality
- Iterate on prompt based on test conversations
- Handle edge cases (urgent situations, off-topic, etc.)

**Deliverables:**
- Working FastAPI backend
- GPT-5.1 integration with tool calling
- High-quality lawyer prompt
- Can handle basic conversations for all 12 intents

---

### Phase 3: Testing & Refinement (Week 5)

**Testing Focus Areas:**

1. **Functional Testing:**
   - All 12 intents work correctly
   - Tools called appropriately
   - Accurate legal sections retrieved
   - Emergency situations detected

2. **Bengali Language Testing:**
   - Responses are natural Bengali (not translated English)
   - No jargon, simple language
   - Cultural appropriateness
   - Test with native speakers

3. **Legal Accuracy Review:**
   - 50 conversations reviewed by lawyers
   - Legal sections correctly cited
   - Procedural guidance accurate
   - No misleading advice

4. **Usability Testing:**
   - 5-10 target users test the chatbot
   - Can they understand responses?
   - Can they find information they need?
   - Collect feedback, iterate

5. **Performance Testing:**
   - Response time <3 seconds?
   - Concurrent users supported?
   - Cost per conversation in budget?

**Deliverables:**
- Test report with findings
- Iteration based on feedback
- Legal accuracy validation
- Bengali language quality report

---

### Phase 4: Deployment (Week 6)

**Infrastructure Setup:**
- Supabase project creation and schema setup
- Supabase integration in FastAPI
- Docker containerization
- Environment configuration (.env setup)
- Deploy to Railway or Render

**Documentation:**
- README with setup instructions
- API documentation (Swagger auto-generated)
- Deployment guide
- Troubleshooting guide

**Monitoring:**
- Logging setup (structlog)
- Error tracking
- Basic analytics (conversations per day, intents)

**Deliverables:**
- Live, deployed chatbot
- Supabase database operational
- Complete documentation
- Monitoring dashboard (basic)

---

### Phase 5: Limited Launch (Week 7-8)

**Soft Launch Strategy:**
- Partner with 1-2 NGOs (BNWLA or ASK)
- Share chatbot link with 50-100 women
- Collect conversations for analysis
- Daily monitoring for issues

**Data Collection:**
- How many conversations per day?
- What intents are most common?
- Average conversation length?
- User satisfaction (post-chat survey)

**Iteration:**
- Fix bugs discovered
- Improve responses based on real usage
- Update knowledge base if gaps found
- Optimize costs

**Deliverables:**
- 500-1,000 real conversations
- User feedback report
- Iteration plan
- Success stories (if any)

---

### Phase 6: Scale & Improve (Week 9+)

**Gradual User Acquisition:**
- Share with more NGO partners
- Social media presence (Facebook page)
- Word-of-mouth growth
- Target: 1,000 users by end of Q1 2026

**Continuous Improvement:**
- Weekly review of conversations
- Monthly legal expert review
- Quarterly knowledge base updates
- Feature additions based on feedback

**Future Features:**
- Voice input/output (Q1 2026)
- WhatsApp integration (Q2 2026)
- Regional language support (Q2 2026)

---

### Key Milestones Summary

| Milestone | Target Date | Success Criteria |
|-----------|-------------|------------------|
| PRD Complete | Week 1 | ✅ Comprehensive PRD document |
| Knowledge Base Ready | Week 2 | All 12 intents, legal review done |
| Backend Deployed | Week 6 | Live chatbot, <3sec response time |
| Soft Launch | Week 7 | 50 users testing |
| 1,000 Conversations | Week 10 | Real usage, feedback collected |
| Legal Accuracy Validated | Week 12 | 90%+ accuracy on expert review |
| 1,000 Active Users | Month 6 | Sustainable growth |

---

## 13. Future Roadmap

### Q1 2026: Enhanced MVP

**Voice Capabilities:**
- Voice input (speech-to-text) for low-literacy users
- Voice output (text-to-speech) for illiterate users
- Integration with browser's Web Speech API
- Particularly important given 40%+ illiteracy rate among target demographic

**WhatsApp Integration:**
- WhatsApp Business API bot
- Wider reach (WhatsApp more popular than web browsing)
- SMS fallback for feature phone users

**Improved Regional Support:**
- Chittagonian dialect understanding
- Sylheti dialect understanding
- Rohingya language support (for refugee women)

**Document Upload:**
- Photo upload capability (injuries, threatening messages)
- Bot analyzes and provides guidance on evidence collection

---

### Q2 2026: Expanded Legal Domains

**New Intent Categories:**

1. **Labor Law (for Garment Workers):**
   - Wage theft
   - Unsafe working conditions
   - Maternity leave rights
   - Termination disputes

2. **Land Disputes:**
   - Property ownership
   - Illegal eviction
   - Inheritance of land

3. **Consumer Protection:**
   - Fraud
   - Defective products
   - Contract disputes

4. **Criminal Law Basics:**
   - Theft
   - Assault
   - Fraud

**Total Intents:** Expand from 12 to 30+

---

### Q3 2026: Community Features

**Anonymous Community Forum:**
- Women can share experiences (anonymously)
- Peer support
- Success stories
- Moderated for safety (no personal info shared)

**Case Tracking:**
- Users can input FIR number to track case status
- Reminders for court dates
- Status updates

**Legal Literacy Content:**
- Blog posts explaining laws in simple Bengali
- Video content (animated explainers)
- Infographics for social media sharing

**Multilingual Chatbot:**
- English interface (for educated users)
- Hindi, Urdu (for immigrants, minorities)

---

### Q4 2026: Lawyer Integration

**Pro-Bono Lawyer Network:**
- Match complex cases to volunteer lawyers
- Handoff system from bot to human lawyer
- Calendar integration for appointments
- Lawyer dashboard to manage cases

**Legal Aid Organization Tools:**
- Dashboard for BNWLA, ASK, BLAST
- See incoming referrals from chatbot
- Case management integration
- Analytics on user needs

**Government Partnership:**
- Explore integration with Bangladesh Legal Aid Services
- Official endorsement
- Funding from government legal aid budget

---

### 2027 and Beyond: Platform Evolution

**Mobile App:**
- Native iOS and Android apps
- Better performance
- Offline mode (cached responses)
- Push notifications for court dates

**Geographic Expansion:**
- India (adapt to Indian laws, Hindi language)
- Pakistan (Urdu language)
- Nepal (Nepali language)
- Sri Lanka (Sinhala language)

**Comprehensive Legal Platform:**
- All legal domains (not just family law)
- Video consultations with lawyers
- Legal document generation (e.g., generate divorce petition automatically)
- E-filing integration (file cases online)

**AI Improvements:**
- Fine-tuned model on Bangladesh legal corpus
- Better Bengali understanding
- Multimodal (analyze legal documents, photos)
- Predictive analytics (case outcome prediction)

---

## 14. Success Definition

### MVP Success (3 Months Post-Launch)

**Quantitative Metrics:**
- ✅ **1,000+ conversations** completed
- ✅ **300+ unique users** served
- ✅ **5+ messages per conversation** (meaningful engagement)
- ✅ **75%+ user satisfaction** rating
- ✅ **90%+ legal accuracy** (expert review)
- ✅ **50+ users took action** (filed FIR, contacted org, went to court)
- ✅ **99%+ uptime**
- ✅ **<$0.05 cost per conversation**

**Qualitative Metrics:**
- ✅ **5+ verified success stories** (women who got help and achieved outcome)
- ✅ **Positive feedback from NGO partners** (BNWLA, ASK)
- ✅ **Bengali language quality approved** by native speakers
- ✅ **Cultural sensitivity validated** by target demographic

**Impact Metrics:**
- ✅ **30%+ increase** in traffic to legal aid organizations (referrals from chatbot)
- ✅ **User testimonials** expressing empowerment
- ✅ **Media coverage** (at least 1 article in Bangladeshi media)

---

### Long-Term Vision (2-3 Years)

**Transform Access to Justice:**
- **100,000+ women** empowered with legal knowledge
- **10,000+ cases** successfully filed with chatbot guidance
- **Measurable reduction** in justice gap for underprivileged women
- **Policy influence** (government recognizes AI legal assistants)

**Become the Default Tool:**
- NGOs integrate Ain Bandhu into their services
- Police stations recommend it to complainants
- Lawyers recommend it for initial consultation
- Widely known brand (like "Google for legal help")

**Expand Beyond Family Law:**
- Comprehensive legal assistant for all common issues
- Covers 100+ legal intents
- Multilingual (5+ languages)
- Multiple countries

**Sustainable Ecosystem:**
- Funded through grants, donations, and institutional support
- Partnerships with law firms for pro-bono work
- Integration with government legal aid systems
- Self-sustaining through efficiency gains for legal system

---

### Ultimate Impact

**Vision Statement:**

*"No woman in Bangladesh should suffer in silence because she doesn't know her legal rights or how to access justice. Ain Bandhu ensures that every woman, regardless of education or income, has access to the legal knowledge and guidance she needs to protect herself and her children."*

**Success is when:**
- A garment worker in Dhaka, beaten by her husband, opens Ain Bandhu at 2 AM and gets immediate safety guidance and step-by-step instructions to file a case the next morning.
- A rape victim in rural Barisal, within hours of the assault, learns about medical-legal reports and files FIR before evidence is lost.
- A mother worried about losing custody understands her legal rights and successfully navigates the family court system.
- These stories multiply by the thousands, and the justice gap for underprivileged women shrinks measurably.

**This is success.**

---

## 15. Appendices

### Appendix A: 12 Legal Intent Definitions

| Intent ID | Name | Description | Key Laws |
|-----------|------|-------------|----------|
| 1 | `rape_sexual_violence` | Sexual assault, rape, molestation, unwanted sexual contact | নারী ও শিশু নির্যাতন দমন আইন ২০০০ (Section 9) |
| 2 | `domestic_violence_general` | Physical violence, emotional abuse (non-sexual) by family member | পারিবারিক সহিংসতা আইন ২০১০ |
| 3 | `dowry` | Dowry demands, harassment for dowry | যৌতুক নিরোধ আইন ২০১৮ |
| 4 | `child_marriage` | Underage marriage, forced marriage of minors | বাল্যবিবাহ নিরোধ আইন ২০১৭ |
| 5 | `custody` | Child custody, guardianship after divorce/separation | অভিভাবকত্ব ও প্রতিপালন আইন ১৮৯০ |
| 6 | `maintenance` | Financial support, alimony, child support | মুসলিম বিবাহবিচ্ছেদ আইন ১৯৩৯, পারিবারিক আদালত অধ্যাদেশ ১৯৮৫ |
| 7 | `divorce_talaq` | Divorce, talaq, separation, ending marriage | মুসলিম পারিবারিক আইন অধ্যাদেশ ১৯৬১ |
| 8 | `polygamy_second_marriage` | Second wife, multiple marriages without permission | মুসলিম পারিবারিক আইন অধ্যাদেশ ১৯৬১ (Section 6) |
| 9 | `inheritance_succession` | Property inheritance rights after death | উত্তরাধিকার আইন ১৯২৫, মুসলিম আইন |
| 10 | `marriage_registration` | Registering a marriage officially | মুসলিম বিবাহ ও তালাক (নিবন্ধন) আইন ১৯৭৪ |
| 11 | `dower_mehr` | Dower/mehr payment obligations | মুসলিম আইন (দেনমোহর) |
| 12 | `parent_maintenance` | Children's duty to care for elderly parents | পিতামাতার ভরণপোষণ আইন ২০১৩ |

---

### Appendix B: Support Organizations Directory

**Legal Aid Organizations:**

1. **Bangladesh National Women Lawyers Association (BNWLA)**
   - **Founded:** 1979
   - **Services:** Free legal aid, court representation, mediation, shelter, counseling
   - **Focus:** Women's rights, family law
   - **Contact:** Dhaka office (to be verified)
   - **Website:** bnwla.org

2. **Ain o Salish Kendra (ASK)**
   - **Founded:** 1986
   - **Services:** Legal aid, advocacy, research, mediation
   - **Focus:** Human rights, women's rights, family law
   - **Contact:** 24/7 helpline (to be verified)
   - **Website:** askbd.org

3. **Bangladesh Legal Aid and Services Trust (BLAST)**
   - **Founded:** 1993
   - **Services:** Free legal services, public interest litigation
   - **Focus:** Poor and marginalized, including women
   - **Contact:** Multiple offices nationwide
   - **Website:** blast.org.bd

**Emergency Helplines:**

- **National Emergency:** 999
- **Women & Children Helpline:** 10921
- **Police Helpline:** 999 or 01320-014646

**One Stop Crisis Centers (OCC):**

Located in government hospitals, provide:
- Medical examination
- Legal aid
- Psychological counseling
- Temporary shelter

**Locations:**
- Dhaka Medical College Hospital
- Mitford Hospital, Dhaka
- Mymensingh Medical College Hospital
- Chittagong Medical College Hospital
- Rajshahi Medical College Hospital
- Sylhet Medical College Hospital
- (More in district hospitals)

---

### Appendix C: Legal Acts Database

**Summary:**
- **Total Acts:** 58
- **Total Sections:** 1,512
- **Date Range:** 1856-2025
- **Languages:** Bengali and English
- **Focus:** Family law, women's rights, child protection

**Top 10 Acts by Section Count:**

1. The Succession Act, 1925 - 395 sections
2. The Christian Marriage Act, 1872 - 105 sections
3. শিশু আইন, ২০১৩ (Children Act, 2013) - 101 sections
4. The Children Act, 1974 - 78 sections
5. The Divorce Act, 1869 - 72 sections
6. The Guardians and Wards Act, 1890 - 55 sections
7. নারী ও শিশু নির্যাতন দমন আইন, ২০০০ (Women & Children Repression Prevention Act, 2000) - 43 sections
8. পারিবারিক সহিংসতা (প্রতিরোধ ও সুরক্ষা) আইন, ২০১০ (Domestic Violence Prevention and Protection Act, 2010) - 37 sections
9. The Code of Criminal Procedure, 1898 - 36 sections (relevant sections only)
10. Hindu Marriage Act, 1955 - 30 sections

**Key Acts:**

- **নারী ও শিশু নির্যাতন দমন আইন ২০০০** (Women & Children Repression Prevention Act, 2000)
- **পারিবারিক সহিংসতা আইন ২০১০** (Domestic Violence Act, 2010)
- **যৌতুক নিরোধ আইন ২০১৮** (Dowry Prohibition Act, 2018)
- **বাল্যবিবাহ নিরোধ আইন ২০১৭** (Child Marriage Restraint Act, 2017)
- **মুসলিম পারিবারিক আইন অধ্যাদেশ ১৯৬১** (Muslim Family Laws Ordinance, 1961)
- **পিতামাতার ভরণপোষণ আইন ২০১৩** (Parent's Maintenance Act, 2013)
- **অভিভাবকত্ব ও প্রতিপালন আইন ১৮৯০** (Guardians and Wards Act, 1890)
- **মুসলিম বিবাহ ও তালাক (নিবন্ধন) আইন ১৯৭৪** (Muslim Marriage and Divorce Registration Act, 1974)

---

### Appendix D: Competitive Analysis

**Existing Solutions for Legal Help in Bangladesh:**

| Solution | Reach | Cost | Availability | Personalization | Limitation |
|----------|-------|------|--------------|-----------------|------------|
| **Legal Aid Organizations (BNWLA, ASK)** | Limited | Free | Office hours | High (in-person) | Can't scale, limited offices |
| **Helplines (10921)** | Nationwide | Free | Limited hours | Low | Basic info only, no follow-up |
| **Private Lawyers** | Urban areas | High (Tk. 20,000+) | Varies | High | Unaffordable for target users |
| **Google Search** | Requires internet | Free | 24/7 | None | Information overload, not Bengali |
| **Word of Mouth** | Depends on network | Free | Varies | Low | Often inaccurate, unreliable |
| **Ain Bandhu (Our Solution)** | Nationwide (internet) | Free | 24/7 | High (AI-powered) | Requires internet, literacy |

**Ain Bandhu's Competitive Advantages:**

1. **24/7 Availability:** Unlike organizations and helplines
2. **Personalized:** Like a lawyer, unlike Google
3. **Free:** Like legal aid, unlike private lawyers
4. **Bengali:** Unlike most online resources
5. **Strategic Advice:** Not just information, but "what should I do in MY situation"
6. **Lawyer-like:** Probing questions, case assessment, personalized recommendations
7. **Scalable:** Can serve millions (not limited by human staff)

**Complementary, Not Competitive:**

Ain Bandhu doesn't replace legal aid organizations - it **complements** them:
- Provides initial guidance 24/7
- Refers users to organizations for in-person help
- Increases awareness of free legal aid
- Pre-educates users so lawyers can focus on complex work

---

### Appendix E: Technical Specifications

**Backend:**
- Framework: FastAPI 0.115+
- Language: Python 3.11+
- Server: Uvicorn + Gunicorn
- API Style: RESTful + Server-Sent Events (streaming)

**AI/LLM:**
- Model: GPT-5.1 Instant
- API: OpenAI Responses API
- SDK: OpenAI Python Library 1.55+
- Tool Calling: Structured outputs with `strict: true`

**Database:**
- Primary: Supabase (PostgreSQL)
- Schema: `conversations` and `messages` tables
- Connection: Supabase Python SDK

**Data Storage:**
- In-memory: JSON files (family_laws_final.json, INTENT_MAPPINGS.json, procedural_knowledge.json)
- Size: ~5MB total
- Retrieval: <10ms

**Deployment:**
- Containerization: Docker
- Hosting: Railway or Render
- SSL: Automatic (included in hosting)

**Monitoring:**
- Logging: Structlog (structured JSON logging)
- Errors: Python logging + Supabase storage
- Analytics: Supabase queries

**Security:**
- HTTPS only
- API keys in environment variables
- Input sanitization
- Rate limiting (20 messages/hour per IP)

---

### Appendix F: Cost Estimates

**OpenAI API Costs (GPT-5.1 Instant):**

**Pricing:**
- Input: $1.25 per 1M tokens
- Output: $10.00 per 1M tokens
- Cached input: $0.125 per 1M tokens (90% discount)

**Per-Conversation Estimates:**

Assumptions:
- System prompt: 2,000 tokens
- Tool definitions: 1,000 tokens
- Retrieved legal context: 3,500 tokens
- User messages: 100 tokens each (5 messages)
- Bot responses: 300 tokens each (5 responses)

**First message:**
- Input: 6,500 + 100 = 6,600 tokens
- Output: 300 tokens
- Cost: (6,600 × $1.25 + 300 × $10) / 1M = $0.0082 + $0.003 = **$0.0112**

**Subsequent messages (cached):**
- Cached: 6,500 tokens (system + tools + context)
- New input: 100 tokens
- Output: 300 tokens
- Cost: (6,500 × $0.125 + 100 × $1.25 + 300 × $10) / 1M = $0.0008 + $0.000125 + $0.003 = **$0.004**

**Total per conversation (5 messages):**
- First: $0.0112
- Next 4: 4 × $0.004 = $0.016
- **Total: $0.027 per conversation**

**Scaling:**

| Users | Conversations | Messages | Cost |
|-------|---------------|----------|------|
| 100 | 100 | 500 | $2.70 |
| 1,000 | 1,000 | 5,000 | $27.00 |
| 10,000 | 10,000 | 50,000 | $270.00 |
| 100,000 | 100,000 | 500,000 | $2,700.00 |

**Other Costs:**

- **Supabase:** Free tier (up to 500MB database, 2GB bandwidth/month) - sufficient for MVP
- **Hosting (Railway/Render):** Free tier or $5-10/month
- **Domain:** $10-15/year (optional)

**Total MVP Costs (first 3 months):**
- 1,000 users: ~$27 (OpenAI) + $0 (Supabase free tier) + $0-10 (hosting) = **$30-40 total**

---

### Appendix G: Glossary of Legal Terms (Bengali-English)

| Bengali | English | Simple Explanation |
|---------|---------|-------------------|
| ধর্ষণ | Rape | Sexual assault without consent |
| পারিবারিক সহিংসতা | Domestic Violence | Violence by family member |
| যৌতুক | Dowry | Money/gifts demanded from bride's family |
| বাল্যবিবাহ | Child Marriage | Marriage before legal age (18 for girls) |
| হিজানত | Custody (Hizanat) | Right of mother to care for young children |
| ভরণপোষণ | Maintenance | Financial support |
| তালাক | Talaq (Divorce) | Islamic divorce initiated by husband |
| খোলা | Khula (Divorce) | Divorce initiated by wife |
| দেনমোহর | Dower (Mehr) | Mandatory gift from groom to bride |
| FIR | First Information Report | Official police complaint |
| GD | General Diary | Police record (not formal complaint) |
| সুরক্ষা আদেশ | Protection Order | Court order to keep abuser away |
| পারিবারিক আদালত | Family Court | Specialized court for family matters |
| আইনি সহায়তা | Legal Aid | Free legal help |

---

## Conclusion

This Product Requirements Document defines a comprehensive vision for **Ain Bandhu (আইন বন্ধু)**, an AI-powered legal assistant that will democratize access to justice for underprivileged Bangladeshi women.

By acting as an accessible lawyer - asking strategic questions, assessing cases, providing personalized guidance, and empowering women with knowledge - Ain Bandhu bridges the justice gap that leaves millions of women vulnerable and without recourse.

**The opportunity is clear:** Build a tool that provides immediate, 24/7, free legal guidance in simple Bengali, backed by comprehensive legal knowledge and thoughtful procedural guidance.

**The impact is measurable:** Empower thousands of women to understand their rights, navigate the legal system, and access justice - measurably reducing gender-based violence and family law suffering.

**The technology is ready:** GPT-5.1's lawyer-like conversational abilities, combined with Bangladesh's rich legal database, enable us to create a chatbot that truly performs the role of a lawyer.

**Now it's time to build.**

---

**Document Version:** 1.0
**Last Updated:** November 23, 2025
**Next Review:** After MVP launch (Week 8)

**Approval:**
- [ ] Product Manager
- [ ] Technical Lead
- [ ] Legal Advisor
- [ ] BRAC Program Director

---
