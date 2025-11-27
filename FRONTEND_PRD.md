# Ain Bandhu - Frontend PRD

**AI Legal Assistant for Bangladeshi Women**

Version: 3.0 | Updated: November 27, 2025 | Status: Ready for Development

---

## Executive Summary

**What**: A mobile-first chat interface providing free legal guidance to Bangladeshi women on family law - in Bengali, available 24/7.

**Why**: Millions of women face domestic violence, divorce, custody battles but can't access legal help due to cost (₹5,000-50,000), language barriers, social stigma, and geographic distance from legal aid.

**How**: WhatsApp-style chat powered by GPT-5.1 with 58 verified Bangladesh legal sections covering 15 family law topics. Users ask questions in Bengali, get accurate legal guidance instantly, anonymously, and for free.

**Impact**:
- Cost: ₹0 vs ₹5,000+ for lawyer
- Speed: 10-40 seconds vs weeks for legal aid appointment
- Access: 24/7 from home vs 9-5 in distant offices
- Privacy: Anonymous vs public legal aid centers
- Language: Simple Bengali vs complex legal jargon

**Backend**: Live at Railway (`https://final-family-law-production.up.railway.app`)

**Frontend**: To be built - Next.js 14 + Tailwind CSS + TypeScript, deployed on Vercel

**Timeline**: 8 days from start to production

---

## Product Overview

### What is Ain Bandhu?

Ain Bandhu (আইন বন্ধু - "Legal Friend") is a free AI-powered legal assistant designed specifically for Bangladeshi women facing family law issues. It provides accurate, empathetic legal guidance in Bengali - their own language.

**The Problem We're Solving:**

Millions of Bangladeshi women face legal issues but can't access help because:
- **Legal services are expensive** - Most can't afford lawyers (₹5,000-50,000 per case)
- **They don't know their rights** - 70% of women don't know basic family law protections
- **Language barriers** - Legal documents and lawyers use complex English/legal Bengali
- **Social stigma** - Afraid to ask about divorce, domestic violence, rape publicly
- **Geographic barriers** - Legal aid offices only in major cities
- **Time constraints** - Working women can't visit lawyers during office hours

**Our Solution:**

A mobile-first chat interface that feels like texting a trusted friend who happens to be a legal expert. Available 24/7, completely free, and private.

**Not a chatbot. An AI lawyer.**

Ain Bandhu doesn't just answer questions - it:
- Asks clarifying questions like a real lawyer would
- Explains laws in simple, conversational Bengali
- Provides specific next steps ("Go to this court", "File this form")
- Checks safety first in crisis situations
- Connects to support organizations when needed
- Remembers conversation context (no need to repeat your story)

### Who We Serve

**Primary Users:**
- Women aged 18-45 with smartphones
- Limited digital literacy (many first-time internet users)
- Facing domestic violence, divorce, custody battles, dowry harassment
- Low to middle income families
- Both urban and rural areas

**Real User Scenarios:**
- *Rabeya, 28, Dhaka*: "আমার স্বামী আমাকে মারধর করে। পুলিশে গেলে কি হবে?"
- *Nasima, 35, Sylhet*: "স্বামী দ্বিতীয় বিয়ে করেছে। আমার কি করার আছে?"
- *Fatema, 42, Chittagong*: "তালাকের পর সন্তানের হেফাজত কিভাবে পাব?"
- *Shilpi, 24, Khulna*: "কর্মক্ষেত্রে যৌন হয়রানির শিকার। কোথায় অভিযোগ করব?"

### Impact Metrics (Goals)

- **Reach**: 10,000 women in first 6 months
- **Accessibility**: 24/7 availability vs lawyers' 9-5
- **Cost**: ₹0 vs ₹5,000+ for lawyer consultation
- **Response Time**: 10-40 seconds vs days/weeks for legal aid appointment
- **Language**: Simple Bengali vs complex legal jargon
- **Privacy**: Anonymous, no registration vs public legal aid offices

### Key Stats

- **15 Legal Topics**: Domestic violence, rape, divorce, custody, dowry, inheritance, and more
- **58 Legal Sections**: From 8 Bangladesh family law acts (no Indian law, 100% local)
- **Powered by GPT-5.1**: Natural conversations with legal reasoning
- **Response Time**: 10-40 seconds (complex legal queries take time - worth the wait)
- **Accuracy**: Grounded in actual Bangladesh law, not hallucinated advice
- **Language**: Bengali only - the language women actually speak at home

---

## Core User Experience

### The Conversation Flow

```
User: "আমার স্বামী আমাকে মারধর করে। আমি কী করতে পারি?"

Ain Bandhu:
- First checks safety ("আপনি এখন নিরাপদ তো?")
- Explains the law in simple Bengali
- Gives specific, actionable steps
- Provides emergency numbers if needed
- Weaves support organization info naturally
- Remembers context in follow-ups

User: "FIR করতে কত টাকা লাগে?"

Ain Bandhu:
- Short, direct answer
- Doesn't repeat emergency numbers again
- Just answers what was asked
```

