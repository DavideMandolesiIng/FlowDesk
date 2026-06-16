-- FlowDesk initial database schema
CREATE TABLE users (
    id          SERIAL PRIMARY KEY,
    email       VARCHAR(255) NOT NULL UNIQUE,
    password    VARCHAR(255) NOT NULL,
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE tasks (
    id              SERIAL PRIMARY KEY,
    user_id          INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title           VARCHAR(255) NOT NULL,
    description     TEXT DEFAULT 'No description',
    priority        SMALLINT NOT NULL DEFAULT 0,
    status          SMALLINT NOT NULL DEFAULT 0,
    due_date        TIMESTAMP NOT NULL,
    created_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    completed_at    TIMESTAMP
);

CREATE TABLE notes (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title       VARCHAR(255) NOT NULL,
    body        TEXT NOT NULL DEFAULT '',
    created_at  TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE habits (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title       VARCHAR(255) NOT NULL,
    frequency   SMALLINT[] NOT NULL,
    createdAt   TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE note_tags (
    id       SERIAL PRIMARY KEY,
    note_id  INTEGER NOT NULL REFERENCES notes(id) ON DELETE CASCADE,
    tag      VARCHAR(100) NOT NULL
);

CREATE TABLE habit_logs (
    id          SERIAL PRIMARY KEY,
    habit_id    INTEGER NOT NULL REFERENCES habits(id) ON DELETE CASCADE,
    logged_at   TIMESTAMP NOT NULL
);
-- unique habit per day 
CREATE UNIQUE INDEX idx_habit_logs_unique_day
ON habit_logs(habit_id, CAST(logged_at AS date));

-- most frequent queries
CREATE INDEX idx_tasks_user_id    ON tasks(user_id);
CREATE INDEX idx_notes_user_id    ON notes(user_id);
CREATE INDEX idx_habits_user_id   ON habits(user_id);

CREATE INDEX idx_habit_logs_habit_id_date ON habit_logs(habit_id, logged_at DESC);

CREATE INDEX idx_note_tags_note_id ON note_tags(note_id);
CREATE INDEX idx_note_tags_tag     ON note_tags(tag);