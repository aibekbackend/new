import psycopg2
from faker import Faker
import random


# Функция для создания таблиц
def create_tables():
    conn = psycopg2.connect(
        dbname="blog_db",
        user="blog_user",
        password="fortest2023",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # Создаем таблицу users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        )
    ''')

    # Создаем таблицу posts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            content TEXT NOT NULL,
            user_id INTEGER REFERENCES users(id)
        )
    ''')

    # Создаем таблицу comments
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                id SERIAL PRIMARY KEY,
                text TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                post_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (post_id) REFERENCES posts(id)
            )
    ''')

    conn.close()



comments = [
    'Great post!',
    'Thanks for sharing!',
    'I found it very useful.',
    'Interesting news indeed.',
    'Looking forward to more.',
    'Well written!',
    'You nailed it!',
    'I agree with your points.',
    'Very informative.',
    'Impressive content!',
    'This is amazing!',
    'Keep up the good work!',
    'You have a unique perspective.',
    'I learned something new.',
    'You have a talent for writing.',
    'I enjoyed reading this.',
    'Awesome insights!',
    'You inspired me.',
    'Fantastic post!',
    'Your ideas are spot on.',
    'This is exactly what I needed.',
    'Keep sharing your knowledge!',
    'You have a great writing style.',
    'This deserves more attention.',
    'This is a game-changer.',
    'Thank you for sharing your expertise.',
    'Your writing is captivating.',
    'You have a gift for explaining complex topics.',
    'Brilliantly written!',
    'You made me think.',
    'I will definitely share this.',
    'Well-researched content.',
    'Your post is a must-read!',
    'I am impressed by your knowledge.',
    'You have got a new fan!',
    'This is so helpful.',
    'You put things into perspective.',
    'I cannot wait for your next post.',
    'I will be coming back for more.',
    'You are making a difference.',
    'This is thought-provoking.',
    'Excellent job!',
    'I am sharing this with my friends.',
    'Your insights are valuable.',
    'You have a way with words.',
    'I could not agree more!',
    'This deserves to go viral.',
    'Thank you for sharing your expertise with us.'
]


# Функция для заполнения таблиц данными
def insert_data():
    conn = psycopg2.connect(
        dbname="blog_db",
        user="blog_user",
        password="fortest2023",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # Вставляем данные в таблицу users
    fake = Faker()
    users_data = [(fake.name(), fake.email()) for _ in range(20)]
    cursor.executemany('INSERT INTO users (name, email) VALUES (%s, %s)', users_data)

    # Вставляем данные в таблицу posts
    # Список постов для вставки
    posts_data = [
        (
        'Healthy Eating Habits', 'Discover some nutritious recipes and healthy eating tips to improve your well-being.',
        3),
        ('Traveling on a Budget', 'Learn how to travel to your dream destinations without breaking the bank.', 2),
        ('Technology Trends', 'Explore the latest advancements in technology and their potential impact on our lives.',
         1),
        ('Gardening for Beginners', 'Start your own garden and enjoy the satisfaction of growing your own plants.', 4),
        ('Career Development Strategies', 'Useful strategies to boost your career and achieve your professional goals.',
         5),
        ('Art of Photography', 'Unleash your creativity with photography and capture stunning moments.', 6),
        ('Effective Time Management', 'Master the art of time management and increase your productivity.', 7),
        ('Mindfulness Meditation', 'Embrace mindfulness meditation to reduce stress and enhance mental clarity.', 8),
        ('Home Organization Tips', 'Create a clutter-free and organized living space with these practical tips.', 9),
        ('Financial Planning 101', 'Get started with financial planning and secure your financial future.', 10),
        ('DIY Home Improvement', 'Transform your home with simple and budget-friendly DIY home improvement projects.',
         11),
        (
        'Fitness and Exercise Routines', 'Stay fit and healthy with effective exercise routines and workout tips.', 12),
        ('Fashion Trends', 'Stay updated with the latest fashion trends and style inspirations.', 13),
        ('Delicious Dessert Recipes', 'Indulge in delightful dessert recipes that will satisfy your sweet tooth.', 14),
        ('Pet Care Tips', 'Learn how to take care of your furry friends and keep them happy and healthy.', 15),
        ('Learning a New Language', 'Start your language-learning journey and open doors to new cultures.', 16),
        ('Parenting Insights', 'Discover valuable insights and advice for being a great parent.', 17),
        (
        'Book Recommendations', 'Find your next great read with these book recommendations from different genres.', 18),
        ('Music and Its Impact', 'Explore the world of music and its profound impact on emotions and culture.', 19),
        ('Inspirational Quotes', 'Get inspired by powerful quotes from influential figures and thinkers.', 20),
        ('Cooking Adventures', 'Embark on culinary adventures and experiment with new recipes from around the world.',
         3),
        ('Budgeting Tips', 'Learn effective budgeting techniques to manage your finances wisely.', 4),
        ('Web Development Basics', 'Begin your journey into web development and learn the fundamental concepts.', 5),
        ('Yoga and Meditation',
         'Experience the transformative power of yoga and meditation for physical and mental well-being.', 6),
        ('Minimalist Living', 'Embrace a minimalist lifestyle and simplify your life for greater contentment.', 7),
        ('Digital Marketing Strategies', 'Explore various digital marketing strategies to grow your online presence.',
         8),
        ('Declutter Your Mind', 'Discover methods to declutter your mind and achieve mental clarity.', 9),
        ('Investing for Beginners', 'Start your investment journey and build a strong financial portfolio.', 10),
        (
        'Interior Design Inspiration', 'Get inspired by stunning interior design ideas to create your dream home.', 11),
        ('Cardio Workouts', 'Engage in heart-pumping cardio workouts to stay active and healthy.', 12),
        ('Fashionable Workwear', 'Find stylish workwear ideas to express your personality in the workplace.', 13),
        ('Baking Delights', 'Delve into the art of baking and create delectable treats for your loved ones.', 14),
        ('Pet Training Techniques',
         'Learn effective pet training techniques for a harmonious relationship with your pets.', 15),
        ('Cultural Immersion', 'Immerse yourself in different cultures and broaden your horizons.', 16),
        ('Positive Parenting', 'Practice positive parenting techniques to nurture happy and confident children.', 17),
        ('Science Fiction Must-Reads', 'Explore the fascinating world of science fiction with these must-reads.', 18),
        ('Music Therapy', 'Discover the therapeutic effects of music and how it can improve well-being.', 19),
        (
        'Motivational Stories', 'Read inspiring stories of perseverance and determination to overcome challenges.', 20),
        ('Photography Composition', 'Master the art of photography composition and capture captivating images.', 3),
        ('Productivity Hacks', 'Implement productivity hacks to accomplish more in less time.', 4),
        ('Data Science Fundamentals', 'Dive into data science and learn the foundational principles.', 5),
        ('Mediterranean Cuisine', 'Indulge in the flavors of Mediterranean cuisine and savor delicious dishes.', 6),
        ('Sustainable Living', 'Embrace sustainable practices to protect the environment and reduce waste.', 7),
        ('Social Media Marketing', 'Utilize social media marketing strategies to grow your business online.', 8),
        ('Stress Relief Techniques', 'Explore effective techniques to manage and reduce stress in your daily life.', 9),
        ('Retirement Planning', 'Plan for a secure retirement and enjoy your golden years to the fullest.', 10),
        ('Home Renovation Ideas', 'Get inspired by creative home renovation ideas for a fresh new look.', 11),
        ('Strength Training', 'Build strength and muscle with effective strength training workouts.', 12),
        ('Capsule Wardrobe Essentials', 'Curate a timeless capsule wardrobe with essential fashion pieces.', 13),
        ('Healthy Smoothie Recipes', 'Blend delicious and nutritious smoothies for a healthy lifestyle.', 14),
        ('Pet Health and Wellness', 'Learn about pet health and wellness to ensure the well-being of your pets.', 15),
        ('Exploring Different Cultures', 'Embark on a journey of exploration and learn about diverse cultures.', 16),
        ('Positive Discipline', 'Practice positive discipline techniques for effective child behavior management.', 17),
        ('Classic Literature Classics', 'Rediscover classic literature and timeless literary works.', 18),
        ('Music and Emotional Connection', 'Explore the emotional connection between music and the human experience.',
         19),
        ('Inspirational Life Lessons', 'Learn valuable life lessons from inspirational stories and experiences.', 20),
    ]

    cursor.executemany('INSERT INTO posts (title, content, user_id) VALUES (%s, %s, %s)', posts_data)

    # Вставляем данные в таблицу comments
    user_ids = list(range(1, 21))  # Пользователи имеют id от 1 до 20
    post_ids = list(range(1, 51))  # Посты имеют id от 1 до 50
    comments_data = []

    for _ in range(250):
        comment_text = random.choice(comments)
        user_id = random.choice(user_ids)
        post_id = random.choice(post_ids)
        comments_data.append((comment_text, user_id, post_id))

    cursor.executemany('INSERT INTO comments (text, user_id, post_id) VALUES (%s, %s, %s)', comments_data)

    conn.close()


if __name__ == "__main__":
    create_tables()
    insert_data()