### What Makes It Different

**From Traditional Legal Services:**
- ✅ Free (lawyers cost ₹5,000-50,000)
- ✅ 24/7 available (lawyers are 9-5)
- ✅ Anonymous (no fear of judgment)
- ✅ Instant responses (legal aid takes weeks for appointments)
- ✅ Bengali language (not complex legal jargon)
- ✅ Mobile-first (accessible from home, no travel needed)

**From Other Chatbots:**
- ✅ **Context-Aware**: Remembers your story, doesn't make you repeat
- ✅ **Natural Conversations**: Talks like a friend, not a robot with templates
- ✅ **Safety-First**: Asks "আপনি এখন নিরাপদ তো?" before legal theory
- ✅ **100% Bangladesh Law**: No Indian law, no generic Google answers
- ✅ **Real Legal Knowledge**: 58 sections from 8 actual Bangladesh acts
- ✅ **Actionable Advice**: Tells you WHERE to go, WHAT to file, HOW to proceed

**From Generic AI:**
- ✅ **No Hallucinations**: Only answers from verified legal database
- ✅ **Specific to Bangladesh**: Knows Dhaka courts, Bangladesh procedures
- ✅ **Women-Focused**: Understands the unique challenges women face
- ✅ **Crisis-Aware**: Recognizes domestic violence urgency vs general queries

---

## Design Principles

### 1. Mobile-First, Always

**Why**: 85% of Bangladeshi women access internet via smartphone, not desktop.

- Design for 360x640 screens (most common budget Android size)
- Optimize for 2G/3G networks (not everyone has 4G)
- Works on low-end phones with 2-4GB RAM
- Touch targets minimum 44x44px (many users have long nails)
- Large, readable fonts (14-16px) - many users have vision issues

### 2. Bengali-First, English Never

**Why**: Women are more comfortable expressing trauma in their mother tongue.

- All UI text in Bengali (buttons, labels, errors)
- Bengali keyboard support (auto-detect)
- Bengali date/time formatting ("১২:৩০ PM" not "12:30 PM")
- Bengali numerals where culturally appropriate
- Use "আপনি" (formal you) to show respect

### 3. Privacy is Paramount

**Why**: Women fear their husbands/family finding out they're seeking legal help.

- No registration required (anonymous by default)
- No phone number collection
- No email verification
- Sessions stored locally (not cloud-synced)
- Easy "নতুন চ্যাট" button to clear conversation quickly
- No "Share on Facebook" - privacy over virality

### 4. Assume Low Digital Literacy

**Why**: Many users are first-time smartphone users.

- Single primary action per screen (no overwhelming menus)
- Clear visual feedback for every action
- Undo-friendly (can clear chat and start over)
- No complex gestures (no swipe, pinch, long-press)
- Error messages in simple Bengali, not technical jargon
- Auto-scroll so users don't need to know to scroll

### 5. Safety Over Everything

**Why**: Some women access this while their abuser is in the next room.

- Quick exit button (if needed in future)
- No notification sounds (silent by default)
- Fast load times (can check quickly and close)
- Offline mode shows generic error, not "Loading legal advice"
- Consider: Disguised app icon for V2

### 6. Empathy, Not Pity

**Why**: Women want help, not sympathy.

- Conversational tone, not formal legal language
- Practical steps, not just "we understand your pain"
- Empowering language ("You have rights") not victimizing
- Focus on solutions, not just problems
- No excessive emojis or patronizing language

### 7. Build Trust Immediately

**Why**: Users need to know this is real legal help, not a scam.

- Show "আইন বন্ধু" branding clearly
- Cite specific laws ("পারিবারিক সহিংসতা (প্রতিরোধ ও সুরক্ষা) আইন ২০১০")
- Mention BRAC or partner organizations
- Consistent, professional responses
- No ads, no spam, no upsells

---

## User Research Insights

### What We Learned (from BRAC field work)

**About Legal Access:**
- Women don't know where to start ("কোথায় যাব?")
- Fear of police/courts ("পুলিশ আমাকে বিশ্বাস করবে না")
- Can't afford lawyers ("আমার টাকা নেই")
- Don't know their basic rights ("আমি কি তালাক দিতে পারি?")

**About Digital Usage:**
- Prefer WhatsApp-style interfaces (familiar)
- Often share phones with family (privacy is critical)
- Limited data plans (optimize for low bandwidth)
- Use phones mostly at night when alone

**About Language:**
- "পারিবারিক সহিংসতা" is understood, "domestic violence" is not
- Prefer "স্বামী" (husband) over "পতি" (more formal)
- "থানা" (police station) over "পুলিশ স্টেশন"
- Regional dialects vary, but standard Bengali works

