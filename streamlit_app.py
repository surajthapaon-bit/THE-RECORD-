import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="STATEMENT OF ACCOUNT — FINAL",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# STYLING — institutional, formal, bill-like, memorable
# ============================================================
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
    .rule {
        text-align: center;
        font-family: Georgia, serif;
        letter-spacing: 6px;
        color: #999;
        margin: 2.4rem 0;
        font-size: 0.9rem;
    }
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

# ============================================================
# HEADER
# ============================================================
issued = datetime.now().strftime("%B %d, %Y — %H:%M")

st.markdown('<h1 class="title">STATEMENT OF ACCOUNT</h1>', unsafe_allow_html=True)
st.markdown('<div class="status">FINAL · DUE UPON RECEIPT · NO REVISIONS</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">ISSUED TO STEPHANIE LALAP · ISSUED BY SURAJ THAPA</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="header-block">
<b>Issued to:</b> Stephanie Lalap<br>
<b>Issued by:</b> Suraj Thapa<br>
<b>Date:</b> {issued}<br>
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

# ============================================================
# SECTION III — NO PROGRESS WITHOUT LANGUAGE
# ============================================================
st.markdown('<div class="section">Section III — No Progress Without Language</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">III.1</span> You cannot build a team in silence. You cannot build it in hints. You cannot build it in “you should just know.”
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
<span class="num">III.3</span> Silence, deflection, and “okay” with nothing behind it do not move the relationship forward.
<span class="sub">Not slowly. Not at all. They are the absence of movement, dressed up as patience.</span>
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

# ============================================================
# SECTION V — WHAT I HAVE OBSERVED
# ============================================================
st.markdown('<div class="section">Section V — What I Have Observed, On the Record</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">V.1</span> You move toward me on the surface. You call. You show up. You do small things.
<span class="sub">I am not saying none of it is real. Some of it is real. I am saying what is real is also the ceiling.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">V.2</span> When something gets heavy, it stops.
<span class="sub">When I ask a question that requires you to think, sit with something, be vulnerable, admit something, or look at yourself — it does not go anywhere. The conversation stays surface level, or it ends, or it becomes “okay” and then nothing.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">V.3</span> Light is allowed. Heavy is not.
<span class="sub">That is the pattern. Not silence. Not fighting. A ceiling. And I have spent months calling it “your own time” — I am not calling it that anymore.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">V.4</span> What it actually is: the highest you can currently go, and I have been hoping it changes.
<span class="sub">Hope is not the same thing as evidence. Waiting on hope while calling it patience is not a relationship. It is a holding pattern.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">V.5</span> I am writing this down because I am not going to pretend I did not see it.
<span class="sub">Not to punish you. Because I cannot build anything real on top of a version of events that neither of us actually lived.</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION VI — THE RUPTURE IS ON THE RECORD
# ============================================================
st.markdown('<div class="section">Section VI — The Rupture Is On the Record</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VI.1</span> The phone call. The five months of mixed signals.
<span class="sub">I am not relitigating it. I am also not letting it disappear from the shared record.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VI.2</span> You sleeping in my bed while I sat in the laundry room trying to make the math work.
<span class="sub">That happened. It does not need to be argued about. It needs to exist on the same page for both of us.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VI.3</span> The record exists so that neither of us can later say it was never said, never meant, or never remembered.
<span class="sub">That is not aggression. That is accuracy.</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION VII — WHAT I OWN
# ============================================================
st.markdown('<div class="section">Section VII — What I Own, Fully</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VII.1</span> I own my part. The hundreds of texts. The overfunctioning. The pushing when I should have paused.
<span class="sub">The carrying of what was never mine to carry. The turning of understanding into a job. I own it. No excuses.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VII.2</span> Owning my part does not mean I carry yours.
<span class="sub">Those are two separate things, and I am done confusing them. My responsibility ends where yours begins.</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SECTION VIII — TERMS OF CONTINUED PARTICIPATION
# ============================================================
st.markdown('<div class="section">Section VIII — Terms of Continued Participation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VIII.1</span> I will not do the five-month limbo again.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VIII.2</span> I will not accept mixed signals as a permanent condition.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VIII.3</span> I will not translate silence into meaning and then be blamed when I translate it wrong.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VIII.4</span> I will not abandon myself to keep you comfortable.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VIII.5</span> I will not teach what should already be there.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">VIII.6</span> I will not wait forever on hope while calling it patience.
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
# SECTION IX — WHAT HAPPENS AFTER THIS
# ============================================================
st.markdown('<div class="section">Section IX — What Happens After This</div>', unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IX.1</span> I am not asking you to respond today. I am not asking you to perform anything.
<span class="sub">I am giving you this so there is no confusion about where I stand.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IX.2</span> After this, I will not explain further.
<span class="sub">No follow-up. No clarification. No re-asking. This document is the entire record, and it is final.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IX.3</span> I will live my life and observe reality.
<span class="sub">What you do — over time, in the hard moments and not just the easy ones — will be the answer. Whatever it is, I will respect it, including if it is nothing.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="item">
<span class="num">IX.4</span> My life continues either way.
<span class="sub">That is not a threat. That is arithmetic. This statement is the record. What happens next is not a conversation. It is what it is.</span>
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
Status: FINAL — no revisions, no amendments, no follow-ups<br>
This statement is the record. The record stands.<br><br>
— Suraj Thapa
</div>
""", unsafe_allow_html=True)
