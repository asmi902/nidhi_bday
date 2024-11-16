import streamlit as st
import random

# Aesthetic Setup
st.set_page_config(page_title="Nidhi's Affirmation Bot 🌸", page_icon="🎀")
st.title("🌸 Nidhi's Affirmation Chatbot 🎀")
st.markdown("""
    <style>
    .big-font { font-size: 28px !important; color: #FF69B4; }
    .small-font { font-size: 16px; color: #A020F0; }
    .affirmation { 
        background-color: #FFB6C1; 
        padding: 15px; 
        border-radius: 15px; 
        color: white; 
        font-size: 20px; 
        font-family: 'Arial', sans-serif; 
        text-align: center; 
    }
    .game-title { font-size: 22px; color: #FFD700; font-weight: bold; }
    .footer { text-align: center; font-size: 14px; margin-top: 50px; color: #B22222; }
    </style>
    """, unsafe_allow_html=True)

# Affirmations Section
st.markdown('<p class="big-font">Hello Nidhi! 🌟</p>', unsafe_allow_html=True)
affirmations = [
    "You are capable of amazing things, Nidhi! 💪💖",
    "Believe in yourself, you’re unstoppable! ✨🌸",
    "Your kindness is a gift to everyone you meet. 🌼💕",
    "You radiate positivity and light. 🌈☀️",
    "You have the power to create the life you want. 🌟💫",
    "You are a ray of sunshine on a cloudy day. 🌞",
    "Your determination inspires those around you. 💪",
    "You have an aura of brilliance and warmth. ✨",
    "You make people feel valued and loved. 💝",
    "You are full of creativity and unique ideas. 🌟",
    "Your energy lights up the room. 🌈",
    "You are destined for greatness. 🏆",
    "You bring out the best in others. 💕",
    "You deserve all the happiness in the world. 🌏",
    "Your laughter is music to everyone’s ears. 🎵",
    "You are resilient and strong. 💖",
    "You always find a way to make things work. 🔑",
    "You’re one of a kind, and that’s your power. 🌟",
    "You are loved more than you know. 🌹",
    "You are a masterpiece in progress. 🎨"
]
st.markdown('<div class="affirmation">' + random.choice(affirmations) + '</div>', unsafe_allow_html=True)

# Random Compliments Section
st.header("💖 Compliments Galore!")
if st.button("Generate 20 Compliments"):
    compliments = [
        "You light up every room you enter! 🌟",
        "Your smile is contagious. 😊",
        "You have an incredible sense of humor. 😂",
        "You’re an amazing friend. 💕",
        "You’re so thoughtful and kind-hearted. 🌼",
        "You inspire others to be their best selves. ✨",
        "You are the epitome of grace and elegance. 💃",
        "Your presence is so calming and reassuring. 🌸",
        "You are truly irreplaceable. 💖",
        "You are a natural-born leader. 🏆",
        "Your kindness could change the world. 🌏",
        "You are the definition of brilliance. 🌟",
        "You make life so much more vibrant. 🌈",
        "You are such a compassionate soul. 💕",
        "You are stronger than you realize. 💪",
        "You are a trendsetter in your own unique way. 🌟",
        "You are an unstoppable force of positivity. 🌞",
        "Your optimism is truly contagious. 🌸",
        "You make everything better just by being you. 💝",
        "You are an absolute gem! 💎"
    ]
    for compliment in random.sample(compliments, 20):
        st.write(f"💬 {compliment}")

# Mini-Games Section
st.header("🎮 Fun Games to Play!")
game_choice = st.selectbox(
    "Choose a game to play:", 
    ["Never Have I Ever", "Truth or Situations", "How Well Do You Know Me?"]
)

# Game Logic
if game_choice == "Never Have I Ever":
    st.markdown('<p class="game-title">Never Have I Ever 🎉</p>', unsafe_allow_html=True)
    statements = [
        "Never have I ever lied about my age. 😳",
        "Never have I ever stalked someone on social media. 🔍",
        "Never have I ever eaten a whole tub of ice cream in one sitting. 🍨",
        "Never have I ever sent a text to the wrong person. 📱",
        "Never have I ever ghosted someone. 👻",
        "Never have I ever cheated on a test. 📝",
        "Never have I ever cried during a Disney movie. 😢",
        "Never have I ever had a crush on a teacher. 🤭",
        "Never have I ever fallen asleep in public. 😴",
        "Never have I ever kept a secret from my best friend. 🤐",
        "Never have I ever binge-watched an entire series in a day. 📺",
        "Never have I ever had a wardrobe malfunction in public. 👗",
        "Never have I ever walked into a glass door. 😂",
        "Never have I ever danced like nobody was watching. 💃",
        "Never have I ever embarrassed myself in front of a crush. 😳",
        "Never have I ever pulled an all-nighter. 🌙",
        "Never have I ever forgotten someone's birthday. 🎂",
        "Never have I ever lied to get out of plans. 🙈",
        "Never have I ever been caught sneaking out. 🚪",
        "Never have I ever had a weird nickname. 🤪"
    ]
    st.write(random.choice(statements))