**About Trust:**
- Need to see specific laws cited (not just general advice)
- Want to know cost upfront ("কত টাকা লাগবে?")
- Need step-by-step instructions ("প্রথমে কি করব?")
- Appreciate when AI admits uncertainty vs making up answers

### User Journey Map

**Discovery** (How they find us):
- WhatsApp sharing from friends
- NGO field workers
- Facebook groups for women
- Google search for "আইনি সহায়তা"

**First Interaction** (What they do):
- Land on chat interface
- See Bengali welcome message → feels accessible
- See example questions → knows what to ask
- Types first question (often testing: "হেলো")
- Gets fast response → builds trust
- Asks real question

**Ongoing Usage**:
- Ask follow-up questions
- See AI remembers context → appreciates it
- Gets specific legal citations → trusts it
- Gets next steps → feels empowered
- Shares with friends if helpful

**Exit Points** (Where we lose users):
- If response is too slow (>60 seconds) → "আবার চেষ্টা করুন"
- If Bengali is incorrect → lose trust
- If answer is generic → "এটা Google থেকে পেতে পারতাম"
- If too complicated → give up

---

## Legal Knowledge Base

### What Makes Our Database Special

Unlike ChatGPT or Google, Ain Bandhu's legal knowledge comes from:

**1. Actual Bangladesh Laws (58 Sections from 8 Acts)**:
- পারিবারিক সহিংসতা (প্রতিরোধ ও সুরক্ষা) আইন, ২০১০
- নারী ও শিশু নির্যাতন দমন আইন, ২০০০ (সংশোধিত ২০০৩)
- মুসলিম পারিবারিক আইন অধ্যাদেশ, ১৯৬১
- দেনমোহর আইন, ১৮৭৬
- মুসলিম বিবাহ বিচ্ছেদ আইন, ১৯৩৯
- ডিজিটাল নিরাপত্তা আইন, ২০১৮
- হিন্দু বিবাহ নিবন্ধন আইন, ২০১২
- পিতামাতা ভরণপোষণ আইন, ২০১৩

**2. Procedural Knowledge (How to Actually Use the Law)**:
- Where to file FIR (থানা jurisdiction rules)
- Court procedures (Family Courts Act 1985)
- Timelines (custody hearing: 6-12 months)
- Costs (FIR: free, court fees: ₹500-2000)
- Required documents (marriage certificate, ID, witnesses)
- Support organizations (Ain o Salish Kendra, BLAST, etc.)

**3. Real-World Context**:
- What happens after filing FIR (investigation → chargesheet → trial)
- Practical challenges women face (police may refuse FIR)
- Alternative options if one path doesn't work
- Safety planning for domestic violence cases
- How to get free legal aid

### Coverage: 15 Legal Intents

All family law issues Bangladeshi women commonly face:

1. **গৃহ সহিংসতা** (Domestic Violence)
   - Physical, emotional, economic, sexual abuse
   - Protection orders, shelter homes, police action

2. **ধর্ষণ ও যৌন সহিংসতা** (Rape & Sexual Violence)
   - Marital rape, gang rape, statutory rape
   - Medical evidence, legal process, victim rights

3. **যৌন হয়রানি** (Sexual Harassment)
   - Workplace, public places, stalking
   - Complaint mechanisms, employer obligations

4. **যৌতুক** (Dowry)
   - Dowry demand, dowry violence, dowry death
   - Criminal penalties, how to report

5. **বাল্যবিবাহ** (Child Marriage)
   - Legal age, how to prevent, how to annul
   - Protection for underage girls

6. **তালাক** (Divorce/Talaq)
   - Muslim divorce (Talaq, Khula), Hindu separation
   - Maintenance during iddat, post-divorce rights

7. **সন্তানের হেফাজত** (Child Custody)
   - Mother's right to hizanat, father's guardianship
   - Age limits, court procedures, visitation

8. **ভরণপোষণ** (Maintenance)
   - Wife's right to maintenance, during marriage and after
   - How to claim, enforcement

9. **পিতামাতার ভরণপোষণ** (Parent Maintenance)
   - Children's duty to support elderly parents
   - Court process for claiming

10. **বহুবিবাহ/দ্বিতীয় বিয়ে** (Polygamy/Second Marriage)
    - When second marriage is legal/illegal
    - Wife's recourse if husband remarries

11. **উত্তরাধিকার** (Inheritance)
    - Muslim, Hindu inheritance laws
    - Women's share, how to claim

12. **বিবাহ নিবন্ধন** (Marriage Registration)
    - Why register, how to register, delayed registration
    - Nikah Nama/marriage certificate importance

13. **দেনমোহর** (Dower/Mehr)
    - What is dower, when payable, how to claim
    - Prompt vs deferred dower

