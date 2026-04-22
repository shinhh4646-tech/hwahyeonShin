-- 1. User Table: Information for all accounts
CREATE TABLE Users (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    status VARCHAR(20) DEFAULT 'Normal', -- Normal, Suspected, Blocked
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login_ip VARCHAR(45)
);

-- 2. Post Table: User-generated posts
CREATE TABLE Post (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES Users(id),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Comment Table: Feedback on posts
CREATE TABLE Comment (
    id BIGSERIAL PRIMARY KEY,
    post_id BIGINT REFERENCES Post(id),
    user_id BIGINT REFERENCES Users(id),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Follow Table: User-to-user relationships
CREATE TABLE Follow (
    id BIGSERIAL PRIMARY KEY,
    follower_id BIGINT REFERENCES Users(id),
    following_id BIGINT REFERENCES Users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. Like Table: Reaction to posts
CREATE TABLE Likes (
    id BIGSERIAL PRIMARY KEY,
    post_id BIGINT REFERENCES Post(id),
    user_id BIGINT REFERENCES Users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. SearchLog Table: User search history
CREATE TABLE SearchLog (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES Users(id),
    keyword VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 7. Report Table: User reports against bots
CREATE TABLE Report (
    id BIGSERIAL PRIMARY KEY,
    reporter_id BIGINT REFERENCES Users(id),
    target_id BIGINT REFERENCES Users(id),
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);