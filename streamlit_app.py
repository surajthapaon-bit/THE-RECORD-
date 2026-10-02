import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="STATEMENT OF ACCOUNT — FINAL",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stApp {background-color: #f7f5f0;}
    .block-container {max-width: 820px; padding-top: 2.5rem; padding-bottom: 5rem;}

    h1.title {
        text-align: center;
        font-family: Georgia, 'Times New Roman', serif;
        letter-spacing: 6px;
        font-size: 2.1rem;
        font-weight: 700;
        color: #111;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        text-align: center;
        font-family: Georgia, serif;
        letter-spacing: 4px;
        font-size: 0.85rem;
        color: #444;
        margin-bottom: 2.2rem;
    }
    .header-block {
        font-family: Georgia, serif;
        font-size: 0.95rem;
        line-height: 1.9;
        border-top: 3px solid #111;
        border-bottom: 3px solid #111;
        padding: 1.3rem 0;
        margin: 1rem 0 2.5rem 0;
        color: #111;
    }
    .header-block b {letter-spacing: 1px;}

    .section {
        margin-top: 2.6rem;
        margin-bottom: 0.6rem;
        padding-bottom: 0.4rem;
        border-bottom: 1px solid #111;
        font-family: Georgia, serif;
        font-size: 0.78rem;
        letter-spacing: 3px;
        color: #111;
        font-weight: 700;
        text-transform: uppercase;
    }
    .item {
        font-family: Georgia, serif;
        font-size: 1rem;
        line-height: 1.8;
        color: #1a1a1a;
        margin-bottom: 1.15rem;
    }
    .num {
        font-weight: 700;
        margin-right: 0.6rem;
        color: #000;
    }
    .sub {
        display: block;
        margin-top: 0.45rem;
        margin-left: 1.7rem;
        font-size: 0.9rem;
        color: #555;
        line-height: 1.7;
        font-style: italic;
    }
    .exhibit {
        font-family: 'Courier New', monospace;
        font-size: 0.85rem;
        line-height: 1.7;
        color: #222;
        background-color: #efece5;
        padding: 1rem 1.2rem;
        margin: 1rem 0;
        border-left: 3px solid #111;
    }
    .def {
        font-family: Georgia, serif;
        font-size: 0.95rem;
        line-height: 1.75;
        color: #222;
        margin-bottom: 1rem;
    }
    .def b {letter-spacing: 0.5px;}
    .callout {
        font-family: Georgia, serif;
        font-size: 1.02rem;
        line-height: 1.9;
        color: #111;
        border-left: 4px solid #111;
        padding: 0.9rem 1.2rem;
        margin: 1.6rem 0;
        background-color: #efece5;
        font-style: italic;
    }
    .stamp {
        text-align: center;
        font-family: Georgia, serif;
        font-weight: 700;
        letter-spacing: 8px;
        font-size: 1.15rem;
        color: #8a1f1f;
        border: 3px double #8a1f1f;
        padding: 1rem 1.4rem;
        margin: 3rem auto 1.4rem auto;
        max-width: 420px;
        transform: rotate(-1.4deg);
    }
    .signature-block {
        font-family: Georgia, serif;
        font-size: 0.9rem;
        line-height: 1.9;
        color: #333;
        border-top: 1px solid #999;
        border-bottom: 1px solid #999;
        padding: 1.2rem 0;
        margin: 2rem 0;
    }
    .footer {
        margin-top: 3rem;
        padding-top: 1.2rem;
        border-top: 1px solid #999;
        font-family: Georgia, serif;
        font-size: 0.78rem;
        color: #666;
        text-align: center;
        letter-spacing: 1px;
        line-height: 1.9;
    }
    .status {
        text-align: center;
        font-family: Georgia, serif;
        font-weight: 700;
        letter-spacing: 5px;
        font-size: 0.85rem;
        color: #8a1f1f;
        margin-bottom: 0.6rem;
    }
</style>
""", unsafe_allow_html=True)

issued = datetime.now().strftime("%B %d, %Y — %H:%M")

# ============================================================
# HEADER
# ============================================================
st.markdown('<h1 class="title">STATEMENT OF ACCOUNT</h1>', unsafe_allow_html=True)
st.markdown('<div class="status">FINAL · DUE UPON RECEIPT · NO REVISIONS</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">ISSUED TO STEPHANIE LALAP · ISSUED BY SURAJ THAPA</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="header-block">
<b>Issued to:</b> Stephanie Lalap<br>
<b>Issued by:</b> Suraj Thapa<br>
<b>Date:</b> {issued}<br>
<b>Document ID:</b> SOA-2026-FINAL-001<br>
<b>Status:</b> FINAL — no revisions, no amendments, no follow-ups<br>
<b>Balance:</b> Due upon receipt<br>
<b>Reference:</b> This document is the record.
</div>
""", unsafe_allow_html=True)