14. **সাইবার অপরাধ** (Cybercrime)
    - Morphed photos, revenge porn, online harassment
    - Digital Security Act provisions

15. **হিন্দু বিবাহ বিচ্ছেদ** (Hindu Separation)
    - Grounds for separation, maintenance, property rights
    - Differences from Muslim law

### What We DON'T Cover (Out of Scope)

- Criminal law beyond women's issues (theft, murder, etc.)
- Property law beyond inheritance
- Business/commercial law
- Immigration/passport issues
- General civil disputes
- Tax law
- **Indian law** (common mistake - we're Bangladesh-only)

### How We Ensure Accuracy

1. **Grounded Responses**: AI can ONLY cite from our legal database
2. **No Hallucinations**: If answer not in database → "আমি নিশ্চিত নই, আইনজীবীর পরামর্শ নিন"
3. **Source Citations**: Every answer cites specific act and section
4. **Human Review**: Legal experts reviewed all 58 sections
5. **Regular Updates**: When laws change, we update database

---

## Technical Specifications

### API Endpoint

**Base URL**: `https://final-family-law-production.up.railway.app`

#### POST /chat

**Request**:
```json
{
  "session_id": "user-uuid-or-string",
  "message": "আমার স্বামী আমাকে মারধর করে"
}
```

**Response**:
```json
{
  "session_id": "user-uuid-or-string",
  "response": "আপনি এখন নিরাপদ তো? যদি বিপদ থাকে...",
  "intent": "domestic_violence_general",
  "tools_used": [...],
  "tokens_used": 21866,
  "response_time_ms": 9910,
  "success": true
}
```

**Error Response**:
```json
{
  "response": "দুঃখিত, একটি সমস্যা হয়েছে। অনুগ্রহ করে আবার চেষ্টা করুন।",
  "success": false
}
```

### Session Management

- Store `session_id` in localStorage
- Generate with `crypto.randomUUID()` on first visit
- Send with every request
- Clear when user clicks "নতুন চ্যাট"

### Timeout Handling

**Important**: The timeout is a safety mechanism, NOT a hard cap on response time.

- Set 90-second timeout for API calls (allows for complex queries)
- Most responses complete in 10-40 seconds
- If timeout occurs, show friendly error and allow retry
- Timeout is configurable - adjust based on actual usage patterns

```typescript
// Generous timeout for GPT-5.1 reasoning
const TIMEOUT_MS = 90000 // 90 seconds

const controller = new AbortController()
const timeout = setTimeout(() => controller.abort(), TIMEOUT_MS)
```

---

## API Integration Deep Dive

### Request Flow

```
User types → Input validation → Add to UI → Call API → Show typing indicator
                                                ↓
                              Response arrives → Parse → Add to UI → Auto-scroll
```

### Complete API Client Implementation

**`lib/api.ts`** (Full implementation):

```typescript
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'https://final-family-law-production.up.railway.app'
const TIMEOUT_MS = 90000 // 90 seconds

export interface ChatRequest {
  session_id: string
  message: string
}

export interface ChatResponse {
  session_id: string
  response: string
  intent: string
  tools_used: string[]
  tokens_used: number
  response_time_ms: number
  success: boolean
}

export interface ChatError {
  response: string
  success: false
}

export async function sendChatMessage(
  sessionId: string,
  message: string
): Promise<ChatResponse | ChatError> {
  const controller = new AbortController()
  const timeout = setTimeout(() => controller.abort(), TIMEOUT_MS)

  try {
    const response = await fetch(`${API_URL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        session_id: sessionId,
        message: message.trim(),
      }),
      signal: controller.signal,
    })

    clearTimeout(timeout)

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`)
    }

    const data = await response.json()
    return data
  } catch (error) {
    clearTimeout(timeout)

    // Timeout
    if (error instanceof Error && error.name === 'AbortError') {
      return {
        response: 'সংযোগ সময় শেষ। আবার চেষ্টা করুন।',
        success: false,
      }
    }

    // Network error
    if (!navigator.onLine) {
      return {
        response: 'ইন্টারনেট সংযোগ নেই। অনুগ্রহ করে আপনার সংযোগ চেক করুন।',
        success: false,
      }
    }

    // Generic error
    return {
      response: 'দুঃখিত, একটি সমস্যা হয়েছে। অনুগ্রহ করে আবার চেষ্টা করুন।',
      success: false,
    }
  }
}

export async function healthCheck(): Promise<boolean> {
  try {
    const response = await fetch(`${API_URL}/health`, {
      method: 'GET',
    })
    return response.ok
  } catch {
    return false
  }
}
```

### Response Handling Strategy

**Success Response**:
```typescript
if (data.success) {
  // Add assistant message to chat
  setMessages(prev => [...prev, {
    id: crypto.randomUUID(),
    role: 'assistant',
    content: data.response,
    timestamp: new Date(),
  }])
}
```

