
CREATE TABLE IF NOT EXISTS api_response(
    id SERIAL PRIMARY KEY NOT NULL,
    request_uuid varchar(250) NOT NULL,
    date_start_request TIMESTAMP NOT NULL,
    description varchar(250) NOT NULL,
    attachment jsonb
);