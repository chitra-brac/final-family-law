# Ain Bandhu - Frontend PRD

**AI Legal Assistant for Bangladeshi Women**

Version: 3.0 | Updated: November 27, 2025 | Status: Ready for Development

---

## Product Overview

### What is Ain Bandhu?

A mobile-first chat interface for an AI legal assistant that provides free legal guidance to Bangladeshi women on family law issues - in Bengali.

**Not a chatbot. An AI lawyer.**

Ain Bandhu acts like a knowledgeable friend who understands Bangladesh law, asks the right questions, and gives practical advice on domestic violence, divorce, custody, maintenance, and other family law matters.

### Key Stats

- **15 Legal Topics**: All major family law issues covered
- **Powered by GPT-5.1**: Natural, conversational responses
- **Response Time**: 10-30 seconds
- **Target Users**: Women with smartphones, limited digital literacy
- **Primary Language**: Bengali

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

1. **Context-Aware** - Remembers conversation, doesn't repeat unnecessarily
2. **Natural Language** - No rigid templates or robotic responses
3. **Focused Answers** - In follow-ups, answers only what's asked
4. **Safety First** - For urgent cases, prioritizes immediate safety
5. **100% Bangladesh** - No Indian law, no generic advice

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

- Set 60 second timeout for API calls
- Show timeout error if exceeded
- Allow retry

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
- App Router
- Server-side rendering
- Built-in optimizations
- Easy Vercel deployment

### Styling: Tailwind CSS
- Utility-first
- Minimal bundle
- Responsive by default

### State: React useState/useContext
- No Redux/Zustand needed
- Keep it simple

### HTTP: Native fetch
- No axios needed

---

## File Structure

```
frontend/
├── app/
│   ├── page.tsx              # Landing → Redirect to /chat
│   ├── chat/
│   │   └── page.tsx          # Main chat interface
│   ├── layout.tsx            # Root layout
│   └── globals.css           # Global styles
├── components/
│   ├── ChatMessage.tsx       # Message bubble
│   ├── ChatInput.tsx         # Input field
│   ├── TypingIndicator.tsx   # Loading indicator
│   ├── Header.tsx            # App header
│   └── EmptyState.tsx        # First screen
├── lib/
│   ├── api.ts                # API client
│   └── session.ts            # Session management
├── types/
│   └── chat.ts               # TypeScript types
└── public/
    └── logo.png              # Ain Bandhu logo
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
const timeout = setTimeout(() => controller.abort(), 60000)

try {
  await fetch(url, { signal: controller.signal })
} catch (error) {
  if (error.name === 'AbortError') {
    showError('সময় শেষ। আবার চেষ্টা করুন।')
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

## Development Phases

### Phase 1: MVP (Week 1)
- [ ] Next.js setup
- [ ] Chat UI components
- [ ] API integration  
- [ ] Message display
- [ ] Send functionality
- [ ] Loading states
- [ ] Error handling
- [ ] Mobile responsive

### Phase 2: Polish (Week 2)
- [ ] Empty state
- [ ] Typing indicator
- [ ] Auto-scroll
- [ ] Session persistence
- [ ] Bengali fonts
- [ ] Markdown rendering
- [ ] Accessibility
- [ ] Performance tuning

### Phase 3: Deploy (Week 3)
- [ ] Production build
- [ ] Vercel deployment
- [ ] Domain + SSL
- [ ] Analytics (optional)
- [ ] User testing
- [ ] Bug fixes

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

## Future Enhancements (V2)

- Voice input (Bengali STT)
- Share as PDF
- Dark mode
- PWA (install as app)
- Offline message queue
- Quick reply suggestions

---

**Ready to build!**

Contact: Backend API is live and stable at Railway