**Error Response**:
```typescript
if (!data.success) {
  // Show error bubble with retry option
  setError({
    message: data.response,
    retryable: true,
  })
}
```

### Session Management

**`lib/session.ts`**:

```typescript
const SESSION_KEY = 'ain_bandhu_session'

export function getSessionId(): string {
  if (typeof window === 'undefined') return ''

  let sessionId = localStorage.getItem(SESSION_KEY)

  if (!sessionId) {
    sessionId = crypto.randomUUID()
    localStorage.setItem(SESSION_KEY, sessionId)
  }

  return sessionId
}

export function clearSession(): void {
  if (typeof window !== 'undefined') {
    localStorage.removeItem(SESSION_KEY)
  }
}

export function newSession(): string {
  clearSession()
  return getSessionId()
}
```

### Real-time Feedback

**Loading States Timeline**:
```
0ms: User clicks send
  → Disable input
  → Add user message to UI
  → Show send button spinner

100ms: API call initiated
  → Hide spinner
  → Show typing indicator "আইন বন্ধু লিখছে..."

10-40s: Waiting for response
  → Typing indicator animating
  → User can see their message
  → Input still disabled

Response: API returns
  → Hide typing indicator
  → Add assistant message
  → Re-enable input
  → Auto-scroll to bottom
  → Focus input
```

---

## UI/UX Requirements

### Mobile-First Design

**Target Devices**:
- Android 8+ (Chrome 90+)
- Small screens (360x640 minimum)
- Low-end phones (2-4GB RAM)
- 2G/3G connectivity

### Screen Layout

```
┌─────────────────────────┐
│  আইন বন্ধু        [≡]   │ ← Header (56px, fixed)
├─────────────────────────┤
│                         │
│  [Assistant Message]    │
│     12:30 PM           │
│                         │
│          [User Message] │
│         12:31 PM       │
│                         │
│  [Assistant Message]    │
│     12:31 PM           │
│                         │
│  আইন বন্ধু লিখছে... ●●● │ ← Typing indicator
│                         │
├─────────────────────────┤
│ [Type here...    ] [→]  │ ← Input (auto-resize)
└─────────────────────────┘
```

### Component Specs

#### 1. Header
- Height: 56px
- Background: #065f46 (dark green)
- Title: "আইন বন্ধু" (white, 18px)
- Menu icon: hamburger (optional)

#### 2. Message Bubbles

**User Message**:
- Align: Right
- Background: #dbeafe (light blue)
- Text: #1e40af (dark blue)
- Max width: 80%
- Border radius: 16px
- Padding: 12px 16px
- Font: 14-16px Noto Sans Bengali

**Assistant Message**:
- Align: Left  
- Background: #f3f4f6 (light gray)
- Text: #1f2937 (dark gray)
- Max width: 85%
- Border radius: 16px
- Padding: 12px 16px
- Font: 14-16px Noto Sans Bengali
- Markdown: Bold, lists, line breaks