# ============================================================
# PREAMBLE
# ============================================================
st.markdown('<div class="section">Preamble</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
This is not a letter. This is not a text. This is not an argument, an apology, a plea, or a breakup. 
This is a <b>statement</b> — the way a bank issues a statement, the way a utility issues a bill. 
It is the record of what has been used, what is owed, and what the terms are. 
It does not change based on whether the recipient agrees with it, remembers it, or likes it.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="callout">
A bill does not argue. A bill does not hope. A bill states the amount, sets the terms, and waits. 
That is what this is.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<b>Why this exists:</b> I am not writing this to convince you of anything. I am writing it because I am no longer 
willing to spend my own nervous system repeating myself. Everything I would have said across months of 
conversations is here, once, in writing, permanently. If you want to understand — the door is this document. 
If you don't — I will see that too. Either way, I am not explaining again.
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION I — WHAT IS REAL
# ============================================================
st.markdown('<div class="section">Section I — What Is Real, and Is Not Being Erased</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">I.1</span> I love you. That has not changed, and I am not going to pretend it has just to make this easier.
<span class="sub">This is not leverage. It is context. It is stated so that nothing that follows can be read as indifference.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">I.2</span> I loved the person in front of me — not an idea, not your potential, not a version I was hoping you would become.
<span class="sub">The years were not a placeholder. They were the actual thing. I am not rewriting them.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">I.3</span> What was real was real. What was good was good. What we built, we built.
<span class="sub">Acknowledging what happened later does not require erasing what came before. Both can stand.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">I.4</span> This document is not a verdict on you as a person. It is a verdict on a pattern.
<span class="sub">You are not the pattern. But the pattern is real, and it cannot keep standing in the doorway of my life.</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION II — THE FOUNDATION IS NOT MINE TO TEACH
# ============================================================
st.markdown('<div class="section">Section II — The Foundation Is Not Mine to Teach</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">II.1</span> I am not your teacher, and this is not a lesson plan.
<span class="sub">I am not running a course on what partnership is. I am not signing up to install the basics.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">II.2</span> Knowing what a team is — showing up, moving toward someone instead of away, staying in a hard conversation instead of disappearing from it — is the foundation.
<span class="sub">The foundation is not mine to build for you. It is yours to already have, or to build. On your own. No matter how long it takes.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">II.3</span> If you don't know it, that is your homework. Not mine.
<span class="sub">And it is not homework you do for me. It is homework you do because you actually want a real life with someone — or you don't. That part is on you.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">II.4</span> I can point at the exhaust. I can explain the noise. I cannot make you look underneath your own car.
<span class="sub">That is not cruelty. That is the boundary. Some things cannot be taught. They can only be chosen.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">II.5</span> I am not running out of patience. I am running out of interest in carrying the lesson.
<span class="sub">There is a difference between loving you and teaching you. I have always done both. I am done doing the second one.</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION III — NO PROGRESS WITHOUT LANGUAGE
# ============================================================
st.markdown('<div class="section">Section III — No Progress Without Language</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">III.1</span> You cannot build a team in silence. You cannot build it in hints. You cannot build it in "you should just know."
<span class="sub">Two people cannot become a team without words. Real words. Direct words. Uncomfortable words. Said out loud, even when they are hard.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">III.2</span> Language is not decoration on top of a relationship. Language is the road.
<span class="sub">If we cannot talk about what is actually happening, there is no road. There is no progress. There is only two people standing still, hoping the other one moves first.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">III.3</span> Silence, deflection, and "okay" with nothing behind it do not move the relationship forward.
<span class="sub">Not slowly. Not at all. They are the absence of movement, dressed up as patience.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">III.4</span> If you cannot put it into words, you cannot build with it. A feeling that never becomes language is not a foundation. It is fog.
<span class="sub">I can respect confusion. I cannot build on top of it. Fog is not a road.</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION IV — VERIFICATION, NOT ASSUMPTION
# ============================================================
st.markdown('<div class="section">Section IV — Verification, Not Assumption</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IV.1</span> Just because you think something does not make it right.
<span class="sub">Same goes for me. Our heads tell us stories. Those stories are not reality. They are what our nervous systems are running at the time.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IV.2</span> Reality has to be verified. Together when we can. On our own when we cannot. Then we return to the table with what is actually real.
<span class="sub">Not assumption. Not certainty. Not feeling. Reality — checked, or at least honestly attempted.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IV.3</span> If we cannot do that, then we are not in a relationship. We are two people defending two separate versions of events that never actually met.
<span class="sub">That is not a partnership. That is a negotiation that never closes.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IV.4</span> Reality does not care about our intentions. It only cares about what actually happened.
<span class="sub">Good intentions are not a defense. The pattern is still the pattern.</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION V — DEFINITIONS
# ============================================================
st.markdown('<div class="section">Section V — Definitions, So There Is No Interpretation Gap Later</div>', unsafe_allow_html=True)

st.markdown("""
<div class="def">
<b>"Movement."</b> Not a single phone call. Not a single good day. Not a promise. A pattern, over time, of moving toward me — consistently, in hard moments and easy ones. One date of kindness is not movement. A month of consistency is movement.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="def">
<b>"Heavy."</b> A conversation that requires you to sit with something uncomfortable, look at yourself, admit something, or be vulnerable about your own inner state. Not a topic. A depth. If the conversation only works when it stays light, it is not depth. It is a ceiling.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="def">
<b>"Surface Level."</b> Calls, presence, small gestures, plans, kindness — all real, all warm, but they stay on top of things. Heavy conversations, hard questions, real vulnerability, and honest self-reflection do not happen. Surface level is not a failure. It is the ceiling. It cannot hold a partnership on its own.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="def">
<b>"Team."</b> Two people facing reality together — including uncomfortable reality — with honesty, directness, and consistency, over time. Not two people standing near each other. Not two people agreeing to feel better. Two people doing the actual work, together, when it is not convenient.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="def">
<b>"Homework."</b> The inner work that belongs to you. Not the relationship's work. Not my work. Yours. Learning what partnership actually is, learning how to use language under pressure, learning how to stay present when it is uncomfortable. This is not a favor you do for me. It is the work every adult has to do, eventually, if they want a real life with someone.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="def">
<b>"Ceiling."</b> The highest level of depth a conversation can reach before it stops. Not because the person is bad. Because the person cannot currently go further. Ceilings are not moral failures. But they are also not rooms you can build a life inside forever.
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION VI — WHAT I HAVE OBSERVED
# ============================================================
st.markdown('<div class="section">Section VI — What I Have Observed, On the Record</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VI.1</span> You move toward me on the surface. You call. You show up. You do small things.
<span class="sub">I am not saying none of it is real. Some of it is real. I am saying what is real is also the ceiling.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VI.2</span> When something gets heavy, it stops.
<span class="sub">When I ask a question that requires you to think, sit with something, be vulnerable, admit something, or look at yourself — it does not go anywhere. The conversation stays surface level, or it ends, or it becomes "okay" and then nothing.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VI.3</span> Light is allowed. Heavy is not.
<span class="sub">That is the pattern. Not silence. Not fighting. A ceiling. And I have spent months calling it "your own time" — I am not calling it that anymore.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VI.4</span> What it actually is: the highest you can currently go, and I have been hoping it changes.
<span class="sub">Hope is not the same thing as evidence. Waiting on hope while calling it patience is not a relationship. It is a holding pattern.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VI.5</span> I am writing this down because I am not going to pretend I did not see it.
<span class="sub">Not to punish you. Because I cannot build anything real on top of a version of events that neither of us actually lived.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VI.6</span> This is not me assuming you cannot. This is me observing that you have not, consistently, up to this point.
<span class="sub">Those are different things. Assumption is on me. Observation is on reality. I am only doing the second one.</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION VII — EXHIBIT A
# ============================================================
st.markdown('<div class="section">Exhibit A — Specific Recorded Observations</div>', unsafe_allow_html=True)

st.markdown("""
<div class="exhibit">
EXHIBIT A.1 — Dec 2025 & onward.<br>
The change was noticeable before the rupture. Lower energy. Shorter replies. Small fights that were not about the thing being fought about. When asked directly what was wrong, the answer was "okay" or "I'll tell you later" — and later never came.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="exhibit">
EXHIBIT A.2 — The phone call, Tim Hortons night.<br>
You were with someone else. It was not disclosed. I heard the other voice in the background. When I asked, the answer did not match what I could plainly hear. That night, the shared reality between us stopped matching.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="exhibit">
EXHIBIT A.3 — The five months following.<br>
Heavy pursuit on my end. Mixed signals on yours. Close moments, then distance. "I love you" alongside continued contact with the other person. "I don't deserve you" and "you should move on" spoken while you also stayed. The pattern kept the relationship neither closed nor open. It was neither.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="exhibit">
EXHIBIT A.4 — The laundry room.<br>
You slept in my bed. I sat in the laundry room, body overheating, trying to make the math work. Not because I wanted to sit there. Because the room I was supposed to feel safe in had become the room I could not breathe in.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="exhibit">
EXHIBIT A.5 — Recent pattern, ongoing.<br>
The same ceiling. Calls happen. Presence happens. But when a heavy question is asked, or a vulnerable conversation is opened, the depth stops. The conversation does not move forward — it resets to light. Every time.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="exhibit">
EXHIBIT A.6 — My own part, recorded for accuracy.<br>
Hundreds of texts. Pushing when I should have paused. Overfunctioning. Carrying what was not mine. This is on the record too, not because I am minimizing yours, but because the record has to be true.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="exhibit">
EXHIBIT A.7 — The good years, also on the record.<br>
Three and a half years. Food brought to me while I was working. Ordinary days. Road trips. Movies. Your family. My family. Years of real life. This exhibit is here so that nothing in this document can be read as if the years did not matter. They mattered.
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION VIII — WHAT I OWN
# ============================================================
st.markdown('<div class="section">Section VIII — What I Own, Fully</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VIII.1</span> I own my part. The hundreds of texts. The overfunctioning. The pushing when I should have paused.
<span class="sub">The carrying of what was never mine to carry. The turning of understanding into a job. I own it. No excuses.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VIII.2</span> Owning my part does not mean I carry yours.
<span class="sub">Those are two separate things, and I am done confusing them. My responsibility ends where yours begins.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VIII.3</span> I am not using my pain as leverage. I am using it as information.
<span class="sub">If anything in this document reads as a weapon, read it again. It is not. It is a record.</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION IX — TERMS OF CONTINUED PARTICIPATION
# ============================================================
st.markdown('<div class="section">Section IX — Terms of Continued Participation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IX.1</span> I will not do the five-month limbo again.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IX.2</span> I will not accept mixed signals as a permanent condition.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IX.3</span> I will not translate silence into meaning and then be blamed when I translate it wrong.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IX.4</span> I will not abandon myself to keep you comfortable.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IX.5</span> I will not teach what should already be there.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IX.6</span> I will not wait forever on hope while calling it patience.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IX.7</span> I will not keep my own depth hidden just to keep the room comfortable.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="callout">
These are not requests. These are terms. They are what a relationship actually is. 
If they cannot be met, that is information — not a failure on your part, and not a failure on mine. 
It just means we are not building the same thing.
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION X — WHAT I AM NOT ASKING FOR
# ============================================================
st.markdown('<div class="section">Section X — What I Am Not Asking For</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">X.1</span> I am not asking you to become a different person. I am asking you to become a person who can go deep with someone who loves you.
<span class="sub">If that sounds like a different person to you, that is information.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">X.2</span> I am not asking for perfection. I am asking for direction.
<span class="sub">Someone moving toward depth, honestly, even imperfectly, is different from someone who cannot move there at all.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">X.3</span> I am not asking you to know everything. I am asking you to be willing to learn — on your own, without me running the classroom.
<span class="sub">The willingness is yours. The teaching is not mine.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">X.4</span> I am not asking you to hurry. I am asking you to move.
<span class="sub">Time is yours. Direction is not negotiable. Slow movement toward me is real. No movement, slowly, is still no movement.</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION XI — CONSEQUENCES, PLAINLY STATED
# ============================================================
st.markdown('<div class="section">Section XI — Consequences, Plainly Stated</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">XI.1</span> If the pattern holds — surface movement, ceiling on depth, no willingness to sit in the heavy — then the outcome is already decided, regardless of how either of us feels about it.
<span class="sub">Not as punishment. As arithmetic. Two people cannot build a house if one of them can only stand in the entryway.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">XI.2</span> I will not end this out of anger. I will end it, if it ends, because the terms were not met and I am not willing to keep standing in a room that cannot hold me.
<span class="sub">That is not a threat. That is the same honesty this entire document is built on.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">XI.3</span> My life moves forward either way. School. Work. Peace. My own ground. That does not pause while I wait for this to resolve.
<span class="sub">If we end up building together, it will be from two solid foundations — not from one person holding the whole structure up.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">XI.4</span> This document is not the last word because I am angry. It is the last word because I am done explaining.
<span class="sub">Explaining is not partnership. Explaining is what one person does when the other person cannot hear. I am done being the person who explains.</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION XII — WHAT HAPPENS AFTER THIS
# ============================================================
st.markdown('<div class="section">Section XII — What Happens After This</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">XII.1</span> I am not asking you to respond today. I am not asking you to perform anything.
<span class="sub">I am giving you this so there is no confusion about where I stand.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">XII.2</span> After this, I will not explain further.
<span class="sub">No follow-up. No clarification. No re-asking. This document is the entire record, and it is final.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">XII.3</span> I will live my life and observe reality.
<span class="sub">What you do — over time, in the hard moments and not just the easy ones — will be the answer. Whatever it is, I will respect it, including if it is nothing.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">XII.4</span> My life continues either way.
<span class="sub">That is not a threat. That is arithmetic. This statement is the record. What happens next is not a conversation. It is what it is.</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION XIII — SEVERABILITY
# ============================================================
st.markdown('<div class="section">Section XIII — Severability</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">XIII.1</span> If you disagree with any single section of this document, that disagreement does not invalidate the rest.
<span class="sub">Reality does not become less real because someone disagrees with one part of it. The record stands in full.</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION XIV — ACKNOWLEDGEMENT OF RECEIPT
# ============================================================
st.markdown('<div class="section">Section XIV — Acknowledgement of Receipt</div>', unsafe_allow_html=True)

st.markdown("""
<div class="signature-block">
This document is considered received the moment it is opened. No signature is required. No reply is required. <br><br>
A response is information. <br>
Silence is information. <br>
Continued surface-level presence without depth is information. <br>
Real movement toward a partnership is information. <br><br>
All of it will be observed — not argued with, not chased, not explained.
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION XV — FINAL WORD (NEW)
# ============================================================
st.markdown('<div class="section">Section XV — Final Word</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
I am not writing this because I stopped loving you. I am writing this because I finally stopped believing that love alone was going to be enough.
<span class="sub">Love was never the problem. Depth was. Movement was. Language was. Those are not things I can give you. They are things you either bring, or you don't.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
If you bring them, I will meet you there. If you don't, I will go on. Not because I stopped caring. Because I finally started caring about myself as much as I cared about you.
<span class="sub">That is the whole statement. Everything above is just detail.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="callout">
I am not asking you to answer this. I am asking you to live it — or not. Either way, this document is the last time I say it.
</div>
""", unsafe_allow_html=True)

# ============================================================
# STAMP
# ============================================================
st.markdown('<div class="stamp">FINAL · NO REVISIONS</div>', unsafe_allow_html=True)

# ============================================================
# CLOSING
# ============================================================
st.markdown(f"""
<div class="footer">
Issued: {issued}<br>
Document ID: SOA-2026-FINAL-001 · Version: 1.0<br>
Status: FINAL — no revisions, no amendments, no follow-ups<br>
This statement is the record. The record stands.<br><br>
— Suraj Thapa
</div>
""", unsafe_allow_html=True)