elif game_choice == "Truth or Situations":
    st.markdown('<p class="game-title">Truth or Situations 🤔</p>', unsafe_allow_html=True)
    truth_questions = [
        "What’s the most embarrassing thing you’ve ever done? 😳",
        "What’s a secret you’ve never told anyone? 🤫",
        "Who’s your current crush? 😍",
        "What’s the worst lie you’ve ever told? 😈",
        "Have you ever been caught red-handed? 🤭",
        "What’s the weirdest habit you have? 🌀",
        "Have you ever betrayed a friend? 😬",
        "What’s your most irrational fear? 😱",
        "What’s a guilty pleasure you never admit to? 🍫",
        "Who do you secretly admire? 🌟",
        "What’s the most ridiculous rumor you’ve ever heard about yourself? 🕵️‍♀️",
        "What’s the most trouble you’ve ever gotten into? 🚨",
        "Who’s the last person you Googled? 🔍",
        "What’s your biggest insecurity? 😔",
        "Have you ever lied to your best friend? 🙊",
        "What’s the most daring thing you’ve ever done? 🌟",
        "What’s the pettiest thing you’ve ever done? 😅",
        "Who do you wish you were closer to? 🤗",
        "Have you ever pretended to like someone? 😶",
        "What’s the most awkward moment of your life? 😬"
    ]
    situations = [
        "If you were invisible for a day, what would you do? 🕵️‍♀️",
        "If you could switch lives with anyone for a week, who would it be? 🌍",
        "If you could relive any day in your life, what would it be? 🕰️",
        "If you had to survive on one food forever, what would it be? 🍕",
        "If you won the lottery, what’s the first thing you’d do? 💰",
        "If you could read minds, whose would you read first? 🧠",
        "If you could time travel, where would you go? 🕒",
        "If you had a superpower, what would it be? 🦸‍♀️",
        "If you had to choose between fame or fortune, which would you pick? 🌟",
        "If you were stranded on an island, what three things would you take? 🏝️",
        "If you could ask anyone one question, who would it be and what would you ask? 🤔",
        "If you could only wear one outfit for the rest of your life, what would it be? 👗",
        "If you had to sing karaoke right now, what song would you pick? 🎤",
        "If you were a fictional character, who would you be? 📖",
        "If you had 24 hours to live, what would you do? ⏳",
        "If you could change one thing about yourself, what would it be? 💭",
        "If you were granted one wish, what would it be? 🌠",
        "If you had to delete all but one app on your phone, which one would it be? 📱",
        "If you could relive one embarrassing moment, would you? Why or why not? 😳",
        "If you could have dinner with anyone, dead or alive, who would it be? 🍽️"
    ]
    game_mode = st.radio("Pick your mode:", ["Truth", "Situations"])
    if game_mode == "Truth":
        st.write(random.choice(truth_questions))
    else:
        st.write(random.choice(situations))

elif game_choice == "How Well Do You Know Me?":
    st.markdown('<p class="game-title">How Well Do You Know Me? 🧠</p>', unsafe_allow_html=True)
    questions = {
        "What was Nidhi's team color back in DPGA?": "Red",
        "What’s Nidhi's current college's name?": "AMITY",
        "What’s my go-to comedian?": "Akash Gupta",
        "What’s my star sign?": "Scorpio",
        "What’s was Nidhi's favourite subjects in highshcool?": "Mathematics",
        "What are the names of Nidhi's cats?": "Keebo and Kenzo",
        "What’s was Nidhi's favourite movie to see with Asmi?": "To all the boys I've loved before",
        "What’s the name of the Korean boyband Nidhi discussed with Shristi?": "BTS",
        "What’s the name of the imaginary boyfriend Nidhi created for Shrishti?": "ShinChan",
        "What’s my favorite animal?": "Cat!",
        "What’s my dream job?": "ML engineer",
        "What is Nidhi's nickname for her sister Niyati?": "Niyu",
        "What’s my guilty pleasure?": "Talking about her past life of having 1000 crushes",
        "Who are Nidhi's favourite people to chat on video calls?": "Asmi AND Shristi <3"
    }

    question, correct_answer = random.choice(list(questions.items()))
    # Generate 2 random incorrect answers
    all_answers = list(questions.values())
    all_answers.remove(correct_answer)
    incorrect_answers = random.sample(all_answers, 2)

    # Combine correct answer with incorrect ones and shuffle
    options = random.sample([correct_answer] + incorrect_answers, 3)

    user_answer = st.radio(f"{question}", options)
    if st.button("Submit Answer"):
        if user_answer == correct_answer:
            st.success("Correct! 🎉 You know me so well!")
        else:
            st.error(f"Oops! The correct answer was: {correct_answer}")

# Footer
st.markdown('<p class="footer">✨ Made with love by Asmi ✨</p>', unsafe_allow_html=True)