#### 3. Input Field
- Auto-resize textarea (1-4 lines)
- Placeholder: "আপনার প্রশ্ন লিখুন..."
- Border radius: 24px
- Padding: 12px 16px
- Send button: → icon (#065f46)
- Disable while sending

#### 4. Typing Indicator
- Show during API call
- Text: "আইন বন্ধু লিখছে..."
- 3 animated dots: ● ● ●
- Same style as assistant message

### Empty State

```
┌─────────────────────────┐
│                         │
│   আসসালামু আলাইকুম      │
│   আমি আইন বন্ধু          │
│                         │
│   আপনার আইনি সমস্যা      │
│   সম্পর্কে জিজ্ঞাসা করুন │
│                         │
│   যেমন:                 │
│   • গৃহ সহিংসতা          │
│   • তালাক                │
│   • সন্তানের হেফাজত      │
│   • ভরণপোষণ              │
│                         │
└─────────────────────────┘
```

### Loading States

**Initial Load**: Spinner with "চ্যাট লোড হচ্ছে..."

**Sending Message**:
- Message appears immediately
- Input disabled
- Send button shows spinner

**Waiting for Response**:
- Typing indicator visible
- Auto-scroll to bottom

**Error State**:
```
[Error bubble]
দুঃখিত, একটি সমস্যা হয়েছে।
[আবার চেষ্টা করুন] button
```

---

## Recommended Tech Stack

### Framework: Next.js 14+
**Why**: Production-ready with minimal configuration
- App Router for modern React patterns
- Server-side rendering for fast initial load
- Built-in image optimization
- Easy Vercel deployment with zero config
- TypeScript support out of the box

### Styling: Tailwind CSS v3+
**Why**: Fast development, small bundle, mobile-first
- Utility-first CSS (no custom CSS files needed)
- Minimal bundle size with PurgeCSS
- Responsive by default (mobile-first breakpoints)
- Dark mode support (future enhancement)
- JIT compiler for instant builds

### State Management: React Hooks
**Why**: Simple, no overhead for this use case
- `useState` for local component state
- `useContext` for session/theme if needed
- `useReducer` for complex message state (optional)
- No Redux/Zustand - conversation is linear, not complex

### HTTP Client: Native fetch API
**Why**: Modern, built-in, zero dependencies
- AbortController for timeout handling
- Native Promise support
- Streaming support (future: SSE for typing indicator)
- No axios overhead

### Markdown: react-markdown
**Why**: Render bold, lists, line breaks in responses
```bash
npm install react-markdown
```

### Font Loading: next/font
**Why**: Optimized Bengali font loading
```typescript
import { Noto_Sans_Bengali } from 'next/font/google'

const notoSansBengali = Noto_Sans_Bengali({
  subsets: ['bengali'],
  weight: ['400', '500', '600'],
  display: 'swap',
})
```

---

## File Structure

```
frontend/
├── app/
│   ├── page.tsx              # Landing → Redirect to /chat
│   ├── chat/
│   │   └── page.tsx          # Main chat interface
│   ├── layout.tsx            # Root layout with font config
│   └── globals.css           # Global styles + Tailwind imports
├── components/
│   ├── ChatMessage.tsx       # Message bubble (user/assistant variants)
│   ├── ChatInput.tsx         # Auto-resize textarea + send button
│   ├── TypingIndicator.tsx   # Animated dots during loading
│   ├── Header.tsx            # App header with menu (optional)
│   ├── EmptyState.tsx        # Welcome screen with examples
│   └── ErrorBubble.tsx       # Error display with retry button
├── lib/
│   ├── api.ts                # API client with timeout & error handling
│   ├── session.ts            # localStorage session management
│   └── utils.ts              # Date formatting, scroll helpers
├── hooks/
│   ├── useChat.ts            # Chat state management hook
│   ├── useSession.ts         # Session persistence hook
│   └── useAutoScroll.ts      # Auto-scroll to bottom hook
├── types/
│   ├── chat.ts               # Message, ChatResponse, ChatError types
│   └── api.ts                # API request/response types
├── public/
│   ├── logo.png              # Ain Bandhu logo
│   └── favicon.ico           # Browser favicon
└── config/
    └── constants.ts          # API URL, timeouts, limits
```

### Key Files Details

**`app/chat/page.tsx`**
- Main chat interface
- Message list with auto-scroll
- Empty state when no messages
- Error handling UI

**`lib/api.ts`**
```typescript
export async function sendMessage(sessionId: string, message: string) {
  const controller = new AbortController()
  const timeout = setTimeout(() => controller.abort(), 90000)

  try {
    const res = await fetch(`${API_URL}/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ session_id: sessionId, message }),
      signal: controller.signal,
    })

    return await res.json()
  } catch (error) {
    // Handle timeout, network errors, etc.
  } finally {
    clearTimeout(timeout)
  }
}
```

**`hooks/useChat.ts`**
```typescript
export function useChat(sessionId: string) {
  const [messages, setMessages] = useState<Message[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const sendMessage = async (content: string) => {
    // Add user message
    // Call API
    // Add assistant response
    // Handle errors
  }

  return { messages, loading, error, sendMessage }
}
```

---

## Mobile Optimizations

### 1. Viewport
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

### 2. Performance
- Lazy load non-critical components
- Limit history to last 50 messages
- Debounce scroll events
- Optimize images

### 3. Touch Targets
- Minimum 44x44px
- Adequate spacing
- Large input area

### 4. Keyboard Handling
```typescript
// Auto-scroll when keyboard opens
useEffect(() => {
  window.scrollTo(0, document.body.scrollHeight)
}, [messages])
```

### 5. Offline Detection
```typescript
if (!navigator.onLine) {
  showError('ইন্টারনেট সংযোগ নেই')
}
```

---

## Error Handling

### Network Errors
```typescript
catch (error) {
  if (error.message.includes('timeout')) {
    return 'সংযোগ ধীর। আবার চেষ্টা করুন।'
  }
  if (!navigator.onLine) {
    return 'ইন্টারনেট সংযোগ নেই।'
  }
  return 'দুঃখিত, একটি সমস্যা হয়েছে।'
}
```

### Timeout
```typescript
const controller = new AbortController()
const timeout = setTimeout(() => controller.abort(), 90000) // 90 seconds

try {
  await fetch(url, { signal: controller.signal })
} catch (error) {
  if (error.name === 'AbortError') {
    showError('সংযোগ সময় শেষ। আবার চেষ্টা করুন।')
  }
} finally {
  clearTimeout(timeout)
}
```

---

## Accessibility

### ARIA Labels
```tsx
<button aria-label="বার্তা পাঠান">→</button>
<div role="log" aria-live="polite">
  {messages.map(...)}
</div>
```

### Keyboard Navigation
- Tab through all elements
- Enter to send
- Escape to clear input

### Semantic HTML
```tsx
<main>
  <header>আইন বন্ধু</header>
  <section role="log">{messages}</section>
  <form>{input}</form>
</main>
```

---

## Design System

### Colors
```css
/* Primary */
--green-900: #064e3b
--green-700: #065f46  /* Main */
--green-100: #d1fae5

/* Messages */
--blue-100: #dbeafe   /* User bg */
--blue-700: #1e40af   /* User text */
--gray-100: #f3f4f6   /* Assistant bg */
--gray-900: #1f2937   /* Assistant text */

/* Feedback */
--red-100: #fee2e2    /* Error bg */
--red-700: #b91c1c    /* Error text */
```

### Typography
```css
font-family: 'Noto Sans Bengali', sans-serif;

--text-sm: 14px     /* Messages */
--text-base: 16px   /* Input */
--text-lg: 18px     /* Header */

--font-normal: 400
--font-medium: 500
--font-semibold: 600
```

---

## Component Implementation Guide

### ChatMessage Component

```typescript
interface ChatMessageProps {
  message: Message
  isUser: boolean
}

export function ChatMessage({ message, isUser }: ChatMessageProps) {
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4`}>
      <div
        className={`max-w-[85%] rounded-2xl px-4 py-3 ${
          isUser
            ? 'bg-blue-100 text-blue-900'
            : 'bg-gray-100 text-gray-900'
        }`}
      >
        <ReactMarkdown className="text-sm leading-relaxed">
          {message.content}
        </ReactMarkdown>
        <div className="text-xs opacity-60 mt-1">
          {formatTime(message.timestamp)}
        </div>
      </div>
    </div>
  )
}
```

### ChatInput Component with Auto-resize

```typescript
export function ChatInput({ onSend, disabled }: ChatInputProps) {
  const [input, setInput] = useState('')
  const textareaRef = useRef<HTMLTextAreaElement>(null)

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault()
    if (!input.trim() || disabled) return

    onSend(input.trim())
    setInput('')
  }

  // Auto-resize textarea
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto'
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`
    }
  }, [input])

  return (
    <form onSubmit={handleSubmit} className="flex gap-2 p-4 bg-white border-t">
      <textarea
        ref={textareaRef}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="আপনার প্রশ্ন লিখুন..."
        disabled={disabled}
        rows={1}
        className="flex-1 resize-none rounded-3xl border px-4 py-3 focus:outline-none focus:ring-2"
        style={{ maxHeight: '120px' }}
      />
      <button
        type="submit"
        disabled={disabled || !input.trim()}
        className="rounded-full bg-green-700 p-3 text-white disabled:opacity-50"
      >
        {disabled ? <Spinner /> : <SendIcon />}
      </button>
    </form>
  )
}
```

### TypingIndicator Component

```typescript
export function TypingIndicator() {
  return (
    <div className="flex justify-start mb-4">
      <div className="bg-gray-100 rounded-2xl px-4 py-3">
        <div className="flex items-center gap-2">
          <span className="text-sm text-gray-700">আইন বন্ধু লিখছে</span>
          <div className="flex gap-1">
            <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce [animation-delay:-0.3s]" />
            <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce [animation-delay:-0.15s]" />
            <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" />
          </div>
        </div>
      </div>
    </div>
  )
}
```

## Development Phases

### Phase 1: Core Functionality (Days 1-3)
**Goal**: Working chat interface with API integration

- [x] Next.js 14 project setup with TypeScript
- [x] Tailwind CSS configuration
- [x] Bengali font loading (next/font)
- [ ] Basic layout: Header + Messages + Input
- [ ] ChatMessage component (user/assistant variants)
- [ ] ChatInput component with auto-resize
- [ ] API client (`lib/api.ts`) with error handling
- [ ] Session management (`lib/session.ts`)
- [ ] Basic message sending and receiving
- [ ] Mobile responsive layout (360px minimum)

**Success Criteria**: Can send a message and get a response

### Phase 2: UX Polish (Days 4-5)
**Goal**: Professional, smooth user experience

- [ ] Empty state with examples
- [ ] TypingIndicator with animated dots
- [ ] Auto-scroll to bottom on new messages
- [ ] Auto-scroll when keyboard opens (mobile)
- [ ] Session persistence in localStorage
- [ ] Error handling UI with retry button
- [ ] Loading states (disabled input, spinner)
- [ ] Markdown rendering (react-markdown)
- [ ] Time formatting for messages
- [ ] Input validation (trim, max length)

**Success Criteria**: Feels smooth and professional

### Phase 3: Optimization (Days 6-7)
**Goal**: Fast, accessible, production-ready

- [ ] Performance audit (Lighthouse)
- [ ] Lazy load non-critical components
- [ ] Optimize images and fonts
- [ ] Message history limit (last 50)
- [ ] Keyboard navigation (Tab, Enter, Escape)
- [ ] ARIA labels for screen readers
- [ ] Offline detection
- [ ] Network error handling
- [ ] Touch target sizes (min 44x44px)
- [ ] Test on low-end Android device

**Success Criteria**: Lighthouse score > 90, works on 2G

### Phase 4: Deployment (Day 8)
**Goal**: Live in production

- [ ] Environment variables setup
- [ ] Production build (`npm run build`)
- [ ] Vercel deployment
- [ ] Custom domain + SSL (if applicable)
- [ ] Analytics setup (optional: Vercel Analytics)
- [ ] Error monitoring (optional: Sentry)
- [ ] User acceptance testing
- [ ] Bug fixes from UAT
- [ ] Documentation

**Success Criteria**: Live URL accessible from mobile devices

---

## Success Metrics

### Technical
- First Contentful Paint < 1.5s
- Time to Interactive < 3s
- Lighthouse score > 90
- Works on Android 8+

### UX
- Message send success > 98%
- Error recovery > 95%
- Users complete conversation successfully

---

## Open Questions

1. **Authentication**: Anonymous or require login?
2. **History**: Save conversations or ephemeral?
3. **Export**: Allow PDF/text export?
4. **Typing Indicator**: Show during 10-30s waits?
5. **Multi-device**: Sync across devices?

---

## Deployment

### Vercel
```bash
vercel

