CREATE TABLE Users (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    status VARCHAR(20) DEFAULT 'Normal',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login_ip VARCHAR(45)
);

CREATE TABLE Post (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES Users(id),
    content TEXT,
    captured_at TIMESTAMP NOT NULL,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    is_realtime BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Comment (
    id BIGSERIAL PRIMARY KEY,
    post_id BIGINT REFERENCES Post(id),
    user_id BIGINT REFERENCES Users(id),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Follow (
    id BIGSERIAL PRIMARY KEY,
    follower_id BIGINT REFERENCES Users(id),
    following_id BIGINT REFERENCES Users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Likes (
    id BIGSERIAL PRIMARY KEY,
    post_id BIGINT REFERENCES Post(id),
    user_id BIGINT REFERENCES Users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE SearchLog (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES Users(id),
    keyword VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Report (
    id BIGSERIAL PRIMARY KEY,
    reporter_id BIGINT REFERENCES Users(id),
    target_id BIGINT REFERENCES Users(id),
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);