# Set environment variable
vercel env add NEXT_PUBLIC_API_URL
```

### Environment Variables
```env
NEXT_PUBLIC_API_URL=https://final-family-law-production.up.railway.app
```

---

## Testing Checklist

### Manual Testing

**Core Functionality**:
- [ ] Send message and receive response
- [ ] Session persists across page refresh
- [ ] "নতুন চ্যাট" clears conversation
- [ ] Empty state shows on first visit
- [ ] Typing indicator shows during API call
- [ ] Messages display correctly (user right, assistant left)
- [ ] Markdown renders (bold, lists, line breaks)
- [ ] Timestamps show correctly

**Mobile Testing** (Chrome DevTools + Real Device):
- [ ] Works on 360x640 viewport
- [ ] Input auto-resizes (1-4 lines)
- [ ] Keyboard doesn't hide messages
- [ ] Auto-scroll on new message
- [ ] Touch targets are 44x44px minimum
- [ ] Text is readable (14-16px)
- [ ] Works offline (shows error)
- [ ] Works on slow 2G (doesn't timeout)

**Error Scenarios**:
- [ ] Network offline → Shows "ইন্টারনেট সংযোগ নেই"
- [ ] API timeout → Shows "সংযোগ সময় শেষ"
- [ ] API error → Shows retry button
- [ ] Empty message → Send button disabled
- [ ] Very long message → Textarea scrolls, doesn't overflow

**Accessibility**:
- [ ] Tab navigation works
- [ ] Enter sends message
- [ ] Screen reader announces messages
- [ ] Focus visible on all elements
- [ ] High contrast mode works

### Performance Testing

**Lighthouse Audit** (Mobile):
- [ ] Performance: > 90
- [ ] Accessibility: > 95
- [ ] Best Practices: > 90
- [ ] SEO: > 85

**Load Testing**:
```bash
# Test API with concurrent requests
for i in {1..10}; do
  curl -X POST https://final-family-law-production.up.railway.app/chat \
    -H "Content-Type: application/json" \
    -d '{"session_id": "test-'$i'", "message": "হেলো"}' &
done
```

### Browser Testing

**Primary**: Chrome 90+ on Android 8+
**Secondary**: Safari iOS, Firefox Android

## Future Enhancements (V2)

### Voice Features
- Bengali speech-to-text (STT)
- Text-to-speech for responses
- Voice activation ("Hey Ain Bandhu")

### Export & Sharing
- Share conversation as PDF
- Export as text file
- Share via WhatsApp/Messenger

### Progressive Web App (PWA)
- Install as app (Add to Home Screen)
- Offline message queue
- Push notifications for updates
- Background sync

### UX Improvements
- Dark mode toggle
- Quick reply suggestions
- Copy message to clipboard
- Message search/filter
- Multi-language support (Chittagonian, Sylheti)

### Advanced Features
- Voice call with AI lawyer
- Document upload (scan legal papers)
- Legal form generator
- Court date reminders
- Connect to real lawyers

---

**Ready to build!**

**Backend**: Live at `https://final-family-law-production.up.railway.app`
**Stack**: Next.js 14 + Tailwind CSS + TypeScript
**Deploy**: Vercel (one-click deployment)
**Timeline**: 8 days from start to production
